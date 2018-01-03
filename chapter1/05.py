#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def ngram(input,num):
    last_word = len(input) - num + 1
    output = []
    for i in range(0,last_word):
        output.append(input[i:i+num])
    return output

str = "I am an NLPer"
# 文字bi-gram
print(ngram(str,2))
# 単語bi-gram
print(ngram(str.split(),2))

# 結果
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
