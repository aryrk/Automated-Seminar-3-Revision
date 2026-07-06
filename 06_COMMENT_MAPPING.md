# 06_COMMENT_MAPPING — Analisis Komentar Dosen

> **Fungsi dalam pipeline**: Mapping ini menghubungkan komentar eksplisit maupun implisit (tanda) di draft laporan (`20260407_[REVISI] Laporan Tugas Akhir.md`) dengan transcript sidang (`05_TRANSCRIPT_CLEANED.md`) dan standar tata tulis. Menjadi dasar pembuatan Roadmap.

---

## 1. CATATAN UMUM (DARI SAMPUL DEPAN/AKHIR)

Ditemukan catatan umum (Commented [AR1]) di halaman awal laporan yang berisi poin-poin berikut:
- **Isi -> Tidak Sumatif**: Mengindikasikan isi laporan kurang analitis/sumatif.
- **4 Indikator? Apa Problemnya?**: Dosen mempertanyakan justifikasi pemilihan 4 indikator.
- **RUBRIC BASED DIGITAL SCAFFOLDING UTILIZATION -> Intervensi**: Menggarisbawahi bahwa fokus utama adalah intervensi scaffolding.
- **Signivikan vs tidak dgnifikan, bagaimana kondisinya? Selaras 18%, contoh yang tidak selaras, contoh yang sangat selaras**: Dosen meminta analisis kualitatif dari hasil eksperimen.
- **<25 kata -> tidak detail (teori?)**: Komentar terkait standar penulisan (mungkin untuk abstrak atau elaborasi).
- **Sistem Berjalan -> 4 indikator / Rubrik Eksperimen**: Mempertanyakan metodologi (sistem berjalan vs eksperimen).

---

## 2. PEMETAAN KOMENTAR SPESIFIK KE TEMA TRANSCRIPT

Berikut adalah tabel pemetaan komentar spesifik dosen di draf terhadap tema yang dibahas saat sidang:

| ID | Lokasi (Bab/Bagian) | Teks Draf / Konteks | Komentar Dosen | Hipotesis Makna & Bukti Transcript | Pattern / Kategori |
|---|---|---|---|---|---|
| **AR9** | BAB I - Latar Belakang | "Sistem belum memiliki kapabilitas real-time untuk memproses teks saat diketik." | `? Problem` | Dosen mempertanyakan apakah kapabilitas real-time adalah akar masalah. Sesuai transcript, masalah intinya adalah evaluative expression mahasiswa, bukan sistem real-time-nya. | P1: Problem Statement |
| **AR10** | BAB I - Latar Belakang | "...selama sesi penulisan berlangsung." | `Develop?` | Dosen menangkap kesan "development" (membuat sistem) alih-alih riset. Ini bukti kuat **Tema 1 (Terlalu development-heavy)**. Latar belakang harus berujung pada research gap, bukan sekadar bikin aplikasi. | P2: Riset vs Dev |
| **AR11** | BAB I - RQ 1 | "RQ 1: Sejauh mana pipeline digital scaffolding mampu mendeteksi..." | `Jawaban apa yang diharapkan - Bu Ani` | RQ kurang outcome-focused. Sesuai **Tema 3 & 4**, dosen (SP01) meminta RQ dijawab dengan jelas melalui eksperimen, bukan deskripsi sistem. | P3: RQ & Tujuan |
| **AR12** | BAB I - RQ 1 | "...keempat indikator tekstual narasi feedback..." | `Ada latar belakang apa keempat indikator ini? - Bu Ani` | Dosen mempertanyakan dasar teori 4 indikator ini. Di transcript, SP01 menanyakan hal yang sama (darimana asalnya, mengapa 4 ini yang diuji). Harus diperkuat justifikasinya. | P1: Problem Statement |
| **AR13** | BAB I - RQ 2 | "RQ 2: Sejauh mana intervensi digital scaffolding..." | `Jawaban apa yang diharapkan? - Bu Ani` | Sama seperti AR11. RQ 2 tentang intervensi harus jelas dijawab dengan statistik (signifikansi), sesuai permintaan di halaman depan (signifikan vs tidak). | P3: RQ & Tujuan |
| **AR14** | BAB I - Tujuan | "Tujuan utama dari penelitian ini..." | `Apa yang dilihat dalam konteks penelitian dan RQ-nya - Bu Ani` | Tujuan penelitian belum sejalan dengan RQ secara eksplisit, dan berfokus pada "Merancang pipeline". Bukti **Tema 3 (Tujuan harus outcome-focused)**. | P3: RQ & Tujuan |
| **AR23, AR26** | BAB II - Tinjauan Pustaka | (Berbagai subbab teori teknis seperti Rule Based, Desain Eksperimen) | `Method`, `Method?` | Dosen menegaskan bahwa teori operasional (seperti desain eksperimen, rule-based spesifik) seharusnya masuk ke Bab III (Metodologi). Sesuai **Tema 12 (Pencampuran bab)** dari SP01. | P4: Struktur Bab |
| **AR35, AR36** | BAB III - Metodologi | "Struktur Data Peer/Self Assessment" | `Rancangan?` | Penjelasan struktur data tabel rinci dianggap sebagai bagian dari tahap "Perancangan/Desain (Bab IV)", bukan metodelogi riset tingkat tinggi. | P4: Struktur Bab |
| **AR39, AR42, AR43, AR44** | BAB IV - Hasil Pengembangan APE | "Analisis Sistem Berjalan", "Distribusi Skor", "Hasil Akhir Dekomposisi" | `?`, `Hasil?` | Dosen bingung membaca Bab IV. Kenapa "Analisis Sistem Berjalan" ada di hasil APE? Kenapa "Distribusi skor" masuk ke sini (bukannya hasil eksperimen)? Bukti kuat **Tema 1 (Laporan terlalu berat & salah fokus)**. | P4: Struktur Bab & P2: Riset vs Dev |
| **AR49** | BAB VI - Analisis Dampak | Judul Bab VI | `(kertas dilipat tanpa keterangan)` | Kertas dilipat menandakan ada masalah besar/frustrasi. Sesuai transcript **Tema 5**, SP01 sangat tidak setuju Bab VI berisi dampak fungsional. | P5: Dampak Riset |
| **AR50** | BAB VI - Analisis Dampak | "...hasil pengujian menunjukkan bahwa fitur-fitur..." | `(Kertas dilipat tanpa keterangan)` | Ini adalah kalimat tentang pengujian fungsionalitas (NFR/FR). Sesuai ucapan SP01: "Masak ngobrol fungsionalnya, penelitian fungsional terhadap APE itu kan sampah". Harus dibongkar total. | P5: Dampak Riset |

---

## 3. PEMETAAN KOMENTAR IMPLISIT (DILINGKARI / DIGARISBAWAHI)

Banyak komentar hanya berupa tanda. Berdasarkan konteks kalimat dan transcript, berikut maknanya:

- **Tanda pada teknis APE (AR2, AR3, AR4, AR6, AR7, AR8)**: Di Bab I dan abstrak, istilah-istilah teknis seperti "mekanisme deterministik", "pipeline", dilingkari/digarisbawahi. Makna: Bahasa yang digunakan terlalu teknis-software-engineering, menghilangkan nuansa riset ilmiah.
- **Tanda pada model / algoritma (AR20)**: "arsitektur SBERT" dilingkari. Sesuai **Tema 2 dan 8**, model embedding sebaiknya diperlakukan sebagai *black-box tool*, tidak perlu dieksploitasi arsitektur dalamnya (kecuali kalau meneliti arsitekturnya).
- **Tanda pada pengujian / hasil (AR47, AR48)**: "NFR-01", "Kuesioner Evaluasi". Dosen melipat kertas pada bagian ini, menandakan penolakan terhadap cara pelaporan pengujian software-engineering konvensional di dalam TA riset (Sesuai **Tema 1**).

---

## 4. DAFTAR PATTERN KESALAHAN (GLOBAL)

Berdasarkan analisis di atas, kesalahan dapat dikelompokkan ke dalam 5 Pattern utama yang harus diperbaiki:

| Pattern ID | Nama Kategori | Penjelasan & Aturan yang Dilanggar | Solusi Global |
|---|---|---|---|
| **P1** | Problem Statement Kurang Kualitatif | Fokus permasalahan jatuh pada "sistem tidak bisa real-time" (dev problem) bukan pada gap literasi feedback. | Tulis ulang latar belakang berfokus pada masalah evaluative expression mahasiswa. |
| **P2** | Riset vs Development | Bab I, III, dan IV dipenuhi narasi pembuatan aplikasi (software engineering). Melanggar kaidah TA tipe Riset. | Kurangi porsi "pembuatan aplikasi". Ubah bahasa dari "merancang aplikasi" menjadi "mengembangkan instrumen eksperimen". |
| **P3** | RQ & Tujuan Kurang Outcome-Focused | RQ dan Tujuan berfokus pada proses ("sejauh mana bisa mendeteksi"), dosen meminta fokus pada *outcome* ("apa hasil evaluasinya"). | Rombak redaksi RQ dan Tujuan di Bab I agar berfokus pada hasil/dampak (evaluasi efikasi sistem). |
| **P4** | Struktur Bab (Misplaced Content) | Teori (Bab II) tercampur metode (Bab III). Metode tercampur hasil rancangan (Bab IV). Hasil eksperimen (Bab V) tercampur dengan hasil dev (Bab IV). | Pindahkan konten sesuai panduan tata tulis Polban yang ketat. Teori = Konsep. Metode = Cara kerja riset. |
| **P5** | Bab VI (Analisis Dampak) Salah Isi | Bab VI membahas fungsionalitas APE (usabilitas, testing), padahal seharusnya membahas dampak *hasil riset* bagi JTK. | Hapus bagian fungsionalitas APE dari Bab VI. Tulis ulang Bab VI berfokus pada manfaat scaffolding bagi JTK/mitra (sesuai janji mahasiswa di transcript). |

---

*Dibuat pada: 2026-07-04*
*Referensi: Draft TA (20260407_[REVISI] Laporan Tugas Akhir.md) & 05_TRANSCRIPT_CLEANED.md*
