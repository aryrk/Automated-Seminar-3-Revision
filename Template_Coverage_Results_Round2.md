# Hasil Validasi Template Coverage — Round 2

> **31 skenario** | ✅ 21 PASS | ❌ 10 FAIL | ⚠️ 0 Error

## Coverage Matrix

| Template | Active Indicators | Status | Skenario |
|---|---|---|---|
| `0000` | (tidak ada intervensi) | ✅ Terpicu | W01 |
| `0001` | Relevansi Topik | ✅ Terpicu | W02, U01, Y01 |
| `0010` | Kedalaman Elaborasi | ❌ Belum terpicu | - |
| `0011` | Relevansi Topik, Kedalaman Elaborasi | ✅ Terpicu | U03 |
| `0100` | Koherensi Evaluatif | ✅ Terpicu | U04b |
| `0101` | Relevansi Topik, Koherensi Evaluatif | ❌ Belum terpicu | - |
| `0110` | Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Terpicu | U06, U07 |
| `0111` | Relevansi Topik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Terpicu | U02a, U02b |
| `1000` | Cakupan Rubrik | ✅ Terpicu | U08, X01, Y02 |
| `1001` | Relevansi Topik, Cakupan Rubrik | ❌ Belum terpicu | - |
| `1010` | Cakupan Rubrik, Kedalaman Elaborasi | ✅ Terpicu | U10, U11 |
| `1011` | Relevansi Topik, Cakupan Rubrik, Kedalaman Elaborasi | ❌ Belum terpicu | - |
| `1100` | Cakupan Rubrik, Koherensi Evaluatif | ✅ Terpicu | U04a, U05, U09, U12, X03, Y03 |
| `1101` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif | ✅ Terpicu | U13, X02, X04 |
| `1110` | Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Terpicu | U14, Y04 |
| `1111` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Terpicu | U15 |
| `invalid` | (tidak ada intervensi) | ✅ Terpicu | V01, V02, V03, V04 |

## V — Template 'invalid'

| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **V01** | `invalid` | `invalid` | 3 | 0 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V02** | `invalid` | `invalid` | 3 | 25 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V03** | `invalid` | `invalid` | 3 | 0 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V04** | `invalid` | `invalid` | 3 | 6 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |

## W — Template '0000' (semua terpenuhi)

| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **W01** | `0000` | `0000` | 5 | 34 | True | 0 | 0 | 0 | 0 | - | ✅ PASS | - |
| **W02** | `0000` | `0001` | 5 | 32 | True | 0 | 0 | 0 | 1 | - | ❌ FAIL | d4(E:0,A:1), key(E:0000,A:0001) |

## U — Kombinasi '0001'–'1111'

| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U01** | `0001` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | - | ✅ PASS | - |
| **U02a** | `0010` | `0111` | 4 | 13 | True | 0 | 1 | 1 | 1 | - | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), key(E:0010,A:0111) |
| **U02b** | `0010` | `0111` | 4 | 16 | True | 0 | 1 | 1 | 1 | - | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), key(E:0010,A:0111) |
| **U03** | `0011` | `0011` | 3 | 16 | True | 0 | 0 | 1 | 1 | - | ✅ PASS | - |
| **U04a** | `0100` | `1100` | 5 | 40 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), key(E:0100,A:1100) |
| **U04b** | `0100` | `0100` | 5 | 36 | True | 0 | 1 | 0 | 0 | - | ✅ PASS | - |
| **U06** | `0110` | `0110` | 5 | 13 | True | 0 | 1 | 1 | 0 | - | ✅ PASS | - |
| **U05** | `0101` | `1100` | 5 | 33 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), d4(E:1,A:0), key(E:0101,A:1100) |
| **U07** | `0111` | `0110` | 5 | 13 | True | 0 | 1 | 1 | 0 | - | ❌ FAIL | d4(E:1,A:0), key(E:0111,A:0110) |
| **U08** | `1000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | - | ✅ PASS | - |
| **U09** | `1001` | `1100` | 3 | 38 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d2(E:0,A:1), d4(E:1,A:0), key(E:1001,A:1100) |
| **U10** | `1010` | `1010` | 5 | 9 | True | 1 | 0 | 1 | 0 | - | ✅ PASS | - |
| **U11** | `1011` | `1010` | 3 | 9 | True | 1 | 0 | 1 | 0 | - | ❌ FAIL | d4(E:1,A:0), key(E:1011,A:1010) |
| **U12** | `1100` | `1100` | 1 | 32 | True | 1 | 1 | 0 | 0 | - | ✅ PASS | - |
| **U13** | `1101` | `1101` | 1 | 31 | True | 1 | 1 | 0 | 1 | - | ✅ PASS | - |
| **U14** | `1110` | `1110` | 1 | 8 | True | 1 | 1 | 1 | 0 | - | ✅ PASS | - |
| **U15** | `1111` | `1111` | 1 | 10 | True | 1 | 1 | 1 | 1 | - | ✅ PASS | - |

## X — Variasi Multi-Question

| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **X01** | `0000` | `1000` | 5 | 33 | True | 1 | 0 | 0 | 0 | - | ❌ FAIL | key(E:0000,A:1000) |
| **X02** | `1101` | `1101` | 4 | 30 | True | 1 | 1 | 0 | 1 | - | ✅ PASS | - |
| **X03** | `1100` | `1100` | 1 | 33 | True | 1 | 1 | 0 | 0 | - | ✅ PASS | - |
| **X04** | `1001` | `1101` | 3 | 31 | True | 1 | 1 | 0 | 1 | - | ❌ FAIL | key(E:1001,A:1101) |

## Y — Verifikasi Variabel Template

| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Y01** | `0001` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | vars_ok | ✅ PASS | - |
| **Y02** | `1000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | vars_ok | ✅ PASS | - |
| **Y03** | `1100` | `1100` | 1 | 32 | True | 1 | 1 | 0 | 0 | vars_ok | ✅ PASS | - |
| **Y04** | `1110` | `1110` | 1 | 8 | True | 1 | 1 | 1 | 0 | vars_ok | ✅ PASS | - |

---

## Temuan & Analisis Round 2

### ⚠️ Template Belum Terpicu
- `0010` (Kedalaman Elaborasi)
- `0101` (Relevansi Topik, Koherensi Evaluatif)
- `1001` (Relevansi Topik, Cakupan Rubrik)
- `1011` (Relevansi Topik, Cakupan Rubrik, Kedalaman Elaborasi)

### Pola Perilaku d-bit yang Teridentifikasi

| Indikator | Pola Perilaku |
|---|---|
| **d4 (Relevansi Topik)** | Hanya terpicu via *mutual exclusivity* — narasi menggunakan keyword rubrik dalam konteks aspek berbeda (pasar, produktivitas di QID kualitas). Narasi completely off-topic (resep, berita) TIDAK memicu d4. |
| **d1 (Cakupan Rubrik)** | Sering co-trigger dengan d2. Narasi yang inkoherensi (skor≠narasi) cenderung tidak cover kriteria rubrik secara eksplisit. |
| **d2 (Koherensi)** | Dapat berdiri sendiri (template 0100) hanya jika narasi EKSPLISIT menyebut semua keyword rubrik tapi skor tidak sesuai. |
| **d3 (Elaborasi)** | Paling deterministik: count kata < 25 → d3=1. Sering co-trigger karena narasi pendek juga ambigu secara semantik. |

---
*Round 2 — 31 skenario*
