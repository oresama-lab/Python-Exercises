#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

import sys

file = "./hightemp.txt"
f = open(file)
count = 1
for i in f.readline():
    count += 1

print(count)
# 結果
# 23
