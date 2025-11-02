# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA  

---

## 1. Tujuan
```
- Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
- Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
- Mengimplementasikan algoritma transposisi sederhana.
- Menjelaskan kelemahan algoritma kriptografi klasik.
```

---

## 2. Dasar Teori
Cipher klasik merupakan teknik kriptografi generasi awal yang digunakan untuk menjaga kerahasiaan informasi dengan cara mengubah plaintext menjadi ciphertext menggunakan aturan tertentu. Secara umum, cipher klasik terbagi menjadi dua kategori utama, yaitu cipher substitusi dan cipher transposisi. Pada cipher substitusi, setiap huruf pada plaintext digantikan dengan huruf lain berdasarkan pola tertentu. Contoh sederhana adalah Caesar Cipher yang mengganti setiap huruf berdasarkan pergeseran alfabet tetap sebanyak k posisi. Sementara itu, Vigenère Cipher menggunakan kata kunci yang diulang sepanjang plaintext untuk menentukan jumlah pergeseran tiap karakter, sehingga bersifat polialfabetik. Berbeda dengan substitusi, pada cipher transposisi huruf-huruf pada plaintext tidak diganti melainkan diacak posisi atau urutannya, sehingga struktur huruf tetap tetapi susunannya berubah. Meskipun metode ini tergolong sederhana dan sangat berpengaruh dalam sejarah kriptografi, cipher klasik memiliki banyak kelemahan sehingga tidak lagi dianggap aman dalam sistem modern.

Kelemahan utama pada Caesar Cipher terletak pada ruang kunci yang sangat kecil—hanya 25 kemungkinan pergeseran—yang membuatnya sangat mudah dipecahkan menggunakan brute-force attack. Cipher ini juga tidak mengubah distribusi frekuensi huruf, sehingga huruf yang paling sering muncul di ciphertext tetap merepresentasikan huruf paling sering pada plaintext. Maka dari itu, analisis frekuensi dapat dengan mudah digunakan untuk membongkar pesan. Sementara itu, Vigenère Cipher memang lebih kuat karena bersifat polialfabetik, namun masih memiliki titik lemah apabila kunci yang digunakan pendek dan berulang. Struktur pengulangan kunci menghasilkan pola tertentu yang bisa dianalisis menggunakan metode Kasiski Examination atau Index of Coincidence. Setelah panjang kunci diketahui, ciphertext dapat dipisah berdasarkan posisi huruf kunci dan tiap bagian dapat dianalisis menggunakan frekuensi monoalfabetik. Dengan demikian, Caesar Cipher gagal karena keterbatasan kunci dan pola statis, sedangkan kelemahan terbesar Vigenère Cipher muncul saat kunci tidak acak atau terlalu pendek dibanding panjang pesan.

Cipher klasik pada umumnya sangat rentan terhadap analisis frekuensi karena bahasa manusia memiliki pola statistik yang konsisten. Misalnya, dalam Bahasa Inggris huruf seperti E, T, A, dan O muncul jauh lebih sering dibanding huruf Z atau Q. Cipher substitusi tidak merusak pola frekuensi huruf-huruf tersebut, hanya mengganti identitasnya. Akibatnya, siapa pun yang menganalisis ciphertext cukup menghitung frekuensi kemunculan huruf, lalu memetakannya dengan tabel statistik bahasa. Dalam kasus cipher polialfabetik seperti Vigenère Cipher, meskipun frekuensi huruf tidak langsung terlihat, pola pengulangan kunci akan menciptakan struktur yang dapat dikenali. Setelah panjang kunci ditemukan, setiap huruf dapat dianalisis seperti cipher substitusi tunggal (monoalfabetik). Artinya, selama cipher tidak mampu menyembunyikan pola statistik bahasa (baik frekuensi tunggal, bigram, maupun trigram), cipher tersebut dapat diretas dengan teknik analisis frekuensi.

Jika dibandingkan, cipher substitusi dan transposisi memiliki kelebihan dan kekurangannya masing-masing. Cipher substitusi mengganti identitas simbol, sehingga mudah diaplikasikan namun sangat rentan terhadap analisis statistik jika hanya menggunakan satu alfabet tetap. Polialfabetik seperti Vigenère Cipher memang memberikan peningkatan keamanan, tetapi tetap gagal melindungi pesan jika kunci pendek atau digunakan berulang. Cipher transposisi tidak mengganti huruf tetapi hanya mengacak urutannya, sehingga distribusi frekuensi huruf tetap utuh. Keuntungannya adalah struktur kata asli sulit dikenali secara langsung, tetapi kelemahannya adalah pola frekuensi tetap tersedia sehingga masih dapat dianalisis. Cipher transposisi juga dapat dipecahkan jika format kolom atau panjang blok diketahui. Karena cipher substitusi memberikan confusion (pengacakan makna) dan cipher transposisi memberi diffusion (pengacakan posisi), keduanya lebih kuat jika dikombinasikan bersama—konsep ini yang kemudian menjadi dasar desain cipher modern.

---

## 3. Alat dan Bahan
- Visual Studio Code
- Git dan akun GitHub  
- Python 3.11

---

## 4. Langkah Percobaan
1. Melakukan persiapan untuk implementasi cipher dengan python di VSC.
2. Implementasi pertama caesar-cipher.py.
3. Implementasi kedua vigenere-cipher.py.
4. Implementasi simple-transposition.py.
5. Mencari teori caesar cipher klasik dan dibuat rangkuman untuk dimasukkan ke bagian teori pada ``laporan.md``
6. Menjawab pertanyaan diskusi.
   
---

## 5. Source Code
```python
ntar
```

---

## 6. Hasil dan Pembahasan
![Hasil Output](screenshots/output.png)

---

## 7. Jawaban Pertanyaan
1. Pertanyaan 1: Kelemahan Caesar Cipher dan Vigenere Cipher. Untuk ``Caesar Cipher`` kelemahannya mudah ditebak/ _brute-force_ , tidak mengubah distribusi frekuensi pada huruf-hurufnya, dan kelemahan lainnya juga tidak tahan dengan analisis statistik. Sedangkan untuk ``Vigenere Cipher`` kelemahannya justru pada perulangan pada pola kunci jika dilakukan analisis frekuensi/ metode statistik.
2. Pertanyaan 2: Cipher klasik mudah diserang dengan analisis frekuensi adalah pernyataan yang bisa dibilang tepat. Karena bahasa alami  (bahasa Inggris/ bahasa Indonesia) punya distribusi huruf yang tidak seragam. Teknik substitusi yang tidak mengubah pola relatif (monoalfabetik) hanya mengubah identitas simbol, bukan frekuensi relatifnya. Oleh karena itu, pemetaan frekuensi ciphertext menjadi plaintext bisa memberi petunjuk kuat tentang substitusi yang digunakan. Bahkan untuk sistem polialfabetik seperti Vigenere, jika ada pengulangan kunci atau struktur, analisis frekuensi bisa diterapkan setelah memisahkan ciphertext menjadi sisi-sisi yang dibentuk oleh setiap huruf kunci. Dengan metode seperti Kasiski examination dan Index of Coincidence (Friedman) bisa digunakan untuk menemukan panjang kunci sehingga analisis frekuensi dapat dieksekusi pada setiap subsekuen.
3. Pertanyaan 3: Perbandingan kelebihan + kelemahan dari Cipher Substitusi dengan Transposisi
Substitusi, kelebihan mudah diimplementasikan secara manual. Polialfabetik (Vigenère) bisa memecah keterkaitan langsung antara huruf plaintext dan ciphertext sehingga lebih kuat dibanding monoalfabetik.Sedangkan bagian kelemahannya justru karena monoalfabetik rentan terhadap analisis frekuensi dan polialfabetik rentan kalau kunci pendek/diulang (distribusi akhir masih mengandung pola jika kunci tidak ideal). Umumnya tidak mengubah urutan huruf → struktur kata (pattern) tetap ada (mis. pola kata seperti “THERE” bisa dikenali lewat pola pengulangan huruf).
Transposisi, punya kelebihan buat mengubah urutan huruf, sehingga statistik frekuensi huruf tetap sama (huruf-huruf muncul sama jumlahnya) tapi struktur tata kata dan posisi diacak. Jika dikombinasikan dengan substitusi (menjadi hybrid cipher), maka keamanan meningkat signifikan. Mengenai kelemahannya, karena frekuensi huruf tetap, analisis berbasis frekuensi masih bisa dimanfaatkan. Jika hanya transposisi sederhana (mis. kolom sederhana), pola pozisi dan indikator panjang blok dapat dieksploitasi untuk membalikkan transposisi. Serta untuk implementasi manual agar transposisinya kuat (banyak lapis) itu bisa sangat merepotkan.

---

## 8. Kesimpulan
Cipher klasik seperti Caesar dan Vigenère Cipher penting sebagai dasar sejarah kriptografi, namun secara keamanan sudah tidak relevan digunakan karena masih mempertahankan pola statistik bahasa sehingga mudah dipecahkan dengan analisis frekuensi. Caesar Cipher sangat lemah karena ruang kunci kecil dan pola huruf tidak berubah, sedangkan Vigenère Cipher sedikit lebih kuat tetapi tetap dapat ditembus jika kunci pendek atau berulang. Baik cipher substitusi maupun transposisi memiliki kelemahan masing-masing—substitusi menyamarkan huruf tetapi tetap mempertahankan struktur kata, sedangkan transposisi mengacak urutan tetapi tidak menyembunyikan frekuensi huruf—sehingga keduanya belum mampu memberikan perlindungan yang kuat jika berdiri sendiri. Kesimpulannya, cipher klasik lebih bernilai sebagai fondasi teori dan pembelajaran, sementara keamanan modern membutuhkan kombinasi confusion dan diffusion seperti pada cipher masa kini (AES, DES, dan sejenisnya).

---

## 9. Daftar Pustaka
```java
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. (2006). Network Security Essentials: Applications and Standards (3rd ed.). Prentice Hall.
- Kahn, D. (1967). The Codebreakers: The Story of Secret Writing. New York: Macmillan.
- Shannon, C. E. (1949). Communication theory of secrecy systems. Bell System Technical Journal, 28(4), 656–715.
- Friedman, W. F. (1922). The Index of Coincidence and Its Applications in Cryptology. Riverbank Publications.
- Singh, S. (1999). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Anchor Books.
```

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week5-cipher-klasik
Author: Amru Muiz Fauzan <amrumuzan092@gmail.com>
Date:   2025-11-02

    week5-cipher-klasik: implementasi caesar-cipher, vigenere-cipher, simple-transposition dan laporan singkat.
```
