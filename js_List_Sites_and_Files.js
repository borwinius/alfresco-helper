// https://myalfresco.my.dom.ain/share/page/console/admin-console/javascript-console
// liste all Sites und die Anzahl der Dateien auf / rb / 2025
var s = {};
var x = {};

s.page = {};
x.page = {};
	
//s.query         = "SELECT cmis:objectTypeId, cmis:name,cmis:lastModifiedBy,cmis:createdBy,cmis:objectId,cmis:parentId,cmis:lastModificationDate FROM st:site ORDER BY cmis:lastModificationDate";
s.query         = "SELECT * FROM st:site ORDER BY cmis:lastModificationDate";

//s.language      = 'cmis-strict';
s.language      = 'cmis-alfresco';
s.page.maxItems = 20000;

var nodes = search.query(s);

print("Anzahl Sites: "+nodes.length);
for each(var node in nodes) {
	
	r = (JSON.stringify(node.nodeRef).replace("workspace://SpacesStore/", ""));
	q = "SELECT cmis:objectId FROM cmis:document where IN_TREE("+r+")";
	q = (q.replace("\"", "'"));
	x.query = (q.replace("\"", "'"));
    x.language      = 'cmis-alfresco';
    x.page.maxItems = 20000;
    var nodesf = search.query(x);

    print("Anzahl Dateien in Site: "+ node.name +" : " +nodesf.length);
      for each(var nodex in nodesf) {
      //print(nodex.name + " " + nodex.lastModificationDate + nodex.nodeRef);
	  }
}
///
