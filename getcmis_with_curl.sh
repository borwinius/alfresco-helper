#!bin/bash
# getcmis_with_curl.sh per xml / rb / 2025

echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'>query.xml
echo '<cmis:query xmlns:cmis="http://docs.oasis-open.org/ns/cmis/core/200908/">'>>query.xml
echo "<cmis:statement>SELECT cmis:name from st:site WHERE cmis:name ='software*'</cmis:statement>">>query.xml
echo '</cmis:query>' >>query.xml

curl -u admin:admin  -v -X POST http://myalfsrv.my.dom.ain:8080/alfresco/s/cmis/queries -H "Content-Type: application/cmisquery+xml" -d @query.xml
rm query.xml
