#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

import random

input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


def typoglycemia(input):
    output = []
    for word in input.split(' '):
        if len(word) <= 4:
            output.append(word)
        else:
            middle_char = list(word[1:-1])
            random.shuffle(middle_char)
            output.append(word[0] + ''.join(middle_char) + word[-1])
    return ' '.join(output)

print(typoglycemia(input))
# 結果
# I cd'nuolt bleeive that I could aualctly urnantdsed what I was rianedg : the poneneahml peowr of the haumn mind .
