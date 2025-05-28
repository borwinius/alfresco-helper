#!/usr/bin/env python3
# uploadFile.py / rb / 2025
# upload a file per api
import requests

mysrv = 'https://myalfsrv.my.dom.ain'
myauth=("admin","admin")
mypath = r"Sites/alfrescomigration/documentLibrary/Skripte/ein/zwei/drei"
print(mypath)

# upload a existing file
# old url = "http://localhost:8080/alfresco/service/api/upload"
files = {"filedata": open("afile.bin", "rb")}
data = {
"name":"testdatei.xlsx",
"cm:author":"myexistingusername",
"relativePath": mypath }

myurl =f"{mysrv}/alfresco/api/-default-/public/alfresco/versions/1/nodes/-root-/children"
x = requests.post(myurl, auth = myauth, files=files, data=data)

if x.status_code > 201:
   print(x.text)
else:
   print("file ",data["name"], " created in :", mypath)
