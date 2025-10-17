def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b 
    return a
    
print("gcd dari (54, 24) adalah ", gcd_euclidean(54, 24))