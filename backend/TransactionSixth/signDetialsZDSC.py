import sys
def signDetails(session, LR_Date, invoice_array, Plant):

    print('This is in signDetails function',invoice_array[0],invoice_array[-1],LR_Date,Plant[0])
    # sys.exit()
    session.findById("wnd[0]/usr/ctxtSO_VBELN-LOW").text = invoice_array[0]
    session.findById("wnd[0]/usr/ctxtSO_VBELN-HIGH").text = invoice_array[-1]

    
    session.findById("wnd[0]/usr/ctxtSO_WERKS-LOW").text = Plant[0]

    
    
    session.findById("wnd[0]/usr/ctxtSO_FKDAT-LOW").text =  LR_Date[0]


    session.findById("wnd[0]/usr/chkRDC1").selected = True
    
    session.findById("wnd[0]/usr/radRD_4").select()
    
    session.findById("wnd[0]/usr/radRD_1").select()

    session.findById('wnd[0]').sendVKey(8)