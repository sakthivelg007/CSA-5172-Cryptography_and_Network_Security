def generate_subkeys(initial_key):
    key_permutation_table = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    left_shift_table = [
        1, 1, 2, 2, 2, 2, 2, 2,
        1, 2, 2, 2, 2, 2, 2, 1
    ]

    round_key_permutation_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]

    key = apply_permutation(initial_key, key_permutation_table)

    left_half = key[:28]
    right_half = key[28:]

    subkeys = []

    for i in range(16):
        left_half = left_shift(left_half, left_shift_table[i])
        right_half = left_shift(right_half, left_shift_table[i])
        combined_half = left_half + right_half

        subkey = apply_permutation(combined_half, round_key_permutation_table)

        subkeys.append(subkey)

    return subkeys

def apply_permutation(bits, permutation_table):
    return [bits[i - 1] for i in permutation_table]

def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]

initial_key = [
    0, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 1, 0, 0, 1, 1,
