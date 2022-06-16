import time
import os

os.system("title "+"Debug Console")
try:
    print("\033[1;32;40m" + "Debug Started!" + "\033[0m") ## Green

    def follow(thefile):
        thefile.seek(0,2)
        while True:
            line = thefile.readline().rstrip('\n')
            if not line:
                time.sleep(0.1)
                continue
            yield line
            
    patch = os.path.join(os.getcwd(), ".\logs\debug.log")
    logfile = open(patch,"r")
    loglines = follow(logfile)
    for line in loglines:
        print(line)
except Exception as e:
    print(e)
    