# -----------------------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Builds final log lines with placeholder replacements.
# -----------------------------------------------------------------------

from helper import getCurrentTimestamp

def buildLogMessage(formatString, levelString, clientID, messageBody):
    rawLevel = levelString.upper() # convert to uppercase
    tempString = formatString # store in temp
    if "{timestamp}" in tempString: # placeholder present
        tempString = tempString.replace("{timestamp}", getCurrentTimestamp()) # replace it
    else: # not present
        tempString += " " + getCurrentTimestamp() # get time anyway
    if "{level}" in tempString: # if level placeholder
        tempString = tempString.replace("{level}", rawLevel) # replace with uppercase
    else: # not found
        tempString += " " + rawLevel # add to end
    if "{client_id}" in tempString: # if client_id placeholder
        tempString = tempString.replace("{client_id}", str(clientID)) # replace
    else: # missing
        tempString += " " + str(clientID) # add ID manually
    if "{message}" in tempString: # if message placeholder
        tempString = tempString.replace("{message}", messageBody) # replace
    else: # missing
        tempString += " " + messageBody # just add on message
    return tempString #final result