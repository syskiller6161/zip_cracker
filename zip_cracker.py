import zipfile
from colorama import Fore
import os

print(Fore.MAGENTA + """
                                               __   _  ____             __              __
                               ______  _______/ /__(_) / /__   _____   / /_____  ____  / /
                             / ___/ / / / ___/ //_/ / / / _ \ / ___/  / __/ __ \/ __ \/ / 
                             (__  ) /_/ (__  ) ,< / / / /  __/ /     / /_/ /_/ / /_/ / /  
                            /____/\__, /____/_/|_/_/_/_/\___/_/      \__/\____/\____/_/   
                                 /____/                                    
                                                                                        by:syskiller              
   
            
      
      
      """)


Zip_file = input(Fore.RED + "enter the zip file path: ")

wordlist = input(Fore.RED + "enter the path for the wordlist: ")

with open(wordlist , "r") as f:
   wordlists =  f.read().splitlines()

for password in wordlists:
   try:
    with zipfile.ZipFile(Zip_file) as zf:
        zf.setpassword(password.encode('utf-8'))
        zf.extractall()
        if password:
            print(Fore.GREEN + "password found: ",password)
            
        
        else:
            (Fore.RED + "wrong password: ",password)
   except Exception as e :
      print("password not found", password)

  