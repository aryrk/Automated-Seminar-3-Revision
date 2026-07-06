# 07_ROADMAP_INTERNAL — Panduan Revisi Draft TA

> **Fungsi dalam pipeline**: Roadmap ini berisi langkah-langkah konkret perbaikan dokumen draf TA (`20260407_[REVISI] Laporan Tugas Akhir.md`), disusun secara berurutan dari BAB I sampai BAB VI. Setiap item mengacu pada Pattern-ID dari `06_COMMENT_MAPPING.md`.

---

## BAB I - PENDAHULUAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 1 | `I.1 Latar Belakang` (Baris ~791) | **P1, AR9, AR10** | Membahas ketiadaan sistem real-time sebagai inti permasalahan (terkesan development software). | Ubah fokus masalah pada kesenjangan evaluative expression (kemampuan memberi feedback), sedangkan sistem real-time hanya sebagai sarana intervensi eksperimen. | Tinggi | Sedang |
| 2 | `I.3 Research Question` (Baris ~804) | **P3, AR11, AR12, AR13** | RQ 1 dan RQ 2 terfokus pada "proses deteksi/sistem", dan tidak dijustifikasi (kenapa 4 indikator?). | Tulis ulang RQ agar berfokus pada **outcome** eksperimen (bagaimana dampak scaffolding terhadap pemenuhan indikator). Tambahkan 1-2 kalimat justifikasi 4 indikator di latar belakang. | Tinggi | Ringan |
| 3 | `I.4 Tujuan Penelitian` (Baris ~817) | **P3, AR14** | Tujuan 1 adalah "Merancang pipeline". Ini melanggar kaidah TA Riset. | Ubah redaksi "Merancang pipeline" menjadi "Membangun dan mengevaluasi efikasi digital scaffolding...". Pastikan tujuan linier dengan RQ baru. | Tinggi | Ringan |

## BAB II - TINJAUAN PUSTAKA

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 4 | `II.1.7.3 Arsitektur Transformer` dsk. (Baris ~1321) | **P2, AR20** | Pembahasan arsitektur dalam model SBERT terlalu mendalam padahal model hanya dipakai sebagai black box. | Ringkas bagian teori NLP/SBERT. Cukup sebutkan fungsionalitas dan justifikasi pemilihannya. | Tinggi | Sedang |
| 5 | `II.1.14 Desain Eksperimen...` (Baris ~1984) | **P4, AR23, AR26** | Membahas metode desain eksperimen di dalam Tinjauan Pustaka. | Pindahkan bahasan desain eksperimen murni (rule-based spesifik, metode eksperimen) ke **BAB III Metodologi**. | Tinggi | Sedang |

## BAB III - METODOLOGI PENELITIAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 6 | `III.1 Penjelasan Penelitian` dsk. | **P4, S5 (Transcript)** | Kurang tegas bagaimana tahapan-tahapan yang ada digunakan untuk menjawab RQ. | Tambahkan peta alur atau kalimat eksplisit di awal Bab III yang menghubungkan tiap subbab dengan cara menjawab RQ. | Tinggi | Sedang |
| 7 | `III.3 Data Penelitian` (Baris ~2640) | **P4, AR35, AR36** | Menyajikan struktur tabel/database aplikasi di dalam metodologi riset. | Pindahkan hal yang sangat detail (struktur tabel/ERD) ke **Lampiran** atau rangkum saja konsepnya. | Tinggi | Ringan |

## BAB IV - HASIL PENGEMBANGAN APE

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 8 | `IV.4 Hasil Implementasi APE` (Baris ~3501) | **P2, AR39, AR40** | Pembahasan analisis sistem berjalan, use case, dan BPMN sangat dominan layaknya TA pengembangan sistem informasi. | Sesuai saran dosen SP01: berikan **gambaran besar saja**. Persingkat bagian Use Case dan BPMN, fokuskan Bab IV pada model eksperimen. | Tinggi | Berat |
| 9 | (Keseluruhan Bab IV) | **P2, P4, AR42, AR43** | Terdapat grafik "Distribusi Skor" dan evaluasi parsial di Bab IV yang membuat dosen bingung. | Audit seluruh grafik: jika grafik tersebut adalah **hasil eksperimen (jawaban RQ)**, pindahkan ke Bab V. Jika hanya hasil *pre-processing*, tegaskan di teksnya. | Tinggi | Berat |

## BAB V - HASIL DAN PEMBAHASAN EKSPERIMEN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 10 | `V.2 Hasil Eksperimen` dsk. | **S5, S10 (Transcript)** | Perlu dipastikan kesimpulan "layak diimplementasikan" didukung kuat oleh hasil di bagian ini. | Pastikan ada subbab/paragraf yang secara eksplisit membahas kelayakan berdasarkan hasil eksperimen. | Sedang | Ringan |

## BAB VI - ANALISIS DAMPAK HASIL PENELITIAN

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 11 | `VI.2 Hasil Evaluasi Kinerja dan Kegunaan APE` (Baris ~10101) | **P5, AR49, AR50, S3** | Berisi pengujian fungsionalitas software (FR/NFR) dan usabilitas aplikasi. Dosen sangat menolak ini. | **Hapus/Pindahkan** hasil pengujian NFR/FR ke lampiran. Tulis ulang Bab VI menjadi: Sejauh mana hasil eksperimen bermanfaat bagi mitra (JTK), bukan usabilitas softwarenya. | Sangat Tinggi | Berat |
| 12 | (Subbab baru) | **T9 (Transcript)** | Belum ada rekognisi mitra. | Tambahkan bagian wawancara/pernyataan/analisis dari kacamata mitra (Dosen JTK) mengenai efektivitas scaffolding yang diteliti. | Tinggi | Sedang |

## BAB VII - PENUTUP

| No | Lokasi Spesifik | Referensi | Apa yang Salah | Apa yang Diharapkan (Arah Perbaikan) | Confidence | Estimasi Effort |
|---|---|---|---|---|---|---|
| 13 | `VII.3 Rencana Keberlanjutan...` | **T9 (Transcript)** | Mahasiswa mengakui rencana keberlanjutan belum ditulis. | Tulis rencana keberlanjutan (komersialisasi atau riset masa depan) sesuai form/template Polban. | Tinggi | Sedang |
| 14 | `VII.1 Kesimpulan` | **Sesi Evaluasi AI** | Ada potensi *overclaim* pada penggunaan kata "mampu mendeteksi" (padahal F1=0.43) dan klaim kontribusi bahwa keempat indikator "dapat digunakan sebagai dasar" (padahal 3 indikator tidak signifikan). | Perhalus diksi agar lebih objektif dan tahan peluru dari penguji. Contoh: ganti "mampu" dengan "menunjukkan tingkat kapabilitas yang bervariasi", dan ubah kontribusi menjadi "mengeksplorasi kelayakan". | Tinggi | Ringan |

---
*Dibuat pada: 2026-07-04*
*Tahap berikutnya: Mulai revisi draf mengikuti roadmap ini.*
