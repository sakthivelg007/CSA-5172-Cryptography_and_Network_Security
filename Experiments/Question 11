import math
alphabet = 'abcdefghiklmnopqrstuvwxyz'

def generate_keys():
    keys = []
    for letter1 in alphabet:
        for letter2 in alphabet:
            if letter1 != letter2:
                keys.append(letter1 + letter2)
    return keys

num_keys = len(generate_keys())
exponent = math.log2(num_keys)

print(f"The Playfair cipher has approximately 2^{exponent:.2f} possible keys.")\
