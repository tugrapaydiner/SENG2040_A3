# ------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Entry point that loads config & starts server.
# ------------------------------------------------------

import sys
import configloader
import loggingservice

def mainFunction():
    configPath = None
    if len(sys.argv) > 1: # if we have any arguments
        configPath = sys.argv[1] # take the first as path
    else: # no argument
        configPath = None # keep None
    configData = configloader.loadServerConfig(configPath) # load config from file or fallback
    loggingservice.startLoggingServer(configData) # start the logging server with config

if __name__ == "__main__": # if we run this file directly
    mainFunction() # call mainFunction