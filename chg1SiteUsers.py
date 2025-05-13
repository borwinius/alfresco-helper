#!/usr/bin/env python3
import os, pwd, json, requests
# chgSiteUsers.py
# ermittle aus einer Site die benutzer und Gruppen
# und stufe diese auf Mitarbeiter mit Leserechten zurück
# der letzte Manager der site wird nicht geändert.

mysrv = 'http://sdestecmstest.de.caecorp.cae.com:8080'
myauth = ("admin","admin")
myrole = 'SiteConsumer'
srcurl = f"{mysrv}/alfresco/service/api/sites"
shname = "mytestsite"

print("SiteshortName: ",shname)
srcurl = f"{mysrv}/alfresco/service/api/sites/{shname}/memberships"
r = requests.get(srcurl, auth = myauth)
j = json.loads(r.content)
for entry in j:
      role = entry["role"]
      aT = entry["authority"]["authorityType"]
      if "USER" in aT:
        user = entry["authority"]["userName"]
        print("role: ",role,"user: ",user)
        myurl = f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/members/{user}"
        myjson = {'role': myrole}
        x = requests.put(myurl, json = myjson, auth = myauth)
      if "GROUP" in aT:
        group = entry["authority"]["fullName"]
        #print(entry["authority"])
        print("role: ",role,"id: ",group)
        myurl = f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/group-members/{group}"
        myjson = {'role': myrole}
        x = requests.put(myurl, json = myjson, auth = myauth)
        print(x.text)
