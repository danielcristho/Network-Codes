#!/usr/bin/env python3

import requests
import json
import urllib3

url='https://131.226.217.151/ins'
switchuser='cisco'
switchpassword='C1sco_1234'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "hostname nx-osv-2-new",
      "version": 1.2
    },
    "id": 1
  }
]

urllib3.disable_warnings()
response = requests.post(url, verify=False, data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()