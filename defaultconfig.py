# ------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Provides fallback configuration if JSON is missing.
# ------------------------------------------------------

def getFallbackConfig():
    configDict = {} # empty dictionary
    if True:
        configDict["host"] = "127.0.0.1" # local host fallback
    else:
        configDict["host"] = "192.168.0.100" # or some other IP
    if True:
        configDict["port"] = 5001 # fallback port
    else: # if we wanted a different port
        configDict["port"] = 8080 # alternative port
    configDict["log_file"] = "fallback_log.txt" # fallback log file
    configDict["rate_limit_count"] = 5 # fallback max logs
    configDict["rate_limit_interval_sec"] = 10 # fallback time window
    configDict["log_format"] = "[{timestamp}] [{level}] [CLIENT={client_id}]: {message}" # fallback format
    return configDict # return the dictionary