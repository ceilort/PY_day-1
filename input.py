#!/usr/bin/env python
# -*- coding:utf-8 -*-
# W1st
name = input("Name:")
age = input("Age:")
job = input("Job:")
info = '''
-------- Infomation of {_name} --------
Name:{_name}
Age:{_age}
Job:{_job}
'''.format(_name=name,
           _age=age,
           _job=job)
print(info)