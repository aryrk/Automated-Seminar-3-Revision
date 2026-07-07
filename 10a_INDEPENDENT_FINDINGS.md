# INDEPENDENT FINDINGS (Fase 1)

Berdasarkan investigasi mandiri terhadap draft laporan asli (`20260407_High FIdelity_[REVISI] Laporan Tugas Akhir.md`) dan transcript raw (`Sesi Saran.txt` dan `Manual transcribe.md`), berikut adalah temuan-temuan terkait revisi yang harus dilakukan:

## 1. Porsi Development yang Mengaburkan Riset (Pemindahan ke Lampiran)
- **Komentar Penguji**: Penguji (Pak Yudi & Pak Jonner) merasa laporan terlalu berat di sisi *development* (pembuatan Aplikasi Pendukung Eksperimen / APE) daripada risetnya sendiri. Laporan terlihat seperti laporan pembuatan aplikasi.
- **Temuan di Draft Asli**: Di Bab IV, terdapat subbab panjang mengenai pengembangan APE, mulai dari "Analisis Sistem Berjalan" (IV.4.1), "Perancangan dan Integrasi Komponen" seperti BPMN, Use Case, ERD, Sequence Diagram (IV.4.2), hingga antarmuka/GUI yang sangat detail.
- **Tindakan yang Seharusnya (Expected Fix)**: Bagian-bagian *software development* yang sangat teknis (Analisis Sistem Berjalan, requirement detail, perancangan ERD/Diagram) harus **dipindahkan ke Lampiran**. Bab IV harus difokuskan pada *model scaffolding*-nya dan pengujian indikator, bukan cara membuat aplikasinya.

## 2. Kesalahan Penempatan Teori vs Metode (Bab 2 dipindah ke Bab 3/4)
- **Komentar Penguji**: Ada banyak teknologi atau model (seperti *vector embedding*, SBERT, arsitektur NLP) yang hanya *dipakai/dimanfaatkan* namun dibahas terlalu dalam layaknya bahan kajian utama di Bab 2.
- **Temuan di Draft Asli**: Bab II (Tinjauan Pustaka) memuat sangat detail tentang Arsitektur Transformer, *Multi-Label Classification*, *Vector Embedding*, hingga rumus *Cosine Similarity* (Bab II.1.6 - II.1.7). 
- **Tindakan yang Seharusnya (Expected Fix)**: Karena mahasiswa tidak mengkaji/mengubah model *embedding* tersebut (hanya "memakai"), penjelasan teori mendalam tentang *embedding* ini harus **dihilangkan dari Bab 2 atau dipindahkan ke Bab 3 (Metodologi)** secara ringkas saja. Cukup sebutkan bahwa "untuk kebutuhan X, digunakan model Y" tanpa perlu membahas *state-of-the-art* arsitekturnya secara teoretis.

## 3. Klaim Berlebihan pada Metodologi (Seolah-olah Membuat Sendiri)
- **Komentar Penguji**: Ada frasa-frasa seperti "Pembuatan Rubrik" yang memberi kesan mahasiswa merancang rubrik dari nol, padahal rubriknya sudah ada (milik dosen) dan hanya dimodifikasi.
- **Temuan di Draft Asli**: Di Bab III (Metodologi), ada subbab (misal III.6.5) atau bagian yang menjelaskan pembuatan/dekomposisi rubrik yang terkesan dibuat dari nol.
- **Tindakan yang Seharusnya (Expected Fix)**: Kalimat harus diubah dari "membuat rubrik" menjadi "menyiapkan rubrik" atau "mengadopsi rubrik". Pipeline eksperimen terkait rubrik atau teori yang sudah *given* harus dirujuk sebagai sesuatu yang dimanfaatkan/dimodifikasi, dan referensi dasarnya bisa dimasukkan di Bab 2 atau lampiran.

## 4. Kejelasan Pengujian Eksperimen vs Software Testing
- **Komentar Penguji**: Terjadi kerancuan antara pengujian aplikasi (software testing) dengan pengujian eksperimen riset. Eksperimen harus menguji performa model *scaffolding* dalam mendeteksi 4 indikator tekstual.
- **Tindakan yang Seharusnya (Expected Fix)**: Bab IV dan V harus memperjelas skenario eksperimen yang dirancang untuk menguji deteksi 4 indikator tekstual. Penggunaan data buatan (dummy) menggunakan AI diperbolehkan untuk mensimulasikan semua kombinasi *edge-cases* (misal: nilai tinggi tapi narasi singkat, dsb). Laporan harus "berbunyi" secara riset bahwa skenario pengujiannya mampu menjawab Research Question (RQ).

## 5. Kesimpulan dan Analisis Dampak (Bab 6 & 7) Tidak Menjawab RQ
- **Komentar Penguji**: Di bagian Kesimpulan atau Analisis Dampak, laporan malah menyimpulkan fungsionalitas APE (misal: "aplikasi berhasil berjalan"), padahal seharusnya menyimpulkan hasil penelitian sesuai tujuan (menjawab RQ 1 dan RQ 2).
- **Temuan di Draft Asli**: Bab VI berisi "Hasil Evaluasi Kinerja dan Kegunaan Aplikasi" (VI.2.1 Pengujian Fungsionalitas).
- **Tindakan yang Seharusnya (Expected Fix)**: Bab 6 atau Kesimpulan harus difokuskan pada sejauh mana *scaffolding* (intervensi) berpengaruh terhadap kualitas narasi (feedback), bukan membahas *usability* atau fungsionalitas APE.

---
*End of Independent Investigation (Phase 1).*
