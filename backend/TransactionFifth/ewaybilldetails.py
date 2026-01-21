from connectionSAP import connection


def EWBdetails(session,invoice_array):

    session.findById("wnd[0]/usr/ctxtS_WERKS-LOW").text = "1002"
    session.findById("wnd[0]/usr/ctxtS_VBELN-LOW").text = invoice_array[0]
    session.findById("wnd[0]/usr/ctxtS_VBELN-HIGH").text = invoice_array[-1]
    
    
    session.findById("wnd[0]/usr/radIRN_EWAY").select()
    session.findById("wnd[0]/tbar[1]/btn[8]").press()