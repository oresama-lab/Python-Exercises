#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dict = {}

for (num, word) in enumerate(str,1):
    if num in single:
        dict[num] = word[:1]
    else:
        dict[num] = word[:2]

print (dict)
# print (sorted(dict.items()))
# 結果
# {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}
