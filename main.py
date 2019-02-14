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
        print(c)
        decipher += c
    return decipher


def login():
    w = tk.Tk()
    w.withdraw()
    username = tk.simpledialog.askstring('Username:', 'Username')
    print(username)
    password = tk.simpledialog.askstring('Password:', 'Password', show='*')
    print(password)

    user_list = open('users.txt', 'r')

    for l in user_list:
        group = l.split(':')
        print(decode(group[1]))
        if username == group[0] and password == decode(group[1]):
            print('yep')
        else:
            print('nah mate')

login()

