#!/bin/sh

DOMAIN="<JAMF Server>"
API="JSSResource/computerapplications/application/Mail.app/version/*/inventory/zAPI%20Mozilla%20Add-ons,Brew%20Packages,zAPI%20Chrome%20Extensions,Full%20Name,zAPI%20Macbook%20Applications"
#user account with read only priviledges is recommended
USER="<username>"
PASS="<password>"
FILE="<full path to file>.inv.json"

curl -H "accept:application/json" "https://$DOMAIN/$API" -u $USER:$PASS | python -m json.tool > $FILE
