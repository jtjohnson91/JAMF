1) Install extension attributes into JAMF. If you have already installed my other extension attributes you do not need to add the brew one again.

2) Edit each variable in the .run_reports.sh and .JAMF_API.sh scripts as well as completing file path for chosen directory in all .sh and .py files.

3) For the automated email to send with mutt you will need to edit your ~/.muttrc file appropriately. If you wish to not have an automated email sent just comment out (#) the last line in .run_reports.sh

4) Run sh Generate_Reports.sh to execute the creation of your reports.
