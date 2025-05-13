#!/usr/bin/env python3
# copySites.py
# copy Alfresco-Sites from an old to a new Server
import requests
# import os, pwd
import json

### Site auf neuem Alfresco-Server estellen / rb / 2025
# https://api-explorer.alfresco.com/api-explorer/
###################################
mysrcsrv = 'https://oldalfsrv.my.dom.ain'
mysrcauth=("admin","passwdonoldsrv")
mydestsrv = 'https://newalfsrv.my.dom.ain'
mydestauth=("admin","passwdonnewsrv")

srcurl = f"{mysrcsrv}/alfresco/service/api/sites"
r = requests.get(srcurl, auth = mysrcauth)
# print(r.text)

j = json.loads(r.content)

for entry in j:

    # print("shortName: ",entry["shortName"]);
    mydesturl = f"{mydestsrv}/alfresco/api/-default-/public/alfresco/versions/1/sites"
    myjson = {'id': entry["shortName"],  'title': entry["title"], 'visibility': entry["visibility"], 'description': entry["description"] }
    shname = entry["shortName"]
    x = requests.post(mydesturl, json = myjson, auth = mydestauth)
    # print(x.text)

    ##### die Sitemanager auslesen und berechtigen ################
    # diese Benutzer müssen sich einmal am neuen Server angemeldet haben

    for sm in entry["siteManagers"] :
        myrol = 'SiteManager'
        mydesturl = f"{mydestsrv}/alfresco/api/-default-/public/alfresco/versions/1/sites/{shname}/members"
        myjson = {'role': myrol, 'id': sm}
        x = requests.post(mydesturl, json = myjson, auth = mydestauth)

        # print(x.text)

################################################
