#!/usr/bin/env python3
# import os, pwd, 
import json, requests
# chgSiteUsers.py
# ermittle in allen Alfresco-Sites(!) die Benutzer und Gruppen
# und stufe diese auf Mitarbeiter und Gruppen nur noch mit Leserechten zurück
# die Site-Manager bleiben davon unberührt

mysrv = 'http://myalfsrv.my.dom.ain:8080'
myauth = ("admin","admin")
myrole = 'SiteConsumer'
srcurl = f"{mysrv}/alfresco/service/api/sites"

r = requests.get(srcurl, auth = myauth)
#print(r.text)
j = json.loads(r.content)
for entry in j:
    shname = entry["shortName"]
    print("SiteshortName: ",shname)
    srcurl = f"{mysrv}/alfresco/service/api/sites/{shname}/memberships"
    r = requests.get(srcurl, auth = myauth)
    j = json.loads(r.content)
    for entry in j:
      role = entry["role"]
      # print(entry)
      aT = entry["authority"]["authorityType"]
      # print(aT)

      if "USER" in aT:
        user = entry["authority"]["userName"]
        print("user: ",user,"role: ",role)
        myurl = f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/members/{user}"
        myjson = {'role': myrole}
        x = requests.put(myurl, json = myjson, auth = myauth)

      if "GROUP" in aT:
        group = entry["authority"]["fullName"]
        print("group: ",group,"role: ",role)
        myurl = f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/groupmembers/{group}"
        myjson = {'role': myrole}
        x = requests.put(myurl, json = myjson, auth = myauth)
