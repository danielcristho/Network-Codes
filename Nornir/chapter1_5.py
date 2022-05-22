from nornir import InitNornir

#from nornir.plugins.tasks.networking import netmiko_send_command
# from nornir.plugins.functions.text import print_result

from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir()

result = nr.run (
    task=netmiko_send_command,
    command_string="show arp"
)
print_result(result)