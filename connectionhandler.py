# ----------------------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Handles each client connection in a separate thread.
# ----------------------------------------------------------------------

from logformat import buildLogMessage

def handleClientConnection(connSocket, addressPair, configDict, rateLimiter):
    clientID = f"{addressPair[0]}:{addressPair[1]}" # combine IP and port
    logFilePath = configDict.get("log_file", "my_log_output.txt") # read log file path
    formatTemplate = configDict.get("log_format", "[{timestamp}] [{level}] [CLIENT={client_id}]: {message}") # read format

    try: # trying to block so we can try to handle incoming data
        while True: # infinite loop
            dataBytes = connSocket.recv(1024) # reading up to 1024 bytes ( Didt see any requremtns so i limited to this for the SET standard)
            if not dataBytes: # if no data
                break # break the loop
            textLine = dataBytes.decode("utf-8").strip() # decode to string
            if "::" in textLine: # if "::"
                parts = textLine.split("::", 1) # split once
                levelPart = parts[0].strip() # left side level
                messagePart = parts[1].strip() # and right is message
                if rateLimiter.allowMessage(clientID): # if we are allowed
                    finalLine = buildLogMessage(formatTemplate, levelPart, clientID, messagePart) # build line
                    with open(logFilePath, "a", encoding="utf-8") as lf: # open file in append mode
                        lf.write(finalLine + "\n") # write line plus newline
                else: # rate limited
                    with open(logFilePath, "a", encoding="utf-8") as lf: # open file
                        lf.write(f"[RATE-LIMITED] [CLIENT={clientID}] {messagePart}\n") # log blocked
            else: # no "::"
                with open(logFilePath, "a", encoding="utf-8") as lf: # open file
                    lf.write(f"[BAD-FORMAT] [CLIENT={clientID}] {textLine}\n") # log bad format
    except Exception as ex: # catch exceptions
        print("Error in handleClientConnection:", ex) # print error
    finally: # finally block
        connSocket.close() # close the connection