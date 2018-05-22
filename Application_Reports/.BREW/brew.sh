#!/bin/sh
python <fullpath to file>Application_Reports/.BREW/brew.py | sort -u | grep -v N/A > <fullpath to file>Application_Reports/brewreport.csv
