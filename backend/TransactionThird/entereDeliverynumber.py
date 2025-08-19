from GetDocument.getDocument import outBoundDelivery
from connectionSAP import connection

def enterDeliveryNumber(session, OD, BillType):
    try:
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').setFocus()
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').caretPosition = 0
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').text = ''
        session.findById('wnd[0]/usr/cmbRV60A-FKART').setFocus()
        session.findById('wnd[0]/usr/cmbRV60A-FKART').key = BillType
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').setFocus()
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').caretPosition = 0
        session.findById('wnd[0]/usr/tblSAPMV60ATCTRL_ERF_FAKT/ctxtKOMFK-VBELN[0,0]').text = OD
        session.findById('wnd[0]').sendVKey(0)
    except Exception as e:
        raise Exception('❌ Error entering Delivery Number')  
 
