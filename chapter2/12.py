#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 12.py
import re

file = "./hightemp.txt"
f = open(file,mode='r')
col1 = open('col1.txt',mode='w')
col2 = open('col2.txt',mode='w')

for line in f:
    cols = line.split()
    col1.write(cols[0] + "\n")
    col2.write(cols[1] + "\n")

f.close()
