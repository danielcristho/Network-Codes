#!/usr/bin/env python3

import requests
import json


url='https://131.226.217.151/ins'
switchuser='cisco'
switchpassword='C1sco_1234'

requests.packages.urllib3.disable_warnings()

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface ethernet 2/12",
      "version": 1.2
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "description foo-bar",
      "version": 1.2
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "end",
      "version": 1.2
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "copy run start",
      "version": 1.2
    },
    "id": 4
  }
]

#urllib3.disable_warnings()
response = requests.post(url, verify=False, data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
