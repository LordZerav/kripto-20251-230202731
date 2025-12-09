# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: Public Key Infrastructure (PKI & Certificate Authority)
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA  

---

## 1. Tujuan
```python
- Membuat sertifikat digital sederhana.
- Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
- Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).
```

---

## 2. Dasar Teori
Certificate Authority (CA) merupakan entitas tepercaya dalam Public Key Infrastructure (PKI) yang bertanggung jawab menerbitkan, mengelola, dan mencabut sertifikat digital untuk mengikat kunci publik dengan identitas pemiliknya, sementara PKI adalah kerangka keseluruhan yang mengintegrasikan kriptografi kunci publik, sertifikat X.509, direktori sertifikat, serta kebijakan untuk mendukung komunikasi aman di jaringan terbuka. CA beroperasi dalam hierarki dengan Root CA di puncak yang menandatangani sertifikat Intermediate CA, memastikan rantai kepercayaan melalui tanda tangan digital yang diverifikasi secara berjenjang, sebagaimana dijelaskan dalam standar PKI yang mencakup Registration Authority (RA) untuk verifikasi identitas pemohon sebelum penerbitan sertifikat.

Peran utama CA meliputi verifikasi identitas entitas seperti individu, organisasi, atau perangkat melalui proses pendaftaran yang ketat, penerbitan sertifikat yang ditandatangani dengan kunci privat CA, serta pemeliharaan Certificate Revocation List (CRL) atau OCSP untuk mencabut sertifikat yang kompromi, sehingga PKI dapat mendeteksi dan menangani ancaman secara real-time. Dalam komunikasi aman, PKI memanfaatkan CA untuk mengaktifkan protokol seperti TLS/SSL pada HTTPS, VPN, dan email S/MIME, di mana sertifikat memvalidasi server agar pengguna menghindari serangan man-in-the-middle, sementara RA mendukung skalabilitas dengan menangani autentikasi lokal.

Kegunaan PKI dengan CA mencakup non-repudiasi melalui tanda tangan digital yang tidak dapat disangkal, autentikasi mutual antarpihak, serta enkripsi data end-to-end yang mencegah intersepsi, sehingga esensial untuk e-commerce, pemerintahan digital, dan IoT di mana kepercayaan atas identitas menjadi pondasi keamanan siber. Manfaatnya termasuk efisiensi distribusi kunci publik tanpa saluran aman terpisah, pengurangan risiko pemalsuan melalui validasi rantai sertifikat, dan kepatuhan regulasi seperti eIDAS di Eropa atau standar NIST di AS, menjadikan PKI sebagai tulang punggung infrastruktur keamanan modern.

---

## 3. Alat dan Bahan
```python
- Visual Studio Code
- Git dan akun GitHub  
- Python 3.11
```

---

## 4. Langkah Percobaan
```python
- Buat program simulasi pembuatan sertifikat digital dengan python atau OpenSSL.
- Buat laporan.md dan menjawab beberapa pertanyaan.
```

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
```python
- Pertanyaan 1: …  
- Pertanyaan 2: …
```


---

## 8. Kesimpulan
Certificate Authority (CA) dan Public Key Infrastructure (PKI) membentuk fondasi kepercayaan dalam kriptografi kunci publik, di mana CA menerbitkan sertifikat digital untuk mengikat kunci publik dengan identitas terverifikasi melalui hierarki rantai kepercayaan, sementara PKI mengintegrasikan sertifikat, CRL, dan protokol seperti TLS untuk autentikasi, enkripsi, serta non-repudiasi dalam komunikasi aman seperti HTTPS, VPN, dan tanda tangan digital, sehingga mencegah pemalsuan, man-in-the-middle, dan memastikan efisiensi keamanan siber modern tanpa saluran kunci terpisah.​

---

## 9. Daftar Pustaka
```python
- Stallings, W. (2017). Cryptography and network security: Principles and practice (7th ed.). Pearson (Chapter on PKI and Certificate Authorities).​
- Tanenbaum, A. S., & Wetherall, D. J. (2011). Computer networks (5th ed.). Pearson (Section on Public Key Infrastructure).​
- Paar, C., Pelzl, J., & Preneel, B. (2010). Understanding cryptography. Springer (PKI frameworks).​
- Rinaldi Munir. (n.d.). Public Key Infrastructure (PKI). Institut Teknologi Bandung. https://informatika.stei.itb.ac.id/~rinaldi.munir/Kriptografi/Public%20Key%20Infrastructure.pdf​
- National Institute of Standards and Technology. (2013). Digital Signature Standard (DSS) (FIPS 186-4). U.S. Department of Commerce. https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf​
- Katz, J., & Lindell, Y. (2020). Introduction to modern cryptography (3rd ed.). CRC Press (Chapter on PKI and CAs).​
---

```

## 10. Commit Log
```
commit week10-pki
Author: Amru Muiz Fauzan <amrumuzan092@gmail.com>
Date:   2025-12-09

    week10-pki: implementasi program python sertifikat digital dan menyelesaikan laporan.md
```
