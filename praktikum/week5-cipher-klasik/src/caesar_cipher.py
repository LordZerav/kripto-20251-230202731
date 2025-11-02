def caesar_super_simple(text, key, mode='encrypt'):
    """
    Versi paling sederhana dari Caesar cipher
    mode: 'encrypt' atau 'decrypt'
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Tentukan apakah huruf besar atau kecil
            if char.isupper():
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            else:
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            
            # Cari posisi huruf saat ini
            current_position = alphabet.find(char)
            
            if mode == 'encrypt':
                # Geser maju untuk enkripsi
                new_position = (current_position + key) % 26
            else:
                # Geser mundur untuk dekripsi
                new_position = (current_position - key) % 26
            
            # Ambil huruf baru
            new_char = alphabet[new_position]
            result += new_char
        else:
            # Karakter selain huruf tetap sama
            result += char
    
    return result

def menu_interaktif():
    print("=== PROGRAM CAESAR CIPHER INTERAKTIF ===")
    
    while True:
        print("\nPilih menu:")
        print("1. Enkripsi teks")
        print("2. Dekripsi teks") 
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == '1':
            # Enkripsi
            print("\n--- ENKRIPSI ---")
            plaintext = input("Masukkan plaintext: ")
            key = int(input("Masukkan kunci (angka 1-25): "))
            
            if key < 1 or key > 25:
                print("Kunci tidak valid! Menggunakan kunci 3.")
                key = 3
            
            ciphertext = caesar_super_simple(plaintext, key, 'encrypt')
            print(f"\nHasil Enkripsi: {ciphertext}")
            
        elif pilihan == '2':
            # Dekripsi
            print("\n--- DEKRIPSI ---")
            ciphertext = input("Masukkan ciphertext: ")
            key = int(input("Masukkan kunci (angka 1-25): "))
            
            if key < 1 or key > 25:
                print("Kunci tidak valid! Menggunakan kunci 3.")
                key = 3
            
            plaintext = caesar_super_simple(ciphertext, key, 'decrypt')
            print(f"\nHasil Dekripsi: {plaintext}")
            
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program!")
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

# Jalankan program
if __name__ == "__main__":
    menu_interaktif()