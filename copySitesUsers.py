#!/usr/bin/env python3
import os, pwd, json, requests
# copySitesUsers.py
# ermittle aus einer Site die Benutzer und
# erstelle diese mit den gleichen Rechten auf einem neuen Server


mysrcsrv = 'https://mysrcsrv.my.dom.aim'
mysrcauth = ("admin","mysecret")

mydestsrv = 'https://mydestsrv.my.dom.ain'
mydestauth = ("admin","admin")

srcurl = f"{mysrcsrv}/alfresco/service/api/sites"
r = requests.get(srcurl, auth = mysrcauth)
print(r.text)
j = json.loads(r.content)
for entry in j:
    shname = entry["shortName"]
    print("SiteshortName: ",shname)
    srcurl = f"{mysrcsrv}/alfresco/service/api/sites/{shname}/memberships"
    r = requests.get(srcurl, auth = mysrcauth)
    j = json.loads(r.content)
    for entry in j:
      role = entry["role"]
      print(role,":")
      user = entry["authority"]["fullName"]
      print(user)

#### add the users with their roles
      mydesturl = f"{mydestsrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/members"
      myjson = {'role': role, 'id': user}
      x = requests.post(mydesturl, json = myjson, auth = mydestauth)
      print(x.text)
