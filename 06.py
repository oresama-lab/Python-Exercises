#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def ngram(input,num):
    last_word = len(input) - num + 1
    output = []
    for i in range(0,last_word):
        output.append(input[i:i+num])
    return output

str0 = "paraparaparadise"
str1 = "paragraph"

X = set(ngram(str0,2))
Y = set(ngram(str1,2))

print (X)
# ['pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se']
print (Y)
# ['pa', 'ar', 'ra', 'ag', 'gr', 'ra', 'ap', 'ph']

# 和集合
union = X | Y
print (union)

# 積集合
intersection = X & Y
print (intersection)

# 差集合
difference = X -Y
print (difference)

# 'se'というbi-gramがXおよびYに含まれるか
print ("se" in X)
print ("se" in Y)

# 結果
# {'se', 'ap', 'di', 'is', 'ra', 'ar', 'pa', 'ad'}
# {'ap', 'ag', 'ph', 'ra', 'gr', 'pa', 'ar'}
# {'se', 'ap', 'ag', 'di', 'ph', 'is', 'ra', 'ar', 'pa', 'gr', 'ad'}
# {'ap', 'ra', 'pa', 'ar'}
# {'se', 'ad', 'is', 'di'}
# True
# False
