#!/usr/bin/env python
# -*- coding:utf-8 -*-
# W1st
'''
for i in range (10):
    print ("---",i)
    for j in range (10):
        print (j)
        if j >5:
            break
'''

usr = input("usrname: ")
fo = open("login_info","r")
if usr in fo.read():
    print("succeed.")
else:
    print("failed.")

