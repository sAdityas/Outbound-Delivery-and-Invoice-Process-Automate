from connectionSAP import connection 
import time
def GOEWAY(session):
        session.findById('wnd[0]/tbar[0]/okcd').text = '/nzewaybill'
        session.findById('wnd[0]').sendVKey(0)