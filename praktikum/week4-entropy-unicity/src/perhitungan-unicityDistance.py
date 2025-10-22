import math

def entropy(ukuran_keyspace):
    return math.log2(ukuran_keyspace)
    
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(99^256)
print("Unicity Distance untuk Caesar Cipher jika diketahui entropynya 99^256 adalah ", unicity_distance(HK))