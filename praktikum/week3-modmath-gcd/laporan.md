# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: week3-modmath-gcd  
Nama: Amru Muiz Fauzan
NIM: 230202731
Kelas: 5IKRA  

---

## 1. Tujuan
```
- Menyelesaikan operasi aritmetika modular.
- Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
- Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
```

---

## 2. Dasar Teori


---

## 3. Alat dan Bahan
```
- Visual Studio Code
- Git dan akun GitHub  
- Terminal
```

---

## 4. Langkah Percobaan
1. Membuat program python yang berisi :
```
- Modular arithmetic (add, sub, mul, exp).
- GCD & Euclidean Algorithm.
- Extended Euclidean & modular inverse.
- Discrete log sederhana.
```
2. Melakukan screenshots hasil eksekusi setiap program.
3. Menyelesaikan laporan.md yang berisi :
```
- Ringkasan teori modular arithmetic & GCD
- Hasil pengujian dengan kasus
- Jawaban atas pertanyaan diskusi
```

---

## 5. Source Code
modular_math.py
```python
def modular_tambah(a, b, x): return (a + b) % x
def modular_kurang(a, b, x): return (a - b) % x
def modular_kali(a, b, x): return (a * b) % x
def modular_eksponensiasi(base, exp, x): return pow(base, exp, x)

print("21 + 7 mod 10 =", modular_tambah(21, 7, 10))
print("21 - 7 mod 10 =", modular_kurang(21, 7, 10))
print("21 * 7 mod 10 =", modular_kali(21, 7, 10))
print("21 ^ 7 mod 10 =", modular_eksponensiasi(21, 7, 10))
```

gcd_euclidean_algorithm.py
```python
def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b 
    return a
    
print("gcd dari (54, 24) adalah ", gcd_euclidean(54, 24))
```

extended_euclidean_algorithm.py
```python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modular_inverse(a, x):
    g, n, _ = extended_gcd(a, x)
    if g != 1:
        return None
    return n % x

print("Invers dari 3 mod 11 adalah", modular_inverse(3, 11))
```

discrete_algorithm.py
```python
def discrete_logarithm(a, b, x):
    for n in range(x):
        if pow(a, n, x) == b:
            return n
    return None

print("Discrete Logarithm dari 3^n ≡ 4 (mod 7) adalah n = ", discrete_logarithm(3, 4, 7))
```

---

## 6. Hasil dan Pembahasan
![Modular Arithmatic](screenshots/ss_modular_math.png)
![GCD & Euclidean Algorithm](screenshots/ss_gcd_euclidean_algorithm.png)
![Extended Euclidean Algorithm](screenshots/ss_extended_euclidean_algorithm.png)
![Discrete Logarithm](screenshots/ss_discrete_logarithm.png)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: 
- Pertanyaan 2: 
- Pertanyaan 3: 

---

## 8. Kesimpulan


---

## 9. Daftar Pustaka
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.
- 

---

## 10. Commit Log
```
commit week3-modmath-gcd
Author: Amru Muiz Fauzan <amrumuzan092@gmail.com>
Date:   2025-10-17

    week3-modmath-gcd: program python modular arithmetic & gcd sekaligus menyelesaikan laporan.md
```
