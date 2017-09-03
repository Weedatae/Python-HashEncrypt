# coding : utf-8
# author : Weedatae
# Title : Script Multi
import time
import sys
import hashlib
import colorama
from colorama import Fore, Back, Style
colorama.init()
       
print(Fore.BLUE + "\n[1] = Encrypt Password" + Style.RESET_ALL)
print(Fore.RED + "Des nouveaux bientot.." + Style.RESET_ALL)
choix = input("\nNuméro : ")

if choix != "1":
		print("\nerror")
		sys.exit(1)

if choix == "1":
 print("Chargement...")
 time.sleep(3)
md5 = input("\nMot de passe a encrypt [MD5] : ")
print("" + Fore.MAGENTA + hashlib.md5(md5.encode('utf-8')).hexdigest() + Style.RESET_ALL)
time.sleep(1)
sha1 = input("\nMot de passe a encrypt [SHA1] : ")
print("" + Fore.YELLOW + hashlib.sha1(sha1.encode('utf-8')).hexdigest() + Style.RESET_ALL)
print(Fore.GREEN + "\nExit...." + Style.RESET_ALL)
time.sleep(2)

#END