from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate dulu pasangan kunci RSA-nya dan disimpan ke file!
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("private.pem", "wb") as private_file:
    private_file.write(private_key)

with open("public.pem", "wb") as public_file:
    public_file.write(public_key)

print("✅ | Pasangan kunci RSA telah dibuat dan disimpan ke file 'private.pem' dan 'public.pem'.")

# Baca kunci dari file
with open("private.pem", "rb") as private_file:
    private_key = RSA.import_key(private_file.read())

with open("public.pem", "rb") as public_file:
    public_key = RSA.import_key(public_file.read())

print("✅ | Kunci RSA telah dibaca dari file.")

# Enkripsi dengan public key
plaintext = b"Belajar RSA pakai PyCryptodome! gini caranya."
cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(plaintext)

print("\n--- Enkripsi ---")
print("Ciphertext (hex): ", ciphertext.hex())

# Dekripsi dengan private key
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(ciphertext)

print("\n--- Dekripsi ---")
print("Decrypted (bytes): ", decrypted)
print("Decrypted teks: ", decrypted.decode())