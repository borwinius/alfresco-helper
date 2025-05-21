#!/usr/bin/env python3
# getnodepath.py
# get the path of a filenode for webdav,ftp,cifs / rb / 2025
import requests, json
###################################
mysrv = 'http://myalfsrv.my.dom.ain:8080'
myauth=("admin","admin")
# id of the filenode:
parentId = "7bb7bfa8-997e-4c55-8bd9-2e5029653bc8"
mypath = ""
name = ""

def getmetadata(parentId):

    myurl = f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{parentId}"
    r = requests.get(myurl, auth = myauth)
    j = json.loads(r.content)
    name = (j["entry"]["name"])
    createdByUser = (j["entry"]["createdByUser"]["id"])
    parentId = (j["entry"]["parentId"])
    return name, createdByUser, parentId

while  name != "Sites":
         name, createdByUser, parentId = getmetadata(parentId)
         mypath=f"/{name}{mypath}"

# you should get like this:
#  "/Sites/swsdp/documentLibrary/Budget Files/Invoices/inv I200-189.png"
print(mypath)
