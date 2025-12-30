import random

# parameters
p = 2**521 - 1  # A large prime number
threshold = 3
jumlah_share = 5

# rahasia yang akan dibagikan
secret_string = "KRIPTOGRAFIUPB2025/2026"
secret = int.from_bytes(secret_string.encode(), 'big')

# fungsi untuk membantu
def eval_polynomial(coeffs, x, p):
    "Menghitung nilai f(x) = a0 + a1*x + a2*x^2 + ... (mod p)"
    result = 0
    for power, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, power, p)) % p
    return result

def generate_shares(secret, k, n, p):
    "Membangun polinomial dan membagi shares"
    coeffs = [secret] + [random.randrange(1, p) for _ in range(k-1)]
    shares = []
    for x in range(1, n + 1):
        y = eval_polynomial(coeffs, x, p)
        shares.append((x, y))
    return shares

def lagrange_interpolation(shares, p):
    "Rekonstruksi secret dengan Lagrange Interpolation"
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        numerator = 1
        denominator = 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                numerator = (numerator * (-xm)) % p
                denominator = (denominator * (xj - xm)) % p
        lagrange_coeff = (numerator * pow(denominator, -1, p)) % p
        secret = (secret + yj * lagrange_coeff) % p
    return secret

# proses
shares = generate_shares(secret, threshold, jumlah_share, p)
print("Shares yang dihasilkan:")
for share in shares:
    print(share)
    
# milih minimal k shares
selected_shares = shares[:threshold]
recovered_secret = lagrange_interpolation(selected_shares, p)

# konversi kembali ke string
recovered_string = recovered_secret.to_bytes((recovered_secret.bit_length() + 7) // 8, 'big').decode()
print("\nRahasia yang direkonstruksi:")
print(recovered_string)