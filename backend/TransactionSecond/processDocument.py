from connectionSAP import connection

def processDocument(session, Partner_ID):
    try:
        session.findById('wnd[0]/tbar[0]/btn[3]').press()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/ctxtLIPS-MATNR[1,0]').setFocus()
        session.findById('wnd[0]/tbar[1]/btn[8]').press()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\08').select()
        partnerID = session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\08/ssubSUBSCREEN_BODY:SAPMV50A:2114/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER_EXT[1,1]')
        partnerID.setFocus()
        partnerID.text = ''
        partnerID.text = Partner_ID
        session.findById('wnd[0]/tbar[0]/btn[3]').press()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/btnRV50A-CHMULT[7,0]').setFocus()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/btnRV50A-CHMULT[7,0]').press()
        for i in range(1, 100):
            try:
                Bqty = session.findById(f'wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-G_LFIMG[2,{i}]')
                pkQty = session.findById(f'wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV50A:1102/tblSAPMV50ATC_LIPS_OVER/txtLIPSD-PIKMG[18,{i}]').Text
                qty = Bqty.Text.strip()
                if qty == '':
                    break
            except:
                pass  # postinserted
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02').select()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]').setFocus()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]').text = ''
        for r in range(1,100):
            pikqty = session.findById(f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,{r}]").text.strip()
            if not pikqty:
                break
            session.findById(f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-PIKMG[7,{r}]").setFocus()
            session.findById(f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-PIKMG[7,{r}]").text = pikqty
            session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]').setFocus()
        session.findById('wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV50A:1104/tblSAPMV50ATC_LIPS_PICK/txtLIPSD-G_LFIMG[5,0]').caretPosition = 0
        session.findById('wnd[0]/tbar[1]/btn[20]').press()
    except Exception as e:
        raise e 