# Create class with ASCII colors

class colors:
    def __init__(self):
        pass

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    RED_BG = '\033[41m'
    GREEN_BG = '\033[42m'
    YELLOW_BG = '\033[43m'
    BLUE_BG = '\033[44m'
    MAGENTA_BG = '\033[45m'
    CYAN_BG = '\033[46m'
    WHITE_BG = '\033[47m'

    BRIGHT_RED_BG = '\033[101m'
    BRIGHT_GREEN_BG = '\033[102m'
    BRIGHT_YELLOW_BG = '\033[103m'
    BRIGHT_BLUE_BG = '\033[104m'
    BRIGHT_MAGENTA_BG = '\033[105m'
    BRIGHT_CYAN_BG = '\033[106m'
    BRIGHT_WHITE_BG = '\033[107m'

    
    CURSOR_UP_ONE = '\033[A'
    ERASE_LINE = '\x1b[2K'

    def print(message, color, background=None):
        if background is None:
            print(color + message + colors.ENDC)
        else:
            print(color + background + message + colors.ENDC)

    def input(message, messageColor, inputColor, background=None):
        if background is None:
            message = input(messageColor + message + colors.ENDC + inputColor)
            print(colors.ENDC)
            return message
        else:
            message = input(messageColor + background + message + colors.ENDC + inputColor)
            print(colors.ENDC)
            return message
    
    def reset_color():
        print(colors.ENDC)