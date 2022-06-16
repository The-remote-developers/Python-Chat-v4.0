import pyrebase
from libs.functions import getMessageStream, variable, toBytes, debugger_log
import time

debugger_log("debug", "[DATABASE] Connecting to Firebase...")

# Firebase configuration
config = {
  "apiKey": variable.get("Database_config")["apiKey"],
  "authDomain": variable.get("Database_config")["authDomain"],
  "databaseURL": variable.get("Database_config")["databaseURL"],
  "storageBucket": variable.get("Database_config")["storageBucket"]
}

firebase = pyrebase.initialize_app(config) # Initialize firebase
# Set firebase realtime database reference
db = firebase.database()

debugger_log("debug", "[DATABASE] Connected to Firebase...")

class database:
  def __init__(self):
    pass

  #--------------#
  #---- MISC ----#
  #--------------#
  def getVersion():
    return db.child("version").get().val()
  
  def getPasscode():
    debugger_log("debug", "[FUNCTION] Run getPasscode function")
    passcode_enc = db.child("passcode").get().val()
    # Remove " from start and and ([1:-1]) of string and return bytes
    return toBytes(passcode_enc)
  
  def exitDB():
    debugger_log("debug", "[FUNCTION] Run exitDB function..") ## Debug
    while True:
        choose = input("Do you want to delete the logs? (yes|no): ")
        if choose == "yes" or choose == "":
            debugger_log("critical", "The logs will be deleted soon")
            time.sleep(0.5)
            fileVariable = open("./logs/debug.log", 'r+')
            fileVariable.truncate(0)
            fileVariable.close()
            print("Logs was deleted...")
            debugger_log("success", "Logs was deleted")
            

        if variable.get("username_logged") in database.getUsernames():
          debugger_log("success", "[USER] Setted online status to false for user: " + variable.get("username_logged"))
          database.setOnlineStatus(variable.get("username_logged"), False)
        else:
          debugger_log("error", "[USER] User not found")
          print('Username "'+variable.get("username_logged")+'" not found!')
        print('\nExting program')
        debugger_log("debug", "Exiting program...")
        message_stream = getMessageStream()
        message_stream.close()
        debugger_log("debug", "Closed message stream")
        exit()
  #------------------#
  #---- END MISC ----#
  #------------------#

  #---------------#
  #---- USERS ----#
  #---------------#
  def pushUsername(username):
    try:
      db.child("users").push(username)
    except Exception as e:
      print(e)
      return False
  
  def removeUsername(username):
    # Get all usernames
    all_users = db.child("users").get()
    # Loop through all usernames
    for user in all_users.each():
      # Check if username is in database
      if user.val() == username:
        # Remove username from database
        db.child("users").child(user.key()).remove()
        return True
    return False
    
  def getUsernames():
    usernames = []
    # Get all usernames
    all_users = db.child("users").get()
    # Loop through all usernames
    for user in all_users.each():
      # Add username to list
      usernames.append(user.key())
    return usernames

  def getLastSeen():
    last_seen = []
    # Get all usernames
    all_users = db.child("users").get()
    # Loop through all usernames
    for user in all_users.each():
      # Add username to list
      last_seen.append(user.val()["last_seen"])
    return last_seen
  
  def setLastSeen(username, last_seen):
    debugger_log("info", "[FUNCTION] Last seen for user " + username + " was set to " + last_seen) # Debug
    return db.child("users").child(username).update({"last_seen": last_seen})
  
  # Function to get online status of user
  def getOnlineStatus():
    # Get status of user
    user_status = []
    # Get all usernames
    all_users = db.child("users").get()
    # Loop through all usernames
    for user in all_users.each():
      # Add user status to list
      user_status.append(user.val()["online"])
    return user_status
  
  def setOnlineStatus(username, status):
    debugger_log("success", "[FUNCTION] The status of user " + username + " is changed") # Debug
    return db.child("users").child(username).update({"online": status})

  #-------------------#
  #---- END USERS ----#
  #-------------------#


  #--------------#
  #---- CHAT ----#
  #--------------#
  def pushMessage(message):
    # Trasform message to string
    try:
      message = str(message)[2:-1] # Remove b' from start and remove ' from end

      db.child("messages").push(message)
      return True
    except Exception as e:
      print(e)
      return False
  
  def removeMessage(message):
    try:
      db.child("messages").child(message).remove()
    except Exception as e:
      print(e)
      return False
  
  def getMessages():
    messages = []
    all_messages = db.child("messages").get()
    # Get all messages
    for message in all_messages.each():
      # Add message to list
      messages.append(message.val())
    return messages

  
  #------------------#
  #---- END CHAT ----#
  #------------------#