from Crypto.Cipher import DES

shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Define the keys in reverse order
k16 = "0123456789ABCDEF"
k15 = "FEDCBA9876543210"
k14 = "0123456789ABCDEF"
k13 = "FEDCBA9876543210"
k12 = "0123456789ABCDEF"
k11 = "FEDCBA9876543210"
k10 = "0123456789ABCDEF"
k9 = "FEDCBA9876543210"
k8 = "0123456789ABCDEF"
k7 = "FEDCBA9876543210"
k6 = "0123456789ABCDEF"
k5 = "FEDCBA9876543210"
k4 = "0123456789ABCDEF"
k3 = "FEDCBA9876543210"
k2 = "0123456789ABCDEF"
k1 = "FEDCBA9876543210"

key = k16 + k15 + k14 + k13 + k12 + k11 + k10 + k9 + k8 + k7 + k6 + k5 + k4 + k3 + k2 + k1

message = "1fa68b0a722f3c08"

cipher = DES.new(bytes.fromhex(key), DES.MODE_ECB)

decrypted_message = cipher.decrypt(bytes.fromhex(message)).hex()
print(f"Decrypted message: {decrypted_message}")
