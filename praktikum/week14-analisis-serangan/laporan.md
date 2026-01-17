# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: Analisis Serangan Kriptografi
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA  

---

## 1. Tujuan
```python
- Mengidentifikasi jenis serangan pada sistem informasi nyata.
- Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
- Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.
```

---

## 2. Dasar Teori
Analisis serangan kriptografi membahas berbagai cara penyerang (cryptanalyst) mencoba memecahkan sistem kriptografi, baik dengan mencoba semua kunci (brute force) maupun dengan memanfaatkan kelemahan matematis atau implementasi dari algoritma tersebut. Dalam pendekatan klasik, serangan diklasifikasikan berdasarkan keterlibatan penyerang (pasif vs aktif) dan berdasarkan teknik yang digunakan, seperti exhaustive/brute force attack (mencoba semua kemungkinan kunci) dan analytical attack (menganalisis kelemahan matematis cipher untuk menemukan kunci atau plainteks). Prinsip Kerckhoffs menyatakan bahwa keamanan sistem kriptografi harus terletak pada kerahasiaan kunci, bukan pada kerahasiaan algoritma, sehingga analisis serangan selalu mengasumsikan penyerang mengetahui algoritma yang digunakan. Berdasarkan data yang tersedia, serangan juga dikategorikan menurut ketersediaan data yang dimiliki penyerang, yaitu ciphertext‑only attack (hanya memiliki cipherteks), known‑plaintext attack (memiliki beberapa pasangan plainteks–cipherteks), chosen‑plaintext attack (dapat memilih plainteks untuk dienkripsi), adaptive‑chosen‑plaintext attack (dapat menyesuaikan plainteks berdasarkan hasil sebelumnya), dan chosen‑ciphertext attack (dapat memilih cipherteks untuk didekripsi). Serangan modern juga mencakup side‑channel attack (mengeksploitasi kebocoran fisik seperti waktu eksekusi, konsumsi daya, atau radiasi elektromagnetik), fault attack (memaksa kesalahan pada perangkat keras/softwar), serta serangan terhadap protokol seperti man‑in‑the‑middle dan downgrade attack. Keamanan komputasional suatu algoritma ditentukan oleh kompleksitas matematisnya, biaya untuk memecahkannya, dan waktu yang dibutuhkan, yang harus lebih besar dari nilai informasi dan masa kerahasiaan data tersebut. Literatur terbaru menunjukkan bahwa meskipun algoritma seperti AES sangat tahan terhadap serangan kriptanalitik klasik (differential, linear, integral cryptanalysis), ancaman utama justru berasal dari serangan implementasi seperti side‑channel dan serangan berbasis quantum computing (misalnya Grover’s algorithm). Oleh karena itu, analisis serangan kriptografi tidak hanya fokus pada kekuatan algoritma secara teoretis, tetapi juga pada keamanan implementasi, desain protokol, dan adaptasi terhadap ancaman baru seperti komputasi kuantum. Pendekatan ini menekankan perlunya desain sistem kriptografi yang mempertimbangkan confusion dan diffusion yang kuat, kunci yang panjang, serta countermeasure terhadap serangan fisik dan logika.

---

## 3. Alat dan Bahan
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Cari studi kasus sistem nyata yang pernah mengalami serangan kriptografi.
2. Identifikasi serangan dan penyebab kelemahan sistemnya.
3. Analisis kelemahan algoritma yang digunakan sistemnya.
4. Apakah kelemahan terletak pada algoritma kriptografi, implementasi atau bahkan pada konfigurasi sistemnya?
5. Usulkan solusi berupa rekomendasi mekanisme yang lebih aman bisa dengan berikan algoritma yang lebih cocok untuk keamanan sistemnya!

---

## 5. Source Code
```python
Tidak ada source code untuk sementara
```

---

## 6. Hasil dan Pembahasan
Salah satu kasus nyata serangan kriptografi yang sangat terkenal adalah Heartbleed Bug, sebuah kerentanan serius yang ditemukan pada tahun 2014 di pustaka kriptografi OpenSSL, yang digunakan secara luas untuk mengamankan komunikasi jaringan melalui protokol TLS/SSL, seperti pada layanan HTTPS, email, dan VPN. Heartbleed memungkinkan penyerang untuk membaca sebagian memori server yang seharusnya bersifat rahasia hanya dengan mengirimkan permintaan khusus tanpa perlu autentikasi. Data yang bocor dari memori ini dapat mencakup informasi sangat sensitif, seperti username dan password pengguna, cookie sesi, serta yang paling berbahaya adalah private key TLS milik server. Kebocoran private key ini berdampak besar karena memungkinkan penyerang melakukan serangan lanjutan seperti man-in-the-middle dan dekripsi komunikasi terenkripsi yang seharusnya aman.

Serangan Heartbleed bukanlah kelemahan pada algoritma kriptografi yang digunakan, seperti RSA, AES, atau SHA-256, melainkan berasal dari kesalahan implementasi pada fitur Heartbeat Extension di OpenSSL. Secara teknis, bug ini disebabkan oleh tidak adanya pemeriksaan batas (bounds checking) terhadap panjang data yang diklaim oleh klien. Server OpenSSL secara keliru mempercayai nilai panjang yang dikirimkan oleh klien dan mengirimkan kembali data dari area memori di luar batas buffer yang seharusnya. Akibatnya, penyerang dapat membaca hingga 64 KB data memori server dalam satu permintaan, dan serangan ini dapat diulang berkali-kali tanpa terdeteksi. Dengan demikian, kelemahan Heartbleed tidak menunjukkan kegagalan teori kriptografi, melainkan kegagalan dalam penerapan kriptografi secara aman di tingkat perangkat lunak.

Dari sudut pandang keamanan sistem, Heartbleed menunjukkan bahwa algoritma kriptografi yang kuat sekalipun tidak menjamin keamanan apabila implementasinya cacat. TLS sebagai protokol tetap aman secara matematis, namun penggunaan pustaka OpenSSL yang memiliki bug memori membuat seluruh sistem menjadi rentan. Hal ini menegaskan bahwa keamanan kriptografi tidak hanya bergantung pada pemilihan algoritma, tetapi juga pada kualitas implementasi, manajemen memori, dan pengujian perangkat lunak. Selain itu, karena serangan ini bersifat pasif dan tidak meninggalkan jejak yang jelas, banyak sistem yang telah disusupi tanpa diketahui oleh administrator, sehingga dampaknya sulit diukur secara pasti.

Sebagai solusi dan rekomendasi, langkah utama yang harus dilakukan adalah memperbarui OpenSSL ke versi yang telah diperbaiki, menonaktifkan fitur Heartbeat pada sistem lama, serta mengganti seluruh kunci kriptografi dan sertifikat digital yang berpotensi telah bocor. Dari sisi desain keamanan jangka panjang, penggunaan protokol yang lebih modern seperti TLS 1.2 atau TLS 1.3 sangat dianjurkan karena memiliki arsitektur yang lebih sederhana dan aman. Selain itu, organisasi disarankan menggunakan pustaka kriptografi yang lebih ketat dalam pengelolaan keamanan, seperti LibreSSL atau BoringSSL, serta menerapkan praktik pengujian keamanan seperti fuzz testing dan audit kode secara berkala. Kasus Heartbleed menjadi pelajaran penting bahwa keamanan kriptografi tidak hanya ditentukan oleh algoritma, tetapi juga oleh implementasi dan konfigurasi sistem yang benar, konsisten, dan teruji.

---

## 7. Jawaban Pertanyaan
```python
- Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap ``brute force`` atau ``dictionary attack``?
- Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
- Pertanyaan 3: Bagaimana suatu organisasi bisa memastikan kalau sistem kriptografi mereka tetap aman di masa depan?
```
``Banyak sistem lama masih rentan brute force atau dictionary attack`` karena menggunakan algoritma hash kata sandi yang lemah, tidak menerapkan salt dan fungsi derivasi kunci yang kuat, serta membiarkan pengguna memilih kata sandi sederhana tanpa kebijakan keamanan yang ketat. ``Kelemahan algoritma`` berarti ada cacat dalam desain matematis cipher itu sendiri (misalnya kunci terlalu pendek atau rentan terhadap cryptanalysis), sedangkan ``kelemahan implementasi`` terjadi ketika algoritma yang aman diimplementasikan secara salah, seperti kesalahan manajemen kunci, bug kode, atau kebocoran melalui side‑channel. ``Untuk memastikan sistem kriptografi tetap aman`` di masa depan, organisasi perlu secara rutin mengaudit dan mengganti algoritma yang usang, menerapkan kebijakan kunci yang kuat, mempersiapkan migrasi ke kriptografi tahan kuantum, serta melakukan pemantauan ancaman, pelatihan keamanan, dan pengujian keamanan berkala.

---

## 8. Kesimpulan
Analisis kasus Heartbleed menunjukkan bahwa keamanan sistem kriptografi tidak hanya ditentukan oleh kekuatan algoritma, tetapi sangat bergantung pada kualitas implementasi dan konfigurasi sistem. Meskipun algoritma kriptografi modern seperti RSA, AES, dan SHA-256 aman secara teoretis, kesalahan implementasi dapat menyebabkan kebocoran data yang berdampak serius terhadap keamanan sistem. Oleh karena itu, penerapan kriptografi yang aman harus mencakup pemilihan algoritma yang tepat, implementasi yang benar, serta audit dan pembaruan sistem secara berkala untuk menghadapi ancaman yang terus berkembang.

---

## 9. Daftar Pustaka
```python
- Stallings, W. (2017). Cryptography and network security: Principles and practice (7th ed.). Pearson Education.
- Rinaldi, M. (2024). Serangan terhadap kriptografi [Materi kuliah IF4020 Kriptografi]. Program Studi Teknik Informatika, STEI ITB.
- Rinaldi, M. (2025). Serangan terhadap kriptografi [Materi kuliah IF4020 Kriptografi]. Program Studi Teknik Informatika, STEI ITB.
- Al‑Ghamdi, L., Al‑Sari, M., Abdullah, M., & Ali, G. A. (2026). Cryptanalysis in block ciphers: A comprehensive review and future directions. Fusion: Practice and Applications, 21(2), 170–187. https://doi.org/10.54216/FPA.210211
- Abid, N., et al. (2024). Evolution of cryptographic techniques: A comprehensive survey. Journal of Cybersecurity and Privacy, 4(1), 1–25.
- Thabit, F., et al. (2021). Security analysis and performance evaluation of a new lightweight cryptographic algorithm for IoT. Internet of Things, 15, 100432. https://doi.org/10.1016/j.iot.2021.100432
- Stinson, D. R., & Paterson, M. B. (2019). Cryptography: Theory and practice (4th ed.). CRC Press.
```

---

## 10. Commit Log
```
commit week14-analisis-serangan
Author: Amru Muiz Fauzan <amrumuzan092@gmail.com>
Date:   2026-01-17

    week14-analisis-serangan: laporan.md
```
