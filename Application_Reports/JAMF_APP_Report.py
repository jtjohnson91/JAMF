#!/usr/bin/python
import requests, json, time, os, jwt, client, difflib
from json import dumps
from httplib2 import Http
from datetime import date
from pathlib import Path

##FUNCTIONS##

def writebl(data1,data2):
 for x in app:
  newfile = open(file1, 'a')
  newfile.write(x)
  newfile.close()
 time.sleep(2)
 cmd = 'sort -u ' + file1 + ' -o ' + file2
 os.system(cmd)

def writenew(data1,data2,data3,data4,data5,data6):
 bl= Path(file1)
 if not bl.is_file():
  writebl(app,file1)
 for x in app:
  newfile = open(file2, 'a')
  newfile.write(x)
  newfile.close()
 time.sleep(2)
 cmd = 'sort -u ' + file2 + ' -o ' + file2
 os.system(cmd)
 diffalert(appname,file1,file2,file3,response)

def diffalert(data1,data2,data3,data4,data5):
 bl = open(file1, 'r')
 new = open(file2, 'r')
 dif = open(file3, 'w')
 diff = difflib.ndiff(bl.readlines(),new.readlines())
 dif.write(''.join(diff))
 dif.close
 dif = open(file3, 'r')
 difflines = dif.readlines()
 x = []
 for line in difflines:
  if line.startswith('+'):
      x.append(line)
 x = str(x)
 headers2 = {'Content-Type': 'application/json'}
##Webhook##
 url = "<INSERT GOOGLE CHAT WEBHOOK HERE>"
 parts = x
 parts = parts.replace('"', '')
 parts = parts.replace("'+ ", "")
 parts = parts.replace("[", "")
 parts = parts.replace("]", "")
 parts = parts.replace(", ", "")
 parts = parts.replace("\\n'", "<br>")
 parts = parts.split("<br>")
 appinstalled = []
 parts.remove('')
 for item in parts:
  for p in json.loads(response.text)["computer_applications"]["versions"]:
   for y in p["computers"]:
    q = str(y)
    if q.find('%s' % (item) + '\\n') != -1:
     appinstalled.append("<b>" + item + "</b>" + " Installed By " + y["Full Name"])
 appinstalled = str(appinstalled)
 appinstalled = appinstalled.replace("[", " ")
 appinstalled = appinstalled.replace("]", "")
 appinstalled = appinstalled.replace("u'", "")
 appinstalled = appinstalled.replace(",", "<br>")
 appinstalled = appinstalled.replace("' ", "<br>")
 appinstalled = appinstalled.replace("'", "")
 msg = {'cards': [{'header': {'title': 'JAMF Reports New %s Installed' % (appname)}, 'sections': [{'widgets': [{'textParagraph': {'text': appinstalled}}]}, {'widgets': [{'buttons': [{'textButton': {'text': 'Navigate to JAMF Cloud', 'onClick': {'openLink': {'url': 'https://thesyscat.jamfcloud.com'}}}}]}]}]}]}
 if x != '[]':
  Http().request(
   uri=url,
   method='POST',
   headers=headers2,
   body=dumps(msg)
  )
 bl.close()
 new.close()
 dif.close()
 baseline(file1, file2, file3)

def baseline(data1,data2,data3):
 cmd = 'mv ' + file2 + ' ' + file1 + '; rm ' + file3
 os.system(cmd)

##API CALL##
DOMAIN="<INSERT DOMAIN NAME HERE FOR JAMF SERVER>"
API="JSSResource/computerapplications/application/Mail.app/version/*/inventory/zAPI%20Mozilla%20Add-ons,Brew%20Packages,zAPI%20Chrome%20Extensions,Full%20Name,zAPI%20Macbook%20Applications"
USER="<API USER NAME>"
PASS="<API USER PASSWORD>"
headers = {
    'accept': 'application/json',
}
response = requests.get('https://%s/%s' % (DOMAIN, API), headers=headers, auth=(USER, PASS))

##BREW##
file1 = '<INSERT PATH HERE>/brew.csv'
file2 = '<INSERT PATH HERE>/brewnew.csv'
file3 = '<INSERT PATH HERE>/brewdiff'
appname = 'Brew Package'
app = []
for x in json.loads(response.text)["computer_applications"]["versions"]:
 for y in x["computers"] :
  app.append(y["Brew Packages"].encode('utf-8'))
writenew(appname,app,file1,file2,file3,response)

##FIREFOX##
file1 = '<INSERT PATH HERE>/firefox.csv'
file2 = '<INSERT PATH HERE>/firefoxnew.csv'
file3 = '<INSERT PATH HERE>/firediff'
appname = 'Firefox Add-on'
app = []
for x in json.loads(response.text)["computer_applications"]["versions"]:
 for y in x["computers"] :
  app.append(y["zAPI Mozilla Add-ons"].encode('utf-8'))
writenew(appname,app,file1,file2,file3,response)

##MAC##
file1 = '<INSERT PATH HERE>/mac.csv'
file2 = '<INSERT PATH HERE>/macnew.csv'
file3 = '<INSERT PATH HERE>/macdiff'
appname = 'Macbook Application'
app = []
for x in json.loads(response.text)["computer_applications"]["versions"]:
 for y in x["computers"] :
  app.append(y["zAPI Macbook Applications"].encode('utf-8'))
writenew(appname,app,file1,file2,file3,response)

##CHROME##
file1 = '<INSERT PATH HERE>/chrome.csv'
file2 = '<INSERT PATH HERE>/chromenew.csv'
file3 = '<INSERT PATH HERE>/chromediff'
appname = 'Chrome Extension'
app = []
for x in json.loads(response.text)["computer_applications"]["versions"]:
 for y in x["computers"] :
  app.append(y["zAPI Chrome Extensions"].encode('utf-8'))
writenew(appname,app,file1,file2,file3,response)
