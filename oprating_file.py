#!/usr/bin/env python
# -*- coding:utf-8 -*-
# W1st
fo = open("login_info","r")
print("filename : ",fo.name)
print("closed : ",fo.closed)
print("mode : ",fo.mode)
info = fo.readline(16)
print("info is: ",info)
fo.close()

