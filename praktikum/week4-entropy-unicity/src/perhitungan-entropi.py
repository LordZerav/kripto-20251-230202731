import math

def entropy(ukuran_keyspace):
    return math.log2(ukuran_keyspace)
    
print("Jika diketahui entropy ruang kuncinya 12^3, maka akan menghasilkan sebanyak ", entropy(12^3), "bit/kombinasi.")
print("Jika diketahui entropy ruang kuncinya 99^256, maka akan menghasilkan sebanyak ", entropy(99^256), "bit/kombinasi.")