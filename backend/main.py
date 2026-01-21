from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
import time

# SAP modules

from connectionSAP import connection

from GetDocument.getDocument import outBoundDelivery as getDeliveryNumber, documentVF01, checkError

# First Way Point
from TransactionSecond.VL01N import VL01N as gotoVL01N
from TransactionSecond.detailsVL01N import detailsVL01N
from TransactionSecond.ZTRDEnter import EnterZtrd
from TransactionSecond.batchDetails import batchInputVL01N
from TransactionSecond.ZTRDDetails import TRD
from TransactionSecond.PGI import PGI
from TransactionSecond.processDocument import processDocument
from TransactionSecond.checkrows import checkRows

# Second Way Point
from TransactionThird.VF01 import gotoCode as gotoVF01
from TransactionThird.entereDeliverynumber import enterDeliveryNumber
from TransactionThird.additionalDetails import additionalDetails
from excelReader import excelReader

# Third Way point
from TransactionFourth.gotoIRN import IRN
from TransactionFourth.documentnumber import docnum
from TransactionFourth.GenIRN import GENIRN

# Fourth Way Point
from TransactionFifth.gotoEWAY import GOEWAY
from TransactionFifth.GENEWAY import GENEWAY
from TransactionFifth.ewaybilldetails import EWBdetails

# Fifth Way Point
from TransactionSixth.signDetialsZDSC import signDetails
from TransactionSixth.detailsZDSC import details
from TransactionSixth.gotoZDSC import gotoZDSC
from TransactionSixth.displayZDSC import display
from TransactionSixth.signZDSC import sign

# Sixth Way Point
from TransactionSeventh.gotocode import asn
from TransactionSeventh.asnDetails import asnDetails

import sys




app = Flask(__name__)
CORS(app)

@app.route('/main', methods=['POST','GET'])
def main_api():
    try:
        invoice_array = []
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return jsonify({'error': 'No file uploaded'}), 400

        os.makedirs('temp', exist_ok=True)
        filename = uploaded_file.filename or "uploaded_file"
        file_path = os.path.join('temp', filename)
        uploaded_file.save(file_path)

        # Read columns with new headers from Excel
        (
            SaleOrder,
            BillType,
            Quantity,
            Vehicle_Number,
            LR_Number,
            Number_of_Package,
            Partner_ID,
            Plant,
            LR_Date
        ) = excelReader(file_path)

        session = connection()
        results = []
        for i in range(len(SaleOrder)):
            try:
                if Quantity[i] <= 0:
                    results.append({
                        'sales_order': SaleOrder[i],
                        'quantity': Quantity[i],
                        'invoice_number': None,
                        'status': 'Skipped',
                        'error': 'Quantity is zero or negative'
                    })
                    continue
                unqBillType = set(BillType)
                gotoVL01N(session)
                time.sleep(1)
                
                detailsVL01N(session, SaleOrder[i], Plant[i])
                PGI(session)
                batchInputVL01N(session, Quantity[i])
                processDocument(session, Partner_ID[i])

                OD = getDeliveryNumber(session)

                gotoVF01(session)
                enterDeliveryNumber(session, OD, BillType[i])
                additionalDetails(session, LR_Date[i], LR_Number[i], Vehicle_Number[i], Number_of_Package[i])

                invoice_number = documentVF01(session)
                invoice_array.append(invoice_number)

                results.append({
                    'sales_order': SaleOrder[i],
                    'quantity': Quantity[i],
                    'invoice_number': invoice_number,
                    'status': 'Success',
                    'error': None
                })
                # Start Invoice from 7000440441 to 7000440451

            except Exception as e:
                results.append({
                    'sales_order': SaleOrder[i],
                    'quantity': Quantity[i],
                    'invoice_number': None,
                    'status': 'Failed',
                    'error': str(e)
                })
        num_of_invoices = len(SaleOrder)
        plant = Plant
        print(invoice_array,Plant, LR_Date)


        IRN(session)
        docnum(session,invoice_array)
        GENIRN(session)

        GOEWAY(session)
        EWBdetails(session,invoice_array)
        GENEWAY(session)

        # gotoZDSC(session)
        # signDetails(session,LR_Date,invoice_array,plant)
        # sign(session)
        # gotoZDSC(session)
        # details(session,LR_Date,invoice_array,plant)
        # display(session,num_of_invoices)

        # asn(session)
        # asnDetails(session,invoice_array,plant,unqBillType)


        return jsonify({'results': results})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ZTRD Tooling PO Automation
@app.route('/ZTRD', methods=['POST', 'GET'])
def tooling():
    import os, time
    try:
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return jsonify({'error': 'No file uploaded'}), 400

        os.makedirs('temp', exist_ok=True)
        file_path = os.path.join('temp', uploaded_file.filename or "uploaded_file.xlsx")
        uploaded_file.save(file_path)

        # ---- Read Excel or CSV ----
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".xlsx":
            df = pd.read_excel(file_path)
        elif ext == ".csv":
            df = pd.read_csv(file_path)
        else:
            return jsonify({'error': f'Unsupported file type: {ext}'}), 400

        # ---- Extract Columns by Name ----
        SaleOrder = df['Sales Document'].tolist()
        BillType = df['Sales Document Type'].tolist()
        Quantity = df['Order Quantity (Item)'].tolist()
        Vehicle_Number = df['Vehicle Number'].tolist()
        LR_Number = df['LR Number'].tolist()
        Number_of_Package = df['Number of Package'].tolist()
        Partner_ID = df['Partner ID'].tolist()
        Plant = df['Plant'].tolist()
        LR_Date = df['Document Date'].tolist()

        # ---- SAP Connection ----
        session = connection()
        results = []

        # ---- Processing Each Sale Order ----
        for idx in range(len(SaleOrder)):
            so = SaleOrder[idx]
            bill_type = BillType[idx]
            qty = Quantity[idx]
            vehicle_number = Vehicle_Number[idx]
            lr_number = LR_Number[idx]
            num_packages = Number_of_Package[idx]
            partner_id = Partner_ID[idx]
            plant = Plant[idx]
            lr_date = LR_Date[idx]

            if qty <= 0:
                results.append({
                    'sales_order': so,
                    'quantity': qty,
                    'invoice_number': None,
                    'status': 'Skipped',
                    'error': 'Quantity is zero or negative'
                })
                continue

            try:
                # Go to VL01N and check delivery
                status_bar_text = checkError(session)
                if "Order cannot be delivered" in status_bar_text:
                    results.append({
                        'sales_order': so,
                        'quantity': qty,
                        'invoice_number': None,
                        'status': 'Blocked',
                        'error': 'Order cannot be delivered'
                    })
                    continue
                
                    
                flag = checkRows(session, so, plant)
                # Re-enter and count rows
                for row_num in range(flag):
                    gotoVL01N(session)
                    EnterZtrd(session,so,plant)
                    TRD(session)
                    if not has_delivery_quantity(session):
                        results.append({
                            'sales_order': so,
                            'quantity': qty,
                            'invoice_number': None,
                            'status': 'Failed',
                            'error': f'No delivery quantity found for row {row_num+1}'
                        })
                        continue

                    PGI(session)
                    batchInputVL01N(session, qty)
                    processDocument(session, partner_id)
                    delivery_number = getDeliveryNumber(session)

                    gotoVF01(session)
                    enterDeliveryNumber(session, delivery_number, bill_type)
                    additionalDetails(session, lr_date, lr_number, vehicle_number, num_packages)
                    invoice_number = documentVF01(session)

                    results.append({
                        'sales_order': so,
                        'quantity': qty,
                        'invoice_number': invoice_number,
                        'status': 'Success',
                        'error': None
                    })

            except Exception as e:
                results.append({
                    'sales_order': so,
                    'quantity': qty,
                    'invoice_number': None,
                    'status': 'Failed',
                    'error': str(e)
                })

        return jsonify({'results': results})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def has_delivery_quantity(session):
    """Check if delivery quantity exists."""
    field = session.findById(
        "wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/"
        "ssubSUBSCREEN_BODY:SAPMV50A:1104/"
        "tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]"
    )
    return bool(field.Text.strip())




if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0', port=5050, use_reloader = False)
 
=======
    app.run(debug=True, host='0.0.0.0', port=5050)
  
 
>>>>>>> e8b807375e0a17248cc438c71da2530ab5532fa8
