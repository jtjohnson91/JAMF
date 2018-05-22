SUBJECT="<email subject>"
EMAIL="<email recipient>"
FILE1="firefoxreport.csv"
FILE2="brewreport.csv"
FILE3="chromereport.csv"
FILE4="macappreport.csv"
BODY=".msgbody.txt"

cd <full path to file>/Application_Reports/.FIREFOX && sh firefox.sh
cd <full path to file>/Application_Reports/.BREW && sh brew.sh
cd <full path to file>/Application_Reports/.MAC && sh mac.sh
cd <full path to file>/Application_Reports/.CHROME && sh chrome.sh
cd <full path to file>/Application_Reports/  && mutt -s "$SUBJECT" $EMAIL -a $FILE1 -a $FILE2 -a $FILE3 -a $FILE4 < $BODY
