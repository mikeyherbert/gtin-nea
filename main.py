#######
#
#
#
#
#
#######

import tkinter as tk
import tkinter.simpledialog

STOCK_FILE = open('STOCK_FILE.txt', 'r')


def encode(non_cipher, key):
    cipher = ''
    for c in non_cipher:
        c = chr(ord(c) + (key + 3))  # key will be length of string + 3
        cipher += c
    return cipher


def decode(cipher):
    decipher = ''
    for c in cipher:
        c = chr(ord(c) - (len(cipher) + 3))
        decipher += c
    return decipher


def login():
    login_w = tk.Tk()
    login_w.withdraw()
    username = ''
    password = ''

    while username == '':
        username = tk.simpledialog.askstring('Username', 'Enter your username:')

    while password == '':
        password = tk.simpledialog.askstring('Password', 'Enter your password:', show='•')

    user_list = open('users.txt', 'r')

    for l in user_list:
        group = l.split(':')
        if username == group[0] and password == decode(group[1]):
            return True
        else:
            return False
