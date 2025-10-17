def modular_tambah(a, b, x): return (a + b) % x
def modular_kurang(a, b, x): return (a - b) % x
def modular_kali(a, b, x): return (a * b) % x
def modular_eksponensiasi(base, exp, x): return pow(base, exp, x)

print("21 + 7 mod 10 =", modular_tambah(21, 7, 10))
print("21 - 7 mod 10 =", modular_kurang(21, 7, 10))
print("21 * 7 mod 10 =", modular_kali(21, 7, 10))
print("21 ^ 7 mod 10 =", modular_eksponensiasi(21, 7, 10))