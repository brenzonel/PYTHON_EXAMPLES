from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

sensitive_data = b"ALIENS DO EXIST!!!!"
key = get_random_bytes(16) #must be 16, 24 or 32 bytes long
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(sensitive_data, AES.block_size))

print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
print(f"ciphertext:{b64encode(ciphertext).decode('utf-8')}")
print(f"key: {b64encode(key).decode('utf-8')}")