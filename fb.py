#!/bin/python
import time,os,sys
from time import sleep

#CODE WARNA

red='\033[31;1m'
green='\033[32;1m'
yellow='\033[33;1m'
blue='\033[34;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
white='\033[37;1m'

#bersih
os.system('git pull')
os.system('clear')

#banner
bnn = """
      ____    _    _   _    _    _   _   ______________________________
     | __ )  / \  | | | |  / \  | \ | | |                              |
     |  _ \ / _ \ | |_| | / _ \ |  \| | | AUTHOR : BAYU ARYA SETA      |
     | |_) / ___ \|  _  |/ ___ \| |\  | | GITHUB : github.com/SetaGanz |
     |____/_/   \_\_| |_/_/   \_\_| \_| |______________________________|
[•]______________________________________________________________________[•]
 |                                                                        |
 |                                                                        |
 |              INSTALL BAHAN BIAR GAK EROR TINGGAL MASUK                 |
 |                                                                        |
 |            [1] INSTALL BAHAN TOOLS           [0] Keluar                |
 |                                                                        |
 |                                                                        |
[•]______________________________________________________________________[•]\n"""


#penginstalan
def menu():
    print (bnn)
    ph = input("               [>_ ] INPUT > ")

#menu1
    if ph =="1":
       os.system('pkg update && pkg upgrade -y')
       os.system('pkg install python python2 git clang -y')
       os.system('git clone https://gitlab.com/mikasa-ex2022/mtf-v4')
       os.system('pip install mechanize -y')
       os.system('pip install request -y')
       os.system('pip install bs4 -y')
       os.system('pip install telethon -y')
       os.system('pip install reporting -y')
       os.system('cd mtf-v4')
       os.system('python fbv4.py')


#menu2
    if ph =="0":
       print ("")
       print ("               [>_ ] KELUAR PROGAM.....")
       sleep(5)
       print ("               [>_ ] BERHASIL KELUAR!!")
       os.system('exit')
    else:
       print ("")
       print ("               [>_ ] PILIH YANG ADA DI MENU TOLOL")
       sleep(5)
       os.system('python fb.py')
menu()
