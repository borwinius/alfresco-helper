#!/usr/bin/env python3
# chguserpw.py / rb / 2025
# reset the userpassword to "changeme" for a user named "theusername"

import requests
import json

myauth = f"https://myalfsrv.my.dom.ain/alfresco/service/api/person/changepassword/theusername"
myjson = {'newpw': 'changeme'}
x = requests.post(myurl, json = myjson, auth = myauth, verify=False)
print(x.text)
