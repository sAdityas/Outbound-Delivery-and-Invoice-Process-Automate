from connectionSAP import connection
import time
import pythoncom
def VL01N(session):
    pythoncom.CoInitialize()
    try:
        session.findById('wnd[0]').maximize()
        session.findById('wnd[0]/tbar[0]/okcd').text = '/nVL01N'
        session.findById('wnd[0]').sendVKey(0)
        time.sleep(0.5)
    except Exception as e:
        raise Exception('❌ Error navigating to VL01N')