
[R00tX V1.1]

PrivEsc Script

<img src="https://github.com/darkseid-security/R00tX/blob/main/img/R00tX2.png">

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
 
TODO
============
 + Add more SUDO exploits
 
RUN
============
 + python3 R00tX.py or ./R00tX on bin file
 + Compile with pyinstaller to run on Linux without python or colorama installed
