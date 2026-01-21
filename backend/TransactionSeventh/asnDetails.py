def asnDetails(session,invoice_array,plant,BillType):
    BillType = list(BillType)
    session.findById("wnd[0]/usr/ctxtS_FKART-LOW").text = BillType[0] 
    if len(BillType) > 1:
        session.findById("wnd[0]/usr/ctxtS_FKART-HIGH").setFocus()
        session.findById("wnd[0]/usr/ctxtS_FKART-HIGH").text = BillType[-1] 
    session.findById("wnd[0]/usr/ctxtS_WERKS-LOW").text = plant[0]
    session.findById("wnd[0]/usr/ctxtS_VBELN-LOW").text = invoice_array[0]
    session.findById("wnd[0]/usr/ctxtS_VBELN-HIGH").text =invoice_array[-1]
    session.findById("wnd[0]").sendVKey(8)
    
    session.findById("wnd[0]/tbar[0]/btn[3]").press()