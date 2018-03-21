#!/usr/bin/env python
# -*- coding:utf-8 -*-
# The author is W1st
# import getpass
count = 3
print("[3] failed logins in a row will result in banning your account!")
fo = open("login_info", "r")
fo_banned = open("login_banned_list", "r")
login_info = fo.read()
login_banned = fo_banned.read()
while count > 0:
    print("You have {_count} remaining tries.".format(_count=count))
    login_username = input("Username: ")
    login_password = input("Password: ")
#     login_password = getpass.getpass("Password: ")
    if login_username in login_info and login_password in login_info and login_username not in login_banned:
        print("Login succeed, welcome '{_username}'! ".format(_username=login_username))
        fo.close()
        fo_banned.close()
        break
    else:
        print("Invalid username or password, please try again.")
        count -= 1
else:
    fo_banned.write(login_username)
    print("Sorry, you have tried too many times and your account has been banned.")
    fo.close()
    fo_banned.close()

