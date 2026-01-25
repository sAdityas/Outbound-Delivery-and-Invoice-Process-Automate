from connectionSAP import connection
import time
def GENEWAY(session,flag):
    try:
        try:
            for i in range(len(flag)):
                print(flag[i])
                if flag[i] == True:
                    session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").modifyCell(i,"DISTANCE","1")
                    flag[i] = False
                    print(flag[i])
                else:
                    pass
                session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").modifyCheckbox(i,"CHECK",True)
                session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").setCurrentCell(i,"CHECK")
                session.findById("wnd[0]/usr/cntlSDCONT/shellcont/shell").triggerModified()
        except:
            pass

        time.sleep(1)
        session.findById("wnd[0]/tbar[1]/btn[7]").press()
    except:
        raise Exception('Error while generating EWAYBILL')