# 10_REVISION_INSTRUCTIONS — Instruksi Revisi Atomik untuk AI

> **Tujuan dokumen ini**: Menjadi panduan eksekusi revisi yang **sangat spesifik** bagi AI asisten. Setiap instruksi bersifat atomik (satu tindakan konkret), disertai lokasi eksak di `REVISI_DOKUMEN.md`, dan menyebutkan isi yang diharapkan.  
>
> **File kerja**:  
> - **Sumber referensi**: `Dokumen TA/20260407_High FIdelity_[REVISI] Laporan Tugas Akhir.md`  
> - **File revisi**: `Dokumen TA/REVISI_DOKUMEN.md` ← **HANYA FILE INI YANG DIEDIT**  
> - **File lampiran**: `Dokumen TA/REVISI_DOKUMEN_LAMPIRAN.md` ← konten dipindah ke sini  
>
> **Prinsip utama**:  
> 1. Jangan menulis ulang kalimat yang tidak perlu diubah — hanya edit yang ditunjuk.  
> 2. Semua konten yang "dipindah ke Lampiran" harus dimasukkan ke `REVISI_DOKUMEN_LAMPIRAN.md` dan diganti dengan kalimat penunjuk (`→ Lihat Lampiran X`).  
> 3. Tandai setiap instruksi selesai dengan `[x]` agar bisa dilacak.

---

## GRUP A — BAB I: PENDAHULUAN

### A1 — Revisi Tujuan Penelitian (I.4) [`KRITIS`]
**Lokasi**: Cari kalimat yang mengandung `"Merancang pipeline digital scaffolding yang mengintegrasikan Natural Language Processing"` di Bab I.  
**Masalah**: Tujuan 1 menggunakan kata "Merancang" yang berkonotasi development, bukan riset.  
**Aksi**: Ubah redaksi Tujuan 1 dari:
> *"Merancang pipeline digital scaffolding yang mengintegrasikan Natural Language Processing (NLP) dengan rule-based..."*

Menjadi:
> *"Membangun dan mengevaluasi efikasi pipeline digital scaffolding yang mengintegrasikan Natural Language Processing (NLP) dengan rule-based..."*

---

### A2 — Pertegas Scope Kajian di I.7 (Batasan Penelitian) [`KRITIS`]
**Lokasi**: Tabel I.1 (Batasan Penelitian), bagian `Batasan Sistem`.  
**Masalah**: Tidak ada pernyataan eksplisit bahwa model embedding digunakan sebagai *black box tool*, bukan objek riset.  
**Aksi**: Tambahkan poin baru ke dalam Tabel I.1, kolom Batasan Sistem:
> *"Model sentence embedding yang digunakan (multilingual-e5-large-instruct) diperlakukan sebagai black box tool dalam penelitian ini. Kajian tidak mencakup arsitektur internal, mekanisme pelatihan, maupun fine-tuning model embedding. Model digunakan semata-mata melalui outputnya (representasi vektor) sebagai komponen dalam pipeline scaffolding."*

---

### A3 — Perhalus RQ 1 dan RQ 2 (I.3) [`TINGGI`]
**Lokasi**: Subbab I.3, kalimat pembuka RQ 1 dan RQ 2.  
**Masalah**: RQ 1 terkesan mendeskripsikan sistem, bukan outcome; RQ 2 belum menyebut ekspektasi jawaban (signifikan/tidak).  
**Aksi RQ 1**: Tambahkan anak kalimat di akhir RQ 1 yang menyebutkan ekspektasi evaluasi performa:
> *"...melalui kombinasi model semantik dan aturan heuristik berbasis rubrik, serta bagaimana pola kegagalan deteksi terdistribusi antar indikator?"*

**Aksi RQ 2**: Pastikan RQ 2 menyebutkan kelompok kontrol-treatment secara eksplisit dan menyinggung arah ukur yang diharapkan:
> *"...ditinjau dari perbedaan tingkat pemenuhan empat indikator tekstual antara kelompok treatment dan kontrol, serta pola interaksi mahasiswa dengan scaffolding — dan apakah perbedaan tersebut signifikan secara statistik?"*

---

## GRUP B — BAB II: TINJAUAN PUSTAKA

### B1 — Pangkas Teori Arsitektur SBERT (II.1.7) [`TINGGI`]
**Lokasi**: Cari judul subbab `"II.1.7 Natural Language Processing (NLP) dan Arsitektur Transformer"` dan isinya.  
**Masalah**: Teori arsitektur internal SBERT/Transformer terlalu mendalam untuk model yang hanya dipakai sebagai black box.  
**Aksi**:
1. Hapus atau **pindahkan ke Lampiran** penjelasan arsitektur internal SBERT (layer, attention head, token, dst) yang bersifat *how it works internally*.
2. **Pertahankan** hanya bagian yang menjelaskan: (a) apa itu sentence embedding, (b) apa itu cosine similarity, (c) mengapa pendekatan ini dipilih untuk mendeteksi kemiripan semantik narasi-rubrik.
3. Di tempat yang dipangkas, tambahkan: `*Penjelasan teknis arsitektur model disajikan pada Lampiran [X] untuk kepentingan transparansi metodologis.*`

---

### B2 — Pindahkan Subbab Desain Eksperimen ke Bab III [`TINGGI`]
**Lokasi**: Cari subbab `"II.1.14 Desain Eksperimen dan Evaluasi Statistik"`.  
**Masalah**: Desain eksperimen adalah bagian metodologi, bukan tinjauan pustaka.  
**Aksi**:
1. Salin seluruh isi `II.1.14` ke dalam `REVISI_DOKUMEN_LAMPIRAN.md` dengan label `## Pindahan dari BAB II ke BAB III`.
2. Di `REVISI_DOKUMEN.md`, hapus isi subbab `II.1.14` dan ganti dengan paragraf transisi singkat:
   > *"Kerangka desain eksperimen yang digunakan dalam penelitian ini, yaitu posttest-only control group design, dijelaskan secara rinci pada BAB III subbab III.6.6 sebagai bagian dari prosedur metodologi."*
3. Di BAB III, pastikan subbab III.6.6 (Perancangan Skenario Eksperimen) memuat konten dari II.1.14 yang dipindah, atau cek apakah sudah ada dan tinggal ditambahkan rujukan.

---

### B3 — Tambahkan Kalimat Kaitan Teori-Penelitian di Setiap Subbab Teori Utama [`SEDANG`]
**Lokasi**: Setiap akhir subbab teori besar di BAB II (PjBL, Feedback Literacy, Scaffolding, Digital Scaffolding).  
**Masalah**: SP01 menyebutkan Bab II harus ada bagian yang "ngomong-ngomong pasal kita" (mengaitkan teori ke penelitian).  
**Aksi**: Untuk setiap subbab teori utama, **periksa** apakah sudah ada paragraf penutup yang mengaitkan teori ke penelitian. Jika belum ada atau hanya 1 kalimat, tambahkan 2-3 kalimat yang menjelaskan: *"Dalam penelitian ini, [teori X] digunakan untuk [tujuan Y] karena [alasan Z]."* Tidak perlu panjang, cukup eksplisit.

---

## GRUP C — BAB III: METODOLOGI

### C1 — Tambahkan Peta Alur RQ-ke-Tahapan di Awal Bab III [`TINGGI`]
**Lokasi**: Setelah paragraf pembuka Bab III, sebelum III.1.  
**Masalah**: Pembaca (dan dosen) sulit melihat bagaimana metodologi menjawab RQ. SP01 menuntut ini sangat jelas.  
**Aksi**: Tambahkan **satu paragraf pengantar** dan **satu tabel ringkasan** yang memetakan tahapan metodologi ke RQ:

| Tahapan | Tujuan | Menjawab |
|---|---|---|
| Pemodelan Pipeline (III.6.3) | Membangun mekanisme deteksi 4 indikator tekstual | RQ 1 |
| Kalibrasi Model / Grid Search (III.6.3) | Menentukan threshold optimal untuk setiap indikator | RQ 1 |
| Perancangan Eksperimen (III.6.6) | Menyiapkan kondisi pengujian treatment vs kontrol | RQ 2 |
| Pengolahan Data Statistik (III.6.7) | Mengukur perbedaan signifikan antar kelompok | RQ 2 |

---

### C2 — Pertegas Posisi Kalibrasi dan Grid Search [`TINGGI`]
**Lokasi**: Subbab III.6.3 (Pemodelan Konfigurasi Pipeline), bagian yang membahas grid search / threshold.  
**Masalah**: SP01 dan SP03 mempertanyakan apa itu "kalibrasi" dan bagaimana prosesnya memvalidasi eksperimen.  
**Aksi**: Pastikan ada sub-paragraf yang secara eksplisit menjelaskan:
1. **Apa** itu kalibrasi dalam konteks penelitian ini: mencari nilai threshold optimal untuk mengubah cosine similarity score menjadi keputusan biner (PASS/FAIL).
2. **Bagaimana** proses grid search dilakukan: iterasi dari 0,00 hingga 1,00 dengan interval 0,01, dipilih threshold dengan F1-Score tertinggi.
3. **Mengapa** ini penting untuk validitas: threshold yang salah bisa menyebabkan over-trigger atau under-trigger scaffolding, yang merusak validitas intervensi di eksperimen.

Jika ketiga poin ini sudah ada di HF, cukup **periksa kalimatnya** dan pastikan bahasanya tidak terlalu teknis (accessible bagi dosen penguji non-ML).

---

### C3 — Pindahkan Detail Struktur Tabel/ERD ke Lampiran [`SEDANG`]
**Lokasi**: Subbab III.3 (Data Penelitian) — tabel yang mendefinisikan struktur data teknis (kolom database, tipe data, dsb).  
**Masalah**: Tabel struktur database (ERD-level) tidak relevan untuk metodologi riset.  
**Aksi**:
1. Pindahkan tabel struktur teknis ke `REVISI_DOKUMEN_LAMPIRAN.md`.
2. Ganti di `REVISI_DOKUMEN.md` dengan kalimat singkat: *"Struktur teknis data yang digunakan disajikan pada Lampiran [X]."*
3. **Pertahankan** di BAB III hanya: jenis data (rubrik/historis/primer), sumber pengumpulan, dan ukuran dataset.

---

## GRUP D — BAB IV: HASIL PENGEMBANGAN APE

### D1 — Persingkat Bagian Analisis Sistem Berjalan (IV.1) [`BERAT`]
**Lokasi**: Subbab IV.4.1 (Hasil Analisis Sistem Berjalan) — BPMN, alur proses existing.  
**Masalah**: SP01 secara langsung mengatakan "gambaran besar saja" untuk bagian APE.  
**Aksi**:
1. **Pertahankan** hanya: (a) diagram BPMN ringkasan *to-be* (pasca-integrasi), (b) 1 paragraf menjelaskan mengapa APE perlu diintegrasikan ke sistem existing.
2. **Pindahkan ke Lampiran**: seluruh BPMN *as-is*, narasi panjang analisis proses existing.
3. Ganti bagian yang dipindah dengan: *"Detail analisis sistem berjalan dan proses integrasi APE disajikan pada Lampiran [X]."*

---

### D2 — Persingkat Bagian Use Case dan Sequence Diagram (IV.4.2) [`BERAT`]
**Lokasi**: Subbab IV.4.2 (Hasil Perancangan dan Integrasi Komponen) — Use Case Diagram, Class Diagram, ERD, Sequence Diagram.  
**Masalah**: Bagian ini terlalu panjang dan menyerupai laporan rekayasa perangkat lunak.  
**Aksi**:
1. **Pertahankan** di BAB IV: (a) arsitektur sistem overview (Gambar IV.35 — Arsitektur Aplikasi setelah Integrasi), (b) tabel titik integrasi (IV.37), (c) 1-2 komponen kunci yang paling relevan dengan pipeline scaffolding (misalnya UC-17 Receive Scaffolding).
2. **Pindahkan ke Lampiran**: Class Diagram, ERD, semua Sequence Diagram kecuali UC-17, semua tabel GUI.
3. Ganti bagian yang dipindah dengan: *"Dokumentasi perancangan teknis lengkap (Class Diagram, ERD, Sequence Diagram) disajikan pada Lampiran [X]."*

---

### D3 — Pertegas Narasi Pengujian APE (IV.4.3) — Kaitkan dengan Test Cases [`TINGGI`]
**Lokasi**: Subbab IV.4.3 (Pengujian Aplikasi), baris sekitar `"42 test case"`.  
**Masalah**: Dosen SP01 dan SP03 mempertanyakan pengujian APE — apakah ada skenario per indikator? Ternyata **sudah ada** di Test Cases file, tapi mungkin tidak cukup terekspos di teks.  
**Aksi**:
1. Pastikan paragraf IV.4.3 menyebutkan secara **eksplisit** bahwa test case diorganisasi per indikator (F1-Cakupan Rubrik: TC14-17, F2-Koherensi: TC18-22, F3-Elaborasi: TC23-26, F4-Relevansi: TC27-30, ditambah test case interface dan dekomposisi rubrik).
2. Tambahkan **satu tabel ringkasan** pengujian per indikator:

| Kelompok Test Case | Modul | Jumlah TC | Hasil |
|---|---|---|---|
| TC01-13 | Antarmuka & Interface | 13 | 13 PASS |
| TC14-17 | F1: Cakupan Rubrik | 4 | 4 PASS |
| TC18-22 | F2: Koherensi Skor-Narasi | 5 | 4 PASS, 1 FAIL* |
| TC23-26 | F3: Kedalaman Elaborasi | 4 | 4 PASS |
| TC27-30 | F4: Relevansi Topik | 4 | 4 PASS |
| TC31-42 | Scaffolding & Dekomposisi | 12 | 12 PASS |
| **Total** | | **42** | **41 PASS, 1 FAIL** |

*TC18 FAIL: sistem mendeteksi inkoherensi tapi gagal mengekstrak skor prediksi secara presisi saat narasi bersentimen sangat negatif.

3. Setelah tabel, tambahkan kalimat: *"Detail eksekusi dan bukti hasil pengujian setiap test case disajikan pada Lampiran [X]."*
4. Pindahkan tabel test case lengkap (42 baris) ke `REVISI_DOKUMEN_LAMPIRAN.md`.

---

### D4 — Audit dan Pindahkan Grafik Distribusi Skor yang Salah Tempat [`BERAT`]
**Lokasi**: Subbab IV.2 (Hasil Anotasi Dataset) — grafik distribusi skor, histogram jumlah kata.  
**Masalah**: SP01 mempertanyakan kenapa ada grafik "distribusi skor" di Bab IV. Ini berpotensi merupakan **hasil eksperimen** yang seharusnya ada di Bab V.  
**Aksi**:
1. **Periksa setiap grafik** di Bab IV. Tanyakan: apakah grafik ini adalah hasil analisis data historis pra-eksperimen (boleh di BAB IV sebagai justifikasi sistem), atau hasil eksperimen treatment vs kontrol (harus di BAB V)?
2. Grafik **distribusi dataset anotasi** (True/False, jumlah kata, overlap indikator) → **pertahankan** di BAB IV (justifikasi pipeline).
3. Grafik **perbandingan kelompok treatment-kontrol** → **pindahkan** ke BAB V jika ada yang terselip di BAB IV.
4. Pastikan setiap grafik di BAB IV memiliki kalimat pengantar yang menyatakan tujuannya (misalnya: *"Grafik berikut disajikan sebagai karakteristik data historis yang memotivasi desain pipeline."*)

---

## GRUP E — BAB V: HASIL DAN PEMBAHASAN

### E1 — Tambahkan Elaborasi "Layak Diimplementasikan" [`SEDANG`]
**Lokasi**: Subbab V.3 (Pembahasan) atau bagian penutup Bab V.  
**Masalah**: SP01 menyatakan klaim "layak diimplementasikan" harus dielaborasi dari hasil eksperimen.  
**Aksi**: Cari kalimat yang mengandung "layak" atau "layak diimplementasikan". Tambahkan setelahnya 2-3 kalimat yang menjelaskan: *"Kelayakan ini disimpulkan berdasarkan [sebutkan hasil konkret: F1 tertinggi, signifikansi MANOVA, effect size] yang menunjukkan bahwa..."*

---

## GRUP F — BAB VI: ANALISIS DAMPAK

### F1 — Hapus Konten Fungsionalitas APE dari BAB VI [`KRITIS`]
**Lokasi**: Subbab VI.2 (Hasil Evaluasi Kinerja dan Kegunaan Aplikasi Setelah Implementasi Hasil Penelitian) dan semua sub-subbabnya (VI.2.1 Pengujian Fungsionalitas, VI.2.2 Pengujian Usabilitas).  
**Masalah**: SP01 sangat menolak ini. Konten fungsionalitas APE tidak relevan untuk bab "Analisis Dampak Hasil Penelitian".  
**Aksi**:
1. **Pindahkan** seluruh isi VI.2.1 (Pengujian Fungsionalitas) ke Lampiran (ini sudah duplikat dari IV.4.3, cukup rujuk saja).
2. **Pindahkan** isi VI.2.2 (Pengujian Usabilitas) ke Lampiran jika berisi hanya data TAM/SUS teknis.
3. **Pertahankan** hanya: hasil kuesioner TAM yang membahas **penerimaan mahasiswa terhadap scaffolding** (bukan terhadap aplikasinya) — ini relevan sebagai bukti dampak riset.

---

### F2 — Tulis Ulang Konten BAB VI menjadi "Dampak Riset" [`KRITIS`]
**Lokasi**: Seluruh Bab VI setelah VI.1.  
**Masalah**: Bab VI seharusnya membahas dampak *hasil penelitian* bagi JTK/mitra, bukan evaluasi aplikasinya.  
**Aksi — Struktur baru BAB VI**:
```
VI.1 Outcome yang Diharapkan dari Pengguna/Mitra (sudah ada)
VI.2 Implikasi Hasil Penelitian bagi Mitra (BARU)
    VI.2.1 Implikasi terhadap Praktik Self dan Peer Assessment di JTK
    VI.2.2 Rekognisi Mitra atas Kebermanfaatan Hasil Penelitian (PERLU DATA BARU*)
VI.3 Keterbatasan dan Arah Pengembangan Lanjutan (opsional, jika tidak ada di Bab V)
```

**VI.2.1 — Cara menulis**: Gunakan hasil eksperimen (signifikansi kedalaman elaborasi, pola interaksi scaffolding) dan tafsirkan dampaknya. Contoh: *"Temuan bahwa scaffolding secara signifikan meningkatkan kedalaman elaborasi narasi (effect size 0,49) mengindikasikan bahwa intervensi berbasis rubrik ini berpotensi meningkatkan kualitas data evaluasi peer-assessment di JTK secara sistemik..."*

**VI.2.2 — Membutuhkan data eksternal**: Rekognisi mitra memerlukan data dari dosen pengampu PjBL (lihat `08_ROADMAP_EXTERNAL.md` item No. 2). Jika belum ada, buat placeholder: *"[PLACEHOLDER: Rekognisi mitra akan diisi setelah wawancara dengan dosen pengampu]"*

---

## GRUP G — BAB VII: PENUTUP

### G1 — Perhalus Diksi Kesimpulan RQ 1 [`TINGGI`]
**Lokasi**: VII.1 Kesimpulan, paragraf RQ 1. Cari kalimat `"pipeline digital scaffolding yang dirancang mampu mendeteksi keempat indikator"`.  
**Masalah**: Kata "mampu" terlalu kuat untuk F1=0,43 (Relevansi Topik).  
**Aksi**: Ubah kalimat tersebut menjadi:
> *"Terkait RQ 1, pipeline digital scaffolding yang dirancang menunjukkan tingkat kapabilitas yang bervariasi dalam mendeteksi keempat indikator tekstual..."*

---

### G2 — Perhalus Klaim Kontribusi Kedua [`TINGGI`]
**Lokasi**: VII.1 Kesimpulan, bagian "tiga kontribusi utama", kalimat kontribusi kedua yang mengandung `"dapat digunakan sebagai dasar komputasional"`.  
**Masalah**: 3 dari 4 indikator tidak signifikan secara statistik, sehingga klaim "dapat digunakan" terlalu kuat.  
**Aksi**: Ubah kontribusi kedua menjadi:
> *"Kedua, mengeksplorasi kelayakan empat indikator tekstual sebagai dasar komputasional untuk mendeteksi kebutuhan scaffolding, sekaligus mengidentifikasi batas performa dan tantangan inferensi pada indikator yang lebih kompleks."*

---

### G3 — Tulis Rencana Keberlanjutan (VII.3) [`TINGGI`]
**Lokasi**: Subbab VII.3 (Rencana Keberlanjutan dan Komersialisasi Hasil Penelitian) — saat ini kosong atau sangat minim.  
**Masalah**: Mahasiswa mengakui sendiri ini belum ditulis.  
**Aksi**: Tulis minimal 3-4 poin rencana keberlanjutan, misalnya:
1. Pengembangan model NLP lebih lanjut (fine-tuning berbahasa Indonesia untuk meningkatkan F1 Relevansi Topik).
2. Replikasi eksperimen di skala lebih besar (bukan hanya pilot study) untuk mendapatkan statistical power yang cukup.
3. Integrasi scaffolding ke mata kuliah PjBL lain di JTK sebagai sistem berjalan.
4. Kolaborasi dengan mitra industri/pendidikan untuk adopsi sistem SAPA secara lebih luas.

---

## GRUP H — ABSTRAK & KATA PENGANTAR

### H1 — Tulis Ulang Abstrak [`SEDANG`]
**Lokasi**: Halaman i — Abstrak Bahasa Indonesia dan Bahasa Inggris.  
**Masalah**: Saat ini masih berupa placeholder `[Keywords]` dan isinya kosong/belum selesai.  
**Aksi**: Tulis abstrak dengan struktur berikut (max ~250 kata per bahasa):
1. **Konteks/Problem**: Narasi self dan peer assessment di PjBL cenderung superfisial karena lemahnya evaluative expression.
2. **Tujuan**: Membangun dan mengevaluasi efikasi pipeline digital scaffolding berbasis rubrik.
3. **Metode**: Pipeline NLP + rule-based, eksperimen posttest-only control group, N=XX subjek.
4. **Hasil**: F1-Score tertinggi XX (indikator X), signifikansi MANOVA peer assessment (p=0.04), kedalaman elaborasi signifikan (effect size ~0,49).
5. **Kesimpulan**: Scaffolding menunjukkan dampak paling kuat pada elaborasi, dengan limitasi pada indikator kompleks.
6. **Kata Kunci**: Digital Scaffolding, Feedback Literacy, NLP, Self dan Peer Assessment, PjBL.

---

## CHECKLIST LAMPIRAN

Berikut adalah semua konten yang perlu dipindah ke `REVISI_DOKUMEN_LAMPIRAN.md`. Beri label dan nomor lampiran yang konsisten:

| No Lampiran | Asal | Isi |
|---|---|---|
| Lampiran 1 | BAB II subbab II.1.7 (arsitektur SBERT) | Penjelasan teknis arsitektur model embedding |
| Lampiran 2 | BAB II subbab II.1.14 | Desain eksperimen (konten detail) |
| Lampiran 3 | BAB III subbab III.3 | Tabel struktur data teknis (ERD-level) |
| Lampiran 4 | BAB IV subbab IV.4.1 | BPMN as-is dan narasi analisis sistem berjalan |
| Lampiran 5 | BAB IV subbab IV.4.2 | Class Diagram, ERD, Sequence Diagram (kecuali UC-17), tabel GUI |
| Lampiran 6 | BAB IV subbab IV.4.3 | Tabel 42 test case lengkap (dari `Test Cases - TC.csv`) |
| Lampiran 7 | BAB VI subbab VI.2.1 | Tabel pengujian fungsionalitas FR/NFR |
| Lampiran 8 | BAB VI subbab VI.2.2 | Data usabilitas (SUS/TAM score mentah) |

---

*Dibuat: 2026-07-06 | Berdasarkan: 05_TRANSCRIPT_CLEANED.md, 06_COMMENT_MAPPING.md, 07_ROADMAP_INTERNAL.md, analisis Test Cases - TC.csv, dan HF TA*
