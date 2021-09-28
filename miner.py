import threading
import requests
import json
import time
import os
import sys

mineraddress = sys.argv[1]
node = sys.argv[2]

def mine(addr):
  while True:
    try:
      data = {
        ## two of the same because i dont remeber if the A is capitalized lolz
        "feeAddress": address,
        "rewardAddress": address,
        "feeadress": address,
        "rewardaddress": address
      }
      output = requests.post(f'{node}/miner/mine', json=data)
  
      threads = 1 # dont change it will only make mining go slower. 
  
      for _ in range(int(treads)):
        minerthread = threading.Thread(target=mine, args=(mineraddress))
        minerthread.start()
    except Exception as e:
      print(e)
      pass
  
 ## done i guess lolz ##
