from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# pesan buat ditandatangani
msg = b"Haloo, ada info penting buat kamu nih! Cek yaaa..."
hash = SHA256.new(msg)

# tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(hash)
print("Signature:", signature.hex())

try:
    pkcs1_15.new(public_key).verify(hash, signature)
    print("Verifikasi berhasil: tanda tangan valid!")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid!")

# simulasi modif pesan
fk_msg = b"Haloo, besok libur btw...."
fk_hash = SHA256.new(fk_msg)

try: 
    pkcs1_15.new(public_key).verify(fk_hash, signature)
    print("Verifikasi berhasil! (seharusnya gagal)")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid dengan pesan.")