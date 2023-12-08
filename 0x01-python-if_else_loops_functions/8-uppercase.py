#!/usr/bin/python3
def uppercase(str):
    num = 0
    while num < len(str):
        if ord(str[num]) >= 97 and ord(str[num]) <= 122:
            print(f"{chr(ord(str[num]) - 32)}", end = "")
        else:
            print(f"{str[num]}", end = "")
        num += 1

