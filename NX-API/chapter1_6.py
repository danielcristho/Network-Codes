#!/usr/bin/env python3

from ncclient import manager 

conn = manager.connect (
    host = '131.226.217.151',
    port = 22,
    username = 'cisco',
    password = 'C1sco_1234',
    hostkey_verify = False,
    device_params = {'name': 'nexus'},
    look_for_keys = False
)

for value in conn.server_capabilities:
    print (value)

conn.close_session()
