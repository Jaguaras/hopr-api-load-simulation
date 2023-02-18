from hoprApi import *
import random, time
from concurrent.futures import ThreadPoolExecutor
import datetime 
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return (result_str)

def random_address():
    peerid_list = [
        "NODE_PEER_ID_1", 
        "NODE_PEER_ID_2"
        ]
    return random.choice(peerid_list)

def task(name):
    return(str(datetime.datetime.utcnow()) + " " + str(send_message(random_address(), get_random_string(483), [""] )))
    
with ThreadPoolExecutor(100) as executor:
    futures = [executor.submit(task, i) for i in range(120)]
    for future in futures:
        print(future.result())