#!/bin/bash
brew="ls /usr/local/Cellar"
if $brew > /tmp/brewpkg; then
		echo "<result>" && cat /tmp/brewpkg && echo "</result>"
else
		echo "<result>N/A</result>"
fi

rm /tmp/brewpkg

exit 0
