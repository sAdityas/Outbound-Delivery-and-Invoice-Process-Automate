import win32com.client
import pythoncom
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
RESET = '\x1b[0m'

def connection():
    try:
        pythoncom.CoInitialize()
        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        application = SapGuiAuto.GetScriptingEngine
        session = application.Children(0).Children(0)
        Client = session.info.Client
        User = session.info.User 
        return session
    except:
        raise Exception('Error: SAP is not logged in OR User Cancelled the Transaction') 
 
