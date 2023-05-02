plaintext = input("Enter plaintext to encrypt: ")
key = " CIPHERABDFGJKLMNOQSTUVWXYZ"
ciphertext = ""

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            ciphertext += key[ord(char) - ord('A')].upper()
        else:
            ciphertext += key[ord(char) - ord('a')].lower()
    else:
        ciphertext += char

print("Ciphertext:", ciphertext)

decrypted_plaintext = ""

for char in ciphertext:
    if char.isalpha():
        if char.isupper():
            decrypted_plaintext += chr(key.upper().index(char) + ord('A'))
        else:
            decrypted_plaintext += chr(key.lower().index(char) + ord('a'))
    else:
        decrypted_plaintext += char

print("Decrypted plaintext:", decrypted_plaintext)


