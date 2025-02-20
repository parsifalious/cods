import json
with open ("sample-data.json","r") as file:
    data=json.load(file)
interfaces=data["imdata"]
print("Interface Status")
print("="*80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)
for interface in interfaces:
    print("{:<50} {:<20} {:<8} {:<6}".format(
        interface["l1PhysIf"]["attributes"]["dn"], 
        interface["l1PhysIf"]["attributes"]["descr"], 
        interface["l1PhysIf"]["attributes"]["speed"], 
        interface["l1PhysIf"]["attributes"]["mtu"]
    ))