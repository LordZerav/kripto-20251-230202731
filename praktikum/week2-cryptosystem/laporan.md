# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Cryptosystem  
Nama: Amru Muiz Fauzan  
NIM: 230202731  
Kelas: 5IKRA  

---

## 1. Tujuan
```
- Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
- Menggambarkan proses enkripsi dan dekripsi sederhana.
- Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
```

---

## 2. Dasar Teori
Kriptosistem adalah sistem yang melibatkan sejumlah komponen utama yaitu plaintext (teks asli tanpa enkripsi), ciphertext (teks asli yang dienkripsi), key (data rahasia yang mengontrol proses enkripsi dan dekripsi), dan algoritma (prosedur enkripsi ataupun dekripsi untuk mengubah plaintext / ciphertext). Proses enkripsi merupakan proses mengubah plaintext menjadi bentuk yang tidak terbaca (ciphertext), sedangkan proses dekripsi merupakan proses mengembalikan ciphertext menjadi plaintext dengan key dan algoritma tertentu. Ada dua jenis utama kriptosistem yang diklasifikasikan berdasarkan jenis key-nya yaitu kriptosistem simetris dan kriptosistem asimetris. Kriptosistem simetris menggunakan satu key yang sama untuk proses enkripsi maupun dekripsi, berbeda dengan kriptosistem asimetris yang menggunakan sepasang key (key public dan key private) untuk kegunaan masing-masing (key public biasanya untuk enkripsi, sedangkan key private untuk dekripsi). Hal ini yang menjadikan kriptosistem asimetris lebih aman distribusi keynya untuk komunikasi.

Kriptosistem simetris merupakan metode di mana pengirim dan penerima berbagi satu key yang sama untuk proses enkripsi maupun dekripsinya. Contohnya adalah algoritma AES (Advanced Encryption Standard) dan Blowfish yang mengoperasikan data dalam bentuk blok / bit / byte. Sistem ini unggul dalam kecepatan dan efisiensi, namun minusnya ada di keamanan distribusi key-nya. Sedangkan untuk kriptosistem asimetris menggunakan sepasang key yang berbeda yaitu key public untuk proses enkripsi dan key private untuk proses dekripsi. Contoh algoritmanya yaitu RSA dan ECC (Elliptic Curve Cryptography). Sistem ini memudahkan pengelolaan distribusi key dan proses autentikasi walau dengan kebutuhan komputasi yang lebih besar karena algoritmanya juga termasuk kompleks.

Perbedaan utama antara sistem simetris dan asimetris terletak pada penggunaan kunci dan aplikasi praktisnya. Kriptografi simetris memakai satu kunci untuk kedua operasi enkripsi-dekripsi, membuatnya lebih cepat dan efisien untuk enkripsi data skala besar, tetapi mengandung risiko tinggi pada distribusi kunci karena satu kunci harus diamankan secara bersamaan oleh semua pihak yang berkomunikasi. Di sisi lain, kriptografi asimetris menggunakan pasangan kunci yang secara matematis terkait tetapi berbeda fungsi, memungkinkan kunci publik tersebar luas tanpa mengorbankan keamanan, sehingga meningkatkan fleksibilitas komunikasi dan keamanan pengiriman kunci. Umumnya, skema ini membutuhkan kunci dengan ukuran lebih panjang untuk tingkat keamanan yang setara dengan kriptografi simetris, misalnya kunci simetris 128 bit setara dengan kunci asimetris 2048 bit. Dengan demikian, kedua tipe kriptografi ini saling melengkapi dengan kelebihan dan kelemahan masing-masing, seringkali digunakan secara hybrid untuk menggabungkan kecepatan enkripsi simetris dan keamanan distribusi kunci asimetris.

---

## 3. Alat dan Bahan
- Python 3.11.0
- Visual Studio Code
- Git dan akun GitHub
- Draw.io

---

## 4. Langkah Percobaan  
```
- Buat skema kriptosistem dasar pakai draw.io
- Implementasikan dengan python, kemudian menyertakan hasil berupa screenshots
- Menulis laporan.md yang berisi ringkasan komponen kriptosistem, penjelasan perbedaan simetris vs asimetris
- Menjawab pertanyaan diskusi
```

---

## 5. Source Code
```python
def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<nim><nama>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```

---

## 6. Hasil dan Pembahasan
```
![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
```

---

## 7. Jawaban Pertanyaan
- Komponen utama dalam sebuah kriptosistem yaitu plaintext, ciphertext, key, algoritma, proses enkripsi dan proses dekripsi.
- Kelebihan dari kriptosistem simetris terletak pada efisiensi dan kecepatannya karena pengirim dan penerima berbagi key yang sama. Konsekuensi dari berbagi key yang sama adalah keamanan pada distribusi key-nya dibandingkan menggunakan kriptosistem asimetris.
- Secara analogi simpel aja sih, kita gak mungkin mau mempercayakan kunci rumah kita kepada orang yang gak kita kenal kan? Secara teknisnya seperti ini, key yang sama harus dibagikan oleh kedua pihak sebelum komunikasi terenkripsi dimulai melalui saluran yang sudah aman. Jika saja key yang dibagikan lewat saluran yang tidak diketahui keamanannya (misal internet biasa), maka bisa saja key tersebut disadap dan membuat proses enkripsi menjadi tidak berguna.

---

## 8. Kesimpulan
Kriptosistem merupakan sistem keamanan yang vital, dibangun di atas lima komponen utama: plaintext; ciphertext; key; algoritma serta ada proses enkripsi dan proses dekripsinya. Klasifikasi kriptosistem terbagi menjadi kriptosistem simetris (berbagi key yang sama) dan kriptosistem asimetris (sepasang key berbeda yaitu key publik dan key private). Distribusi kunci juga menjadi masalah utama yang serius terutama dalam kriptosistem simetris karena key tunggal tersebut harus dibagikan melalui saluran yang sudah pasti aman (bahaya jika disadap). Kedua jenis kriptosistem ini saling melengkapi, jika ingin mengatasi kelemahan pada keamanan maka bisa menggunakan kriptosistem asimetris dan jika tidak peduli dengan keamanannya tapi performa cepat maka kriptosistem simetris dirasa cocok.

---

## 9. Daftar Pustaka
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.
- Tokocrypto News. (2023, August 18). Enkripsi Simetris vs Enkripsi Asimetris dalam Kriptografi. https://news.tokocrypto.com/enkripsi-simetris-vs-enkripsi-asimetris-dalam-kriptografi/
- IBM. (2024, August 8). Apa itu Enkripsi Asimetris?. https://www.ibm.com/id-id/think/topics/asymmetric-encryption
- IBM. (2024, April 29). Jenis Kriptografi. https://www.ibm.com/id-id/think/topics/cryptography-types
- Neliti. (2023). Kriptografi Simetris dan Asimetris dalam Sistem Keamanan Informasi. https://media.neliti.com/media/publications/458062-none-8d4775d7.pdf
- Binance Academy. (2022, November 16). Enkripsi Simetris vs Asimetris. https://academy.binance.com/id/articles/symmetric-vs-asymmetric-encryption
- UMA P3MPBC. (2023, January 7). Perbedaan Simetris dan Asimetris pada Kriptografi. https://p3mpbc.uma.ac.id/2023/01/07/perbedaan-simetris-dan-asimetris-pada-kriptografi/
- BINUS MTI. (2013). Konsep Enkripsi-dekripsi Asimetris. https://mti.binus.ac.id/files/2013/09/Konsep-Enkripsi-dekripsi-Asimetris.pdf
- STEI ITB. (2006-2007). Studi dan Perbandingan Penggunaan Kriptografi Kunci. https://informatika.stei.itb.ac.id/~rinaldi.munir/Kriptografi/2006-2007/Makalah2/Makalah-066.pdf

---

## 10. Commit Log
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
