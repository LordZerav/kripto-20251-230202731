def discrete_logarithm(a, b, x):
    for n in range(x):
        if pow(a, n, x) == b:
            return n
    return None

print("Discrete Logarithm dari 3^n ≡ 4 (mod 7) adalah n = ", discrete_logarithm(3, 4, 7))