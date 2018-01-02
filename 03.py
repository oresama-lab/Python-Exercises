#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

list = []
for word in str:
    list.append(len(word))

print (list)

# 結果
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
