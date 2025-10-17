def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modular_inverse(a, x):
    g, n, _ = extended_gcd(a, x)
    if g != 1:
        return None
    return n % x

print("Invers dari 3 mod 11 adalah", modular_inverse(3, 11)) 