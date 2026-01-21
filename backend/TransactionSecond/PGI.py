from connectionSAP import connection
import time
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
RESET = '\x1b[0m'

def PGI(session):
    try:
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01').select()
        matnr_field = session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/ctxtLIPS-MATNR[1,0]')
        matnr_field.setFocus()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/subSUBSCREEN_ICONBAR:SAPMV50A:1708/btnBT_CHSP_T').press()
    except Exception as e:
        raise e  
 
