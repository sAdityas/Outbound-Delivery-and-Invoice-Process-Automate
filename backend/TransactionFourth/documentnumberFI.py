from connectionSAP import connection
import time


def docnum(session,invoice_array,plant,L_Date,H_Date):
    try:
        session.findById("wnd[0]/usr/ctxtSO_VBELN-LOW").text = invoice_array[0]
        session.findById("wnd[0]/usr/ctxtSO_VBELN-HIGH").text = invoice_array[-1]
        session.findById("wnd[0]/usr/ctxtSO_WERKS-LOW").text = plant
        
        session.findById("wnd[0]/usr/ctxtSO_FKDAT-LOW").text = L_Date
        session.findById("wnd[0]/usr/ctxtSO_FKDAT-HIGH").text = H_Date
        session.findById("wnd[0]/usr/radCREATE").select()
        print('Selecting Create E invoice')
        session.findById("wnd[0]").sendVKey(8)
    except:
        raise Exception('Error while entering required fields ZEINVOICE')

