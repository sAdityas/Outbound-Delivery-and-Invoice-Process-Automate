def asn(session):
    try:

        session.findById('wnd[0]/tbar[0]/okcd').text = '/nzmah_asn'
        session.findById("wnd[0]").sendVKey(0)
    except:
        raise Exception('Error while entering T-Code')