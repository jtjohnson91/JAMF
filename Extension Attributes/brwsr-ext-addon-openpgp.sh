#!/bin/bash
grep -s -R openpgp /Users/*/Library/Application\ Support/Google/Chrome/Default/Extensions/ > /tmp/output
\
grep -s -R openpgp /Users/*/Library/Application\ Support/Firefox/Profiles/*/extensions >> /tmp/output
\
if grep 'openpgp\|matches' /tmp/output > /dev/null; then
		echo "<result>True</result>" && rm /tmp/output
else
		echo "<result>False</result>" && rm /tmp/output
fi

exit 0

