from connectionSAP import connection
import time
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
RESET = '\x1b[0m'

def detailsVL01N(session, SaleOrder, Plant):
    try:
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').setFocus()
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').setFocus()
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').caretPosition = 0
        session.findById('wnd[0]/usr/ctxtLIKP-VSTEL').text = Plant
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').setFocus()
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').text = SaleOrder
        session.findById('wnd[0]/usr/ctxtLV50C-VBELN').caretPosition = 0
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01').select()
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-G_LFIMG[2,0]').setFocus()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-G_LFIMG[2,0]').caretPosition = 1
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02').select()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]').setFocus()
    except Exception as e:
        raise Exception('❌ Error entering VL01N details')