from connectionSAP import connection

def gotoCode(session):
    try:
        session.findById('wnd[0]/tbar[0]/okcd').text = '/nVF01'
        session.findById('wnd[0]').sendVKey(0)
    except Exception as e:
        raise e  
 
