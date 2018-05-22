#!/usr/bin/python
import json, glob
path = "<full path to file>/Application_Reports/inv.json"
for filename in glob.glob(path):
    with open(filename, 'r') as fp:
        obj = json.load(fp)
for x in obj["computer_applications"]["versions"]:
	for y in x["computers"]:
		print y["zAPI Mozilla Add-ons"].encode('utf-8')
