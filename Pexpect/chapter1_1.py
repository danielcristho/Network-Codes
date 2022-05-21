from pexpect import pxssh
child = pxssh.pxssh()

child.login('10.10.20.70 -p 2221', 'admin', 'admin', auto_prompt_reset=False)
child.sendline('show version | i V')
child.expect('r1#')
child.before
child.logout()