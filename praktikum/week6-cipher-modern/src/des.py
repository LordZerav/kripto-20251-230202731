from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Konfigurasi dulu
BLOCK_SIZE = DES.block_size
key = get_random_bytes(8)

iv = get_random_bytes(BLOCK_SIZE)

# Fungsi Enkripsi
def encrypt_des(plaintext_bytes, key, iv):
    "Enkripsi bytes dengan DES-CBC dan padding PKCS#7"
    cipher = DES.new(key, DES.MODE_CBC, iv = iv)
    padded = pad(plaintext_bytes, BLOCK_SIZE)

    ciphertext = cipher.encrypt(padded)
    return ciphertext

# Fungsi Dekripsi
def decrypt_des(ciphertext_bytes, key, iv):
    "Dekripsi bytes dengan DES-CBC dan unpadding PKCS#7"
    cipher = DES.new(key, DES.MODE_CBC, iv = iv)
    padded_plain = cipher.decrypt(ciphertext_bytes)

    plaintext = unpad(padded_plain, BLOCK_SIZE)
    return plaintext

# Penggunaan
if __name__ == "__main__":
    plaintext = b"Hello, DES CBC!"
    print("Plaintext: ", plaintext)

    # Enkripsi
    ciphertext = encrypt_des(plaintext, key, iv)
    print("Key (hex): ", key.hex())
    print("IV (hex): ", iv.hex())
    print("Ciphertext (hex): ", ciphertext.hex())

    # Dekripsi
    decrypted = decrypt_des(ciphertext, key, iv)
    print("Decrypted: ", decrypted)
    print("Decrypted matches plaintext: ", decrypted == plaintext)