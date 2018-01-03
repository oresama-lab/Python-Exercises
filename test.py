import random

# input = "aiueo"
# middle = input[1:-1]
# kekka = random.shuffle(middle.split())
# kekka = ''.join(random.sample(middle,len(middle)))
#
# print(input[0] + str(kekka) + input[-1])




import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word = tuple(str)
output = ''

def middle_to_random(word):
    for i in word:
        m = word[1:-1]
        kekka = ''.join(random.sample(m,len(m)))
        print(word[0] + kekka + word[-1])

print(middle_to_random(word))
