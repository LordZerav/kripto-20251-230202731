def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.lower()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Hitung shift dari key
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            # Tentukan base (A=65, a=97)
            base = ord('A') if char.isupper() else ord('a')
            
            # Enkripsi
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
            key_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.lower()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Hitung shift dari key
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            # Tentukan base (A=65, a=97)
            base = ord('A') if char.isupper() else ord('a')
            
            # Dekripsi
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
            key_index += 1
        else:
            result += char
    
    return result

# testing
msg = "Aku JaWa"
key = "UIA"

enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)

print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)