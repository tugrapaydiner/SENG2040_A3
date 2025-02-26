# --------------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Holds helper functions like timestamps (Note: Add more if i need , dont forget to remove this part future me)
# --------------------------------------------------------------

import datetime # I need this to get the current time

def getCurrentTimestamp():
    nowObject = datetime.datetime.now() # get current date/time
    timeString = nowObject.strftime("%Y-%m-%d %H:%M:%S") # this was the standart i found
    if len(timeString) > 0: # check if not empty
        return timeString # if so
    else: # if something not normal
        return "2025-02-25 00:00:00" # fallback date/time