def gotoZDSC(session):
    session.findById("wnd[0]/tbar[0]/okcd").text = '/nZDSC'
    session.findById("wnd[0]").sendVKey(0)