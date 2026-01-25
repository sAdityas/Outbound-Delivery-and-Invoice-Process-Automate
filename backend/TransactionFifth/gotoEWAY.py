from connectionSAP import connection 
import time
def GOEWAY(session):
        try:

                session.findById('wnd[0]/tbar[0]/okcd').text = '/nzewaybill'
                session.findById('wnd[0]').sendVKey(0)
        except:
                raise Exception('Error while entering T-Code')