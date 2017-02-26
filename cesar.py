# -*- coding: utf-8 -*-

# Tries all possibilities to solve a Cesar code

def fromLettersToNumbers(a): # Converts a word in letters to numbers
    b = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in a:
        for i in range(0,len(alphabet)):
            if letter == alphabet[i]:
                b.append(i)
    return b

def fromNumbersToLetters(a): # Converts a word in numbers to letters
    b = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for number in a:
        # We need to make sure it wraps so that values make sens
        b.append(alphabet[number%len(alphabet)])
    return str(''.join(b))

def add(a,b): # Adds an offset to a word in numbers
    c = []
    for elt in a:
        c.append(elt+b)
    return c


mot = 'wldlwwpepwplfqzjpc' # Word to decode
mot2 = fromLettersToNumbers(mot)

for i in range(0,26): # Try all possibilities
    print(i,fromNumbersToLetters(add(mot2,i))) # Print them



