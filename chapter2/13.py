#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-
# 13.py

with open('col1.txt') as col1, open('col2.txt') as col2:
    line1, line2 = col1.readlines(), col2.readlines()

with open('merge.txt', 'w') as output:
    for i,j in zip(line1,line2):
        output.write(i.rstrip() + "\t" + j.rstrip() + "\n")
