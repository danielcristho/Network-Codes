#### Use this lab:
- [NX-API Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/dae38dd8-e8ee-4d7c-a21c-6036bed7a804?diagramType=Topology)
- [Cisco Meraki](https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology)

#### Configure switch
```yml
# conf t
# feature nxapi
# username cisco password C1sco_1234 role network-operator
# username cisco passphrase lifetime 99999 warntime 14 gracetime 3
# nxapi http port 80
# nxapi sandbox
```

#### launch in browser: http://yourip
