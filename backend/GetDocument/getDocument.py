from connectionSAP import connection
import time

def outBoundDelivery(session):
    try:
        time.sleep(0.7)
        status_bar_text = session.findById('wnd[0]/sbar').Text
        words = status_bar_text.split()
        for word in words:
            if word.isdigit() and len(word) >= 10:
                pass
            else:
                print(f'Document Number:{word}')
                OD = word
            return word
        else:
            print('No document number found.')
    except:
        pass
    raise Exception('Error: Document Number Not Found')

def documentVF01(session):
    try:
        time.sleep(0.7)
        status_bar_text = session.findById('wnd[0]/sbar').Text
        words = status_bar_text.split()
        for word in words:
            if word.isdigit() and len(word) >= 10:
                pass
            else:
                print(f'Document Number: {word}')
                vf = word
                return word
        else:
            print('No document number found.')
    except:
        pass
    raise Exception('Error: Document Number Not Found')