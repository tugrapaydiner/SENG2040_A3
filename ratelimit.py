# ------------------------------------------------------------
# Date: 2025-02-25
# Author: Tugrap Turker Aydiner
# Description: Implemented a basic rate limiter for logs .
# ---------------------------------------------------------

import time
from collections import defaultdict

class BasicRateLimiter:
    def __init__(self, maxLogsAllowed, intervalSecs): # max logs + interval
        self.maxLogsAllowed = maxLogsAllowed # store max logs
        self.intervalSecs = intervalSecs # store interval in seconds
        self.clientHistory = defaultdict(list) # map from client / list of timestamps
    
    def allowMessage(self, clientID):
        nowPoint = time.time() # get current time
        if clientID not in self.clientHistory: # if never seen this client
            self.clientHistory[clientID] = [] # create empty list
        else: # 1f I do have record
            if len(self.clientHistory[clientID]) == 0: # list is empty
                pass # do nothing (just pass)
            else: # we have old timestamps
                while len(self.clientHistory[clientID]) > 0: # while we have timestamps
                    oldest = self.clientHistory[clientID][0] # get oldest time
                    age = nowPoint - oldest # how old is it
                    if age > self.intervalSecs: # if it is outside the interval
                        self.clientHistory[clientID].pop(0) # remove it
                    else: # within the interval
                        break # break out while loop
        
        currentCount = len(self.clientHistory[clientID]) # how many are left
        if currentCount < self.maxLogsAllowed: # if below max
            self.clientHistory[clientID].append(nowPoint) # add the new timestamp
            return True # allow
        else: # at or above limit
            return False # block