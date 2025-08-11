from connectionSAP import connection
import time

def outBoundDelivery(session):
    try:
        time.sleep(0.7)
        status_bar_text = session.findById('wnd[0]/sbar').Text
        words = status_bar_text.split()
        
        for word in words:
            if word.isdigit() and len(word) >= 10:
                print(f"Document Number: {word}")
                return word   # return the first valid document number
        
        # If no valid digit found
        print("No document number found.")
    except Exception as e:
        print(f"Error while fetching document number: {e}")
    
    raise Exception("Error: Document Number Not Found")

def documentVF01(session):
    try:
        time.sleep(0.7)
        status_bar_text = session.findById('wnd[0]/sbar').Text
        words = status_bar_text.split()
        
        for word in words:
            if word.isdigit() and len(word) >= 10:
                print(f"Document Number: {word}")
                return word   # return the first valid document number
        
        # If no valid digit found
        print("No document number found.")
    except Exception as e:
        print(f"Error while fetching document number: {e}")
    
    raise Exception("Error: Document Number Not Found")


def checkError(session):
    try:
        time.sleep(0.7)
        status_bar_text = session.findById('wnd[0]/sbar').Text
        
        
        return status_bar_text  # return the first valid document number
        
    except Exception as e:
        print(f"Error while fetching document number: {e}")
    
        raise Exception("Error: Document Number Not Found")