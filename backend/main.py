from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
import time
import glob
import traceback
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

# Excel and CSV Reader Functions
from excelReader import excelReader
from excelReader import read_csv
from excelReader import save_csv

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


# IRN Distance 
from IRNdistance.processpincode import ppc
from IRNdistance.dicttolist import dicttolist

import sys




app = Flask(__name__)
CORS(app)

MAX_RETRIES = 2

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
            LR_Date,
            pincode
        ) = excelReader(file_path)

        session = connection()
        results = []
        csv_rows = []
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
                gotoVL01N(session)
                
                detailsVL01N(session, SaleOrder[i], Plant[i])
                PGI(session)
                batchInputVL01N(session, Quantity[i])
                postalcodearray = processDocument(session, Partner_ID[i])

                OD = getDeliveryNumber(session)

                gotoVF01(session)
                enterDeliveryNumber(session, OD, BillType[i])
                additionalDetails(session, LR_Date[i], LR_Number[i], Vehicle_Number[i], Number_of_Package[i])

                invoice_number = documentVF01(session)
                invoice_array.append(invoice_number)


                # invoice_array = ['7000440441', '7000440442', '7000440443', '7000440444', '7000440445',]
                # postalcodearray = ['410501', '410501', '410501', '410501', '410501']

                
                salecode = ppc(invoice_array,postalcodearray,pincode)
                invoice_arrays, Flag = dicttolist(salecode)
                invoice_arrays, Flag = dicttolist(salecode)
                csv_rows.append({
                    "invoice_number": invoice_number,
                    "LR_Date": LR_Date[i],
                    "Plant": Plant[i],
                    "BillType": BillType[i],
                    "Flag": Flag
                })
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
        if csv_rows:
            save_csv(csv_rows)
        return jsonify({'results': results}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/zdsc',methods=['POST','GET'])
def zdsc():
    try:
        Desktoppath = r'D:/'
        results = []
        filename = 'DoNotDelete.csv'
        files = glob.glob(os.path.join(Desktoppath, filename))
        if not files:
                    return jsonify({
            'results': [],
            'message': 'No Files Found'
        }), 200

        filename = max(files, key=os.path.getmtime)

        (
            InvoiceNumber,
            Flag,
            Date,
            plant,
            BillType
        ) = read_csv(filename)
        
        invoice_array = InvoiceNumber
        flag = Flag
        LR_Date = Date
        plant = plant
        BillType = BillType

        session = connection()

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                print(f"IRN attempt {attempt}")

                IRN(session)
                docnum(session, invoice_array)
                GENIRN(session)

                GOEWAY(session)
                EWBdetails(session, invoice_array)
                GENEWAY(session, flag)

                print("IRN & E-Way Bill generated successfully")
                break  # ✅ stop after success

            except Exception as e:
                print(f"Attempt {attempt} failed:", e)
                traceback.print_exc()

            if attempt == MAX_RETRIES:
                raise Exception('Error while generating IRN & E-Way Bill')

            time.sleep(2)  # optional wait before retry
        

        gotoZDSC(session)
        signDetails(session,LR_Date,invoice_array,plant)
        sign(session)
        gotoZDSC(session)
        details(session,LR_Date,invoice_array,plant)
        num_of_invoices = len(invoice_array)
        display(session,num_of_invoices)

        # asn(session)
        # asnDetails(session,invoice_array,plant,unqBillType)
        for inv, dt, plant, bill in zip(invoice_array, Date, plant, BillType):
            results.append({
                "Invoice_Number": inv,
                "Date": dt,
                "Plant": plant,
                "BillType": bill,
                "Status": "Success"
            })

        return jsonify({'results': results}) , 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050, use_reloader = False)
