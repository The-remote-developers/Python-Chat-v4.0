# Application chat v4.0
# Import module
import pwinput
import atexit
from tabulate import tabulate
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.validation import Validator, ValidationError

# Setting the working directory to the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import custom module
from libs.config import *
from libs.functions import *
from libs.config import *
from libs.colors import *
from libs.database import *
from libs.security import *
from libs.chat import *

debugger_log("info", "[MAIN] Current Working Directory " + os.getcwd()) # Debug

os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
colors.reset_color()

message_stream = getMessageStream()

# Message validator
class TextEmptyValidator(Validator):
    def validate(self, document):
        text = document.text
        if text == "":
            raise ValidationError(message='Message is empty!')

def main():
    debugger_log("debug", "[FUNCTION] Run main function") # Debug

    colors.print("Welcome to " + variable.get("config_appName"), colors.BRIGHT_GREEN)
    # Ask for username
    username = colors.input("Please enter your username: ", colors.MAGENTA, colors.BRIGHT_GREEN)

    # Check if username is in database
    if(username in database.getUsernames()):
        debugger_log("info", "[FUNCTION] User " + username + " logged into system. Waiting for the passcode") # Debug
        variable.set("username_logged", username)
        # Ask for passcode to unlock program
        passcode = pwinput.pwinput(colors.MAGENTA + "Please enter passcode to unlock program: " + colors.BRIGHT_GREEN)

        colors.reset_color()

        if(security.verifyPasscode(passcode, database.getPasscode())):
            debugger_log("success", "[FUNCTION] User " + username + " logged into system") # Debug
            colors.print("Welcome " + username, colors.BRIGHT_GREEN)
            # Set online status to true
            database.setOnlineStatus(username, True)

            # Get users connected to chat and filter only if online
            # Get all status of users and last seen of users. If user is online, add to list and add last seen to list

            users = database.getUsernames()
            users_online = database.getOnlineStatus()
            users_last_seen = database.getLastSeen()

            users_username_filtered = [] # Store only online users username
            users_online_filtered = []
            users_last_seen_filtered = []

            for user in users:
                # Get user i
                i = users.index(user)
                if(users_online[i]):
                    users_online_filtered.append(user)
                    users_last_seen_filtered.append(users_last_seen[i])
                    users_username_filtered.append(user)

            # Create nested completer for message input
            completer = NestedCompleter.from_nested_dict(chat_commands.initCommand(users_username_filtered))

            print("Users connected:")

            # Concatenate username and last seen
            users_online = list(zip(users_username_filtered, users_last_seen_filtered))
            print(tabulate(users_online, headers=['Users', 'Last Seen'], tablefmt='fancy_grid'))

            print("Getting messages...\n")
            debugger_log("debug", "[FUNCTION] Getting messages...") # Debug
            def stream_handler(message):
                debugger_log("debug", "[FUNCTION] Run stream_handler function")
                try:
                    print(colors.CURSOR_UP_ONE + colors.ERASE_LINE)
                    for mess in message["data"].items():
                        print(security.decrypt(toBytes(mess[1])))
                    variable.set("message_stream_loading", True) # Messages are loaded
                    debugger_log("debug", "[FUNCTION] Messages loaded")
                except:
                    print(colors.CURSOR_UP_ONE + colors.ERASE_LINE)
                    print(security.decrypt(toBytes(message["data"])))
                    

            global message_stream
            message_stream = db.child("messages").stream(stream_handler)
            setMessageStream(message_stream)

            message = ''
            function.wait_until(lambda: variable.get("message_stream_loading") == True, 20)
            while message != 'END':
                # Ask for message
                message = prompt(chat.messageStyle(username), completer=completer, bottom_toolbar=chat.bottom_toolbar(username), style=chat.style, validator=TextEmptyValidator())
                # Check if message is a command
                if(chat_commands.checkCommand(message)):
                    # Remove "/" from message
                    message = message.replace("/", "")
                    # Execute command
                    chat_commands.executeCommand(message)
                else:
                    if message != "":
                    # Add date and time to message
                        message = "[" + function.getCurrentDateTime() + "] " + username + ": " + message
                        # Set last seen to current datetime
                        database.setLastSeen(username, function.getCurrentDateTime())
                        # Push message to database
                        # Encrypt message and push to database
                        database.pushMessage(security.encrypt(message))
                    else:
                        print("Message is empty")
            
        else:
            colors.print("Passcode not valid", colors.BRIGHT_RED)
            debugger_log("error", "[LOGIN] User " + username + " has falied login") # Debug
    else:
        debugger_log("error", "[DATABASE] User " + username + " not found in database") # Debug
        colors.print("User not found!", colors.BRIGHT_RED)

if __name__ == "__main__":
    try:
        colors.reset_color()
        main()
    except KeyboardInterrupt:
        colors.reset_color()
        # Set online status to false and close the message stream
        database.exitDB()

def exit_handler():
    colors.reset_color()
    # Set online status to false and close the message stream
    database.exitDB()
atexit.register(exit_handler)