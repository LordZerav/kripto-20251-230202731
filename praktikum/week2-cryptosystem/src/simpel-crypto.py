def enkripsi(teks_asli, kunci):
    hasil = ""
    # Proses setiap karakter dalam teks
    for karakter in teks_asli:
        if karakter.isalpha():
            nilai_awal = 65 if karakter.isupper() else 97
            hasil += chr((ord(karakter) - nilai_awal + kunci) % 26 + nilai_awal)
        else:
            hasil += karakter
    return hasil

def dekripsi(teks_terenkripsi, kunci):
    hasil = ""
    # Proses setiap karakter dalam teks terenkripsi
    for karakter in teks_terenkripsi:
        if karakter.isalpha():
            nilai_awal = 65 if karakter.isupper() else 97
            hasil += chr((ord(karakter) - nilai_awal - kunci) % 26 + nilai_awal)
        else:
            hasil += karakter
    return hasil

# Program utama yang akan dijalankan jika file ini dieksekusi langsung
if __name__ == "__main__":
    # Data yang akan dienkripsi
    pesan = "<230202731><Amru Muiz Fauzan>"
    kunci = 5

    hasil_enkripsi = enkripsi(pesan, kunci)
    hasil_dekripsi = dekripsi(hasil_enkripsi, kunci)

    print("Teks Asli   :", pesan)
    print("Hasil Enkripsi:", hasil_enkripsi)
    print("Hasil Dekripsi:", hasil_dekripsi)