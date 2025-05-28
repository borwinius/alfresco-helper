#!/usr/bin/env python3
# createFolderwithWebDav.py / rb / 2025
# erstelle Verzeichnisstruktur auf dem ECMS
# needed before: apt install python3-webdavclient
import os
import webdav3.client as wc

mysrv = 'https://myalfsrv.my.dom.ain'
wdoptions = {'webdav_hostname': mysrv,'webdav_login': "admin",'webdav_password': "admin"}
wdclient = wc.Client(wdoptions)
mypath = r"Sites/mysite/documentLibrary/one/two/three"

print("check path: ",mypath)
p = mypath.split('/')
mysite = p[1]
myfolder = os.path.basename(mypath)
y = mypath.split(mysite)[1]
mypushpath = y.split(myfolder)[0]
z = ""

# create the folder(s) rekursiv with webdav if not exist
for x in p:
    z = z+"/"+x
    mywdpath = f"/alfresco/webdav{z}"
    if not wdclient.check(mywdpath):
       print(mywdpath," not exist, try create ...")
       wdclient.mkdir(mywdpath)
