# alfresco-helper
## several Alfresco-helper-Files
### copySites.py  
#### Zweck:
übertrage von einem alten Alfresco-Server die Sites und Ihre Sitemanager auf einen neuen Alfresco-Server.  
Es werden nur die Sites angelegt und berechtigt.  
Es werden noch keine Dateien kopiert.
#### Voraussetzungen:  
beide Alfresco-Server sind gleichwertig konfiguriert.  
auf beiden Server sind die selben Benutzer angelegt.  
Bei LDAP-Authentifizierung müssen die Benutzer sich auf dem neuen Server einmalig angemeldet haben  
damit das Benutzerobjekt in der Datenbank angelegt wurde.  
Die Variablen "mysrcsrv", "mysrcauth", "mydestsrv", "mydestauth" müssen vorher mit den eigenen Werten angepasst werden.  
Backup/Snapshot vorher durchführen.
#### Ausführung:
  python3 copySites.py
#### Erfahrungen:
Alfresco 4.1 -> Alfresco 23.4.1 mit über 800 Sites  
Dauer: ca. 1h


