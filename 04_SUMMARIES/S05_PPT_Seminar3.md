# RINGKASAN: PPT Seminar 3 — Presentasi Sidang (04 Juli 2026)

> **Fungsi dalam pipeline**: Memahami konteks dan konten penelitian TA sebelum membaca transcript. Menjadi referensi untuk interpretasi komentar dosen (Fase 4) dan verifikasi kesesuaian antara isi presentasi dengan laporan tertulis.

> ⚠️ **Sumber**: 2 file PPT tersedia — `Seminar 3.md` (versi ringkas, 743 baris) dan `20260629_Seminar 3.md` (versi detail, 1018 baris). Ringkasan ini berbasis file detail.

---

## 1. Identitas Penelitian

| Aspek | Detail |
|---|---|
| Judul | PEMANFAATAN DIGITAL SCAFFOLDING BERBASIS RUBRIK UNTUK MENDUKUNG INDIKATOR TEKSTUAL FEEDBACK LITERACY PADA PROJECT-BASED LEARNING |
| Mahasiswa | Aryo Rakatama (221524003) dan Muhammad Rama Nurimani (221524021) |
| Prodi | Sarjana Terapan Teknik Informatika, JTK, POLBAN |
| Seminar | Seminar 3, Sabtu 04 Juli 2026 |
| Pembimbing | Irwan Setiawan, S.Si., M.T. dan Jonner Hutahaean, BSET., M.Info.Sys. |
| Penguji | Ani Rahmani, S.Si., M.T. dan Yudi Widhiyasana, S.Si., M.T. |

---

## 2. Ringkasan Penelitian

### Problem

Dalam konteks **Project-Based Learning (PjBL)**, Self & Peer Assessment memberikan narasi kualitatif yang seharusnya merefleksikan dinamika kolaborasi. Namun faktanya:
- Narasi feedback sering **generik dan tidak selaras dengan skor numerik**
- Skala masalah terukur: Self Assessment = 13,2% selaras; Peer Assessment = 23,7% selaras (data historis dari Setiawan, 2026)

**4 gejala tekstual berulang yang teridentifikasi**:
1. Narasi sangat singkat (median 6 kata)
2. Fokus bergeser ke pembahasan di luar topik pertanyaan
3. Skor dan narasi tidak selaras
4. Dimensi penilaian tidak tercakup dalam narasi

**Gap yang diatasi**:
- GAP 1: Karakteristik tekstual teridentifikasi, tetapi belum dioperasionalkan sebagai indikator otomatis yang terdeteksi real-time
- GAP 2: Scaffolding yang ada bersifat post-hoc (setelah penulisan), belum real-time saat penulisan

### Tujuan Penelitian (2 tujuan)

1. **Merancang pipeline digital scaffolding** yang mengintegrasikan NLP dengan rule-based untuk mendeteksi 4 indikator tekstual selama penulisan aktif narasi self dan peer assessment.
2. **Mengukur perbedaan tingkat pemenuhan** keempat indikator tekstual melalui pilot study dengan perbandingan kelompok treatment (dengan scaffolding) vs kelompok kontrol (tanpa scaffolding) → menghasilkan estimasi effect size awal.

### Research Questions

- **RQ 1**: Sejauh mana pipeline digital scaffolding mampu mendeteksi keempat indikator tekstual (cakupan rubrik, koherensi skor-narasi, kedalaman elaborasi, relevansi topik) melalui kombinasi model semantik dan aturan heuristik berbasis rubrik?
- **RQ 2**: Sejauh mana intervensi digital scaffolding berbasis rubrik memengaruhi pemenuhan keempat indikator tekstual, ditinjau dari perbedaan tingkat pemenuhan antara kelompok treatment dan kontrol serta pola interaksi mahasiswa dengan scaffolding?

---

## 3. Metodologi

### Variabel

| Variabel | Detail |
|---|---|
| **Bebas** | Keberadaan bantuan scaffolding (mendapat scaffolding vs tidak mendapat scaffolding) |
| **Terikat (4 indikator)** | f1: Cakupan Rubrik; f2: Koherensi Skor-Narasi; f3: Kedalaman Elaborasi; f4: Relevansi Topik |

### Desain Penelitian

- **Kuantitatif**: Randomized posttest-only control group design (Desain 6) — Campbell et al., 1963; Shadish et al., 2002
- **Evaluasi statistik**: MANOVA (Pillai's Trace) + Cohen's d

### Data Penelitian

| Data | Jumlah |
|---|---|
| Data Feedback historis | 10.098 (8.118 peer, 1.908 self) |
| Sampel Anotasi | 384 sampel |
| Data Eksperimen | 56 mahasiswa: 27 kelompok treatment, 29 kelompok kontrol |

### Pendekatan Teknis — Pipeline Digital Scaffolding

- **Arsitektur**: NLP (Semantic Similarity Embedding) + Rule-Based
- **Model embedding dipilih**: `intfloat/multilingual-e5-large-instruct` (dengan semantic chunking dan mutual exclusivity untuk f2)
- **Dekomposisi Rubrik**: Rubrik didekomposisi menjadi feature-set → vektor → cosine similarity vs teks narasi
- **Threshold**: Kalibrasi menggunakan grid search
- **Intervensi**: Template-based scaffolding (bukan LLM/RAG/fine-tuning) — dipilih karena konsisten dan tidak memicu over-reliance
- **Implementasi**: Terintegrasi di APE bernama **SAPA** (Self and Peer Assessment), debounce 1,5 detik setelah mahasiswa berhenti mengetik

---

## 4. Hasil Pengembangan APE (BAB IV di Laporan)

### Analisis Problem Domain
- Data historis 10.098 narasi menunjukkan 4 pola kegagalan berulang
- Skor numerik tidak mencerminkan kualitas narasi (distribusi panjang narasi per skor saling overlap)
- Terdapat penurunan usaha naratif sepanjang semester
- ±90% mahasiswa menulis lebih panjang pada self dibanding peer (asimetri)

### APE — SAPA (Self and Peer Assessment)
- Integrasi pipeline pada form pengisian assessment → debounce → API → tampilkan scaffolding
- Toggle untuk mengaktifkan/menonaktifkan scaffolding
- Progres dekomposisi rubrik ditampilkan
- Scaffolding berhenti otomatis ketika seluruh indikator terpenuhi

### Hasil Pengujian APE
- 41 test case PASSED, 1 FAIL (kasus narasi dengan sentimen sangat negatif pada indikator koherensi skor — sistem mendeteksi inkonsistensi tetapi belum dapat memprediksi skor tersirat)

---

## 5. Hasil Eksperimen (BAB V di Laporan)

### RQ 1 — Deteksi Indikator

| Indikator | Threshold | F1 | Precision | Recall |
|---|---|---|---|---|
| Cakupan Rubrik (f1) | 0.84 | 0.6140 | 0.5312 | 0.7275 |
| Relevansi Topik (f4) | 0.85 | 0.4296 | 0.4265 | 0.4327 |
| Koherensi Skor (f2) | 0.87 | 0.5314 | 0.4409 | 0.6687 |
| Kedalaman Elaborasi (f3) | Threshold 25 kata | — | — | — |

**Interpretasi**:
- Cakupan rubrik (0,61): model cukup andal mengenali keberadaan topik rubrik secara semantik
- Koherensi skor (0,53): lebih sulit — model harus membedakan tingkat kualitas ordinal
- Relevansi topik (0,42): tersulit — narasi relevan ke proyek tapi tidak spesifik ke aspek rubrik

**Kesimpulan RQ 1**: Pipeline mampu mendeteksi keempat indikator, tetapi kemampuan deteksi bergantung pada karakteristik indikator. Pendekatan hybrid (semantic embedding + heuristik/rule-based) diperlukan untuk performa memadai.

### RQ 2 — Efek Intervensi (MANOVA)

| Jenis Assessment | p-value | Signifikan? |
|---|---|---|
| Self | 0.0688 | Tidak |
| Peer | 0.0441 | Ya |

**Uji univariat (Mann-Whitney U)**:
- f3 Kedalaman Elaborasi: **signifikan** pada Self maupun Peer; effect size f ≈ 0.49 (moderate)
- f1, f2, f4: belum menunjukkan perbedaan signifikan

**Pola revisi mahasiswa setelah menerima scaffolding**:
- Insertion mendominasi: 61,6% (self), 69,5% (peer)
- No Change sangat rendah → scaffolding memicu aksi
- 4/56 mahasiswa menggunakan kalimat bantuan tanpa menambahkan substansi

**Persistensi pemenuhan indikator**:
- f1 Cakupan Rubrik: 93,4% / 95,5% (self/peer) paling sering bertahan tanpa terselesaikan; resolusi terendah (5,1%)
- f3 Kedalaman Elaborasi: paling konsisten bertahan setelah diperbaiki

### Temuan Kuesioner (Kelompok Treatment)
- **TAM**: Respons positif — subjek merasakan manfaat scaffolding
- **Cognitive Load Theory**: Rata-rata menengah ke atas — subjek merasakan beban kognitif berlebih; ada "kebingungan" terhadap scaffolding
- **Fitur yang dianggap membantu**: Sentence Starter lebih banyak dipilih
- **Keluhan**: split attention effect (fokus terpecah saat ada perubahan teks scaffolding), auto-scroll yang merusak fokus

---

## 6. Kesimpulan & Saran

### Kesimpulan
1. Pipeline digital scaffolding **layak diimplementasikan** untuk mendeteksi kualitas narasi feedback secara real-time.
2. Efektivitas intervensi **tidak seragam** pada seluruh indikator.
3. Digital scaffolding **paling efektif** mendorong pengembangan elaborasi narasi (f3); indikator yang memerlukan inferensi evaluatif (f1, f2, f4) masih menjadi tantangan.

### Saran
- Peningkatan kemampuan inferensi pada indikator koherensi dan relevansi topik
- Pengembangan strategi scaffolding yang lebih adaptif dan metakognitif
- Evaluasi pada sampel dan konteks pembelajaran yang lebih luas
- Optimalisasi antarmuka untuk menurunkan cognitive load pengguna

---

## 7. Catatan untuk Fase 4 (Komentar Dosen)

Saat menganalisis transcript komentar dosen, perhatikan apakah ada pertanyaan/catatan dosen tentang:
- **Validitas desain eksperimen** (randomized posttest-only, ukuran sampel 56 mahasiswa = kecil)
- **Keterbatasan pipeline** (False Positive/Negative, overfitting kalibrasi threshold)
- **Keterkaitan tujuan penelitian dengan outcome** (apakah tujuan sudah outcome-based atau masih output-based?)
- **Kedalaman analisis** Bab II (literature review — apakah cukup mensintesiskan dan bukan hanya meringkum?)
- **Kelengkapan pembahasan dampak** (BAB VI — apakah sudah ada pernyataan rekognisi dari mitra/pengguna?)
- **Format sitasi** (apakah konsisten menggunakan dkk. atau et al.?)
- **Kesesuaian jumlah BAB** dengan Template 2026

---

*Sumber: `PPT/20260629_Seminar 3.md` (1018 baris) dan `PPT/Seminar 3.md` (743 baris)*
*Diringkas: 2026-07-04 — Fase 2*
