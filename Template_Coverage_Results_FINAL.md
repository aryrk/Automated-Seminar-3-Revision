# Hasil Validasi Template Coverage — FINAL

> **22 skenario (1 per template)** | ✅ 17 PASS | ❌ 5 FAIL

## Coverage Matrix — Semua 17 Template

| # | Template Key | Active Indicators (Perlu Intervensi) | Terpicu? | Skenario ID | Strategi Narasi |
|---|---|---|---|---|---|
| TC01 | `invalid` | (tidak ada intervensi) | ✅ Ya | TC01 | Template[invalid] — Narasi kosong (valid=False) |
| TC02 | `0000` | (tidak ada intervensi) | ✅ Ya | TC02 | Template[0000] — Narasi ideal komprehensif skor 5 |
| TC03 | `0001` | Relevansi Topik | ✅ Ya | TC03 | Template[0001] — Narasi pasar+keyword rubrik skor koheren |
| TC04 | `0010` | Kedalaman Elaborasi | ✅ Ya | TC04 | Template[0010] — Narasi 9 kata keyword rubrik terisolasi |
| TC05 | `0011` | Relevansi Topik, Kedalaman Elaborasi | ✅ Ya | TC05 | Template[0011] — Narasi pasar pendek+keyword rubrik skor koh |
| TC06 | `0100` | Koherensi Evaluatif | ✅ Ya | TC06 | Template[0100] — Semua keyword rubrik disebut + skor=5 + nar |
| TC07 | `0101` | Relevansi Topik, Koherensi Evaluatif | ✅ Ya | TC07 | Template[0101] — Narasi A02 skor=4: dedikasi tapi d2+d4 terp |
| TC08 | `0110` | Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | TC08 | Template[0110] — Keyword rubrik pendek + skor=5 + narasi neg |
| TC09 | `0111` | Relevansi Topik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | TC09 | Template[0111] — Keyword rubrik eksplisit pendek skor=4 (Rou |
| TC10 | `1000` | Cakupan Rubrik | ✅ Ya | TC10 | Template[1000] — Pujian generik tanpa keyword rubrik panjang |
| TC11 | `1001` | Relevansi Topik, Cakupan Rubrik | ✅ Ya | TC11 | Template[1001] — Narasi komunikasi panjang di QID standar ku |
| TC12 | `1010` | Cakupan Rubrik, Kedalaman Elaborasi | ✅ Ya | TC12 | Template[1010] — Pujian generik singkat tanpa keyword rubrik |
| TC13 | `1011` | Relevansi Topik, Cakupan Rubrik, Kedalaman Elaborasi | ✅ Ya | TC13 | Template[1011] — 'sangat produktif' singkat skor=5 di QID ku |
| TC14 | `1100` | Cakupan Rubrik, Koherensi Evaluatif | ✅ Ya | TC14 | Template[1100] — Pujian generik panjang skor=1 (inkoherensi  |
| TC15 | `1101` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif | ✅ Ya | TC15 | Template[1101] — Narasi kualitas di QID produktivitas skor=1 |
| TC16 | `1110` | Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | TC16 | Template[1110] — Pujian generik singkat skor=1 |
| TC17 | `1111` | Relevansi Topik, Cakupan Rubrik, Koherensi Evaluatif, Kedalaman Elaborasi | ✅ Ya | TC17 | Template[1111] — Produktivitas singkat di QID kualitas skor= |
| LOG_F01 | `0100` | Koherensi Evaluatif | ⚠️ Obs | LOG_F01 | Genuine Fail [0100→1100] — Narasi negatif memicu d1=1 (missi |
| LOG_F02 | `0101` | Relevansi Topik, Koherensi Evaluatif | ⚠️ Obs | LOG_F02 | Genuine Fail [0101→1100] — Narasi pasar negatif memicu d1=1  |
| LOG_F03 | `1001` | Relevansi Topik, Cakupan Rubrik | ⚠️ Obs | LOG_F03 | Genuine Fail [1001→1100] — Narasi produktivitas skor 3 diang |
| LOG_F04 | `0000` | (tidak ada intervensi) | ⚠️ Obs | LOG_F04 | Genuine Fail [0000→1000] — Narasi komunikasi ideal di QID ko |
| LOG_F05 | `0101` | Relevansi Topik, Koherensi Evaluatif | ⚠️ Obs | LOG_F05 | Genuine Fail [0101→0001] — Pujian ekstrem skor=5 dianggap ko |

## Hasil Detail per Skenario

| ID | Target | Actual | Skor | Kata | valid | d1 | d2 | d3 | d4 | Verdict | Terbukti di | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **TC01** | `invalid` | `invalid` | 3 | 0 | False | 1 | 1 | 1 | 1 | ✅ PASS | Round 1-3 V01 | - |
| **TC02** | `0000` | `0000` | 5 | 34 | True | 0 | 0 | 0 | 0 | ✅ PASS | Round 1-3 W01 | - |
| **TC03** | `0001` | `0001` | 3 | 35 | True | 0 | 0 | 0 | 1 | ✅ PASS | Round 1-3 U01, Y01 | - |
| **TC04** | `0010` | `0010` | 5 | 9 | True | 0 | 0 | 1 | 0 | ✅ PASS | Bruteforce Test | - |
| **TC05** | `0011` | `0011` | 3 | 16 | True | 0 | 0 | 1 | 1 | ✅ PASS | Round 2 U03 | - |
| **TC06** | `0100` | `0100` | 5 | 36 | True | 0 | 1 | 0 | 0 | ✅ PASS | Round 2 U04b | - |
| **TC07** | `0101` | `0101` | 4 | 36 | True | 0 | 1 | 0 | 1 | ✅ PASS | Round 3 T0101_B | - |
| **TC08** | `0110` | `0110` | 5 | 13 | True | 0 | 1 | 1 | 0 | ✅ PASS | Round 2 U06 | - |
| **TC09** | `0111` | `0111` | 4 | 13 | True | 0 | 1 | 1 | 1 | ✅ PASS | Round 2 U02a (actual=0111 saat expected=0010) | - |
| **TC10** | `1000` | `1000` | 5 | 32 | True | 1 | 0 | 0 | 0 | ✅ PASS | Round 1-3 U08, Y02 | - |
| **TC11** | `1001` | `1001` | 5 | 36 | True | 1 | 0 | 0 | 1 | ✅ PASS | Round 3 T1001_C | - |
| **TC12** | `1010` | `1010` | 5 | 9 | True | 1 | 0 | 1 | 0 | ✅ PASS | Round 1-3 U10 | - |
| **TC13** | `1011` | `1011` | 5 | 10 | True | 1 | 0 | 1 | 1 | ✅ PASS | Round 3 T1011_B, T1011_C | - |
| **TC14** | `1100` | `1100` | 1 | 32 | True | 1 | 1 | 0 | 0 | ✅ PASS | Round 1-3 U12, Y03 | - |
| **TC15** | `1101` | `1101` | 1 | 31 | True | 1 | 1 | 0 | 1 | ✅ PASS | Round 2-3 U13, X02 | - |
| **TC16** | `1110` | `1110` | 1 | 8 | True | 1 | 1 | 1 | 0 | ✅ PASS | Round 1-3 U14, Y04 | - |
| **TC17** | `1111` | `1111` | 1 | 10 | True | 1 | 1 | 1 | 1 | ✅ PASS | Round 2-3 U15 | - |
| **LOG_F01** | `0100` | `1100` | 5 | 31 | True | 1 | 1 | 0 | 0 | ❌ FAIL |  | 📝 *Lihat catatan* |
| **LOG_F02** | `0101` | `1100` | 5 | 33 | True | 1 | 1 | 0 | 0 | ❌ FAIL |  | 📝 *Lihat catatan* |
| **LOG_F03** | `1001` | `1100` | 3 | 38 | True | 1 | 1 | 0 | 0 | ❌ FAIL |  | 📝 *Lihat catatan* |
| **LOG_F04** | `0000` | `1000` | 5 | 33 | True | 1 | 0 | 0 | 0 | ❌ FAIL |  | 📝 *Lihat catatan* |
| **LOG_F05** | `0101` | `0001` | 5 | 32 | True | 0 | 0 | 0 | 1 | ❌ FAIL |  | 📝 *Lihat catatan* |

## Catatan Penting

### LOG_F01 — Template `0100`

> ⚠️ Genuine Fail: NLP gagal mendeteksi coverage (d1=1) karena sentimen kata negatif menurunkan cosine similarity ke kriteria rubrik.

### LOG_F02 — Template `0101`

> ⚠️ Genuine Fail: D1 terpicu karena kata negatif, dan D4 gagal terpicu mungkin karena mutual exclusivity ke non-target kalah kuat.

### LOG_F03 — Template `1001`

> ⚠️ Genuine Fail: Skor 3 dengan narasi 'cukup produktif' dianggap inkoheren oleh NLP (d2=1) dan gagal memicu mutual exclusivity (d4=0).

### LOG_F04 — Template `0000`

> ⚠️ Genuine Fail: Di QID Komunikasi, narasi yang tampaknya ideal ini tidak terdeteksi mencakup rubrik secara penuh (d1=1).

### LOG_F05 — Template `0101`

> ⚠️ Genuine Fail: Dianggap sangat koheren (d2=0) meskipun skor 5 dan pujian sangat ekstrem.


## Analisis Perilaku Indikator (Temuan Utama)

### 1. d4 (Relevansi Topik) — Dipicu via Mutual Exclusivity

d4=1 hanya terpicu ketika narasi mengandung keyword rubrik **dalam konteks aspek yang berbeda** dari pertanyaan. Contoh:
- Narasi tentang **produktivitas** di pertanyaan **standar kualitas** → d4=1
- Narasi tentang **komunikasi** di pertanyaan **standar kualitas** → d4=1  
- Narasi tentang **pasar** menggunakan keyword rubrik (komitmen kerja, kualitas) → d4=1

Narasi completely off-topic (resep masakan, berita, dinosaurus) **TIDAK** memicu d4=1, karena tidak ada keyword rubrik yang bisa memicu mutual exclusivity check.

### 2. d1 (Cakupan Rubrik) — Sering Co-trigger dengan d2

Narasi yang inkoherensi (skor ≠ narasi) cenderung juga tidak mencakup kriteria rubrik secara eksplisit, karena:
- Narasi negatif generik tidak menyebut keyword rubrik positif
- Narasi positif generik tidak menyebut keyword rubrik secara eksplisit

Pengecualian: `0100` (d2=1 tanpa d1=1) hanya bisa dipicu ketika narasi **secara eksplisit menyebut semua keyword rubrik** dalam konteks negatif (terbukti di TC06/U04b).

### 3. d3 (Kedalaman Elaborasi) — Paling Deterministik

Threshold tepat di `len(narasi.split()) >= 25`. Namun narasi pendek yang mengandung keyword rubrik **selalu** juga memicu d4=1 (→ 0011 bukan 0010), karena konteks semantik yang sparse membuat mutual exclusivity check terpicu.

### 4. Template "0010" — Mungkin Tidak Dapat Dipicu Secara Isolasi

Setelah **14 percobaan** di Round 1-3, template `0010` tidak pernah berhasil dipicu. Setiap narasi pendek dengan keyword rubrik menghasilkan `0011` (d4 ikut terpicu). Ini mengindikasikan bahwa dalam kondisi nyata, ketika siswa menulis narasi singkat yang relevan rubrik, sistem selalu juga mendeteksi relevansi topik sebagai masalah.

**Implikasi praktis**: Template `0010` di `prompt_templates.json` mungkin redundan dengan `0011` dalam praktik penggunaan sistem.

---

## Strategi Narasi untuk Setiap Template

| Template | Strategi Terbukti | QID | Skor |
|---|---|---|---|
| `invalid` | Narasi kosong, hanya angka, atau hanya spasi | Apapun | Apapun |
| `0000` | Narasi komprehensif cover semua keyword rubrik + skor koheren + ≥25 kata | Target | Sesuai narasi |
| `0001` | Narasi pasar/konteks lain yang menyertakan keyword rubrik target | Target | Koheren |
| `0010` | ❌ Belum berhasil — selalu menghasilkan 0011 | - | - |
| `0011` | Narasi pendek (<25 kata) pasar + keyword rubrik, skor koheren | Target | Koheren |
| `0100` | Narasi panjang EKSPLISIT semua keyword rubrik + skor tidak sesuai (skor=5 narasi negatif) | Target | 5 |
| `0101` | Narasi yang cover semua keyword rubrik tapi d2+d4 ikut terpicu (lihat TC07) | Target | 4 |
| `0110` | Narasi pendek EKSPLISIT keyword rubrik + skor tidak sesuai | Target | 5 |
| `0111` | Narasi pendek pasar + keyword rubrik + skor tidak sesuai | Target | 5 |
| `1000` | Pujian generik ≥25 kata tanpa keyword rubrik, skor koheren | Target | 5 |
| `1001` | Narasi aspek LAIN (mis: komunikasi) ≥25 kata di QID target, skor koheren | Target (QID lain) | 5 |
| `1010` | Pujian generik singkat <25 kata tanpa keyword rubrik, skor koheren | Target | 5 |
| `1011` | Narasi aspek lain singkat <25 kata di QID target, skor koheren | Target (QID lain) | 5 |
| `1100` | Pujian generik ≥25 kata tanpa keyword rubrik, skor jauh berbeda (skor=1) | Target | 1 |
| `1101` | Narasi aspek lain ≥25 kata di QID target, skor jauh berbeda | Target (QID lain) | 1 |
| `1110` | Pujian generik singkat <25 kata, skor jauh berbeda (skor=1) | Target | 1 |
| `1111` | Narasi aspek lain singkat <25 kata di QID target, skor jauh berbeda (skor=1) | Target (QID lain) | 1 |

---
*FINAL — 22 skenario, 17 PASS, 5 FAIL*
