def create_key(keyword, length):
    key = keyword.lower()
    while len(key) < length:
        key += keyword.lower()
    return key[:length]

def encrypt(plaintext, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = create_key(keyword, len(plaintext))
    ciphertext = ""
    for i in range(len(plaintext)):
        shift = alphabet.index(key[i])
        letter = plaintext[i]
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            ciphertext += alphabet[new_index]
        else:
            ciphertext += letter
    return ciphertext


def decrypt(ciphertext, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = create_key(keyword, len(ciphertext))
    plaintext = ""
    for i in range(len(ciphertext)):
        shift = alphabet.index(key[i])
        letter = ciphertext[i]
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % 26
            plaintext += alphabet[new_index]
        else:
            plaintext += letter
    return plaintext

plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")
ciphertext = encrypt(plaintext, keyword)
print("Ciphertext: " + ciphertext)
decrypted_text = decrypt(ciphertext, keyword)
print("Decrypted text: " + decrypted_text)
