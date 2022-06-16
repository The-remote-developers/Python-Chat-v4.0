import json
import os
from libs.functions import debugger_log, variable

dir = os.path.join(os.getcwd(), "config.json")
with open(dir, "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    
    variable.set("config_debug", data["App_config"]["debug"]) # 0 - Write and open console log, 1 - Write only, 2 - Nothing
    variable.set("config_appVersion", data["App_config"]["appVersion"])
    variable.set("config_appName", data["App_config"]["appName"] + " " + str(variable.get("config_appVersion")))

    variable.set("Database_config", data["Database_config"])
    
    debugger_log("info", "[CONFIG] Loaded config: " + str(data))
    jsonfile.close()
