# math = __import__('math')
# import math as mathmatics
# from math import pi, sin
# from math import *

# print(pi)
# print(sin(10))

# import sys

# print(sys.version)
# print(sys.argv)

# import datetime

# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# import time

# print('a')
# time.sleep(5)
# print('b')

# from urllib import request

# target = request.urlopen('http://hanbit.co.kr')
# content = target.read()

# print(content[:101])

import os

def read_file_name(path):
    print(path)
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(f'{path}/{item}'):
            read_file_name(f'{path}/{item}')
        else:
            print('file: ', item)

read_file_name('.')