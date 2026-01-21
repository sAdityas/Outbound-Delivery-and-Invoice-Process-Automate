import sys
def details(session,LR_Date,invoice_array,plant):

    session.findById("wnd[0]/usr/ctxtSO_VBELN-LOW").text = invoice_array[0]
    session.findById("wnd[0]/usr/ctxtSO_VBELN-HIGH").text = invoice_array[-1]
    
    session.findById("wnd[0]/usr/ctxtSO_FKDAT-LOW").text = LR_Date[0]
    session.findById("wnd[0]/usr/ctxtSO_FKDAT-HIGH").text = LR_Date[-1]

    
    session.findById("wnd[0]/usr/ctxtSO_WERKS-LOW").text = plant[0]

    session.findById("wnd[0]/usr/chkRDC1").selected = True
    session.findById("wnd[0]/usr/radRD5").select()
    session.findById("wnd[0]/usr/radRD_1").select()
        
    session.findById('wnd[0]').sendVKey(8)