#!/usr/bin/env python
# -*- coding:utf-8 -*-
# W1st
age_of_oldboy= 56
count = 0
while count <3:
    guess_age_of_oldboy = int (input("guess age of oldboy:"))
    if guess_age_of_oldboy ==age_of_oldboy:
        print("you got it!!!")
        break
    elif guess_age_of_oldboy > age_of_oldboy:
        print("think smaller.")
    else:
        print("think bigger.")
    count += 1
else:
    print ("Sorry, you have tried too many times.")

