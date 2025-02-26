# ---------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Loads config from JSON or uses fallback.
# ---------------------------------------------------------

import json
import os
from defaultconfig import getFallbackConfig # get fallback config

def loadServerConfig(filePath=None): #load server config
    if filePath is None: # if not provided a path
        filePath = "server_config.json" # default to server_config.json
    if os.path.exists(filePath): # if exists
        with open(filePath, "r", encoding="utf-8") as theFile: # open the file
            loadedData = json.load(theFile) # parse JSON
        if len(loadedData) > 0: # if we actually got some data
            return loadedData # return that data
        else: # empty somehow
            return getFallbackConfig() # fallback to default config
    else: # path not found
        print("NOTICE: Config file not found, using fallback!") # print a note
        return getFallbackConfig() # return fallback