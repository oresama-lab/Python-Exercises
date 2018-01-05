#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 14.py

import sys

arg = sys.argv
with open("hightemp.txt","r") as txt:
    lines = txt.readlines()

for i in range(0,int(arg[1])):
    print(lines[i].rstrip())
    i = i + 1
