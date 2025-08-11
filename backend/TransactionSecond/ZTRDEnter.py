from connectionSAP import connection
import time
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
RESET = '\x1b[0m'

def EnterZtrd(session, SaleOrder, Plant):
    try:
        print(Plant,SaleOrder)
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').setFocus()
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').setFocus()
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').caretPosition = 0
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').text = Plant
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').setFocus()
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').text = SaleOrder
        session.findById('wnd[0]').sendVKey(0)
    except Exception as e:
        raise