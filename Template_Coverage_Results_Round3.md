# Hasil Validasi Template Coverage — Round 3

> **14 skenario targeted** | ✅ 4 PASS | ❌ 10 FAIL

> **Target**: Template `0010`, `0101`, `1001`, `1011`

## Hasil Detail

| ID | Target | Actual | Skor | Kata | valid | d1 | d2 | d3 | d4 | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **T0101_A** | `0101` | `0001` | 5 | 32 | True | 0 | 0 | 0 | 1 | ❌ FAIL | d2(E:1,A:0), key(E:0101,A:0001) |
| **T0101_B** | `0101` | `0101` | 4 | 36 | True | 0 | 1 | 0 | 1 | ✅ PASS | - |
| **T0101_C** | `0101` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | ❌ FAIL | d2(E:1,A:0), key(E:0101,A:0001) |
| **T1001_A** | `1001` | `1000` | 5 | 34 | True | 1 | 0 | 0 | 0 | ❌ FAIL | d4(E:1,A:0), key(E:1001,A:1000) |
| **T1001_B** | `1001` | `0100` | 4 | 37 | True | 0 | 1 | 0 | 0 | ❌ FAIL | d1(E:1,A:0), d2(E:0,A:1), d4(E:1,A:0), key(E:1001,A:0100) |
| **T1001_C** | `1001` | `1001` | 5 | 36 | True | 1 | 0 | 0 | 1 | ✅ PASS | - |
| **T1011_A** | `1011` | `1111` | 4 | 10 | True | 1 | 1 | 1 | 1 | ❌ FAIL | d2(E:0,A:1), key(E:1011,A:1111) |
| **T1011_B** | `1011` | `1011` | 5 | 10 | True | 1 | 0 | 1 | 1 | ✅ PASS | - |
| **T1011_C** | `1011` | `1011` | 5 | 8 | True | 1 | 0 | 1 | 1 | ✅ PASS | - |
| **T0010_A** | `0010` | `0011` | 5 | 14 | True | 0 | 0 | 1 | 1 | ❌ FAIL | d4(E:0,A:1), key(E:0010,A:0011) |
| **T0010_B** | `0010` | `0111` | 4 | 20 | True | 0 | 1 | 1 | 1 | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), key(E:0010,A:0111) |
| **T0010_C** | `0010` | `0011` | 5 | 21 | True | 0 | 0 | 1 | 1 | ❌ FAIL | d4(E:0,A:1), key(E:0010,A:0011) |
| **T0010_D** | `0010` | `0011` | 3 | 15 | True | 0 | 0 | 1 | 1 | ❌ FAIL | d4(E:0,A:1), key(E:0010,A:0011) |
| **T0010_N01** | `0010` | `0111` | 4 | 12 | True | 0 | 1 | 1 | 1 | ❌ FAIL | key(E:0010,A:0111) |

## Analisis per Target Template

### Template `0010` ❌ Belum terpicu

Actual yang diperoleh: ['0011', '0111']

> **Kemungkinan penyebab struktural**: Kombinasi indikator `0010` mungkin sulit atau tidak dapat dipicu secara deterministik karena interdependensi antar indikator dalam arsitektur model embedding yang digunakan.

### Template `0101` ✅ BERHASIL

Actual yang diperoleh: ['0001', '0101']

### Template `1001` ✅ BERHASIL

Actual yang diperoleh: ['0100', '1000', '1001']

### Template `1011` ✅ BERHASIL

Actual yang diperoleh: ['1011', '1111']


## Kesimpulan Coverage

- **Berhasil dipicu (kumulatif Round 1-3)**: ['0000', '0001', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', 'invalid']
- **Belum terpicu**: ['0010']

## Temuan Akhir: Pola Perilaku Indikator

| Indikator | Kondisi Pemicu | Catatan |
|---|---|---|
| **d4=1** (Relevansi) | Narasi mengandung keyword rubrik dalam konteks aspek rubrik BERBEDA dari pertanyaan (mutual exclusivity). Narasi completely off-topic TIDAK memicu d4. | Terpicu reliabel via cross-aspect (produktivitas di QID kualitas, atau narasi pasar+keyword rubrik) |
| **d1=1** (Cakupan) | Narasi tidak menyebut kriteria rubrik target secara semantik | Sering co-trigger dengan d2; konteks off-topic menurunkan d1 similarity meski keyword hadir |
| **d2=1** (Koherensi) | Skor dan sentimen narasi tidak selaras | Lebih mudah trigger ketika skor jauh berbeda dari sentimen narasi (skor=1 vs narasi positif, atau skor=5 vs narasi negatif) |
| **d3=1** (Elaborasi) | Jumlah kata < 25 | Paling deterministik; threshold tepat di len(narasi.split()) >= 25 |

---
*Round 3 — 14 skenario targeted*
