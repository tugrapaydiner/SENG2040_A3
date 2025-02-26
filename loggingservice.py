# ----------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Launches the TCP server and spawns threads.
# ----------------------------------------------------------

import socket 
import threading
from ratelimit import BasicRateLimiter
from connectionhandler import handleClientConnection

def startLoggingServer(configDict):
    hostVal = configDict.get("host", "0.0.0.0") # host from config
    portVal = configDict.get("port", 5001) # port from config
    if configDict.get("rate_limit_count"): # rate_limit_count
        limitCount = configDict["rate_limit_count"] # store it
    else: # if not default
        limitCount = 5 # fallback
    if configDict.get("rate_limit_interval_sec"): # if we have rate_limit_interval_sec
        limitWindow = configDict["rate_limit_interval_sec"] # store it
    else: # not?
        limitWindow = 10 # fallback
    rateLimiter = BasicRateLimiter(limitCount, limitWindow) # build limiter

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
    serverSock.bind((hostVal, portVal)) # bind host and port
    serverSock.listen(5) # start listening with backlog=5
    print(f"Server listening on {hostVal}:{portVal}") # show that we are listening

    try: # accepting new connections
        while True: # loop forever
            conn, addr = serverSock.accept() # accept new client
            print("New client connected ->", addr) # print who connected
            threadObj = threading.Thread( # create new thread
                target=handleClientConnection, # set handler
                args=(conn, addr, configDict, rateLimiter) # pass arguments
            )
            threadObj.daemon = True # set daemon so we can exit quickly
            threadObj.start() # start thread
    except KeyboardInterrupt: # if user hits Ctrl+C
        print("Shutting down server (keyboard interrupt).") # print a note
    finally: # finally block
        serverSock.close() # close the server socket