from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time

# SAP modules
from connectionSAP import connection
from GetDocument.getDocument import outBoundDelivery as getDeliveryNumber, documentVF01
from TransactionSecond.VL01N import VL01N as gotoVL01N
from TransactionSecond.detailsVL01N import detailsVL01N
from TransactionSecond.batchDetails import batchInputVL01N
from TransactionSecond.PGI import PGI
from TransactionSecond.processDocument import processDocument
from TransactionThird.VF01 import gotoCode as gotoVF01
from TransactionThird.entereDeliverynumber import enterDeliveryNumber
from TransactionThird.additionalDetails import additionalDetails
from excelReader import excelReader

app = Flask(__name__)
CORS(app)

@app.route('/main', methods=['POST'])
def main_api():
    try:
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return jsonify({'error': 'No file uploaded'}), 400

        os.makedirs('temp', exist_ok=True)
        file_path = os.path.join('temp', uploaded_file.filename)
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

                gotoVL01N(session)
                time.sleep(1)

                delqty_obj = detailsVL01N(session, SaleOrder[i], Plant[i])
                delqty = delqty_obj.Text if delqty_obj else 'N/A'

                PGI(session)
                batchInputVL01N(session, Quantity[i], delqty)
                processDocument(session, Partner_ID[i])

                OD = getDeliveryNumber(session)

                gotoVF01(session)
                enterDeliveryNumber(session, OD, BillType[i])
                additionalDetails(session, LR_Date[i], LR_Number[i], Vehicle_Number[i], Number_of_Package[i])

                invoice_number = documentVF01(session)
                time.sleep(1)

                results.append({
                    'sales_order': SaleOrder[i],
                    'quantity': Quantity[i],
                    'invoice_number': invoice_number,
                    'status': 'Success',
                    'error': None
                })

            except Exception as e:
                results.append({
                    'sales_order': SaleOrder[i],
                    'quantity': Quantity[i],
                    'invoice_number': None,
                    'status': 'Failed',
                    'error': str(e)
                })

        return jsonify({'results': results})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
