#!/usr/bin/env python
import getpass
from pexpect import pxssh

devices = {'r1': {'prompt': 'r1#', 'ip': '10.10.20.70 -p 2221'},
        'r2': {'prompt': 'r2#', 'ip': '10.10.20.70 -p 2231'}}

commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

# starts the loop for devices
for device in devices.keys():
    outputFilename = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pxssh.pxssh()
    child.login(devices[device] ['ip'], username.strip(), password.strip(), auto_prompt_reset=False)

    #starts the loop for commands and write to output
    with open(outputFilename, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)

child.logout
