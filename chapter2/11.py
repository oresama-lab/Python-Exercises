#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 11.py
import re

file = "./hightemp.txt"
f = open(file)
lines = f.read()
f.close()
print(lines.replace("\t"," "),end="")
