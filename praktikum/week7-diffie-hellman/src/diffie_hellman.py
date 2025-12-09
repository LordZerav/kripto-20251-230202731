import random

# parameters
p = 79 # bilangan prima
g = 9 # generator

# private keys
a = random.randint(1, p-1) # punya Andre
b = random.randint(1, p-1) # punya Sule

# public keys
A = pow(g, a,p)
B = pow(g, b,p)

# pertukaran public keys
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Private key Andre: ", shared_secret_A)
print("Private key Sule: ", shared_secret_B)