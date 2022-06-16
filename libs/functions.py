import datetime
import time

class variable:
    def __init__(self):
        pass

    # Create a variable    
    def set(variable, value):
        globals()[variable] = value
        debugger_log("info", "[VARIABLE] Created variable: " + variable)
        
    def get(variable):
        # If variable not found, return None
        try:
            return globals()[variable]
        except:
            return None

class function:
    def __init__(self):
        pass 
        
    # Function to get current time
    def getCurrentTime():
        return datetime.datetime.now().strftime("%H:%M:%S")
        
    # Function to get current date
    def getCurrentDate():
        return datetime.datetime.now().strftime("%d/%m/%Y")

    def getCurrentDateTime():
        return datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
        #debugger_log("debug", "[FUNCTION] Run wait_until function")
        mustend = time.time() + timeout
        while time.time() < mustend:
            if somepredicate(*args, **kwargs): 
                return True
            time.sleep(period)
        return False

debug = variable.get("config_debug")
if debug == 1 or debug == 2:
    from libs.console_log import logger
print(debug)

def debugger_log(type, string):    
    if debug == 1 or debug == 2:
        if type == "error":
            logger.error(string)
        elif type == "warning":
            logger.warning(string)
        elif type == "debug":
            logger.debug(string)
        elif type == "success":
            logger.success(string)
        elif type == "critical":
            logger.critical(string)
        elif type == "info":
            logger.info(string)
debugger_log("success", "[FUNCTION] debugger_log loaded...") # Debug
      
def toBytes(text):
    # Remove " from start and and ([1:-1]) of string and return bytes
    return text.encode().decode('unicode_escape').encode("raw_unicode_escape")#[1:-1]

message_stream = ""
def setMessageStream(stream):
    global message_stream
    message_stream = stream
    
def getMessageStream():
    return message_stream
