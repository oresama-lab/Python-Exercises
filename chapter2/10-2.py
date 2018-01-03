#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

import sys

file = "./hightemp.txt"
f = open(file)
lines = f.readlines()
f.close()

print(len(lines))
# 結果
# 24
