import logging
import os
from libs.colors import *
from libs.functions import variable

debug = variable.get("config_debug")
write = False
if debug == 0:
    # Nothing
elif debug == 1:
    # Write only
    write = True
elif debug  == 2:
    # Write and open debug console
    os.system('start cmd /K python "' + os.path.join(os.getcwd(), "libs/console_view.py") + '"')
    write = True

logger = logging.getLogger(__name__)

# set success level
logging.SUCCESS = 25  # between WARNING and INFO
logging.addLevelName(logging.SUCCESS, 'SUCCESS')
setattr(logger, 'success', lambda message, *args: logger._log(logging.SUCCESS, message, args))

class CustomFormatter(logging.Formatter):

    format = "[%(asctime)s][%(name)s] [%(levelname)s] - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: colors.MAGENTA + format + colors.ENDC,
        logging.INFO: colors.CYAN + format + colors.ENDC,
        logging.WARNING: colors.BRIGHT_YELLOW + format + colors.ENDC,
        logging.ERROR: colors.BRIGHT_RED + format + colors.ENDC,
        logging.CRITICAL: colors.RED_BG + colors.BRIGHT_WHITE + format + colors.ENDC,
        logging.SUCCESS: colors.GREEN + format + colors.ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)



logger.setLevel(logging.DEBUG)

if write:
    ch = logging.FileHandler("./logs/debug.log")
    
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)