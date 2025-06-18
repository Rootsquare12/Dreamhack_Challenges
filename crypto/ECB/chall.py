from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import json
import os
import re

key = os.urandom(32)

login = None

FLAG = 'DH{**flag**}'

def print_menu():
    print("1. Register")
    print("2. Login")
    print("3. Buy flag")
    print("4. Exit")

def make_account():
    if login == None:
        name = input('Input your name : ').strip()
        pattern = r"^[a-zA-Z0-9]{1,20}$"
        if re.match(pattern,name):
            cipher = AES.new(key,AES.MODE_ECB)
            data = json.dumps({"username": name, "money": 1000})
            data = pad(data.encode(),16)
            account = cipher.encrypt(data)
            print("Your account code(hex) : " + bytes.hex(account))
        else:
            print("Name must match this regular expression : ^[a-zA-Z0-9]{1,20}$")
    else:
        print("You already logged in!")

def set_account():
    global login
    if login == None:
        account_input = input('Input your account(hex) : ').strip()
        try:
            account = bytes.fromhex(account_input)
            cipher = AES.new(key,AES.MODE_ECB)
            decrypted = cipher.decrypt(account)
            data = unpad(decrypted,16).decode()
            data = json.loads(data)
            login = data
            print('Login successful!')
        except:
            print('Invalid Account.')
    else:
        print("You already logged in!")

def get_flag():
    if login == None:
        print('Login First!')
    else:
        try:
            if login['money'] >= 31337:
                print('Flag is ' + FLAG)
            else:
                print('You are too poor to buy a flag!')
        except:
            print('System Error! Please DM Rootsquare.')

def main():
    print("Welcome to Electronic Cryptocurrency Bank!")
    while True:
        print_menu()
        try:
            choice = int(input('> '))
            if choice == 1:
                make_account()
            elif choice == 2:
                set_account()
            elif choice == 3:
                get_flag()
            elif choice == 4:
                print('Good bye!')
                break
            else:
                print('Input 1, 2, 3 or 4.')
        except:
            print("Input 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()