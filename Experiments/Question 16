import string

alphabet = string.ascii_lowercase
common_letters = ['e', 't', 'a', 'o', 'i', 'n']

def letter_freq(text):
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

def decrypt(message, key):
    decrypted = ""
    for char in message:
        if char.isalpha():
            decrypted += key[char.lower()]
        else:
            decrypted += char
    return decrypted

def frequency_attack(message, num_plaintexts):
    freq = letter_freq(message)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_chars = [pair[0] for pair in sorted_freq][:6]
    possible_plaintexts = []
    for char in top_chars:
        shift = (alphabet.index(char) - alphabet.index('e')) % 26
        key = {}
        for i in range(26):
            key[alphabet[i]] = alphabet[(i+shift) % 26]
        plaintext = decrypt(message, key)
        score = sum([plaintext.count(word) for word in ['the', 'and', 'of', 'to', 'in', 'that']])
        possible_plaintexts.append((plaintext, score))
    sorted_plaintexts = sorted(possible_plaintexts, key=lambda x: x[1], reverse=True)[:num_plaintexts]
    return sorted_plaintexts

message = "lcllewljazlnnzmvyiylhrmhza"
num_plaintexts = 10
plaintexts = frequency_attack(message, num_plaintexts)
for i, (plaintext, score) in enumerate(plaintexts):
    print(f"Plaintext {i+1}: {plaintext} (score: {score})")
