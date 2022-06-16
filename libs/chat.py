from libs.security import *
from libs.functions import *
from libs.colors import *
from libs.database import *
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
import os

class chat:
    def __init__(self):
        pass

    # Function to send message
    def sendMessage(message, username):
        debugger_log("debug", "[FUNCTION] Run senMessage function")
        # Encrypt message
        message = function.getCurrentDateTime() + " " + username + ": " + message
        encryptedMessage = security.encrypt(message)
        # Send encrypted message
        return encryptedMessage

    # Function to receive message
    def receiveMessage(message):
        debugger_log("debug", "[FUNCTION] Run receiveMessage function")
        # Decrypt message
        decryptedMessage = rsa.decrypt(message, privateKey).decode('utf-8')
        # Send decrypted message
        return decryptedMessage

    def bottom_toolbar(username):
            return HTML('Logged as <b><style bg="ansired">'+username+'</style></b>!')

    def messageStyle(username):
        messageStyle = [
            ('class:username', username),
            ('class:colon',    ':'),
            ('class:pound',    '> '),
        ]
        return messageStyle
    
    style = Style.from_dict({
        # User input (default text).
        '':          '#ff0066',

        # Prompt.
        'username': '#884444',
        'colon':    '#0000aa',
        'pound':    '#00aa00',
    })

class chat_commands:
    def __init__(self):
        pass
    
    def initCommand(user_online):
        global commands_dict

        commands_dict = {
            '/exit': None,
            '/logout': None,
            '/help': None,
            '/clear': None,
            '/poke': {}
            
        }
        for i in user_online:
            commands_dict['/poke'][i] = None
        return commands_dict


    def checkCommand(command):
        if command in commands_dict:
            return True
        else:
            return False

    def help():
        debugger_log("debug", "[FUNCTION] Run help function")
        print(colors.CURSOR_UP_ONE + colors.ERASE_LINE + """ 
        /exit - Exit chat
        /logout - Logout from chat
        /help - Show this help
        /clear - Clear chat
        /poke <user> - Poke user
        """)
    
    def executeCommand(command):
        command = "/" + command
        # Run command function if command is in commands_dict
        if chat_commands.checkCommand(command):
            if command == "/exit":
                database.exitDB()
            elif command == "/logout":
                database.exitDB()
            elif command == "/help":
                chat_commands.help()
            elif command == "/clear":
                os.system('cls')
            elif command == "/poke":
                pass
            
        else:
            print(colors.CURSOR_UP_ONE + colors.ERASE_LINE + "Command not found")
