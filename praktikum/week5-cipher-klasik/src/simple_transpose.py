def transpose_encrypt_visual(plaintext, key=5):
    """
    Enkripsi dengan visualisasi grid
    """
    print(f"\n--- ENKRIPSI ---")
    print(f"Plaintext: {plaintext}")
    print(f"Key (kolom): {key}")
    
    # Buat grid
    grid = [''] * key
    
    # Isi grid vertikal
    for col in range(key):
        pos = col
        while pos < len(plaintext):
            grid[col] += plaintext[pos]
            pos += key
    
    # Tampilkan grid
    print("\nGrid:")
    max_len = max(len(col) for col in grid)
    for i in range(max_len):
        row_chars = []
        for col in grid:
            if i < len(col):
                row_chars.append(col[i])
            else:
                row_chars.append(' ')
        print("  ".join(row_chars))
    
    ciphertext = ''.join(grid)
    print(f"\nCiphertext: {ciphertext}")
    return ciphertext

def transpose_decrypt_visual(ciphertext, key=5):
    """
    Dekripsi dengan visualisasi
    """
    print(f"\n--- DEKRIPSI ---")
    print(f"Ciphertext: {ciphertext}")
    print(f"Key (kolom): {key}")
    
    total_chars = len(ciphertext)
    num_cols = (total_chars + key - 1) // key
    num_rows = key
    empty_cells = (num_cols * num_rows) - total_chars
    
    # Buat grid horizontal
    grid = [''] * num_cols
    col, row = 0, 0
    
    for char in ciphertext:
        grid[col] += char
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - empty_cells):
            col = 0
            row += 1
    
    # Tampilkan grid
    print(f"\nGrid ({num_cols} kolom x {num_rows} baris):")
    for i in range(num_rows):
        row_chars = []
        for j in range(num_cols):
            if i < len(grid[j]):
                row_chars.append(grid[j][i])
            else:
                row_chars.append(' ')
        print("  ".join(row_chars))
    
    # Baca vertikal
    plaintext = ''
    for i in range(num_cols):
        for j in range(num_rows):
            if i < len(grid[j]):
                plaintext += grid[j][i]
    
    print(f"\nPlaintext: {plaintext}")
    return plaintext

# testing
print("=== SIMPLE TRANSPOSITION CIPHER ===")
msg = "AKUJAWAJAWAJAWAJAWA"
key = 4

enc = transpose_encrypt_visual(msg, key)
dec = transpose_decrypt_visual(enc, key)

print(f"\n✓ Final check: '{msg}' -> '{dec}'")