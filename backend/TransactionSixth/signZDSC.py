import time

def sign(session):
    session.findById("wnd[0]/tbar[1]/btn[16]").press()
    session.findById("wnd[0]/tbar[1]/btn[13]").press()
    print("Pressed Select All")
    time.sleep(1)
    session.findById("wnd[0]").sendVKey(12)
    try:

        session.findById("wnd[1]/tbar[0]/btn[0]").press()
    except:
        pass
    session.findById("wnd[0]/tbar[0]/btn[3]").press()