from connectionSAP import connection

def additionalDetails(session, Vehicle_Number, LR_Number, LR_Date, Number_of_Package):
    try:
        session.findById('wnd[0]/usr/btnTC_HEAD').press()
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU').select()
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZVEHICLE_NO').text = LR_Date
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZVEHICLE_NO').caretPosition = 0
        session.findById('wnd[0]').sendVKey(0)
        if str(LR_Number).lower() == 'nan':
            session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZLR_NO').text = ''
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZLR_NO').setFocus()
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZLR_NO').caretPosition = 0
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_2').text = Vehicle_Number
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_2').setFocus()
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_2').caretPosition = 0
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_1').text = Number_of_Package
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_1').setFocus()
        session.findById('wnd[0]/usr/tabsTABSTRIP_OVERVIEW/tabpKFCU/ssubSUBSCREEN_BODY:SAPMV60A:6101/ssubCUSTOMER_SCREEN:ZVF01HEADER:1000/txtVBRK-ZZDUMMY_1').caretPosition = 0
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/tbar[0]/btn[11]').press()
    except Exception as e: 
        raise Exception('Error: While Entering the Header Details') 
 
