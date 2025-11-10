from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Konfigurasi dulu
KEY_SIZE = 16
key = get_random_bytes(KEY_SIZE)
print("Key (hex): ", key.hex())

# Fungsi Enkripsi
def encrypt_aes(plaintext_bytes, key):
    "Enkripsi bytes dengan AES-EAX"
    cipher = AES.new(key, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)
    return cipher.nonce, ciphertext, tag

# Fungsi Dekripsi
def decrypt_aes(nonce, ciphertext_bytes, tag, key):
    "Dekripsi bytes dengan AES-EAX"
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext_bytes, tag)
    return plaintext

# Penggunaan
if __name__ == "__main__":
    plaintext = b"Belajar AES dengan mode EAX!, contoh simpel!"
    print("Plaintext: ", plaintext)

    # Enkripsi
    nonce, ciphertext, tag = encrypt_aes(plaintext, key)
    print("\n--- Enkripsi ---")
    print("Nonce (hex): ", nonce.hex())
    print("Ciphertext (hex): ", ciphertext.hex())
    print("Tag (hex): ", tag.hex())

    # Dekripsi
    decrypted = decrypt_aes(nonce, ciphertext, tag, key)
    print("\n--- Dekripsi ---")
    print("Decrypted (bytes): ", decrypted)
    print("Decrypted teks: ", decrypted.decode())