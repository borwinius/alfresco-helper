#!/usr/bin/env python3
# chguserpw.py / rb / 2025
# reset the userpassword to "changeme" for a user named "theusername"

import requests, json

myurl = f"https://myalfsrv.my.dom.ain/alfresco/service/api/person/changepassword/theusername"
myauth=("admin","admin")
myjson = {'newpw': 'changeme'}
x = requests.post(myurl, json = myjson, auth = myauth, verify=False)
print(x.text)
