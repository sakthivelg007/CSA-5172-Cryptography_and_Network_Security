def create_matrix(keyword):
    alphabet = "abcdefghiklmnopqrstuvwxyz" 
    matrix = []
    for letter in keyword:
        if letter not in matrix and letter in alphabet:
            matrix.append(letter)
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    return matrix

def find_positions(matrix, letter1, letter2):
    index1 = matrix.index(letter1)
    index2 = matrix.index(letter2)
    row1, col1 = divmod(index1, 5)
    row2, col2 = divmod(index2, 5)
    return row1, col1, row2, col2

def encrypt(plaintext, matrix):

    plaintext = plaintext.replace(" ", "").lower()
    if len(plaintext) % 2 == 1:
        plaintext += "x"

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        letter1, letter2 = plaintext[i:i+2]
        row1, col1, row2, col2 = find_positions(matrix, letter1, letter2)
        if row1 == row2:
            ciphertext += matrix[row1*5+(col1+1)%5]
            ciphertext += matrix[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[((row1+1)%5)*5+col1]
            ciphertext += matrix[((row2+1)%5)*5+col2]
        else:
            ciphertext += matrix[row1*5+col2]
            ciphertext += matrix[row2*5+col1]
    return ciphertext


def decrypt(ciphertext, matrix):

    ciphertext = ciphertext.replace(" ", "").lower()
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i:i+2]
        row1, col1, row2, col2 = find_positions(matrix, letter1, letter2)
        if row1 == row2:
            plaintext += matrix[row1*5+(col1-1)%5]
            plaintext += matrix[row2*5+(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[((row1-1)%5)*5+col1]
            plaintext += matrix[((row2-1)%5)*5+col2]
        else:
            plaintext += matrix[row1*5+col2]
            plaintext += matrix[row2*5+col1]
    return plaintext


keyword = input("Enter keyword: ")
matrix = create_matrix(keyword)
print("Matrix:")
for i in range(5):
    print(matrix[i*5:i*5+5])
plaintext = input("Enter plaintext to encrypt: ")
ciphertext = encrypt(plaintext, matrix)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, matrix)
print("Decrypted plaintext:", decrypted_plaintext)
