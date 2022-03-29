import pexpect
import sys

conn = pexpect.spawn('ssh admin@192.168.1.10')
conn.logfile = sys.stdout.buffer
conn.expect('password')
conn.sendline('admin')
conn.expect('>')
conn.sendline('enable')
conn.expect('Password')
conn.sendline('cisco')
conn.expect('#')
conn.sendline('conf t')
conn.expect('#')
conn.sendline('do show ip int brief')
conn.expect('#')

x = conn.before.decode('utf-8').splitlines()

conn.sendline('exit')

with open('log.txt','w') as file:
    for line in x:
        file.write(line + '\n')








