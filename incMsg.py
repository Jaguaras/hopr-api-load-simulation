
import json
import requests
import datetime 
from websocket import create_connection
ws = create_connection("ws://127.0.0.1:3001/api/v2/messages/websocket?apiToken=ACCESS_TOKEN")

counter = 0
while True:
    result = ws.recv()
    if 'ack' not in result:
        counter += 1
        print(str(counter) + " - " + str(datetime.datetime.utcnow()) + ": GOT MSG!")
        
ws.close()