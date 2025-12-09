from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# generate key pair RSA
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# buat subjek dan issuer (CA sederhana = self-signed)
s = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"upbKriptografi.id"),
])

# buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(s)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# save sertifikat ke pem file
with open("sertifikat-digital.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat berhasil dibuat dan disimpan sebagai 'sertifikat-digital.pem'")