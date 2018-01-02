#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

for (num, word) in enumerate(str,1):
    print (word[:1])
