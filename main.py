#######
#
#
#
#
#
#######

import tkinter as tk

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
    user_intro = tk.Label(login_w, text='Username:')
    user_req = tk.Entry(login_w)
    user_intro.pack()
    user_req.pack()
    password_intro = tk.Label(login_w, text='Password:')
    password_req = tk.Entry(login_w, show='•')
    password_intro.pack()
    password_req.pack()

    username = user_req.get()
    password = password_req.get()

    user_list = open('users.txt', 'r')

    for l in user_list:
        group = l.split(':')
        if username == group[0] and password == decode(group[1]):
            return True
        else:
            return False
