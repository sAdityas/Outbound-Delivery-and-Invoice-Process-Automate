from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time

# SAP modules

from connectionSAP import connection


# IRN
from TransactionFourth.gotoIRN import IRN
from TransactionFourth.documentnumberFI import docnum
from TransactionFourth.GenIRN import GENIRN

# ZDSC
from TransactionSixth.signDetialsZDSCFI import signDetails
from TransactionSixth.detailsZDSCFI import details
from TransactionSixth.gotoZDSC import gotoZDSC
from TransactionSixth.displayZDSC import display
from TransactionSixth.signZDSC import sign


app = Flask(__name__)
CORS(app)

MAX_RETRIES = 2


@app.route('/irn', methods=['POST','GET'])
def irn_api():
    try:
        payload = request.get_json()
        print(payload)

        data = payload.get('data', {})

        firstInvoice = data.get('firstInvoice')
        lastInvoice = data.get('lastInvoice')
        firstDate = data.get('firstDate')
        lastDate = data.get('lastDate')
        plant = data.get('plant')

        print(firstInvoice, lastInvoice, firstDate, lastDate, plant)

        session = connection()
        invoice_array = [str(i).zfill(10) for i in range(int(firstInvoice), int(lastInvoice) + 1)]
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                
                IRN(session)
                docnum(session, invoice_array, plant, firstDate, lastDate)
                GENIRN(session)
                break  # ✅ stop after success

            except Exception as e:
                print(f"Attempt {attempt} failed:", e)

            if attempt == MAX_RETRIES:
                raise  # 🔥 propagate error after final attempt

            time.sleep(2)
        return {'message': 'Success'}, 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

                
@app.route('/zdsc', methods=['POST','GET'])
def dsc_api():
    try:
        payload = request.get_json()
        
        data = payload.get('data', {})
        firstInvoice = data.get('firstInvoice')
        lastInvoice = data.get('lastInvoice')
        firstDate = data.get('firstDate')
        lastDate = data.get('lastDate')
        plant = data.get('plant')
        typeofinvoice = data.get('typeofinvoice')
        
        num_of_invoices = int(lastInvoice) - int(firstInvoice) + 1
        session = connection()
        invoice_array = [str(i).zfill(10) for i in range(int(firstInvoice), int(lastInvoice) + 1)]
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                gotoZDSC(session)
                signDetails(session,firstDate,lastDate,invoice_array,plant,typeofinvoice)
                sign(session)
                gotoZDSC(session)
                details(session,firstDate,lastDate,invoice_array,plant,typeofinvoice)
                display(session,num_of_invoices)
                break  # ✅ stop after success

            except Exception as e:
                print(f"Attempt {attempt} failed:", e)

            if attempt == MAX_RETRIES:
                raise  # 🔥 propagate error after final attempt

            time.sleep(2)
        return {'message': 'Success'}, 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050, use_reloader = False)