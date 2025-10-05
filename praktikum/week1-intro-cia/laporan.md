# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: CIA
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA

---

## 1. Tujuan
- Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
- Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
- Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
- Menyiapkan repositori GitHub sebagai media kerja praktikum

---

## 2. Dasar Teori
Kriptografi adalah ilmu dan seni menyembunyikan informasi sehingga hanya pihak yang berwenang yang dapat membacanya. Pada era kriptografi klasik, teknik seperti Caesar Cipher digunakan dengan cara mengganti setiap huruf dalam pesan dengan huruf lain berdasarkan aturan tertentu, misalnya menggeser huruf sebanyak tiga posisi. Contoh lain adalah Vigenère Cipher, yang menggunakan kunci berulang untuk menyandikan pesan lebih kompleks dibanding penggeseran sederhana, sehingga lebih sulit dipecahkan.

Perkembangan kriptografi modern mulai terlihat dengan hadirnya algoritma seperti RSA dan Advanced Encryption Standard (AES). RSA adalah metode kriptografi kunci publik yang memungkinkan komunikasi aman tanpa perlu berbagi kunci rahasia secara langsung, sedangkan AES adalah standar enkripsi yang digunakan secara luas untuk melindungi data digital secara efisien dan aman. Kedua teknologi ini mendasari keamanan berbagai aplikasi digital saat ini, dari transaksi online sampai komunikasi pribadi.

Evolusi kriptografi berlanjut ke era kontemporer dengan penerapan teknologi terkini seperti blockchain dan cryptocurrency (misalnya Bitcoin). Blockchain memanfaatkan kriptografi untuk menciptakan sistem terdistribusi yang aman tanpa perlu perantara, sehingga data dapat diverifikasi dan tidak mudah diubah. Selain itu, bidang kriptografi juga berkembang ke teknologi baru seperti kriptografi kuantum yang menyediakan tingkat keamanan lebih tinggi dengan prinsip fisika kuantum.

Tiga pilar keamanan informasi dan contohnya:
Confidentiality (Kerahasiaan), menjaga agar data hanya dapat diakses oleh pihak yang berwenang. Contohnya:
- Email terenkripsi agar hanya penerima dapat membacanya.
- Sistem perbankan online yang melindungi informasi nasabah dengan SSL/TLS.
- WhatsApp menggunakan enkripsi end-to-end untuk pesan pribadi.

Integrity (Integritas), memastikan data tidak berubah atau dimodifikasi tanpa izin selama penyimpanan atau transmisi. Contohnya:
- Pemeriksaan hash file saat mengunduh software untuk memastikan file tidak diubah.
- Digital signature pada dokumen elektronik untuk membuktikan isi tidak diubah.
- Sistem pembayaran yang memverifikasi transaksi tidak dimanipulasi.

Availability (Ketersediaan), menjamin sistem dan data dapat diakses oleh pengguna yang berwenang kapan pun diperlukan. Contohnya:
- Server cloud yang memiliki sistem backup untuk mencegah kehilangan data.
- Jaringan telekomunikasi yang menyediakan akses nonstop bagi pelanggan.
- Sistem layanan darurat yang harus selalu online untuk dihubungi.

---

## 3. Alat dan Bahan
- Python 3.11.0
- Visual Studio Code
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
- Melakukan fork-repo kriptografi punya dosen.
- Melakukan clone-repo ke komputer lokal.
- Buat folder `praktikum/week1-intro-cia/` yang isinya file laporan.md dan folder screenshots.
- Menulis ringkasan sejarah kriptogri dan prinsip CIA beserta contoh nyata dalam aspek kehidupan.
- Menjawab quiz singkat.

---

## 5. Source Code
Untuk saat ini belum ada keperluan ngodingnya!
```python
Belum ngoding bung!
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Tokoh yang dianggap sebagai bapak kriptografi modern adalah **Claude Shannon**.
2. Algoritma kunci publik yang masih populer hingga kini yaitu **RSA**.
3. Perbedaan utama kriptografi klasik terletak pada penggunaan kunci simetris dan sederhana, sedangkan kriptografi modern menggunakan algoritma kompleks dan kunci asimetris.

---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
