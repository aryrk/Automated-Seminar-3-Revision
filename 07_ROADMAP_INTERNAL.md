# 07_ROADMAP_INTERNAL — Panduan Revisi Draft TA

> **Fungsi dalam pipeline**: Roadmap ini berisi langkah-langkah konkret perbaikan dokumen draf TA (`20260407_[REVISI] Laporan Tugas Akhir.md`), disusun secara berurutan dari BAB I sampai BAB VI. Setiap item mengacu pada Pattern-ID dari `06_COMMENT_MAPPING.md` dan masukan dari evaluasi AI eksternal.

---

## HOUSEKEEPING & FORMATTING

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 0 | Seluruh Dokumen | **Evaluasi AI** | Masih terdapat sisa residu MS Word Comment (misal: `Commented [AR1]`, `Commented [AR42]`, dll). | Hapus semua teks sisa komentar MS Word dari dalam file `.md` agar dokumen bersih dan terlihat profesional. | Sangat Tinggi | Ringan |

## BAB I - PENDAHULUAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 1 | `I.1 Latar Belakang` (Baris ~791) | **P1, AR9, AR10** | Membahas ketiadaan sistem real-time sebagai inti permasalahan (terkesan development software). | Ubah fokus masalah pada kesenjangan evaluative expression (kemampuan memberi feedback), sedangkan sistem real-time hanya sebagai sarana intervensi eksperimen. | Tinggi | Sedang |
| 2 | `I.3 Research Question` (Baris ~804) | **P3, AR11, AR12, AR13** | RQ 1 dan RQ 2 terfokus pada "proses deteksi/sistem", dan tidak dijustifikasi (kenapa 4 indikator?). | Tulis ulang RQ agar berfokus pada **outcome** eksperimen (bagaimana dampak scaffolding terhadap pemenuhan indikator). Tambahkan 1-2 kalimat justifikasi 4 indikator di latar belakang. | Tinggi | Ringan |
| 3 | `I.4 Tujuan Penelitian` (Baris ~817) | **P3, AR14** | Tujuan 1 adalah "Merancang pipeline". Ini melanggar kaidah TA Riset. | Ubah redaksi "Merancang pipeline" menjadi "Membangun dan mengevaluasi efikasi digital scaffolding...". Pastikan tujuan linier dengan RQ baru. | Tinggi | Ringan |

## BAB II - TINJAUAN PUSTAKA

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 4 | `II.1.7.3 Arsitektur Transformer` dsk. | **P2, AR20** | Pembahasan arsitektur dalam model SBERT terlalu mendalam padahal model hanya dipakai sebagai black box. | Ringkas bagian teori NLP/SBERT. Cukup sebutkan fungsionalitas dan justifikasi pemilihannya. (*Sudah dipindah ke Lampiran 1*) | Tinggi | Selesai |
| 5 | `II.1.14 Desain Eksperimen...` | **P4, AR23, AR26** | Membahas metode desain eksperimen di dalam Tinjauan Pustaka. | Pindahkan bahasan desain eksperimen murni (rule-based spesifik, metode eksperimen) ke **BAB III Metodologi**. (*Sebagian sudah dipindah*) | Tinggi | Selesai |

## BAB III - METODOLOGI PENELITIAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 6 | `III.1 Penjelasan Penelitian` dsk. | **P4, S5 (Transcript)** | Kurang tegas bagaimana tahapan-tahapan yang ada digunakan untuk menjawab RQ. | Tambahkan peta alur atau kalimat eksplisit di awal Bab III yang menghubungkan tiap subbab dengan cara menjawab RQ. | Tinggi | Sedang |
| 7 | `III.3 Data Penelitian` | **P4, AR35, AR36** | Menyajikan struktur tabel/database aplikasi di dalam metodologi riset. | Pindahkan hal yang sangat detail (struktur tabel/ERD) ke **Lampiran** atau rangkum saja konsepnya. (*Sudah dipindah ke Lampiran 2*) | Tinggi | Selesai |

## BAB IV - HASIL PENGEMBANGAN -> KONSTRUKSI & VALIDASI INSTRUMEN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 8 | `Judul Utama BAB IV` | **Evaluasi AI** | Judul bab masih: "HASIL PENGEMBANGAN: APLIKASI PENDUKUNG EKSPERIMEN". Kosakata "Pengembangan" sangat ditentang penguji riset. | Ubah judul BAB IV menjadi: **"KONSTRUKSI DAN VALIDASI INSTRUMEN PENELITIAN"**. | Sangat Tinggi | Ringan |
| 9 | `IV.3.2`, `IV.3.5`, `IV.3.6` | **Evaluasi AI** | Judul subbab mengandung kosakata Rekayasa Perangkat Lunak (Desain, Implementasi, Realisasi). | Ubah nama subbab: "Desain Pipeline" -> "Spesifikasi Final Pipeline". "Implementasi Rule Based" -> "Konfigurasi Logika Scaffolding". "Realisasi Teks" -> "Konstruksi Teks Scaffolding". | Sangat Tinggi | Ringan |
| 10 | `IV.3.4` (Kalibrasi) vs `V.2.1` (Evaluasi Deteksi) | **Evaluasi AI** | Ada potensi duplikasi pelaporan F1-Score di Bab IV dan Bab V yang akan membingungkan penguji ("Mana yang jawaban RQ1?"). | Konsolidasi: Pastikan Bab IV (IV.3.4) fokus pada "Tuning Threshold" (persiapan alat), dan Bab V (V.2.1) fokus pada pelaporan metrik formal sebagai jawaban RQ1. Jika datanya sama, jelaskan peruntukannya. | Tinggi | Sedang |
| 11 | `IV.4 Hasil Implementasi APE` | **P2, Evaluasi AI** | Masih dominan rekayasa perangkat lunak. Subbab menyebut spesifik "Use Case, Class Diagram, ERD". | Jangan sebutkan nama-nama diagram di judul/narasi secara eksplisit. Cukup tulis: "Rancangan teknis disajikan pada Lampiran 3". (*Sudah dipindahkan, sisa perbaikan narasi*) | Tinggi | Sedang |

## BAB V - HASIL DAN PEMBAHASAN EKSPERIMEN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 12 | `V.2 Hasil Eksperimen` dsk. | **S5, S10 (Transcript)** | Perlu dipastikan kesimpulan "layak diimplementasikan" didukung kuat oleh hasil di bagian ini. | Pastikan ada subbab/paragraf yang secara eksplisit membahas kelayakan berdasarkan hasil eksperimen. | Sedang | Ringan |
| 13 | `V.4 Hasil Perbaikan Aplikasi` | **Evaluasi AI** | Kisah perbaikan iterasi UI nangkring di tengah laporan hasil eksperimen (Bab V), merusak alur narasi hasil eksperimen. | **Pindahkan V.4** (Hasil perbaikan aplikasi) ke **Bab VI** (Kinerja Aplikasi) atau ke Lampiran. Sisakan satu kalimat ringkas di Keterbatasan (V.5). | Sangat Tinggi | Ringan |

## BAB VI - ANALISIS DAMPAK HASIL PENELITIAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 14 | `VI.2 Hasil Evaluasi Kinerja dan Kegunaan APE` | **P5, AR49, S3, Evaluasi AI** | Berisi pengujian fungsionalitas software (FR/NFR) dan usabilitas aplikasi secara operasional. Dosen menolak ini. | Pangkas detail QA/Usabilitas menjadi 1 paragraf simpulan (justifikasi instrumen reliabel). Pindahkan rincian pengujian ke lampiran. Ubah fokus Bab VI menjadi Dampak Hasil Penelitian bagi Mitra. | Sangat Tinggi | Berat |
| 15 | (Subbab baru) | **T9 (Transcript)** | Belum ada rekognisi mitra. | Tambahkan bagian wawancara/pernyataan/analisis dari kacamata mitra (Dosen JTK) mengenai efektivitas scaffolding yang diteliti. | Tinggi | Sedang |

## BAB VII - PENUTUP

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 16 | `VII.3 Rencana Keberlanjutan...` | **T9 (Transcript)** | Mahasiswa mengakui rencana keberlanjutan belum ditulis. | Tulis rencana keberlanjutan (komersialisasi atau riset masa depan) sesuai form/template Polban. | Tinggi | Sedang |
| 17 | `VII.1 Kesimpulan` | **Sesi Evaluasi AI** | Ada potensi *overclaim* pada penggunaan kata "mampu mendeteksi" (padahal F1=0.43) dan klaim kontribusi. | Perhalus diksi agar lebih objektif. Contoh: ganti "mampu" dengan "menunjukkan tingkat kapabilitas yang bervariasi". | Tinggi | Ringan |

---
*Diperbarui pada: 2026-07-06 (Pasca Evaluasi AI Eksternal)*
*Tahap berikutnya: Mulai revisi draf mengikuti roadmap terpadu ini (Fokus Bab IV level-struktur & Bab V-VI).*
