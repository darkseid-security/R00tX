
[R00tX V1.2]

PrivEsc Enumeration Script

<img src="https://github.com/darkseid-security/R00tX/blob/main/Screenshots/rootx3.png">

Features
============
 + Checks if vulnerable to SUDO exploit CVE-2019-14287 if yes generates root shell
 + Checks if Root account has No password set
 + Checks current user permissions
 + Checks SUID binaries
 + Checks for Write Permissions 
 + Gets current username
 + Gets Kernal Version
 + Gets OS name and verion
 + Checks for any Cronjobs
 + List all users excluding service accounts
 + Checks read access to SSH private key
 + Checks for access to the shadow file
 + [*New Feature] Login to MYSQL as root with no passwd
 + [*New Feature] List installed software packages 
 
TODO
============
 + Add more SUDO exploits
 
RUN
============
 + python3 R00tX.py or ./R00tX on bin file
 + Compile with pyinstaller to run on Linux without python or colorama installed
