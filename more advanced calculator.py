def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def mul(x,y):
    z = x * y
    return z

def div(x,y):
    z = x / y
    return z

a = int(input("enter a "))

op = None
operations = ("+", "-", "*", "/" )
while op not in operations:
    op = input("enter operation ")


b = int(input("enter b "))


if op == "+":
    print(add(a,b))

if op == "-":
    print(sub(a,b))

if op == "*":
    print(mul(a,b))

if op == "/":
    print(div(a,b))

import os
os.system("pause")