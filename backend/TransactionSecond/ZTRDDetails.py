import time 
def TRD(session):
    def process_tab(tab_code):
        """Handles MKAL -> POLO -> Quantity entry on given tab code"""
        # Go to tab
        session.findById(f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}").select()

        
        
        if  session.findById(
            f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,1]"
        ).Text:
            # Press MKAL
            session.findById(
                f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/subSUBSCREEN_ICONBAR:SAPMV50A:1708/btnBT_MKAL_T"
            ).press()
            # Unselect first row 
            session.findById(
                f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK"
            ).getAbsoluteRow(0).selected = False

            # Focus material field
            session.findById(
                f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/ctxtLIPS-MATNR[1,0]"
            ).setFocus()

            # Press POLO
            session.findById(
                f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/subSUBSCREEN_ICONBAR:SAPMV50A:1708/btnBT_POLO_T"
            ).press()

            # Confirm popup
            session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
        

        # Switch to overview tab
        session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01").select()
        session.findById("wnd[0]").sendVKey(0)

        # Focus quantity field
        session.findById(
            "wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-G_LFIMG[2,0]"
        ).setFocus()
        time.sleep(1)
        session.findById(
            "wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-G_LFIMG[2,0]"
        ).caretPosition = 1
        session.findById("wnd[0]").sendVKey(0)

        # Return to picking tab
        session.findById(f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}").select()
        session.findById(
            f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]"
        ).setFocus()

    # --- Try tab \02 first, if fails use tab \01 ---
    for tab_try in ["02", "01"]:
        try:
            process_tab(tab_try)
            break
        except Exception as e:
            print(f"Tab {tab_try} failed: {e}")
            raise Exception("Didn't Work")
