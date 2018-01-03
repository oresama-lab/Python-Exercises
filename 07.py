#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

x = 12
y = "気温"
z = 22.4

def tenki(x,y,z):
    return str(x) + u"時の" + y + u"は" + str(z)

print(tenki(x,y,z))

# 結果
# 12時の気温は22.4
