# Hasil Validasi Template Coverage

> **30 skenario total** | ✅ 12 PASS | ❌ 18 FAIL | ⚠️ 0 Error

## Coverage Matrix — Semua Template

| Template Key | Active Indicators | Triggered? | Skenario |
|---|---|---|---|
| `0000` | (tidak ada intervensi) | ✅ Ya | W01 |
| `0001` | Relevansi Topik | ✅ Ya | U01, Y01 |
| `0010` | Kedalaman Elaborasi | ❌ Belum | - |
| `0011` | Relevansi Topik, Kedalaman Elaborasi | ❌ Belum | - |
| `0100` | Koherensi Evaluatif | ❌ Belum | - |
| `0101` | Relevansi Topik, Koherensi Evaluatif | ✅ Ya | W02 |
| `0110` | Koherensi Evaluatif, Kedalaman Elaborasi | ❌ Belum | - |
| `0111` | Relevansi Topik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | U02 |
| `1000` | Cakupan Rubrik | ✅ Ya | U08, X01, X04, Y02 |
| `1001` | Relevansi Topik, Cakupan Rubrik | ❌ Belum | - |
| `1010` | Cakupan Rubrik, Kedalaman Elaborasi | ✅ Ya | U10 |
| `1011` | Relevansi Topik, Cakupan Rubrik, Kedalaman Elaborasi | ❌ Belum | - |
| `1100` | Cakupan Rubrik, Koherensi Evaluatif | ✅ Ya | U04, U05, U09, U12, U13, X05, Y03 |
| `1101` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif | ✅ Ya | X02 |
| `1110` | Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | U03, U06, U07, U11, U14, U15, X03, Y04 |
| `1111` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ❌ Belum | - |
| `invalid` | (tidak ada intervensi) | ✅ Ya | V01, V02, V03, V04 |

## V — Template 'invalid' (narasi tidak valid)

| ID | Key Exp | Key Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **V01** | `invalid` | `invalid` | 3 | 0 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V02** | `invalid` | `invalid` | 3 | 25 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V03** | `invalid` | `invalid` | 3 | 0 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |
| **V04** | `invalid` | `invalid` | 3 | 6 | False | 1 | 1 | 1 | 1 | - | ✅ PASS | - |

## W — Template '0000' (semua indikator terpenuhi)

| ID | Key Exp | Key Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **W01** | `0000` | `0000` | 5 | 34 | True | 0 | 0 | 0 | 0 | - | ✅ PASS | - |
| **W02** | `0000` | `0101` | 4 | 36 | True | 0 | 1 | 0 | 1 | - | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), template_key(E:0000,A:0101) |

## U — Kombinasi Template '0001'–'1111' (1 atau lebih indikator perlu intervensi)

| ID | Key Exp | Key Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U01** | `0001` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | - | ✅ PASS | - |
| **U02** | `0010` | `0111` | 4 | 9 | True | 0 | 1 | 1 | 1 | - | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), template_key(E:0010,A:0111) |
| **U03** | `0011` | `1110` | 3 | 11 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d1(E:0,A:1), d2(E:0,A:1), d4(E:1,A:0), template_key(E:0011,A:1110) |
| **U04** | `0100` | `1100` | 5 | 31 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), template_key(E:0100,A:1100) |
| **U05** | `0101` | `1100` | 5 | 26 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), d4(E:1,A:0), template_key(E:0101,A:1100) |
| **U06** | `0110` | `1110` | 5 | 9 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d1(E:0,A:1), template_key(E:0110,A:1110) |
| **U07** | `0111` | `1110` | 5 | 8 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d1(E:0,A:1), d4(E:1,A:0), template_key(E:0111,A:1110) |
| **U08** | `1000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | - | ✅ PASS | - |
| **U09** | `1001` | `1100` | 3 | 31 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d2(E:0,A:1), d4(E:1,A:0), template_key(E:1001,A:1100) |
| **U10** | `1010` | `1010` | 5 | 9 | True | 1 | 0 | 1 | 0 | - | ✅ PASS | - |
| **U11** | `1011` | `1110` | 3 | 8 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d2(E:0,A:1), d4(E:1,A:0), template_key(E:1011,A:1110) |
| **U12** | `1100` | `1100` | 1 | 32 | True | 1 | 1 | 0 | 0 | - | ✅ PASS | - |
| **U13** | `1101` | `1100` | 1 | 26 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d4(E:1,A:0), template_key(E:1101,A:1100) |
| **U14** | `1110` | `1110` | 1 | 8 | True | 1 | 1 | 1 | 0 | - | ✅ PASS | - |
| **U15** | `1111` | `1110` | 1 | 9 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d4(E:1,A:0), template_key(E:1111,A:1110) |

## X — Variasi Multi-Question (lintas QID)

| ID | Key Exp | Key Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **X01** | `0000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), template_key(E:0000,A:1000) |
| **X02** | `1000` | `1101` | 4 | 30 | True | 1 | 1 | 0 | 1 | - | ❌ FAIL | d2(E:0,A:1), d4(E:0,A:1), template_key(E:1000,A:1101) |
| **X03** | `0010` | `1110` | 4 | 6 | True | 1 | 1 | 1 | 0 | - | ❌ FAIL | d1(E:0,A:1), d2(E:0,A:1), template_key(E:0010,A:1110) |
| **X04** | `0000` | `1000` | 5 | 33 | True | 1 | 0 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), template_key(E:0000,A:1000) |
| **X05** | `0100` | `1100` | 5 | 36 | True | 1 | 1 | 0 | 0 | - | ❌ FAIL | d1(E:0,A:1), template_key(E:0100,A:1100) |

## Y — Verifikasi Variabel Template (substitusi placeholder)

| ID | Key Exp | Key Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Y01** | `0001` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | vars_resolved | ✅ PASS | - |
| **Y02** | `1000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | vars_resolved | ✅ PASS | - |
| **Y03** | `0100` | `1100` | 5 | 31 | True | 1 | 1 | 0 | 0 | vars_resolved | ❌ FAIL | template_key(E:0100,A:1100) |
| **Y04** | `1111` | `1110` | 1 | 9 | True | 1 | 1 | 1 | 0 | vars_resolved | ❌ FAIL | d4(E:1,A:0), template_key(E:1111,A:1110) |

---

## Catatan Analisis

### ⚠️ Template yang Belum Terpicu

- `0010` — Active: Kedalaman Elaborasi
- `0011` — Active: Relevansi Topik, Kedalaman Elaborasi
- `0100` — Active: Koherensi Evaluatif
- `0110` — Active: Koherensi Evaluatif, Kedalaman Elaborasi
- `1001` — Active: Relevansi Topik, Cakupan Rubrik
- `1011` — Active: Relevansi Topik, Cakupan Rubrik, Kedalaman Elaborasi
- `1111` — Active: Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi

> Skenario tambahan diperlukan untuk memicu template di atas.

---
*Endpoint: `http://host.docker.internal:8080/feedback/analyze` — 30 skenario template coverage*
