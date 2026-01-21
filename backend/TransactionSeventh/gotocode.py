def asn(session):
    session.findById('wnd[0]/tbar[0]/okcd').text = '/nzmah_asn'
    session.findById("wnd[0]").sendVKey(0)