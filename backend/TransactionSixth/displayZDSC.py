import time

def display(session, numofinvoices):
    session.findById("wnd[0]/tbar[1]/btn[16]").press()
    session.findById("wnd[0]/tbar[1]/btn[13]").press()
    print("Waiting For user to Click on Remember me and Allow.")
    for _ in range(numofinvoices):
        for _ in range(3):
            try:
                time.sleep(0.5)
                session.findById("wnd[0]").sendVKey(12)
            except:
                pass
    time.sleep(0.5)
    session.findById("wnd[0]/tbar[0]/btn[3]").press()
