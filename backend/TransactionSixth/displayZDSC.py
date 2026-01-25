import time

def display(session, numofinvoices):
    try:
        session.findById("wnd[0]/tbar[1]/btn[16]").press()
        session.findById("wnd[0]/tbar[1]/btn[13]").press()
        for _ in range(numofinvoices):
            time.sleep(0.5)
            session.findById("wnd[0]").sendVKey(12)
        time.sleep(0.5)
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
    except:
        raise Exception('Error while displaying invoices')
