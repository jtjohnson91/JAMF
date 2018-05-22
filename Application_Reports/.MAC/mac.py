#!/usr/bin/python
import json, glob
fp = None
path = "inv.json"
for filename in glob.glob(path):
    with open(filename, 'r') as fp:
        obj = json.load(fp)
for x in obj["computer_applications"]["versions"]:
	for y in x["computers"]:
		print y["zAPI Macbook Applications"].encode('utf-8')
