import sys
def details(session,L_Date,H_Date,invoice_array,plant,typeofinvoice):
    try:
        session.findById("wnd[0]/usr/ctxtSO_VBELN-LOW").text = invoice_array[0]
        session.findById("wnd[0]/usr/ctxtSO_VBELN-HIGH").text = invoice_array[-1]
        session.findById("wnd[0]/usr/ctxtSO_FKDAT-LOW").text = L_Date
        session.findById("wnd[0]/usr/ctxtSO_FKDAT-HIGH").text = H_Date
        session.findById("wnd[0]/usr/ctxtSO_WERKS-LOW").text = plant

        session.findById("wnd[0]/usr/chkRDC1").selected = True
        session.findById("wnd[0]/usr/radRD5").select()
        if typeofinvoice == '2':
            session.findById("wnd[0]/usr/radRD_3").select()
        else:
            session.findById("wnd[0]/usr/radRD_1").select() 
            
        session.findById('wnd[0]').sendVKey(8)
    except:
        raise Exception('Error while entering required fields Displaying ZDSC')