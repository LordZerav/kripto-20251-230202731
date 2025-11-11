# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: Diffie-Hellman Key Exchange
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA  

---

## 1. Tujuan
```java
- Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
- Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
- Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).
```

---

## 2. Dasar Teori
Diffie-Hellman itu merupakan algoritma kriptografi kunci publik pertama yang dipublikasikan pada tahun 1976 dan fungsinya memungkinkan untuk kedua pihak yang belum pernah bertemu untuk melakukan pertukaran kunci rahasia secara aman walaupun menggunakan saluran publik. Algoritma ini berdasarkan pada kesulitan dari masalah logaritma diskret yang sangat sulit bagi pihak ketiga untuk menghitung kunci rahasia walaupun memiliki akses informasi publik seperti bilangan prima q dan akar primitif a. Masing-masing pihak ini memilih bilangan rahasia pribadi secara acak dan menghitung nilai publik yang kemudian dipertukarkan. Setelah saling bertukar nilai, nanti kedua pihak menggunakan nilai yang diterima dan bilangan privatnya untuk menghitung kunci rahasia yang identik. Mekanisme ini memungkinkan untuk kedua pihak berbagi kunci rahasia tanpa perlu kirim kunci itu sendiri melalui jaringan sehingga kunci tidak dapat diketahui oleh penyadap.

Mekanisme Diffie-Hellman sebenarnya sederhana namun efektif, misal dua pengguna a dan b punya nilai publik q dan y. A milih bilangan privat Xa, menghitung Ya = y ^ Xa mod q. Kemudian mengirimkan Ya ke B. Di sini B melakukan hal serupa dengan Xb dan Yb. Kunci rahasia yang disepakati diperoleh dengan A menghitung K = Yb ^ Xa mod q dan B menghitung K = Ya ^ Xb mod q yang mana hasilnya identik. Namun, kelemahan utama justru rentan terhadap serangan MITM (Man-in-the-middle), di mana pihak ketiga menyisipkan dirinya di tengah percakapan dan memanipulasi pertukaran kunci dengan cara mengirimkan nilai publik palsu ke kedua pihak. Dengan demikian, pihak ketiga bisa mengakses semua komunikasi yang dienkripsi menggunakan kunci yang diatur olehnya karena kedua pengguna percaya mereka telah berkomunikasi secara langsung dan aman.

Serangan MITM bisa terjadi ketika penyerang mengelabui kedua pihak dengan memperdaya mereka. Penyerang melakukan intercept pada nilai-nilai publik yang dikirim dan mengganti nilai-nilai tersebut dengan publik kuncinya sehingga bisa menbangun dua kunci rahasia independen dengan korban yang terpisah, lalu meneruskan pesan yang sudah dienkripsi sehingga kedua pihak korban merasa komunikasi mereka aman padahal aslinya disadap. Pencegahan serangan ini biasanya melibatkan penggunaan autentikasi tambahan seperti sertifikat digital, tanda tangan digital atau protokol keamanan tambahan yang memungkinkan untuk kedua pihak memverifikasi identitas satu sama lain sebelum memulai pertukaran kunci. Dengan cara inilah kesahihan kunci publik bisa dipastikan dan serangan MITM dapat diminimalkan sehingga menjaga kunci rahasia tidak bocor pada pihak tidak berwenang.

---

## 3. Alat dan Bahan
```java
- Python 3.11
- Visual Studio Code
- Git dan akun GitHub  
```

---

## 4. Langkah Percobaan
1. Implementasi diffie-hellman pada program ``python``
2. Melakukan simulasi serangan ``MITM (Man-in-the-middle)``
3. Menjawab pertanyaan diskusi
4. Membuat ``laporan.md``

---

## 5. Source Code
```python
apa ya
```

---

## 6. Hasil dan Pembahasan
![Hasil Output](screenshots/output.png)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Diffie-Hellman memungkinkan untuk pertukaran kunci di saluran publik karena algoritma ini tuh didasarkan pada operasi matematika yaitu logaritma diskret yang mudah dilakukan satu arah tapi sulit dibalik tanpa informasi kunci privat. Nilai-nilai yang dipertukarkan adalah publik sehingga tidak perlu kirim kunci rahasia secara langsung.
- Pertanyaan 2: Kelemahan utama protokol ini yaitu rentan terhadap serangan MITM, karena penyerang menyisipkan diri dan memanipulasi pertukaran kuncinya tanpa diketahui oleh kedua pihak.
- Pertanyaan 3: Mencegah serangan MITM pada protokol ini bisa dilakukan dengan menambahkan autentikasi tambahan seperti sertifikat digital, tanda tangan digital atau metode autentikasi lain biar memvalidasi kunci publik dan identitas pihak lawan.

---

## 8. Kesimpulan
Diffie-Hellman ini merupakan metode yang inovatif dan efektif buat pertukaran kunci rahasia melalui kanal publik dengan prinsip matematika logaritma diskret yang sulit dipecahkan. Namun, protokol ini memerlukan perlindungan tambahan untuk menghindari serangan MITM yang dapat menggagalkan keamanannya. Implementasi autentikasi kunci dan verifikasi identitas menjadi kunci utama menjaga keutuhan dan kerahasiaan komunikasi yang menggunakan Diffie-Hellman.

---

## 9. Daftar Pustaka
```java
- Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson.
- Diffie, W., & Hellman, M. (1976). New Directions in Cryptography. IEEE Transactions on Information Theory, 22(6), 644-654. https://doi.org/10.1109/TIT.1976.1055638
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
- Krawczyk, H., Bellare, M., & Canetti, R. (1997). HMAC: Keyed-Hashing for Message Authentication. RFC 2104. IETF. https://tools.ietf.org/html/rfc2104
```

---

## 10. Commit Log
```
commit week7-diffie-hellman
Author: Amru Muiz Fauzan <amrumuzan092@gmail.com>
Date:   2025-11-11

    week7-diffie-hellman: implementasi dan laporan
```
