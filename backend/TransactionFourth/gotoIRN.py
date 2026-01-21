from connectionSAP import connection
import time
import pythoncom
def IRN(session):
    pythoncom.CoInitialize()
    try:
        print("IRN") 
        session.findById('wnd[0]').maximize()
        session.findById('wnd[0]/tbar[0]/okcd').text = '/nzeinvoice'
        session.findById('wnd[0]').sendVKey(0)
        time.sleep(0.5)
    except Exception as e:
        raise 