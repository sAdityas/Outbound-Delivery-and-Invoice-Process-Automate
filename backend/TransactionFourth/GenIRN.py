from connectionSAP import connection
import time


def GENIRN(session):
    
    print('Selecting ALl')
    session.findById('wnd[0]').sendVKey(5)
    print('Generating IRN')
    session.findById("wnd[0]/tbar[1]/btn[5]").press()
    print('Clicking Generate IRN')
    session.findById("wnd[0]/tbar[1]/btn[18]").press()
    session.findById('wnd[0]').sendVKey(3)
