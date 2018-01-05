#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 15.py

import sys

arg = sys.argv
with open("hightemp.txt","r") as txt:
    lines = txt.readlines()
end = 0
start = 0 - int(arg[1])
for i in range(start,end):
    print(lines[i].rstrip())
    i = i + 1
