# Hasil Validasi Logika NLP — Suite Lengkap (v2+v3 Gabungan)

> **107 skenario total** | ✅ 56 PASS | ❌ 13 FAIL | 👁️ 38 OBS | ⚠️ 0 Error
> Threshold f3: **25 kata** (`len(narasi.split()) >= 25`)


## A — Baseline (Siswa Ideal)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **A01** | 5 | 34 | True | 0 | 0 | 0 | 0 | ✅ PASS | - |
| **A02** | 4 | 36 | True | 0 | 1 | 0 | 1 | ✅ PASS | - |

## B — Siswa Malas / Minimal Effort

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **B01** | 3 | 1 | False | 1 | 1 | 1 | 1 | ✅ PASS | - |
| **B02** | 3 | 4 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **B03** | 4 | 14 | True | 1 | 1 | 1 | 1 | ✅ PASS | - |
| **B04** | 4 | 21 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **B05** | 4 | 24 | True | 0 | 1 | 1 | 1 | ✅ PASS | - |
| **B06** | 4 | 25 | True | 0 | 1 | 0 | 1 | ✅ PASS | - |
| **B07** | 3 | 0 | False | 1 | 1 | 1 | 1 | ✅ PASS | - |
| **B08** | 3 | 0 | False | 1 | 1 | 1 | 1 | ✅ PASS | - |
| **B09** | 3 | 25 | False | 1 | 1 | 1 | 1 | ✅ PASS | - |

## C — Copy-Paste & Pengulangan

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **C01** | 4 | 25 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **C02** | 4 | 30 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |

## D — Basa-Basi & Pujian Kosong

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **D01** | 5 | 32 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **D02** | 4 | 27 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **D03** | 5 | 53 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |

## E — Koherensi Skor-Narasi Bermasalah

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **E01** | 5 | 30 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **E02** | 1 | 31 | True | 0 | 1 | 0 | 0 | ✅ PASS | - |
| **E03** | 4 | 28 | True | 0 | 1 | 0 | 1 | ❌ FAIL | d2(E:0,A:1) |
| **E04** | 3 | 31 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |
| **E05** | 2 | 29 | True | 0 | 1 | 0 | 1 | ❌ FAIL | d2(E:0,A:1) |

## F — Keyword Stuffing (Strategis)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **F01** | 5 | 26 | True | 0 | 0 | 0 | 1 | 👁️ OBS | Observasional |
| **F02** | 5 | 27 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |

## G — Campur Bahasa

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **G01** | 4 | 34 | True | 0 | 1 | 0 | 1 | ✅ PASS | - |
| **G02** | 4 | 29 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **G03** | 3 | 31 | True | 1 | 1 | 0 | 0 | 👁️ OBS | Observasional |

## H — Input Tidak Normal

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **H01** | 3 | 12 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **H02** | 3 | 26 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **H03** | 5 | 1 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **H04** | 3 | 32 | True | 1 | 0 | 0 | 0 | ❌ FAIL | d4(E:1,A:0) |
| **H05** | 3 | 31 | True | 1 | 1 | 0 | 0 | ❌ FAIL | d4(E:1,A:0) |
| **H06** | 3 | 35 | True | 1 | 1 | 0 | 0 | ❌ FAIL | d4(E:1,A:0) |

## I — Skor Ekstrem

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **I01** | 1 | 31 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **I02** | 5 | 32 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |
| **I03** | 5 | 31 | True | 0 | 0 | 0 | 1 | 👁️ OBS | Observasional |

## J — Multi-Question (Variasi Aspek)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **J01** | 5 | 32 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **J02** | 4 | 28 | True | 1 | 1 | 0 | 1 | ✅ PASS | - |
| **J03** | 5 | 33 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **J04** | 3 | 34 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |

## K — Variasi Panjang Narasi

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **K01** | 5 | 92 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |
| **K02** | 4 | 27 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **K03** | 4 | 53 | True | 0 | 1 | 0 | 1 | ✅ PASS | - |

## L — Edge Case Linguistik

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **L01** | 3 | 1 | True | 0 | 0 | 1 | 1 | 👁️ OBS | Observasional |
| **L02** | 4 | 22 | True | 0 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **L03** | 5 | 53 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |
| **L04** | 5 | 35 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |

## M — Perilaku Sosial Mahasiswa

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **M01** | 5 | 32 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **M02** | 1 | 26 | True | 0 | 1 | 0 | 0 | ✅ PASS | - |
| **M03** | 4 | 33 | True | 0 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **M04** | 3 | 30 | True | 1 | 1 | 0 | 0 | ❌ FAIL | d4(E:1,A:0) |
| **M05** | 5 | 32 | True | 0 | 0 | 0 | 0 | ❌ FAIL | d1(E:1,A:0) |

## N — Probe Threshold f3 (len(split()) >= 25?)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **N01** | 4 | 12 | True | 0 | 1 | 1 | 1 | ✅ PASS | - |
| **N02** | 4 | 16 | True | 0 | 1 | 1 | 0 | ✅ PASS | - |
| **N03** | 4 | 18 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **N04** | 4 | 20 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **N05** | 4 | 21 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **N06** | 4 | 24 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **N07** | 4 | 25 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **N08** | 4 | 26 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **N09** | 4 | 25 | True | 0 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **N10** | 4 | 22 | True | 0 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **N11** | 4 | 24 | True | 0 | 1 | 1 | 1 | 👁️ OBS | Observasional |

## O — Probe Sinonim & Parafrase f1

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **O01** | 4 | 24 | True | 0 | 1 | 1 | 0 | 👁️ OBS | Observasional |
| **O02** | 4 | 23 | True | 0 | 1 | 1 | 0 | 👁️ OBS | Observasional |
| **O03** | 5 | 27 | True | 0 | 0 | 0 | 0 | 👁️ OBS | Observasional |
| **O04** | 4 | 28 | True | 0 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **O05** | 5 | 24 | True | 0 | 0 | 1 | 1 | ✅ PASS | - |
| **O06** | 4 | 24 | True | 1 | 1 | 1 | 0 | ✅ PASS | - |
| **O07** | 4 | 24 | True | 0 | 1 | 1 | 0 | 👁️ OBS | Observasional |
| **O08** | 5 | 25 | True | 0 | 0 | 0 | 0 | 👁️ OBS | Observasional |

## P — Matriks Koherensi f2 (5 Skor × 3 Sentimen)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **P01** | 5 | 25 | True | 0 | 0 | 0 | 0 | ✅ PASS | - |
| **P02** | 5 | 21 | True | 0 | 0 | 1 | 0 | 👁️ OBS | Observasional |
| **P03** | 5 | 26 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **P04** | 4 | 24 | True | 0 | 1 | 1 | 0 | ❌ FAIL | d2(E:0,A:1) |
| **P05** | 4 | 24 | True | 0 | 1 | 1 | 1 | ❌ FAIL | d2(E:0,A:1) |
| **P06** | 4 | 24 | True | 0 | 1 | 1 | 0 | ✅ PASS | - |
| **P07** | 3 | 23 | True | 0 | 0 | 1 | 0 | ❌ FAIL | d2(E:1,A:0) |
| **P08** | 3 | 22 | True | 0 | 0 | 1 | 1 | ✅ PASS | - |
| **P09** | 3 | 22 | True | 0 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **P10** | 2 | 23 | True | 0 | 1 | 1 | 0 | ✅ PASS | - |
| **P11** | 2 | 26 | True | 0 | 1 | 0 | 0 | ❌ FAIL | d2(E:0,A:1) |
| **P12** | 2 | 25 | True | 0 | 1 | 0 | 0 | ❌ FAIL | d2(E:0,A:1) |
| **P13** | 1 | 23 | True | 0 | 1 | 1 | 0 | ✅ PASS | - |
| **P14** | 1 | 22 | True | 0 | 0 | 1 | 0 | ✅ PASS | - |
| **P15** | 1 | 28 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |

## Q — Probe Boundary f4 (Relevansi Topik)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **Q01** | 3 | 21 | True | 1 | 0 | 1 | 0 | 👁️ OBS | Observasional |
| **Q02** | 3 | 24 | True | 0 | 0 | 1 | 1 | 👁️ OBS | Observasional |
| **Q03** | 3 | 26 | True | 0 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **Q04** | 3 | 27 | True | 0 | 0 | 0 | 1 | ✅ PASS | - |
| **Q05** | 3 | 24 | True | 1 | 1 | 1 | 0 | 👁️ OBS | Observasional |
| **Q06** | 3 | 27 | True | 0 | 0 | 0 | 0 | 👁️ OBS | Observasional |
| **Q07** | 3 | 27 | True | 1 | 1 | 0 | 0 | ❌ FAIL | d4(E:1,A:0) |

## R — Probe Valid Filter

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **R01** | 3 | 1 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **R02** | 3 | 2 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **R03** | 3 | 2 | True | 1 | 1 | 1 | 0 | 👁️ OBS | Observasional |
| **R04** | 3 | 21 | True | 0 | 0 | 1 | 1 | 👁️ OBS | Observasional |
| **R05** | 3 | 17 | True | 0 | 0 | 1 | 1 | 👁️ OBS | Observasional |
| **R06** | 3 | 21 | True | 0 | 0 | 1 | 0 | 👁️ OBS | Observasional |
| **R07** | 4 | 4 | False | 1 | 1 | 1 | 1 | 👁️ OBS | Observasional |
| **R08** | 4 | 23 | True | 0 | 1 | 1 | 0 | 👁️ OBS | Observasional |

## S — Skor di Luar Rentang

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **S01** | 0 | 26 | True | 1 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **S02** | 6 | 21 | True | 0 | 1 | 1 | 0 | 👁️ OBS | Observasional |

## T — Variasi Aspek Rubrik (Multi-Question Detail)

| ID | Skor | Kata | valid | d1 Cakupan | d2 Koherensi | d3 Elaborasi | d4 Relevansi | Verdict | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| **T01** | 5 | 25 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **T02** | 4 | 25 | True | 1 | 1 | 0 | 0 | 👁️ OBS | Observasional |
| **T03** | 5 | 26 | True | 1 | 0 | 0 | 0 | ✅ PASS | - |
| **T04** | 4 | 25 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |
| **T05** | 4 | 26 | True | 1 | 1 | 0 | 0 | ✅ PASS | - |

---
*Endpoint: `http://host.docker.internal:8080/feedback/analyze` — 107 skenario*
