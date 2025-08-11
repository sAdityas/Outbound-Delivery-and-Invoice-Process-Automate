from TransactionSecond.VL01N import VL01N
from TransactionSecond.ZTRDEnter import EnterZtrd

def checkRows(session,SaleOrder,Plant):
    flag = 0
    VL01N(session)
    EnterZtrd(session, SaleOrder, Plant)
    def tryCheck(flag,tab_code, subscreen_code, table_suffix):
        
        
        for i in range(1000):
            try:
                nextText = session.findById(
                    f"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\{tab_code}/"
                    f"ssubSUBSCREEN_BODY:SAPMV50A:{subscreen_code}/"
                    f"tblSAPMV50ATC_LIPS_{table_suffix}/ctxtLIPS-MATNR[1,{i}]"
                ).Text
                flag+=1
                if nextText == '':
                    flag -= 1
                    return flag
            except Exception:
                raise Exception("Didn't Work")
        return 0

    for tab_try in ["01", "02"]:
        for subscreen_code in ["1104", "1102"]:
            for table_suffix in ["PICK", "OVER"]:
                try:
                    return tryCheck(flag,tab_try, subscreen_code, table_suffix)
                except Exception as e:
                    raise Exception(f"Tab {tab_try}, subscreen {subscreen_code}, table {table_suffix} failed: {e}")
    return 0