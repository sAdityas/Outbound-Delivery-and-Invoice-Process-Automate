from connectionSAP import connection
import time
def GENEWAY(session):
    flag = True
    i = 0
    while flag:
        try:
            session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").modifyCheckbox (i,"CHECK",True)
            session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").setCurrentCell (i,"CHECK")
            session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").triggerModified()
            print(f"Selecting Row{i}")
            
            i+=1
        except:
            flag = False

    # time.sleep(2)
    session.findById("wnd[0]/tbar[1]/btn[7]").press()
    print("pressed")