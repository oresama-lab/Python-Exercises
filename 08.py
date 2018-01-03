#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def cipher(input):
    output = ""
    for i in input:
        if i.islower():
            output += chr(219 - ord(i))
        else:
            output += i
    return output

input = "If you can dream it, you can do it."
coded = cipher(input)

print(cipher(input))
print(cipher(coded))
# 結果
# Iu blf xzm wivzn rg, blf xzm wl rg.
# If you can dream it, you can do it.
