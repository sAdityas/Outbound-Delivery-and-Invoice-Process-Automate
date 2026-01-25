from connectionSAP import connection
import time


def GENIRN(session):
    try:
        session.findById('wnd[0]').sendVKey(5)
        session.findById("wnd[0]/tbar[1]/btn[5]").press()
        session.findById("wnd[0]/tbar[1]/btn[18]").press()
        session.findById('wnd[0]').sendVKey(3)
    except:
        raise Exception('Error while generating IRN')
