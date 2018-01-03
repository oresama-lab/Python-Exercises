#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = ""
tuple0 = tuple("パトカー")
tuple1 = tuple("タクシー")

for i,j in zip(tuple0, tuple1) :
    str = str + i + j

print (str)
