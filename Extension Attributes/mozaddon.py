#!/usr/bin/python
import json, glob
fp = None
path = "/Users/*/Library/Application Support/Firefox/Profiles/*.default/addons.json"
for filename in glob.glob(path):
    with open(filename, 'r') as fp:
        obj = json.load(fp)
if fp != None:
       	print "<result>"
       	for x in obj["addons"]:
               	print "Name: " + x["name"].encode('utf-8')
               	print "Version: " +  str(x["version"].encode('utf-8'))
               	print "ID: " + x["id"]
               	print "Description: " + x["description"].encode('utf-8') + "\n"
       	print "</result>"
else:
       	print "<result>NA</result>"
