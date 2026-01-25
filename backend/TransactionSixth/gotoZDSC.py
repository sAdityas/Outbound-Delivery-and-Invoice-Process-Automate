def gotoZDSC(session):
    try:

        session.findById("wnd[0]/tbar[0]/okcd").text = '/nZDSC'
        session.findById("wnd[0]").sendVKey(0)
    except:
        raise Exception('Error while entering T-Code')