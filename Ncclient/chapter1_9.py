from ncclient import manager

conn = manager.connect(
    host='sandbox-iosxr-1.cisco.com',
    port=22,
    username='admin',
    password='C1sco12345',
    hostkey_verify=False,
    device_params={'name' : 'iosxr'},
    look_for_keys=False
)
for value in conn.server_capabilities:
    print(value)

conn.close_session()   