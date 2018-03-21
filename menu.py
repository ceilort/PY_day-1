#!/usr/bin/env python
# -*- coding:utf-8 -*-
# W1st
Top = 0
while Top == 0:
    print('''------ Welcome Aboard! ------
Please select the sub menu. 
1. Front-end engineer 
2. Back-end engineer 
3. UI/UE/UX designer 
''')
    select = int(input("Type your select: "))
    Top += 1
    if select == 1:
        print("\n1. HTML\n2. CSS\n3. JavaScript\n0. back")
        select_FE = int(input("Type your select: "))
        if select_FE == 1:
            print("\n1. HTML 5.0\n2. HTML 4.0 or low\n0. back")
            select_HT = int(input("Type your select: "))
            if select_HT == 0:
                break
        elif select_FE == 2:
            print("\n1. CSS 3.0\n2. CSS older\n0. back")
        elif select_FE == 0:
            Top = 0
    elif select == 2:
        print("\n1. Framework\n2. PHP/Python/Ruby/Java/Perl/ASP.net/Node.js\n3. MySQL/PostgreSQL/MongoDB\n0. back")
        select_FE = input("Type your select: ")
    elif select == 3:
        print('''1. Axsure
        2. Photoshop
        3. Illustrator
        0. back
        ''')
    else:
        print("Typing error!!!")
        Top = 0
