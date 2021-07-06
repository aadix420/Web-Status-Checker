import os
from time import sleep
import requests
intro = "Coded by @aadix420"
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
print(intro)
sleep(2)
screen_clear()
file = open('domain.txt', 'r')
domain = file.readline()
response = requests.head(domain)
print("Domain",response.url,"responded with",response.status_code)