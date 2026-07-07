**PEMANFAATAN** *DIGITAL SCAFFOLDING* **BERBASIS RUBRIK UNTUK MENDUKUNG INDIKATOR TEKSTUAL** *FEEDBACK LITERACY* **PADA** *PROJECT-BASED LEARNING*

RUBRIC BASED DIGITAL SCAFFOLDING UTILIZATION FOR SUPPORTING TEXTUAL INDICATOR OF FEEDBACK LITERACY IN PROJECT-BASED LEARNING

**LAPORAN TUGAS AKHIR**

Laporan ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

**Oleh:**

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

PROGRAM SARJANA TERAPAN PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG

**PEMANFAATAN** *DIGITAL SCAFFOLDING* **BERBASIS RUBRIK UNTUK MENDUKUNG INDIKATOR TEKSTUAL** *FEEDBACK LITERACY* **PADA** *PROJECT-BASED LEARNING*

*RUBRIC BASED DIGITAL SCAFFOLDING UTILIZATION FOR SUPPORTING TEXTUAL INDICATOR OF FEEDBACK LITERACY IN PROJECT-BASED LEARNING*

Tipe TA: Riset (Experiment tools)

Oleh:

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

Menyetujui,

Bandung, xx xxxx xx

Pembimbing I, Pembimbing II,

Irwan Setiawan, S.Si., M.T. 198004192005011002 Jonner Hutahaean, BSET., M.Info.Sys. 196210211993031002

Ketua Jurusan Teknik Komputer dan Informatika Koordinator Program Sarjana Terapan Program Studi Teknik Informatika,

Yadhi Aditya Permana, S.T., M.Kom. NIP. 197912242008121001 Santi Sundari, S.Si., M.T. NIP. 197109031999032001

**PEMANFAATAN** *DIGITAL SCAFFOLDING* **BERBASIS RUBRIK UNTUK MENDUKUNG INDIKATOR TEKSTUAL** *FEEDBACK LITERACY* **PADA** *PROJECT-BASED LEARNING*

*RUBRIC BASED DIGITAL SCAFFOLDING UTILIZATION FOR SUPPORTING TEXTUAL INDICATOR OF FEEDBACK LITERACY IN PROJECT-BASED LEARNING*

Tipe TA: Riset (Experiment tools)

Oleh:

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

Tugas Akhir ini telah disidangkan pada tanggal xx xxxxxxxx 20xx sesuai dengan ketentuan.

Tim Penguji: Ketua : Dr. Ani Rahmani, S.Si., M.T. <sup>196810141993032002</sup> ……………….. Anggota : Yudi Widhiyasana, S.Si., M.T. <sup>197407182001121002</sup> ……………….. PERNYATAAN PENULIS

Dengan ini menyatakan bahwa laporan Tugas Akhir dengan judul

"PEMANFAATAN DIGITAL SCAFFOLDING BERBASIS RUBRIK

UNTUK MENDUKUNG INDIKATOR TEKSTUAL FEEDBACK

LITRRACY PADA PROJECT-BASED LEARNING" adalah karya ilmiah yang

bebas dari unsur tindakan plagiarisme, dan sesuai dengan ketentuan tata tulis yang

berlaku.

Apabila dikemudian hari ditemukan adanya unsur plagiarisme, maka hasil penilaian

Tugas Akhir ini akan dicabut dan bersedia menerima sanksi sesuai dengan

ketentuan yang berlaku.

Demikian pernyataan ini dibuat dengan sesungguhnya dalam keadaan sadar

sepenuhnya.

Bandung, xx xxxxxxx 20xx

Aryo Rakatama

221524003

Muhammad Rama Nurimani

221524021

**TURNITIN**

**BIODATA PENULIS**

Nama : Aryo Rakatama

NIM : 221524003

Tempat, Tanggal Lahir : Bandung, 18 Mei 2004

SD & Tahun Lulus : SD Negeri Cibuntu 2 Bandung, 2016

SMP & Tahun Lulus : SMP Negeri 3 Bandung, 2019

SMA & Tahun Lulus : SMK Negeri 11 Bandung, 2022

Prestasi yang pernah dicapai : Juara 3 TISIGRAM 2023

Nama : Muhammad Rama Nurimani

NIM : 221524021

Tempat, Tanggal Lahir : Ciamis, 19 November 2003

SD & Tahun Lulus : SD NEGERI 7 CIAMIS, 2016

SMP & Tahun Lulus : SMP NEGERI 1 CIAMIS, 2019

SMA & Tahun Lulus : SMA NEGERI 1 CIAMIS, 2022

Prestasi yang pernah dicapai :

**ABSTRAK**

Kata Kunci: [Keywords]

**ABSTRACT**

Keywords: [Keywords]

**KATA PENGANTAR**

**DAFTAR ISI**

ABSTRAK: i
ABSTRACT: ii
KATA PENGANTAR: iii
DAFTAR ISI: iv
DAFTAR GAMBAR: ix
DAFTAR TABEL: xiii
DAFTAR RUMUS: xvii
DAFTAR ISTILAH: xix
DAFTAR SINGKATAN: xxi
BAB I PENDAHULUAN ... 1
I.1 Latar Belakang ... 1
I.2 Rumusan Masalah ... 4
I.3 Research Question ... 5
I.4 Tujuan Penelitian ... 6
I.5 Pemangku Kepentingan dan Manfaat Hasil Penelitian ... 6
I.6 Dukungan Data ... 7
I.7 Ruang Lingkup dan Batasan ... 8
I.8 Sistematika Penulisan ... 9
BAB II TINJAUAN PUSTAKA ... 12
II.1 Dasar Teori ... 12
II.1.1 Project Based Learning (PjBL) ... 12
II.1.2 Self Assessment ... 14
II.1.3 Peer Assessment ... 15

II.1.4 Feedback 16
II.1.5 Rubrik 17
II.1.6 Paradigma Anotasi Multi-Label Classification 21
II.1.7 Natural Language Processing (NLP) dan Arsitektur Transformer 22
II.1.8 Rule Based 30
II.1.9 Feedback Literacy 32
II.1.10 Zone of Proximal Development 41
II.1.11 Scaffolding 43
II.1.12 Digital Scaffolding 43
II.1.13 Pendekatan Generasi Teks untuk Scaffolding 44
II.1.14 Desain Eksperimen dan Evaluasi Statistik 48
II.2 Karya Ilmiah Sejenis 50
BAB III METODOLOGI PENELITIAN 54
III.1 Penjelasan Penelitian 54
III.1.2 Formulasi Sistem dan Pengukuran 57
III.2 Variabel Penelitian 61
III.3 Data Penelitian 63
III.3.1 Data Pengembangan dan Validasi Pipeline Scaffolding 63
III.3.2 Data Evaluasi Scaffolding 67
III.4 Objek Penelitian 69
III.4.1 Objek Material 69
III.4.2 Objek Fungsional 70
III.5 Perangkat Pendukung 70
III.6 Tahapan Pelaksanaan Penelitian 71

III.6.2 Studi Literatur dan Pendefinisian Objektif Solusi 74
III.6.3 Pemodelan Konfigurasi Pipeline 75
III.6.4 Formulasi Pendekatan Scaffolding 92
III.6.5 Pembuatan APE 93
III.6.6 Perancangan Skenario Eksperimen 95
III.6.7 Penarikan Kesimpulan dan Perumusan Saran 115
BAB IV HASIL PENGEMBANGAN APLIKASI: PENDUKUNG
EKSPERIMEN 117
IV.1 Analisis Problem Domain 117
IV.1.1 Karakteristik Data Narasi Feedback 117
IV.1.2 Hasil Kuantifikasi Masalah 124
IV.1.3 Spesifikasi dan Objektif Solusi 131
IV.2 Hasil Anotasi Dataset 132
IV.2.1 Hasil Dekomposisi Rubrik 133
IV.2.2 Implementasi Panduan Anotasi 135
IV.2.3 Sampel Hasil Anotasi 136
IV.2.4 Validasi Hasil Anotasi 149
IV.3 Hasil Pemodelan dan Pengembangan Sistem Scaffolding 150
IV.3.2 Desain Pipeline Digital Scaffolding 154
IV.3.3 Landasan Formal dan Pemodelan Pipeline 158
IV.3.4 Hasil Evaluasi dan Kalibrasi Model 172
IV.3.5 Implementasi Rule Based System untuk Scaffolding 186
IV.3.6 Realisasi Teks dan Template Scaffolding 192
IV.4 Hasil Implementasi APE 207
IV.4.1 Hasil Analisis Sistem Berjalan 207

IV.4.2 Hasil Perancangan dan Integrasi Konponen 210
IV.4.3 Pengujian Aplikasi 241
IV.5 Hasil Perancangan Skenario Eksperimen 242
IV.5.1 Pemetaan Subjek Eksperimen 242
IV.5.2 Kuesioner yang Digunakan 243
IV.5.3 Rubrik Eksperimen 245
BAB V HASIL DAN PEMBAHASAN EKSPERIMEN 249
V.1 Ringkasan Metodologi Eksperimen 249
V.2 Hasil Eksperimen 250
V.2.1 Hasil Evaluasi Deteksi Pipeline (RQ 1) 251
V.2.2 Statistik Deskriptif dan Verifikasi Asumsi (RQ 2) 255
V.2.3 Hasil Pengujian Multivariat dan Univariat (RQ 2) 257
V.2.4 Hasil Pengolahan Data Interaksi Scaffolding (RQ 2) 258
V.2.5 Hasil Kuesioner Evaluasi Pengguna 264
V.3 Pembahasan Hasil Eksperimen 267
V.3.1 Pembahasan Kemampuan Deteksi Pipeline (Menjawab RQ 1) 268
V.3.2 Dampak Intervensi terhadap Pemenuhan Indikator Tekstual Narasi Feedback (Menjawab RQ 2) 284
V.4 Hasil Perbaikan Aplikasi Pendukung Eksperimen 293
V.5 Keterbatasan Penelitian 297
V.5.1 Keterbatasan Generalisasi Konteks Penelitian 297
V.5.2 Keterbatasan Desain Eksperimen yang Dipilih 298
V.5.3 Keterbatasan Bentuk Digital Scaffolding 299
BAB VI ANALISIS DAMPAK HASIL PENELITIAN 301
VI.1 Outcome yang Diharapkan dari Pengguna/Mitra 301

VI.2 Hasil Evaluasi Kinerja dan Kegunaan Aplikasi Setelah Implement: asi Hasil
Penelitian ... 302
VI.2.1 Pengujian Fungsionalitas ... 302
VI.2.2 Pengujian Usabilitas ... 303
VI.2.3 Rekognisi Mitra atas Kebermanfaatan Hasil Penelitian ... 304
BAB VII PENUTUP ... 305
VII.1 Kesimpulan ... 305
VII.2 Saran ... 307
VII.3 Rencana Keberlanjutan dan Komersialisasi Hasil Penelitian ... 307
DAFTAR PUSTAKA ... 308
I.AMPIRAN ... 320

**DAFTAR GAMBAR**

Gambar II.1 Siklus PjBL dalam Konteks Penelitian 13
Gambar II.2 Alur Self-Assessment 14
Gambar II.3. Alur Peer-Assessment 15
Gambar II.4. Self dan Peer Assessment sebagai Feedback 17
Gambar II.5. Ilustrasi Multi-Label-Classification 21
Gambar II.6. Arsitektur SBERT untuk Regresi Teks 23
Gambar II.7. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder 24
Gambar II.8. Rerpesentasi Ruang Vektor 25
Gambar II.9. Cosine Similarity dalam Ruang Vektor 26
Gambar II.10. Representasi Pipeline Penelitian 28
Gambar II.11. Balancing Preccision dan Recall untuk F1-Score 30
Gambar II.12 Kerangka Operasionalisasi Evaluative Expression 35
Gambar II.13. Contoh Cakupan Rubrik Tidak Terpenuhi 36
Gambar II.14. Contoh Koherensi Evaluatif Tidak Terpenuhi 37
Gambar II.15. Contoh Elaborasi Narasi Feedback 38
Gambar II.16. Contoh Relevansi Tidak Terpenuhi 38
Gambar II.17. Illustrasi Konseptual Dekomposisi Rubrik 40
Gambar II.18 Ilustrasi kerangka ZPD 42
Gambar II.19. Cara Kerja LLM dalam Generasi Teks 45
Gambar II.20. Contoh Penggunaan Few-Shot dan Zero-Shot 46
Gambar II.21. Arsitektur RAG 47
Gambar II.22. Ilustrasi Penggunaan Template untuk Output Teks 48
Gambar II.23. Ilustrasi Eksperimen Post-Test Only 50
Gambar III.1. Korelasi Rubrik, Pertanyaan, dan Feedback 56
Gambar III.2. Pemetaan Feedback kepada Indikator Komputasi 58
Gambar III.3. Alur Komputasi Indikator dan Keputusan Intervensi 59
Gambar III.4. Pemetaan Scaffolding pada Kelompok Eksperimen 68
Gambar III.5. Pemetaan Unit Analisis, Objek Material, dan Vektor Indikator 69
Gambar III.6. Tahapan Pelaksanaan Penelitian 72

Gambar III.7. Peta Sintesis Studi Literatur 74
Gambar III.8. Pemetaan Dataset untuk Evaluasi 76
Gambar III.9. Pemetaan Dekomposisi Rubrik pada Anotasi Dataset 78
Gambar III.10. Pemetaan Rubrik dalam Notasi Dekomposisi 80
Gambar III.11 Alur Dekomposisi dan Pengelompokan Mutual Exclusive 85
Gambar III.12. Alur Anotasi Dataset Cakupan Rubrik 86
Gambar III.13. Alur Anotasi Dataset Relevansi Topik 87
Gambar III.14. Alur Anotasi Dataset Koherensi Skor dan Narasi 88
Gambar III.15. Alur Anotasi Dataset oleh Annotator 89
Gambar III.16. Alur Validasi Dataset 89
Gambar III.17. Pemetaan Eksperimen dan Kalibrasi Model 90
Gambar III.18 Rancangan Eksperimen 96
Gambar III.19. Alur Penentuan dan Pengacakan Subjek Eksperimen 99
Gambar III.20. Flowchart Keputusan Uji Statistik Per Indikator 108
Gambar III.21. Flowchart Tahapan Pengolahan Data Interaksi 111
Gambar IV.1 Perbandingan Rata-Rata Jumlah Kata antar Self dan Peer 126
Gambar IV.2 Sebaran Jumlah Kata antar Peer dan Self Assessment 127
Gambar IV.3 Perbandingan Pola Assessment antar Skor dan Panjang Narasi 128
Gambar IV.4 Pola Periode Pengisian antar Skor dan Panjang Narasi 129
Gambar IV.5 Distribusi Skor Antara Self dan Peer Assessment 130
Gambar IV.6. Distribusi label TRUE dan FALSE pada Dataset 142
Gambar IV.7. Distribusi Tiga Indikator Pada Sampel Anotasi 143
Gambar IV.8. Histogram Jumlah Kata Pada Dataset Anotasi 144
Gambar IV.9 Distribusi Empat Indikator Tekstual Narasi Feedback 145
Gambar IV.10 Hubungan Antar Indikator 146
Gambar IV.11 Pola Overlap Indikator Tidak Terpenuhi 147
Gambar IV.12 Pemenuhan Indikator Cakupan Rubrik berdasarkan Panjang 148
Gambar IV.13 Desain Pipeline yang Dibangun 155
Gambar IV.14. Flowchart Part-of-Speech Tagging 161
Gambar IV.15 Mekanisme Semantic Chunking menggunakan Sentencizer 162
Gambar IV.16. Flowchart Komputasi Indikator Cakupan Rubrik 166

Gambar IV.17. Contoh Komputasi Indikator Koherensi Skor dan Narasi 168
Gambar IV.18. Contoh Komputasi Indikator Relevansi Topik 171
Gambar IV.19. Mekanisme Kalibrasi Model 173
Gambar IV.20. Flowchart Alur Eksekusi Scaffolding 187
Gambar IV.21. Matriks Strategi Scaffolding dan Prompt 196
Gambar IV.22 Ilustrasi Variabel Missing_Coverage 200
Gambar IV.23 Ilustrasi Transformasi Missing Coverage 201
Gambar IV.24 Ilustrasi Pengambilan Variabel Kontekstual untuk Skor 201
Gambar IV.25. Proses Bisnis SAPA 208
Gambar IV.26. BPMN to-be Setelah APE diintegrasikan 212
Gambar IV.27. Use Case Diagram APE yang Akan Dikembangkan 214
Gambar IV.28. Class Diagram Keseluruhan (to-be) 217
Gambar IV.29. Class Diagram Bagian Modifikasi 218
Gambar IV.30. ERD Keseluruhan SAPA 220
Gambar IV.31. ERD Bagian Modifikasi 221
Gambar IV.32. Sequence Diagram UC-05 Manage Assessment 223
Gambar IV.33. Sequence Diagram UC-10 Answer Peer Assessment 224
Gambar IV.34. Sequence Diagram UC-10 Answer Self Assessment 225
Gambar IV.35. Arsitektur Aplikasi setelah Integrasi 237
Gambar V.1. Grafik Indikator Cakupan Rubrik Semantic Chunking 252
Gambar V.2. Grafik Performa Koherensi Skor dengan Semantic Chunking 253
Gambar V.3. Grafik Performa Relevansi Topik dengan Whole-text-embedding 254
Gambar V.4. Frekuensi Kebutuhan Bantuan yang Terdeteksi 259
Gambar V.5. Tingkat Resolusi Keempat Indikator 260
Gambar V.6. Tingkat Persistensi Antar Indikator 260
Gambar V.7. Pola Revisi Perubahan 261
Gambar V.8 Dinamika Pemenuhan Indikator Saat Sesi Eksperimen 262
Gambar V.9 Perbandingan Pemenuhan Indikator Terpenuhi 263
Gambar V.10. Rata-rata Skor Evaluasi Penerimaan (TAM) 265
Gambar V.11. Rata-rata Skor Evaluasi Beban Kognitif 265
Gambar V.12. Komponen Scaffolding yang Dinilai Paling Membantu 266

Gambar V.13. Komponen Scaffolding yang Dinilai Mem9utuhkan Perbaikan . 267
Gambar V.14. Kerangka untuk Menjawab RQ 1 268
Gambar V.15. Distribusi FP dan FN pada Rubrik 269
Gambar V.16. Sebaran FP dan FN berdasarkan Label Anotasi 274
Gambar V.17. Kerangka untuk Menjawab RQ 2 285
Gambar V.18. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup 295
Gambar V.19. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup 296

**DAFTAR TABEL**

Tabel I.1. Batasan Penelitian 8
Tabel II.1. Contoh Instrumen Rubrik PjBL 19
Tabel II.2. Contoh Bentuk Rule-Base pada Sistem 31
Tabel II.3. Tingkatan Dekomposisi Rubrik pada Pipeline 40
Tabel III.1. Notasi Matematis 56
Tabel III.2. Simulasi Alur Data dan Keputusan Intervensi Sistem 59
Tabel III.3. Indikator Tekstual yang Dapat Dikomputasi 61
Tabel III.4. Struktur Data Peer Assessment 65
Tabel III.5. Struktur Data Self Assessment 65
Tabel III.6. Struktur Data Rubrik 66
Tabel III.7. Perangkat Pendukung 70
Tabel III.8 Contoh Proses Dekomposisi Cakupan dan Relevansi Topik 81
Tabel III.9. Contoh Proses Dekomposisi untuk Koherensi Skor dan Narasi 82
Tabel III.10. Contoh Himpunan Koherensi Feature Set 83
Tabel III.11. Contoh Implementasi BARS pada Rubrik CATME 101
Tabel III.12 Format Tabel Pelaporan Verifikasi Asumsi 106
Tabel III.13. Format Pelaporan Uji Manova (Pillai's Trace) 106
Tabel III.14 Tabel Interpretasi Keputusan Uji Asumsi 108
Tabel III.15 Interpretasi Uji Follow Up Per Indikator 110
Tabel III.16 Interpretasi Effect Size 110
Tabel III.17. Format Pelaporan Uji Univariat dan Effect Size 110
Tabel III.18 Karakteristik Perubahan pada Narasi Feedback 112
Tabel III.19. Klasifikasi Pola Revisi 113
Tabel IV.1. Kasus narasi bersifat generik 118
Tabel IV.2. Kasus Cakupan Parsial 119
Tabel IV.3. Kasus Skor Tidak Koheren dengan Narasi yang ditulis 120
Tabel IV.4. Kasus Inkoherensi Skor secara Parsial 121
Tabel IV.5. Kasus Feedback dengan Elaborasi Singkat 122
Tabel IV.6. Kasus Narasi Tidak Relevan dengan Aspek Rubrik Pertanyaan 123

Tabel IV.7. Kasus Narasi Feedback Tidak Relevan Sebagian 123
Tabel IV.8. Detail Data Historis Assessment sebelum Dikomputasi 125
Tabel IV.9 Hasil Akhir Dekomposisi Rubrik untuk Cakupan dan Relevansi 133
Tabel IV.10. Hasil Dekomposisi Rubrik Untuk Koherensi Skor dan Narasi 134
Tabel IV.11. Sampel Data Anotasi Dataset Cakupan Rubrik dan Relevansi 138
Tabel IV.12. Sampel Dataset Koherensi Skor Narasi 1 140
Tabel IV.13. Sampel Dataset Koherensi Skor Narasi 2 141
Tabel IV.14. Pemilihan Pendekatan Komputasional 151
Tabel IV.15. Kandidat Model Sentence Embedding 156
Tabel IV.16. Instruksi Model Untuk Indikator 158
Tabel IV.17. Skenario Evaluasi Part-of-Speech Taging 160
Tabel IV.18. Contoh Perhitungan Indikator Cakupan Rubrik 165
Tabel IV.19. Contoh Komputasi Indikator Elaborasi 169
Tabel IV.20. Performa Model pada Indikator Cakupan Rubrik (1) 174
Tabel IV.21. Performa Model pada Indikator Koherensi Skor dan Narasi 175
Tabel IV.22. Performa Model pada Indikator Relevansi Topik 176
Tabel IV.23. Peningkatan Performa Model dengan Semantic Chunking 177
Tabel IV.24. Performa Cakupan Rubrik dengan Semantic Chunking 178
Tabel IV.25. Performa Sifat Mutual Exclusivity pada 2 179
Tabel IV.26. Performa Akhir Model untuk Setiap Indikator 181
Tabel IV.27 Analisis Implikasi Performa Hasil Evaluasi dan Eksperimen 183
Tabel IV.28. Rule Set untuk Setiap Kombinasi 188
Tabel IV.29. Rincian Logika Aturan 190
Tabel IV.30. Decision Table Intervensi Scaffolding 191
Tabel IV.31 Analisis Pendekatan Generasi Teks Scaffolding 193
Tabel IV.32. Analisis Kebutuhan Teks Scaffolding untuk Setiap Indikator 195
Tabel IV.33 Komponen Teks Scaffolding 198
Tabel IV.34. Variabel Kontekstual yang digunakan Template 199
Tabel IV.35. Himpunan Template Prompt Scaffolding 202
Tabel IV.36 Ilustrasi Adaptivitas Output pada Kondisi  yang Identik 206
Tabel IV.37. Titik Integrasi 209

Tabel IV.38. Komponen Yang Dimodifikasi 209
Tabel IV.39. Komponen Yang Ditambahkan 210
Tabel IV.40. Functional Requirements 213
Tabel IV.41. Non Functional Requirements 213
Tabel IV.42. Use Case Scenario Receive Scaffolding (UC-17) 215
Tabel IV.43. GUI-22 227
Tabel IV.44. GUI-25 228
Tabel IV.45. GUI-21 229
Tabel IV.46. GUI-24 231
Tabel IV.47. GUI-43 233
Tabel IV.48. GUI-46 235
Tabel IV.49. Kuesioner Kelompok Treatment 243
Tabel IV.50. Rubrik CATME yang Dihasilkan 246
Tabel IV.51. Feature-set Eksperimen Cakupan dan Relevansi Topik 247
Tabel IV.52. Feature-set Eksperimen Koherensi Skor dan Narasi 247
Tabel V.1 Rincian Keseluruhan Kemampuan Pipeline 251
Tabel V.2. Sebaran Performa Indikator Cakupan Rubrik 252
Tabel V.3. Sebaran Performa Indikator Koherensi Skor dan Narasi 253
Tabel V.4. Sebaran Nilai FN, FP, TN, TP untuk Indikator Relevansi Topik 254
Tabel V.5. Deskripsi Data Terkumpul dari Eksperimen yang Dilakukan 255
Tabel V.6. Statistik Deskriptif Self Assessment 256
Tabel V.7. Statistik Deskriptif Peer Assessent 256
Tabel V.8. Hasil Uji Asumsi 256
Tabel V.9. Hasil Pengujian Multivariat 257
Tabel V.10. Hasil Pengujian Univariat untuk Self Assessment 258
Tabel V.11. Hasil Pengujian Univariat untuk Peer Assessment 258
Tabel V.12. Jumlah Responden Kuesioner 264
Tabel V.13. Sampel data False Positive 270
Tabel V.14. Sampel Data False Negative 271
Tabel V.15. Sampel Data FP pada Koherensi Skor dan Narasi 274
Tabel V.16. Sampel Data FN pada Koherensi Skor dan Narasi 275

Tabel V.17. Sampel Data FP pada Relevansi Topik 278
Tabel V.18. Sampel Data FN pada Relevansi Topik 279
Tabel V.19. Keluhan Subjek yang menyatakan Distraksi 293

**DAFTAR RUMUS**

Pemetaan Ruang Vektor ... 24
Rumus Cosine Similiarity ... 26
Rumus Pipeline Penelitan ... 27
Formula F1 Score ... 29
Formula Precission ... 29
Formula Recall ... 29
Kondisi Penyelarasan Multi-Dimensi ... 57
Kondisi Deteksi Per Indikator ... 58
Pemicu Intervensi Rule-Based ... 59
Kondisi Terpenuhi untuk setiap Uji Stastistik ... 60
Cochran Formula ... 64
Aspek Rubrik ... 78
Representasi Hubungan Aspek dengan Kriteria ... 78
Representasi Hubungan Kriteria dengan Deskripsi Penilaian Spesifik ... 79
Pemetaan Feature Set Indikator Komputasi ... 81
Feature Set Cakupan dan Relevansi ... 81
Hasil awal Dekomposi ... 82
Himpunan Unit Dekomposisi Feature Set Koherensi Skor dan Narasi ... 83
Himpunan Koherensi Feature Set ... 83
Notasi Constraint Mutual Exclusive ... 84
Elemen Himpunan yang Berkorespondensi dengan Tingkat Skor ... 84
Notasi Constraint Anggota Himpunan ... 84
Tingkat Signifikansi yang Disesuaikan ... 109
Implementation Rate ... 112
Persistence Rate ... 112
Himpunan Kandidat Predikat ... 159
Himpunan Kandidat Subjek ... 160
Valisasi Part-of-Speech Tagging ... 160
Fungsi Segmentasi ... 162

Operator maksimum (Split-Max) 163
Persamaan Cakupan Rubrik 164
Formula Cakupan Rubrik 165
Contoh Perhitungan Indikator Cakupan rubrik 165
Himpunan Kandidat Skor 167
Prediksi Skor Tertinggi Dalam Group 167
Himpunan Prediksi Skor 167
Fungsi Pengukur Koherensi 168
Kondisi Intervensi Kedalaman Elaborasi 169
Himpunan Seluruh Kriteria Penilaian dalam Rubrik 170
Himpunan Unit Dekomposisi Kriteria yang Tidak Menjadi Fokus 170
Nilai Relevansi 170
Notasi Rule based 188
Notasi Scaffolding sebagai Template Instantiation 197

**DAFTAR ISTILAH**

Cohen's d : Varian spesifik dari effect size yang menghitung

selisih rata-rata dua kelompok dibagi oleh standar

deviasi gabungan.

Conditional Prompt : Pesan panduan yang dihasilkan secara otomatis

oleh sistem berdasarkan hasil analisis real-time terhadap input pengguna, bersifat kondisional dan

sugestif.

Cosine Similarity : Metrik yang mengukur kesamaan arah antara dua

vektor dalam ruang berdimensi tinggi, digunakan untuk menentukan kedekatan semantik antara

representasi teks.

Digital Scaffolding : Implementasi scaffolding melalui teknologi digital

yang secara otomatis memberikan panduan adaptif kepada pengguna berdasarkan analisis

komputasional terhadap input mereka.

Effect Size : Ukuran statistik yang mengkuantifikasi besaran

perbedaan antara dua kelompok dalam satuan standar deviasi, independen terhadap ukuran

sampel.

Feedback Literacy : Pemahaman, kapasitas, dan disposisi yang

diperlukan untuk memahami informasi dan menggunakannya untuk meningkatkan pekerjaan

atau pembelajaran.

Large Language Models

(LLM)

: Jenis artificial intelligence yang dapat memahami,

meringkas, menerjemahkan, memprediksi, dan

menghasilkan teks natural.

MANOVA : Teknik statistik untuk menguji perbedaan rata-rata

antara kelompok (variabel independen kategorikal) pada dua atau lebih variabel dependen kontinu secara bersamaan. Ini adalah perluasan dari ANOVA yang menganalisis korelasi antar

variabel dependen

Natural Language

Generation (NLG)

: Cabang dari Kecerdasan Buatan (AI) dan bagian

dari Pemrosesan Bahasa Alami (NLP) yang bertugas mengubah data terstruktur menjadi teks

atau narasi yang mudah dipahami manusia

Natural Language

Processing (NLP)

: Sub-disiplin ilmu komputer dan kecerdasan buatan yang memungkinkan komputer untuk memahami,

memproses, dan menganalisis bahasa alami

manusia.

Natural Language

Understanding (NLU)

: Cabang Kecerdasan Buatan (AI) dan bagian dari pemrosesan bahasa alami (NLP) yang

memungkinkan mesin untuk memahami,

menafsirkan, dan menganalisis konteks, niat (intent), serta sentimen di balik bahasa manusia

Peer Assessment : Bentuk feedback yang dilakukan antar teman

sejawat terhadap kontribusi atau performa anggota

kelompok.

Pillai's trace : Statistik uji yang digunakan dalam MANOVA

untuk mengukur pengaruh variabel independen

terhadap variabel dependen multivariat.

Pipeline : Serangkaian tahapan pemrosesan data yang

terhubung secara sekuensial, di mana output dari satu tahap menjadi input bagi tahap berikutnya.

Project Based Learning

(PjBL)

: Metode pembelajaran yang menggunakan topik/masalah dunia nyata untuk menghubungkan

gap antar teori dengan praktik.

Rubrik : Alat yang digunakan sebagai dasar nilai

menggunakan kriteria yang telah ditentukan.

Rule-Based : Pendekatan komputasi di mana keputusan sistem

ditentukan oleh seperangkat aturan eksplisit yang didefinisikan sebelumnya, bukan oleh

pembelajaran statistik dari data.

Scaffolding : Strategi instruksional yang memberikan dukungan

sementara dan bersyarat kepada peserta didik untuk menyelesaikan tugas yang berada di luar kemampuan mandirinya, dengan tujuan agar dukungan tersebut ditarik secara bertahap seiring

meningkatnya kompetensi.

Self Assessment : Bentuk feedback individu untuk menilai kontribusi

atau performanya sendiri.

Transformer : Arsitektur jaringan saraf tiruan yang menggunakan

mekanisme self-attention untuk memproses data sekuensial secara paralel, menjadi dasar bagi model bahasa modern seperti BERT dan GPT.

Zone of Proximal

Development (ZPD)

: Jarak antara tingkat perkembangan aktual yang ditunjukkan oleh kemampuan pemecahan masalah

secara mandiri dan tingkat perkembangan potensial yang dapat dicapai melalui bimbingan orang dewasa atau kolaborasi dengan rekan yang

lebih kompeten.

Intervensi : Tindakan komputasional sistem berupa pemberian

bantuan atau peringatan tekstual kepada mahasiswa penilai (assessor) yang terdeteksi menghasilkan feedback berkualitas rendah, bertujuan untuk memandu mahasiswa untuk

memperbaiki narasi feedback.

**DAFTAR SINGKATAN**

AI : Artificial Intelligence

BERT : Bidirectional Encoder Representation from

Transformer

E5 : Embeddings from Bidirectional Encoder

Representations.

LLM : Large Language Models

MANOVA : Multivariate Analysis of Variance.  NLP : Natural Language Processing

PjBL : Project Based Learning

SBERT : Sentence-Bidirectional Encoder Representation

from Transformer

ZPD : Zone of Proximal Development

**BAB I**

**PENDAHULUAN**

Bab ini memuat gambaran umum penelitian yang mencakup latar belakang, perumusan masalah, research question, tujuan penelitian, pemangku kepentingan dan manfaat penelitian, dukungan data, ruang lingkup dan batasan, serta sistematika penulisan tugas akhir.

**I.1 Latar Belakang**

Pembelajaran Berbasis Proyek (PjBL) dirancang dengan tujuan yang lebih dalam dari sekadar menghasilkan produk akhir. Pendekatan ini menempatkan proses kolaborasi sebagai inti pembelajaran, di mana mahasiswa membangun tidak hanya kompetensi teknis tetapi juga kapasitas interpersonal seperti kemampuan bekerja dalam tim, mengambil tanggung jawab, dan mengevaluasi kontribusi diri sendiri maupun rekan sejawat (Guo et al., 2020; Krajcik et al., 2006). Namun, proses kolaborasi tersebut tidak selalu dapat diamati secara langsung oleh dosen karena sebagian besar interaksi terjadi di luar sesi pembelajaran formal. Sebaliknya, anggota kelompok yang terlibat dalam proyek memiliki kesempatan yang lebih besar untuk mengamati bagaimana setiap anggota berkontribusi terhadap penyelesaian tugas (Cheng et al., 2008; Dunning et al., 2004).

Salah satu mekanisme yang umum digunakan untuk memperoleh informasi tersebut adalah melalui self assessment dan peer assessment. Dalam konteks PjBL kedua instrumen tersebut berfungsi sebagai penilaian berbasis rubrik yang umumnya terdiri atas dua komponen yaitu komponen skor numerik dan komentar atau narasi kualitatif (Bell, 2010; Winstone & Carless, 2019). Selain menghasilkan nilai, kedua komponen juga memberikan kesempatan bagi pengajar untuk memperoleh gambaran mengenai dinamika kerja kelompok yang tidak selalu tercermin pada produk akhir, seperti bagaimana mahasiswa merefleksikan kinerja diri sendiri, menilai kontribusi rekan, serta menerapkan standar penilaian yang terdapat pada rubrik. (Nicol et al., 2014).

Di antara kedua komponen tersebut, komentar atau narasi kualitatif memiliki peran yang sangat krusial, karena narasi inilah yang secara esensial mentransformasikan sebuah skor angka menjadi feedback yang sesungguhnya (Winstone & Carless, 2019). Tanpa adanya narasi yang mendeskripsikan justifikasi penilaian, sebuah skor numerik hanyalah sebuah vonis yang justru menghentikan tindakan belajar mahasiswa karena tidak memberikan informasi apa pun mengenai langkah perbaikan selanjutnya (Hyland & Hyland, 2001; Mu & Schunn, 2025; Zhang et al., 2024). Oleh karena itu, narasi yang telah berfungsi sebagai feedback ini berperan sebagai sarana refleksi, akuntabilitas, dan dialog pembelajaran antar mahasiswa selama pelaksanaan proyek (Gaynor, 2020; Guo et al., 2020; van Popta et al., 2017).

Fungsi tersebut menjadi berkurang ketika narasi feedback yang ditulis mahasiswa bersifat terlalu umum, terlalu singkat, atau tidak menjelaskan alasan di balik skor yang diberikan (Carless & Boud, 2018). Narasi feedback seperti "pekerjaan dilakukan dengan sangat baik" tidak memberikan informasi yang cukup bagi penerima feedback maupun dosen untuk memahami aspek apa yang sebenarnya dinilai (Aimah & Suhartoyo, 2024; Hattie & Timperley, 2007; Setiawan, 2026a). Akibatnya, kualitas narasi feedback tidak lagi ditentukan hanya oleh skor yang diberikan, tetapi juga oleh bagaimana penilaian tersebut diartikulasikan ke dalam bentuk narasi yang informatif, relevan, dan selaras dengan kriteria penilaian (Brookhart, 2013; Nicol et al., 2014; Winstone & Carless, 2019).

Fenomena tersebut bukan merupakan kasus yang bersifat individual. Penelitian Setiawan (2026a) terhadap 93 mahasiswa Program Studi Teknik Informatika Politeknik Negeri Bandung menunjukkan bahwa hanya 18,4% narasi feedback yang selaras dengan evaluasi numerik yang diberikan. Tingkat keselarasan pada peer assessment bahkan hanya mencapai 13,2%, lebih rendah dibandingkan self assessment sebesar 23,7%.

Temuan tersebut konsisten dengan berbagai penelitian internasional yang menunjukkan empat karakteristik tekstual yang sering muncul pada narasi feedback. Pertama, narasi cenderung terlalu singkat sehingga sulit memuat alasan maupun saran perbaikan yang spesifik (Daou et al., 2020). Kedua, narasi sering membahas aspek yang tidak menjadi fokus rubrik penilaian (Sun et al., 2023). Ketiga, skor numerik dan justifikasi naratif sering muncul sebagai dua komponen yang tidak selaras (Zhang & Schunn, 2023). Keempat, narasi sering kali belum mencakup seluruh aspek yang dipersyaratkan dalam rubrik (Camarata & Slieman, 2020), Karakteristik-karakteristik tersebut menunjukkan bahwa mahasiswa tidak selalu mampu mengartikulasikan keputusan evaluatifnya ke dalam bentuk narasi yang selaras dengan rubrik.

Kesenjangan antara kemampuan melakukan evaluasi dan kemampuan mengartikulasikannya menempatkan penulisan narasi di dalam Zone of Proximal Development (ZPD) yang mendefinisikan rentang tugas yang belum dapat diselesaikan secara mandiri, tetapi dapat dicapai dengan bantuan (Vygotsky et al., 1978). Hal ini didukung oleh Zhang & Schunn (2023) yang mengakui bahwa konstruksi narasi feedback berada di area ini dan perlu diberikan bantuan. Dalam konteks tersebut, bantuan yang paling efektif bersifat contingent, yaitu hanya diberikan ketika dibutuhkan dan dihentikan ketika mahasiswa telah mampu melanjutkan tugasnya secara mandiri (Pea, 2004), Prinsip inilah yang menjadi dasar penerapan digital scaffolding dalam penelitian ini.

Setiawan (2026a) mengidentifikasi potensi sistem berbasis NLP untuk memberikan prompt berbasis rubrik sebagai bentuk scaffolding. Studi terkini yang meneliti mengenai scaffolding memiliki beberapa keterbatasan. Studi yang dilakukan oleh (Ding et al., 2025) menyoroti kemampuan scaffolding dalam konteks pendidikan. Namun, sistem yang dibangun hanya menganalisis makna teks setelah feedback  dituliskan. Selain itu scaffolding berbasis teknologi Generative AI mampu menghasilkan teks bervariasi meski bersifat probabilistik yang tidak memberikan jaminan konsistensi atau transparansi yang diperlukan dalam konteks intervensi pedagogis yang terstruktur (Luan NG et al., 2026). Sementara Mohammad et al. (2025) menerapkan scaffolding dalam bentuk human-in-the-loop berbasis LLM GPT-4 dengan prompt checklist terstruktur dalam konteks penulisan laporan akademik bagi mahasiswa EFL, namun masih menghadapi kelemahan dimana LLM yang berbasis prediksi statistik tersebut berisiko menghasilkan analisis dangkal, plagiarisme, dan halusinasi faktual. Kondisi ini menunjukkan kebutuhan akan mekanisme scaffolding yang deterministik dan beroperasi secara real-time selama proses penulisan berlangsung.

Berdasarkan kesenjangan tersebut, penelitian ini mengusulkan pipeline digital scaffolding berbasis rubrik yang mengintegrasikan Natural Language Processing dan mekanisme deterministik untuk mendeteksi empat indikator tekstual secara real-time selama mahasiswa menulis narasi self assessment dan peer assessment. Ketika satu atau lebih indikator belum terpenuhi, sistem memberikan prompt berbasis rubrik sebagai bentuk scaffolding, kemudian menghentikan bantuan secara otomatis ketika seluruh indikator telah terpenuhi dalam sesi penulisan yang sama. Pipeline yang diusulkan dievaluasi pada dua tahap. Tahap pertama memvalidasi kemampuan deteksi keempat indikator tekstual terhadap anotasi ground truth. Tahap kedua mengevaluasi pengaruh penggunaan digital scaffolding melalui pilot study menggunakan desain randomized posttest-only control group untuk memperoleh estimasi awal mengenai besarnya efek intervensi terhadap tingkat pemenuhan indikator tekstual narasi feedback.

**I.2 Rumusan Masalah**

Penelitian ini dilatarbelakangi oleh tiga kesenjangan dalam pelaksanaan self dan peer assessment berbasis rubrik pada lingkungan PjBL, yaitu gap pedagogis, komputasional, hingga intervensi.

Pertama, pada gap pedagogis, mahasiswa belum selalu mampu mengartikulasikan evaluasi ke dalam narasi feedback yang informatif. Berdasarkan temuan empiris Setiawan (2026a), hanya 18,4% narasi yang selaras dengan skor kuantitatif. Gejala lain yang sering muncul meliputi narasi yang terlalu singkat, cakupan kriteria rubrik yang rendah, dan penyimpangan topik evaluasi.

Kedua, pada gap komputasional, pendekatan sistem berbasis NLP pada penelitian sebelumnya beroperasi secara sumatif, di mana analisis narasi feedback dilakukan setelah proses penulisan selesai (Omotehinwa et al., 2025; Rahimi et al., 2017). Sistem belum memiliki kapabilitas real-time untuk memproses teks saat diketik.

Ketiga, pada gap intervensi, sistem evaluasi yang ada saat ini umumnya berhenti pada tahap analisis atau klasifikasi tekstual narasi feedback, namun belum selalu diikuti dengan mekanisme scaffolding berbasis rubrik. Akibatnya, mahasiswa tidak memperoleh prompt atau panduan terstruktur untuk memperbaiki narasi mereka pada saat proses penulisan sedang berlangsung.

Berdasarkan ketiga kesenjangan tersebut, terdapat kebutuhan terhadap sistem yang mendeteksi gejala tekstual feedback secara real-time, dan secara aktif memberikan intervensi untuk membantu mahasiswa merevisi narasi feedback selama sesi penulisan berlangsung.

**I.3 Research Question**

- RQ 1: Sejauh mana pipeline digital scaffolding mampu mendeteksi keempat indikator tekstual narasi feedback yaitu cakupan rubrik, koherensi skornarasi, kedalaman elaborasi, dan relevansi topik, melalui kombinasi model semantik dan aturan heuristik berbasis rubrik?
- RQ 2: Sejauh mana intervensi digital scaffolding berbasis rubrik memengaruhi pemenuhan keempat indikator tekstual narasi feedback pada mahasiswa dalam lingkungan eksperimen nyata, ditinjau dari perbedaan tingkat pemenuhan empat indikator tekstual antara kelompok treatment dan kontrol serta pola interaksi mahasiswa dengan scaffolding selama proses penyusunan narasi feedback?

**I.4 Tujuan Penelitian**

Sejalan dengan rumusan masalah dan pertanyaan penelitian yang telah ditetapkan, tujuan utama dari penelitian ini dibagi menjadi dua sasaran komputasional dan eksperimental, yaitu:

1. Merancang pipeline digital scaffolding yang mengintegrasikan Natural Language Processing (NLP) dengan rule-based. Arsitektur ini ditujukan untuk mendeteksi keempat indikator tekstual yaitu cakupan rubrik, koherensi skornarasi, kedalaman elaborasi, dan relevansi topik secara real-time selama penulisan aktif narasi self dan peer assessment.
2. Mengukur perbedaan tingkat pemenuhan keempat indikator tekstual melalui pilot study dengan perbandingan kelompok treatment yang menerima scaffolding dan kelompok kontrol tanpa scaffolding untuk menghasilkan estimasi effect size awal.

Kontribusi penelitian ini adalah:

1. Merancang pipeline digital scaffolding berbasis rubrik untuk narasi feedback berbahasa Indonesia.
2. Mengimplementasi empat indikator tekstual narasi feedback.
3. Mengevaluasi performa deteksi indikator dan dampak intervensi melalui pilot study.

**I.5 Pemangku Kepentingan dan Manfaat Hasil Penelitian**

Penelitian ini melibatkan berbagai pihak penting di bidang teknik komputer dan informatika di Politeknik Negeri Bandung, yaitu:

1. Mahasiswa JTK yang mengikuti mata kuliah berbasis PjBL yang memiliki self dan peer assessment sebagai bagian dari proses evaluasi. Studi ini menguji apakah proses penulisan narasi feedback yang dilengkapi bantuan digital scaffolding menghasilkan narasi feedback yang menunjukkan tingkat pemenuhan indikator tekstual yang lebih tinggi, mencakup aspek rubrik yang lebih lengkap, relevansi topik yang lebih baik, serta keselarasan yang lebih tinggi antara skor dan narasi dibandingkan proses penulisan tanpa scaffolding. Kontribusi studi difokuskan pada kualitas output feedback yang dihasilkan selama sesi penulisan dengan dukungan sistem. Evaluasi mengenai perkembangan feedback literacy sebagai kapasitas yang bertahan memerlukan desain longitudinal yang berada di luar cakupan penelitian ini.

2. Dosen pengampu mata kuliah berbasis PjBL yang menggunakan rubrik sebagai komponen evaluasi menerima output self dan peer assessment berupa skor numerik dan narasi kualitatif per kriteria. Dalam konteks ini, sistem menyediakan mekanisme deteksi otomatis terhadap indikator tekstual yang berkaitan dengan cakupan rubrik, relevansi topik, koherensi skor dan narasi, serta kedalaman elaborasi, disertai scaffolding untuk membantu mahasiswa memperbaiki narasi selama proses penulisan berlangsung. Output narasi feedback pada kondisi dengan scaffolding diharapkan memiliki tingkat pemenuhan indikator tekstual yang lebih tinggi sehingga menyediakan informasi evaluatif yang lebih terstruktur dibandingkan output tanpa digital scaffolding.. Reliabilitas dan karakteristik output yang dihasilkan perlu dipahami dalam konteks bahwa narasi feedback tersebut ditulis dengan dukungan digital scaffolding selama proses penilaian berlangsung.

**I.6 Dukungan Data**

Penelitian ini menggunakan tiga kelompok data, yaitu data rubrik merupakan rubrik yang ditulis oleh dosen pengampu PjBL. Data historis serta data primer yang dikumpulkan melalui eksperimen. Data historis telah diperoleh melalui self dan peer assessment pada mata kuliah yang menerapkan PjBL di jurusan teknik komputer dan informatika Politeknik Negeri Bandung dengan total 10.098 data feedback sebagai berikut:

1. Data rubrik self dan peer assessment, mencakup deskripsi aspek feedback serta hubungannya dengan kriteria skor.
2. Data pertanyaan dari self dan peer assessment yang diberikan oleh dosen mengenai pertanyaan yang digunakan dalam feedback.

3. Data hasil penilaian self dan peer assessment, yaitu skor dan teks feedback yang diisi oleh 95 mahasiswa terkait evaluasi anggota kelompok dan diri mereka sendiri dalam mata kuliah PjBL.

Struktur data yang digunakan serta cara pengolahannya dijelaskan secara lebih rinci pada subbab III.3. Bagian ini hanya memberikan gambaran umum mengenai sumber dan jenis data yang digunakan dalam penelitian.

**I.7 Ruang Lingkup dan Batasan**

Untuk menjaga fokus dan arah penelitian, [Tabel I.1](#page-5-0) menyajikan kelompok ruang lingkup dan batasan penelitian ke dalam lima kategori utama.

Tabel I.1. Batasan Penelitian

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**I.8 Sistematika Penulisan**

Sistematika dalam penulisan Tugas Akhir ini dibagi menjadi empat bab dengan penjelasan sebagai berikut:

BAB I Bab ini berisi gambaran umum mengenai penelitian yang dilakukan, termasuk latar belakang penelitian yang menjelaskan permasalahan kualitas narasi feedback pada self dan peer assessment dalam lingkungan Project-Based Learning atau PjBL. Bab ini secara terstruktur menguraikan konteks dan rumusan masalah yang dirumuskan berdasarkan kajian awal, merumuskan research question (RQ) serta tujuan dan manfaat penelitian, serta menjelaskan ruang lingkup, batasan, sumber data, dan sistematika penulisan laporan yang mendukung pengembangan dan evaluasi intervensi digital scaffolding yang diusulkan.

[BAB II](#page-9-0) Bab ini membahas secara rinci kajian literatur yang relevan dengan penelitian, menyajikan kerangka teori yang menjadi dasar dan landasan dalam menjawab research question serta mendukung analisis hasil penelitian ini. Bab ini menetapkan dasar-dasar pedagogis, seperti PjBL, feedback literacy, Zone of Proximal Development (ZPD), serta mekanisme digital scaffolding, sekaligus menjelaskan berbagai teori komputasional dalam Natural Language Processing (NLP). Selain itu, bab ini juga melakukan analisis kritis secara perbandingan terhadap penelitian terdahulu yang memiliki keterkaitan dengan topik yang diteliti guna menunjukkan adanya ketidaksesuaian dalam sistem scaffolding secara real-time.

BAB III Bab ini menjelaskan secara sistematis mengenai metodologi penelitian yang digunakan untuk merancang, mengembangkan, dan mengevaluasi sistem digital scaffolding. Pembahasan dalam bab ini mencakup desain penelitian, metode pengumpulan dan analisis data, variabel penelitian, objek penelitian, serta perangkat dan alat bantu yang digunakan. Selain itu, prosedur penelitian yang mencakup tahapan pengembangan pipeline deteksi indikator tekstual, rancangan digital scaffolding, prosedur eksperimen, serta metode analisis yang digunakan untuk menjawab RQ juga dijelaskan secara rinci.

BAB IV Bab ini membahas analisis kebutuhan eksperimen, desain, serta pembuatan produk aplikasi pendukung eksperimen (APE) dari tahapantahapan pelaksanaan penelitian yang telah direncanakan pada BAB III. Struktur pembahasan dimulai dengan pemaparan hasil analisis masalah pendahuluan yang menjadi justifikasi sistem, dilanjutkan dengan spesifikasi desain, hingga penjelasan rinci mengenai hasil pemodelan Natural Language Processing dan integrasi arsitektur digital scaffolding ke dalam aplikasi SAPA. Pembahasan dalam bab ini mencakup seluruh kegiatan pengembangan perangkat lunak APE sebagai instrumen untuk mendukung tahapan eksperimen, serta aspek teknis yang mendukung validasi hasil penelitian.

BAB V Bab ini menyajikan hasil penelitian berdasarkan analisis data eksperimen dan evaluasi terhadap sistem digital scaffolding yang diusulkan. Evaluasi dilakukan pada dimensi komputasional, outcome, dan proses untuk menilai kemampuan deteksi indikator tekstual, pengaruh intervensi terhadap output feedback yang dihasilkan mahasiswa, serta dinamika interaksi mahasiswa dengan digital scaffolding selama proses penulisan berlangsung. Pembahasan difokuskan pada interpretasi hasil dan perbandingan dengan penelitian sebelumnya untuk menjawab research question. Bagian ini juga membahas evaluasi dampak penggunaan serta tingkat keberterimaan pengguna terhadap hasil penelitian berdasarkan umpan balik yang diperoleh.

BAB VI Bab ini menjelaskan outcome yang diharapkan dari pengguna/mitra. Hal ini ditujukan untuk mengevaluasi minimal sejauh mana keberterimaan pengguna terhadap hasil penelitian ini, sesuai manfaat yang ditetapkan.

BAB VII Bab ini menjelaskan kesimpulan dari keseluruhan hasil penelitian yang telah dilakukan serta menjawab research question yang telah dirumuskan. Kesimpulan disusun berdasarkan hasil analisis dan pembahasan, serta dikaitkan dengan tujuan penelitian. Selanjutnya, disampaikan saran-saran untuk penelitian selanjutnya berdasarkan hasil kesimpulan yang bersifat konstruktif untuk pengembangan lebih lanjut, baik dari aspek teknis, perbaikan metodologi, maupun arah penelitian masa depan serta rencana keberlanjutan yang berpotensi memperluas penerapan sistem yang telah dibangun agar dapat dirasakan manfaatnya dalam jangka panjang.

**BAB II**

**TINJAUAN PUSTAKA**

Bab ini membahas pemahaman dasar mengenai konsep dan teori yang berkaitan dengan topik yang dibahas serta mengidentifikasi karya ilmiah yang relevan sebagai referensi dalam proses penelitian.

**II.1 Dasar Teori**

Dasar teori ini melibatkan konsep-konsep yang mendukung pelaksanaan penelitian. Teori yang dibahas menjadi dasar dalam penyelenggaraan dan penilaian Tugas Akhir.

**II.1.1 Project Based Learning (PjBL)**

Pembelajaran Berbasis Proyek (PjBL) merupakan pendekatan pembelajaran yang secara aktif menggunakan masalah dunia nyata untuk memfasilitasi mahasiswa mengaplikasikan teori ke dalam praktik melalui kerja kelompok kolaboratif (Yew et al., 2016). Karakteristik utama PjBL adalah ketergantungan antar anggota dalam mencapai keberhasilan proyek yang dikerjakan (Yew et al., 2016). Ketergantungan ini menciptakan lingkungan kolektivitisme yang mempengaruhi perilaku sosial dan cara mahasiswa berinteraksi satu sama lain selama proses pengerjaan proyek. Sebagai contoh alur kerja PjBL, [Gambar II.1](#page-10-0) menggambar konteks PjBL pada institusi penelitian, menunjukkan dua fase pengerjaan tugas kelompok dan dua timepoint pelaksanaan self dan peer assessment pada pertengahan dan akhir semester.

Gambar II.1 Siklus PjBL dalam Konteks Penelitian

Dosen pada lingkungan PjBL umumnya terbatas pada produk akhir atau output yang dihasilkan. Sebaliknya, rekan sejawat (peer) terlibat langsung dalam proses harian, pengerjaan dan dinamika internal kelompok, mereka memiliki akses mengenai perilaku serta kontribusi yang tidak teramati oleh dosen (Nicol et al., 2014) . Hal ini menciptakan kondisi dimana Self dan Peer Assessment berperan sebagai instrumen utama mengevaluasi dimensi kolaborasi, tanggung jawab, proses yang mendasari hasil akhir proyek (Cheng et al., 2008; Dornyei & Murphey, 2011; Panadero et al., 2017).

Namun dalam proses evaluasi tersebut, kondisi interdependensi dari PjBL menciptakan risiko sosial yang tinggi. Pada konteks budaya kolektivistik di Indonesia, tuntutan untuk menjaga harmoni sering kali melampaui tuntutan untuk memberikan kritik yang jujur (Brown & Levinson, 1987; Fithriani, 2018; Holmes & Wilson, 2022). Akibatnya, muncul kesenjangan fungsional di mana mahasiswa memiliki kemampuan internal untuk menilai kualitas (evaluative judgement), namun gagal dalam mengomunikasikannya secara tertulis (evaluative expression) demi menghindari friksi interpersonal atau face-threatening acts (Brown & Levinson, 1987; Setiawan, 2026a). Fenomena ini menyebabkan narasi feedback  dalam PjBL cenderung bersifat superfisial dan kehilangan fungsi pedagogisnya. Konsep PjBL digunakan dalam penelitian ini sebagai konteks ekosistem pembelajaran kolaboratif yang menjustifikasi perlunya instrumen evaluasi berupa narasi feedback antar rekan sejawat. Lingkungan interdependen ini memicu masalah kesenjangan artikulasi yang menjadi fokus utama intervensi sistem.

**II.1.2 Self Assessment**

Self assessment atau penilaian diri sendiri merupakan bentuk feedback ketika siswa menjelaskan dan mengevaluasi kualitas proses belajar dan hasil kerja sendiri untuk meningkatkan perbaikan pembelajaran di masa depan (Yan & Carless, 2022) yang digambarkan pada [Gambar II.2](#page-11-0). Penerapan self assessment menunjukkan peningkatan hasil akademik, kemampuan mengatur diri, hingga mendorong kesadaran untuk terus meningkatkan kualitas pembelajaran (Panadero et al., 2017). Secara operasional, proses ini menuntut mahasiswa untuk menginternalisasi kriteria dalam rubrik dan mengomunikasikan hasil penilaian tersebut secara konsisten melalui skor numerik dan narasi kualitatif (Setiawan, 2026a).

Gambar II.2 Alur Self-Assessment

Meskipun memiliki nilai pedagogis yang tinggi, self assessment rentan terhadap bias overestimasi diri (Boud et al., 2013; Dunning et al., 2004), siswa cenderung memberikan skor tinggi namun tidak mampu menyertakan justifikasi naratif yang sesuai dengan kriteria rubrik (Setiawan, 2026a). Dalam konteks ini, bias overestimasi menyebabkan terjadinya distorsi pada evaluative expression, sehingga teks yang dihasilkan hanya berfungsi sebagai pembenaran subjektif yang dangkal alih-alih menjadi sebuah refleksi kritis yang selaras dengan kriteria rubrik. Teori mengenai self assessment diperlukan dalam penelitian ini untuk menjelaskan asal mula teks narasi yang dievaluasi, sekaligus menjustifikasi pentingnya bantuan scaffolding guna memitigasi bias over estimasi yang menyebabkan ketidakselarasan skor-narasi saat mahasiswa menyusun evaluasi mandiri.

**II.1.3 Peer Assessment**

Peer assessment merupakan proses siswa memberikan feedback terhadap kontribusi teman sejawatnya dalam kelompok PjBL yang divisualisasikan pada [Gambar II.3.](#page-12-0) Jika diterapkan dengan tepat, metode ini mendorong kemandirian belajar dan memfasilitasi evaluasi mandiri (Nicol et al., 2014). Efektivitas peerassessment sangat bergantung pada kemampuan mahasiswa mengartikulasikan penilaian evaluatif ke dalam teks narasi yang bermakna (Nicol et al., 2014).

Gambar II.3. Alur Peer-Assessment

Berbeda dengan self assessment yang cenderung dipengaruhi oleh bias overestimasi diri, peer assessment lebih rentan terhadap bias harmoni kelompok, mahasiswa menghindari memberikan kritik demi menjaga hubungan sosial (Setiawan, 2026a). Bias tersebut menghasilkan pola evaluasi di mana skor kuantitatif yang tinggi diberikan sebagai gestur solidaritas, namun disertai dengan narasi yang bersifat normatif, sangat singkat, dan minim evaluasi substantif. Fenomena ini mempertegas kegagalan evaluative expression dalam konteks sosiopragmatis, di mana teks narasi kehilangan fungsi informatifnya akibat tekanan untuk mempertahankan harmoni sosial. Konsep peer assessment digunakan sebagai kerangka masalah untuk menunjukkan bagaimana tekanan harmoni memicu narasi yang tidak substantif. Hal ini mendukung rancangan komponen rule-based untuk mendeteksi narasi dengan cakupan rubrik rendah dan mengarahkan kembali fokus mahasiswa pada kriteria penilaian.

**II.1.4 Feedback**

Feedback secara konseptual adalah informasi yang diberikan oleh pengajar, teman sejawat, atau pengalaman sebagai hasil dari kinerja seseorang untuk mendukung mendorong motivasi, memperbaiki proses belajar, dan mengubah kinerja (Hattie & Timperley, 2007; Nelson & Schunn, 2008). Agar efektif, feedback harus menjawab tiga pertanyaan utama: feed up yaitu capaian mengenai target individu yang menerima feedback, feed back yaitu bagaimana kemajuan saat ini dan feed forward  langkah apa yang harus diambil selanjutnya (Hattie & Timperley, 2007). Ketiga fungsi ini menuntut adanya kejelasan standar dan spesifitas informasi agar kesenjangan antara performa atau kinerja saat ini dan tujuan pembelajaran yang akan dicapai dapat dipersempit.

Dalam konteks assessment berbasis rubrik, efektivitas feedback sering kali terhambat apabila hanya direpresentasikan dalam bentuk skor numerik. Skor numerik memberikan indikasi posisi capaian, namun tidak menyediakan informasi diagnostik yang diperlukan untuk perbaikan (Winstone & Carless, 2019). Oleh karena itu, kehadiran narasi kualitatif merupakan komponen yang menjembatani skor numerik dengan tujuan pedagogis. Narasi kualitatif inilah yang mengubah sebuah angka penilaian menjadi feedback yang sesungguhnya, karena di dalamnya terkandung artikulasi mengenai alasan pemilihan skor, identifikasi kekuatan, serta saran perbaikan yang spesifik.

Dalam penelitian ini, feedback dioperasionalkan sebagai kombinasi antara skor kuantitatif dan narasi kualitatif yang dihasilkan mahasiswa selama proses self dan peer assessment di lingkungan PjBL yang digambarkan pada [Gambar II.4](#page-14-0). Fokus utama penelitian diletakkan pada kualitas narasi kualitatif tersebut, karena teks narasi merupakan manifestasi dari kemampuan mahasiswa dalam mengomunikasikan penilaian evaluatif mereka secara eksplisit dan selaras dengan kriteria rubrik. Dengan demikian, dalam penelitian ini, narasi kualitatif dievaluasi berdasarkan keempat indikator tekstual yaitu cakupan rubrik, koherensi skor-narasi, kedalaman elaborasi, dan relevansi topik, yang merepresentasikan manifestasi terbatas dari evaluative expression yaitu kemampuan untuk mengartikulasikan skor numerik menjadi narasi dapat dideteksi secara komputasional.

Gambar II.4. Self dan Peer Assessment sebagai Feedback

**II.1.5 Rubrik**

Dalam konteks evaluasi kompetensi, rubrik didefinisikan sebagai instrumen penilaian terstruktur yang memuat kriteria spesifik guna menilai kualitas performa

atau hasil kerja peserta didik berdasarkan rangkaian standar pencapaian yang eksplisit (Brookhart, 2013). Pada lingkungan PjBL, rubrik berfungsi sebagai alat standarisasi nilai oleh pengajar serta pemandu kognitif yang membantu mahasiswa memahami standar kualitas secara mandiri (Jonsson & Svingby, 2007). Berdasarkan format rancangannya, rubrik secara umum diklasifikasikan menjadi dua jenis, yaitu rubrik holistik yang mengevaluasi proses atau output secara menyeluruh dan simultan, serta rubrik analitik yang mengurai kriteria penilaian ke dalam dimensi-dimensi performa yang terpisah dan independen satu sama lain (Brookhart, 2013).

Penelitian ini secara khusus mengadopsi pendekatan rubrik analitik. Penggunaan rubrik analitik dinilai memiliki kontribusi pedagogis yang lebih signifikan dalam memfasilitasi aktivitas self dan peer assessment (Jonsson & Svingby, 2007). Karakteristik utama dari rubrik analitik adalah kemampuannya untuk mendistribusikan feedback secara terperinci dalam bentuk formative feedback mengenai kekuatan spesifik dan area kompetensi yang memerlukan improvement lebih lanjut (Panadero et al., 2017). Secara operasional, struktur komponen di dalam rubrik analitik terdiri dari tiga elemen, yaitu kriteria atau dimensi performa yang dinilai, skala penilaian berupa tingkatan skor kuantitatif kontinu, dan deskripsi tingkat capaian tekstual yang merinci karakteristik performa yang spesifik (Jonsson & Svingby, 2007).

[Tabel II.1](#page-1-0) menyajikan contoh instrumen rubrik analitik yang diterapkan dalam PjBL pada Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung untuk mengevaluasi dimensi kolaborasi teknis dan pengolahan data iklan yang dilakukan mahasiswa. Instrumen rubrik tersebut menjadi komponen utama yang digunakan untuk analisis dan proses pengembangan digital scaffolding pada penelitian ini, namun tidak digunakan sebagai rubrik pada eksperimen terhadap mahasiswa kelompok kontrol maupun treatment.

Tabel II.1. Contoh Instrumen Rubrik PjBL

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**II.1.6 Paradigma Anotasi Multi-Label Classification**

Multi-label classification adalah kerangka klasifikasi NLP di mana satu instance teks dapat diberi beberapa label secara simultan, berbeda dari single-label classification yang hanya mengizinkan satu label eksklusif per instance (Tsoumakas & Katakis, 2009). Sebagai contoh, [Gambar II.5](#page-3-0) menyajikan perbedaan paradigma multi-class dan multi-label classification pada studi kasus citra dengan feature matahari, bulan, dan awan. Di mana setiap instance pada multi-label dapat terdiri dari kombinasi beberapa feature. Representasi tersebut selaras dengan konteks NLP pada penelitian ini yang menganalisis feature di dalam teks narasi feedback.

Gambar II.5. Ilustrasi Multi-Label-Classification

Dalam konteks penelitian, skema anotasi mengikuti paradigma Multi Label Classification karena setiap narasi dievaluasi terhadap beberapa aspek rubrik sekaligus, dengan setiap label diberi status biner TRUE/FALSE sehingga satu feedback dapat mencakup beberapa aspek rubrik bersamaan. Pendekatan anotasi ini secara operasional merefleksikan metode Binary Relevance, yaitu setiap aspek rubrik dievaluasi secara independen sebagai tugas binary classification terpisah (Tsoumakas & Katakis, 2009).

**II.1.7 Natural Language Processing (NLP) dan Arsitektur Transformer**

Natural Language Processing (NLP) merupakan bagian dari ilmu komputer dan artificial intelligence yang memungkinkan mesin untuk memahami, memproses, dan menganalisis bahasa alami yang digunakan manusia (C. Manning & Hinrich, 1999), seperti yang dikutip oleh Torfi et al. (2021). Salah satu komponennya adalah Natural Language Understanding (NLU), yang berfokus pada ekstraksi makna semantik dari teks sehingga sistem dapat menginterpretasikan isi bahasa secara komputasional.

Perkembangan NLP didorong oleh penggunaan arsitektur transformer, yang memungkinkan pembentukan representasi teks yang bersifat kontekstual melalui mekanisme pemrosesan yang mempertimbangkan hubungan antar elemen dalam satu sequence secara menyeluruh (Vaswani et al., 2023). Arsitektur ini menjadi dasar bagi berbagai model embedding pre-trained, termasuk Sentence Bidirectional Encoder Representations from Transformers (SBERT) (Reimers & Gurevych, 2019), yang memanfaatkan pemahaman dua arah untuk menangkap hubungan kontekstual dalam teks, dengan [Gambar II.6](#page-5-0) menggambarkan arsitektur SBERT untuk mencari kesamaan dalam dua teks.

Gambar II.6. Arsitektur SBERT untuk Regresi Teks

Dalam implementasinya, terdapat dua pendekatan utama dalam pemrosesan pasangan teks, yaitu cross-encoder dan bi-encoder. Pendekatan cross-encoder memproses dua teks secara bersamaan sehingga memungkinkan interaksi penuh antar token, namun memiliki kompleksitas komputasi yang tinggi. Sebaliknya, pendekatan bi-encoder merepresentasikan setiap teks secara independen ke dalam ruang vektor yang sama, sehingga memungkinkan perbandingan semantik dilakukan secara efisien tanpa memerlukan pemrosesan ulang terhadap seluruh pasangan teks (Devlin et al., 2019; T. Gao et al., 2022; Reimers & Gurevych, 2019). Ilustrasi kedua pendekatan tersebut disajikan pada [Gambar II.7.](#page-6-0)

Gambar II.7. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder

Dalam penelitian ini, komponen NLU diimplementasikan melalui pendekatan berbasis bi-encoder untuk menghasilkan representasi vektor (embedding) dari teks yang lebih lanjut dijelaskan pada subbab [II.1.7.1.](#page-6-1) Representasi ini kemudian digunakan untuk mengukur hubungan semantik antar teks secara kuantitatif. Kesamaan semantik antara dua teks diukur menggunakan cosine similarity yang dijelaskan lebih lanjut pada subbab [II.1.7.2](#page-8-0). Pendekatan ini memungkinkan sistem membandingkan makna narasi feedback mahasiswa dengan deskripsi kriteria secara matematis terlepas dari perbedaan kata yang digunakan, dan hasilnya digunakan sebagai dasar dalam mekanisme pengambilan keputusan berbasis semantik dalam sistem.

**II.1.7.1 Vector Embedding Sebagai Representasi**

Fondasi komputasional dari pemahaman semantik teks adalah representasi teks sebagai vektor dalam ruang berdimensi. Secara formal, diberikan suatu teks sebuah fungsi representasi memetakan teks tersebut ke dalam ruang vektor berdimensi , dipetakan pada rumus [II.1](#page-6-2).

$$f_w(x) \to \mathbb{R}^d$$
 (II.1)

Prinsip dasar dari pendekatan ini berakar pada distributional hypothesis bahwa kata-kata atau ekspresi yang muncul dalam konteks serupa cenderung memiliki makna yang berdekatan (Harris, 1954). [Gambar II.8](#page-7-0) merepresentasikan bagaimana teks feedback dalam penelitian ini disimpan ke dalam representasi vektor menggunakan model embedding, narasi "Iklan yang dikumpulkan amir dikumpulkan dari platform yang beragam" dilakukan transformasi menjadi nilai matematis berupa koordinat dalam ruang vektor.

Gambar II.8. Rerpesentasi Ruang Vektor

Transformasi ini mengubah data teks yang bersifat simbolik menjadi data numerik. Tanpa representasi vektor, sistem tidak dapat melakukan operasi matematika untuk mengukur semantic similarity. Dengan representasi ini, narasi "Sangat baik" dan "Luar biasa" akan memiliki posisi koordinat yang berdekatan dalam ruang vektor.

Sebagai contoh, jika terdapat narasi ="Rekan saya berhasil mengumpulkan 30 data iklan", maka fungsi akan melakukan transformasi teks menjadi sebuah koordinat vektor seperti [0.12, −0.45, … ,0.89] dengan panjang dimensi = 1024 tergantung pada arsitektur model yang digunakan.

Representasi vektor memiliki properti yang tidak dimiliki representasi simbolik di mana ia memungkinkan pengukuran gradasi kemiripan antar konsep. Dalam penelitian ini, fungsi representasi diimplementasikan menggunakan model pretrained yang parameternya tidak dimodifikasi selama pipeline beroperasi. Konsekuensinya, kualitas representasi semantik yang dihasilkan termasuk sejauh mana vektor narasi mahasiswa dapat dibandingkan secara bermakna dengan vektor deskripsi rubrik sepenuhnya bergantung pada geometri ruang yang telah dikodekan model selama pre-training. Pilihan model pre-trained yang tepat menjadi keputusan desain kritis dalam penelitian ini dan dibahas lebih lanjut pada Bab IV.

**II.1.7.2 Cosine Similiarity untuk Eksploitasi Ruang Vektor**

Cosine similarity mengukur sudut antara dua vektor tanpa bergantung pada magnitudonya (C. D. Manning et al., 2009). Formula cosine similarity disajikan pada Rumus [II.2.](#page-8-1)

$$sim(v_i, v_j) = \frac{f_w(v_i) \cdot f_w(v_j)}{||f_w(v_i)|| \cdot ||f_w(v_j)||}$$
(II.2)

Di mana merupakan fungsi embedding yang didefinisikan pada subbab [II.1.7.1](#page-6-1). Nilai akhir similarity berada dalam rentang [-1,1], Invarians terhadap magnitude menjadikannya lebih robust untuk teks dengan panjang berbeda dibandingkan dengan Euclidean distance karena komponen yang diukur adalah arah/orientasi maknanya dalam ruang vektor (C. D. Manning et al., 2009). Cosine similarity mengeksploitasi properti ruang vektor yang sudah terstruktur secara semantik (Weinberger & Saul, 2009).

Contoh penggunaan rumus disajikan pada [Gambar II.9](#page-8-2), dua teks dalam ruang vektor dapat dikomputasi menggunakan cosine similarity untuk mengukur derajat sudut yang menentukan persentase similarity terhadap teks tersebut.

Gambar II.9. Cosine Similarity dalam Ruang Vektor

Dalam penelitian ini, cosine similarity digunakan sebagai alat ukur objektif untuk menentukan apakah sebuah feedback telah mencakup aspek yang diminta oleh rubrik. Sebagai contoh, terdapat dua vektor hasil embedding, yaitu vektor narasi mahasiswa (+,+) dan vektor deskripsi rubrik (-, ), jika hasil perhitungan rumus [II.2](#page-8-1) mendekati nilai 1, misalnya 0,92, maka kedua teks tersebut dianggap memiliki semantic similarity yang sangat tinggi. Sebaliknya, jika mendekati 0, misalnya 0,15, maka narasi mahasiswa dianggap tidak berkaitan dengan kriteria rubrik tersebut.

**II.1.7.3 Landasan Komputasional**

Komponen embedding dan cosine similiarity yang telah dijabarkan pada subbab [II.1.7.1](#page-6-1) dan [II.1.7.2](#page-8-0) menghasilkan sinyal numerik berupa nilai similiarity antar dua unit teks. Subbab ini menjelaskan bagaimana sinyal tersebut berfungsi sebagai basis inferensi yaitu bagaimana nilai kontinu yang dihasilkan ruang vektor dapat di transformasikan menjadi sebuah keputusan.

Nilai similiarity yang dihasilkan merupakan ukuran angular closeness atau sudut orientasi dalam ruang representasi vektor untuk memprediksi kemiripan. Transformasi dari kedekatan ini menjadi keputusan yang dapat ditindaklanjuti memerlukan tambahan yang dibangun di atas lapisan embedding. Alur transformasi dinyatakan pada

$$x \to v_x \to sim(v_x, v_{f_i}) \to \mathcal{D}$$
 (II.3)

Dengan contoh penggunaan,

1. : Mahasiswa menulis narasi "Data diambil dari LinkedIn".
2. , : Teks diubah menjadi vektor [0.11,0.54, … ].
3. / , #& : Vektor dibandingkan dengan vektor kriteria rubrik (#& ) "Keragaman Platform", menghasilkan similarity score 0,87.
4. .: Karena skor 0,87 ≥ threshold (misalnya 0,84), maka sistem mengambil keputusan (.) bahwa kriteria tersebut terpenuhi.

Di mana teks dipetakan menjadi representasi vektor ,, dibandingkan dalam ruang yang sama pada vektor #& , dan menghasilkan suatu keputusan (.) yang bergantung pada mekanisme yang akan dibangun diatasnya sehingga dapat dikatakan bahwa komponen embedding hanya bertugas menghasilkan sinyal dan interpretasi atas sinyal merupakan tanggung jawab lapisan sistem yang lebih tinggi.

Rumus ini merepresentasikan pipeline evaluasi semantik dalam sistem, yaitu mencakup indikator cakupan rubrik, koherensi skor-narasi, dan relevansi topik. Indikator kedalaman elaborasi tidak melalui transformasi ruang vektor ini karena dievaluasi secara independen menggunakan aturan heuristik berbasis jumlah kata. Kegunaannya adalah untuk menunjukkan bahwa komponen embedding hanya bertugas menghasilkan sinyal, sementara keputusan akhir (.) untuk memicu atau tidak memicu scaffolding merupakan tanggung jawab lapisan logika sistem yang membandingkan sinyal tersebut dengan threshold tertentu. Alur komputasi komponen dalam penelitian ini disajikan pada [Gambar II.10.](#page-10-0)

Gambar II.10. Representasi Pipeline Penelitian

Properti ini menilai kualitas inferensi yang dihasilkan dibatasi oleh kualitas representasi yang dihasilkan model, sehingga diperlukan pemilihan model embedding yang akan dikalibrasi pada data aktual sebagaimana dijabarkan pada Tabel IV.15. Selain itu pendekatan ini memiliki batasan interpretabilitas. Representasi vektor yang dihasilkan bersifat laten dan tidak memiliki padanan linguistik eksplisit pada tingkat token atau frasa (Senel et al., 2018) . Keterbatasan ini diterima sebagai konsekuensi yang dapat dikelola selama sinyal yang dihasilkan menunjukkan keselarasan yang memadai dengan penilaian manusia pada data anotasi yang dievaluasi melalui F1 score pada subbab [II.1.7.4.](#page-11-0)

**II.1.7.4 Metrik Evaluasi Kinerja Model dan Kalibrasi Threshold**

Dalam klasifikasi teks pada NLP, terutama pada dataset yang memiliki class imbalance, penggunaan F1-Score menjadi metrik utama untuk mengevaluasi kinerja model. F1-Score merupakan harmonic mean dari precission dan recall menggunakan [II.4](#page-11-1) (Riyanto et al., 2023) yang diilustrasikan pada [Gambar II.11](#page-12-0). Precision mengukur ketepatan model dalam memprediksi kelas positif dari keseluruhan hasil yang diprediksi positif oleh sistem, sedangkan Recall mengukur banyaknya kelas positif yang dideteksi dengan benar, dibandingkan dengan total data positif yang sebenarnya.

$$F1 Score = \frac{2 \times Precission \times Recall}{Precission + Recall}$$
 (II.4)

Dimana precission merupakan ukuran untuk mengukur akurasi prediksi yang benar menggunakan rumus [II.5.](#page-11-2)

$$Precission = \frac{TP}{TP + FP} \tag{II.5}$$

Sementara recall mengukur kemampuan untuk menemukan semua kemungkinan prediksi yang benar menggunakan rumus [II.6](#page-11-3).

$$Recall = \frac{TP}{TP + FN} \tag{II.6}$$

Dengan,

1. 7 atau true positive merupakan jumlah label "TRUE" yang diidentifikasi dengan benar.
2. 7 atau false positive adalah jumlah label "FALSE", namun diidentifikasi sebagai "TRUE".
3. = atau false negative adalah jumlah label "TRUE", namun diidentifikasi sebagai "FALSE".

Gambar II.11. Balancing Preccision dan Recall untuk F1-Score

Dalam skenario multi-label classification berbasis pasangan narasi dan kriteria pada penelitian ini, evaluasi F1-Score dilakukan menggunakan kerangka microaveraging, di mana setiap pasangan diperlakukan secara setara tanpa diberikan bobot berbeda (Sokolova & Lapalme, 2009). Pendekatan ini dipilih karena distribusi pasangan antar aspek rubrik tidak seimbang, sehingga aspek rubrik dengan kriteria yang lebih banyak akan menghasilkan pasangan kriteria evaluasi yang lebih banyak.

Lebih lanjut, dalam arsitektur digital scaffolding, F1-Score merupakan nilai acuan utama yang digunakan untuk melakukan kalibrasi threshold. Karena nilai cosine similarity yang dihasilkan oleh representasi vector embedding berupa nilai kontinu, sistem memerlukan mekanisme untuk menetapkan batas diskrit yang menentukan apakah suatu feedback memerlukan intervensi prompt atau tidak. Melalui pendekatan eksperimen optimasi seperti metode F1 sweep, untuk mencari threshold optimal yang memaksimalkan nilai F1-Score pada data anotasi (X. Gao et al., 2025).

**II.1.8 Rule Based**

Sistem rule based yang digunakan sebagai metode untuk menentukan teks scaffolding dalam penelitian ini mengadaptasi bentuk decision table. Bentuk tersebut adalah representasi tabular dari logika kondisional di mana setiap kombinasi kondisi input yang mungkin dipetakan secara eksplisit ke satu aksi output. Berbeda dari rangkaian if-else yang membiarkan kombinasi implisit, decision table menjamin kelengkapan dan ketunggalan pemetaan secara struktural. Sebuah decision table terdiri dari tiga elemen, yaitu (1) condition stubs yang mendefinisikan variabel input, (2) condition entries yang mendaftarkan seluruh kombinasi nilai, dan (3) action entries yang menentukan aksi untuk setiap kombinasi.

Untuk memberikan gambaran wujud konkret dari struktur ini, [Tabel II.2](#page-13-0) mengilustrasikan contoh rule-base yang digunakan dalam penelitian ini untuk memetakan kombinasi deteksi empat indikator tekstual narasi feedback menjadi aksi scaffolding tertentu, dengan keterangan bahwa nilai 1 merepresentasikan pelanggaran indikator, sedangkan nilai 0 merepresentasikan tidak adanya pelanggaran pada indikator.

Tabel II.2. Contoh Bentuk Rule-Base pada Sistem

Condition Stubs  |  Entry 1  |  Entry 2  |  Entry 3
Cakupan rubrik rendah  |  1  |  0  |  1
Inkoherensi Skor Narasi  |  0  |  1  |  1
Elaborasi dangkal  |  0  |  0  |  0
Topik tidak relevan  |  0  |  0  |  0
Action Entries  |  Tampilkan Template  |  Tampilkan Template  |  Tampilkan Template
Prompt A  |  Prompt B  |  Prompt C

Berdasarkan [Tabel II.2,](#page-13-0) conditional stubs menyatakan pelanggaran indikator tekstual, sedangkan entry menyatakan kombinasinya. Misalnya pada entry 1, jika sistem mendeteksi bahwa narasi mahasiswa melanggar cakupan rubrik namun ketiga indikator lainnya aman, maka aksi yang dipicu secara pasti adalah menampilkan teks dari template prompt A.

Properti utama yang relevan dari struktur pada tabel tersebut adalah completeness,  sehingga setiap kombinasi kondisi memiliki tepat satu aksi terdefinisi dan determinism. Akibatnya, kombinasi yang sama selalu menghasilkan aksi yang sama. Kedua properti ini menjadikan decision table cocok untuk domain keputusan bounded dan memerlukan perilaku yang dapat diaudit.

**II.1.9 Feedback Literacy**

Carless & Boud (2018) mendefinisikan feedback literacy sebagai pemahaman, kapasitas, dan disposisi yang diperlukan untuk memahami informasi evaluatif dan menggunakannya untuk meningkatkan pembelajaran. Konsep ini mencakup empat aspek, yaitu mengenali bentuk feedback, evaluative judgement, mengelola respons emosional, dan menerjemahkan feedback menjadi perbaikan. Salah satu aspeknya, evaluative judgement, merupakan kemampuan untuk menilai kualitas pekerjaan berdasarkan standar yang ditetapkan (Tai et al., 2018).

Carless & Boud (2018) tidak secara eksplisit memisahkan kapasitas menilai (evaluative judgement) dari kemampuan mengartikulasikan penilaian tersebut ke dalam bentuk tertulis. Pemisahan ini diajukan oleh Setiawan (2026a), yang membedakan evaluative judgement yaitu kapasitas internal mahasiswa untuk menilai kualitas suatu pekerjaan, dari evaluative expression, yaitu keberhasilan mengartikulasikan penilaian tersebut ke dalam narasi tertulis yang selaras dengan rubrik dan dapat dipahami oleh penerima feedback (assessee). Penelitian ini mengadopsi pemisahan (Setiawan, 2026a) sebagai dasar konseptual, dengan Carless & Boud (2018) berfungsi sebagai kerangka payung yang melegitimasi feedback literacy sebagai konstruk yang relevan, bukan sebagai sumber langsung dari pemisahan judgement-expression itu sendiri.

Literatur menunjukkan adanya kesenjangan antara kapasitas menilai dan kemampuan mengartikulasikannya. Setiawan (2026a) menemukan bahwa mahasiswa mampu memberikan skor numerik, namun hanya 18,4% menghasilkan narasi yang selaras dengan skor dan kriteria rubrik. (Nicol et al., 2014; Tai et al., 2018) menjelaskan bahwa mengartikulasikan penilaian internal ke dalam teks yang selaras dengan rubrik menuntut kemampuan mendiagnosis performa dan mengonstruksi justifikasi yang spesifik

Literatur menunjukkan adanya kesenjangan antara kapasitas menilai dan kemampuan mengartikulasikannya. Setiawan (2026a) menemukan bahwa mahasiswa mampu memberikan skor numerik, namun hanya 18,4% menghasilkan narasi yang selaras dengan skor dan kriteria rubrik. (Nicol et al., 2014; Tai et al., 2018) menjelaskan bahwa mengartikulasikan penilaian internal ke dalam teks yang selaras dengan rubrik menuntut kemampuan mendiagnosis performa dan mengonstruksi justifikasi yang spesifik, sebuah proses linguistik dan sosiopragmatis yang berbeda dari proses membentuk penilaian itu sendiri. Penjelasan ini, yang menempatkan kesenjangan tersebut secara spesifik pada kapasitas artikulasi dan bukan pada kapasitas menilai, merupakan asumsi motivasional yang diajukan oleh literatur untuk menjelaskan mengapa narasi feedback mahasiswa sering tidak selaras dengan skor yang diberikan. Penelitian ini mengadopsi asumsi tersebut sebagai dasar motivasi, namun tidak menguji secara independen apakah evaluative judgement mahasiswa benar-benar utuh sementara hanya evaluative expression yang bermasalah, karena penelitian ini tidak mengukur evaluative judgement secara terpisah dari teks yang dihasilkan.

Evaluative expression, sebagai keberhasilan artikulasi, merupakan konstruk laten, ia tidak dapat diamati secara langsung, melainkan hanya diinferensi dari ciri-ciri tekstual pada narasi yang dihasilkan. Literatur lain mendokumentasikan empat pola tekstual yang berulang kali muncul pada narasi feedback yang dinilai bermasalah: feedback yang tidak mencakup seluruh komponen rubrik (Camarata & Slieman, 2020), ketidakselarasan antara skor dan narasi (Zhang & Schunn, 2023), elaborasi yang terlalu dangkal berdasarkan jumlah kata (Curtis et al., 2024; Daou et al., 2020), serta narasi yang menyimpang dari topik rubrik yang dinilai (Sun et al., 2023). Literatur-literatur tersebut mendokumentasikan keempat pola ini sebagai gejala tekstual yang sering teridentifikasi pada feedback bermasalah; literatur tersebut tidak membangun atau memvalidasi keempat pola ini sebagai ukuran terstandardisasi terhadap kualitas evaluative expression secara keseluruhan.

Penelitian ini mengadaptasi keempat gejala tekstual tersebut sebagai target deteksi sistem, dengan satu prinsip seleksi: seluruhnya dapat diidentifikasi secara komputasional dari teks yang tersedia tanpa memerlukan interpretasi atau penilaian subjektif manusia terhadap kualitas evaluatif narasi. [Gambar II.12](#page-2-0) menggambarkan posisi keempat indikator ini dalam kerangka konseptual penelitian. Feedback literacy diposisikan sebagai konstruk payung yang mencakup evaluative judgement  sebagai kapasitas internal mahasiswa. Setiawan (2026b) membedakan kapasitas tersebut dari evaluative expression, yaitu keberhasilan mengartikulasikannya ke dalam narasi tertulis. Empat gejala tekstual yang dipilih dalam penelitian ini cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, dan relevansi topik bukan merupakan operasionalisasi langsung dari evaluative expression maupun evaluative judgement, melainkan serangkaian ciri tekstual yang diamati pada level output, yang oleh literatur dikaitkan dengan kegagalan artikulasi. Sistem yang dirancang dalam penelitian ini mendeteksi pemenuhan atau pelanggaran keempat gejala tekstual tersebut sebagai sinyal kebutuhan bantuan, bukan sebagai ukuran langsung terhadap kualitas evaluative expression atau evaluative judgement  mahasiswa. Teori feedback literacy diperlukan sebagai payung konseptual yang menghubungkan fenomena kelemahan penulisan narasi dengan intervensi komputasional. Pemisahan antara kapasitas evaluasi internal (evaluative judgement) dan artikulasinya (evaluative expression) digunakan untuk menjustifikasi bahwa keempat indikator yang dideteksi oleh pipeline berfokus murni pada aspek ekspresi tekstual.

Gambar II.12 Kerangka Operasionalisasi Evaluative Expression

Pertama, cakupan rubrik mengukur sejauh mana narasi feedback secara eksplisit membahas kriteria yang tercantum dalam rubrik penilaian. Feedback dengan cakupan rubrik rendah cenderung bersifat generik dan tidak memberikan informasi yang dapat ditindaklanjuti oleh penerimanya. Indikator ini mencerminkan kemampuan mahasiswa menghubungkan evaluasi mereka dengan kriteria pada rubrik (Camarata & Slieman, 2020; Zhang & Schunn, 2023), dengan contoh yang disajikan pada [Gambar II.13](#page-3-0) menggunakan rubrik pada Tabel II.1.

Gambar II.13. Contoh Cakupan Rubrik Tidak Terpenuhi

Kedua, koherensi evaluatif memastikan keselarasan antara skor numerik yang diberikan mahasiswa dan narasi kualitatif. Ketidakselarasan antara dua komponen ini, misalnya skor tinggi disertai dengan narasi negatif, mengindikasikan bahwa mahasiswa tidak mengintegrasikan penilaian kuantitatif dan kualitatif secara koheren (Zhang & Schunn, 2023), diilustrasikan pada [Gambar II.14.](#page-4-0)

Gambar II.14. Contoh Koherensi Evaluatif Tidak Terpenuhi

Ketiga, kedalaman elaborasi diukur berdasarkan jumlah kata pada narasi feedback. Feedback yang terlalu singkat secara struktural tidak mampu memuat deskripsi spesifik maupun saran perbaikan yang bermakna (Curtis et al., 2024; Daou et al., 2020). Panjang teks dipilih sebagai metrik karena narasi yang lebih panjang terbukti lebih mungkin memuat informasi yang dapat ditindaklanjuti oleh penerima feedback (Curtis et al., 2024), dengan contoh yang disajikan pada [Gambar II.15](#page-5-0). Meskipun berkorelasi, literatur tidak menetapkan threshold minimum yang berlaku universal. Daou et al. (2020) melaporkan median enam kata pada narasi peer review, namun nilai tersebut sangat dipengaruhi oleh perbedaan konteks, instrumen, serta bahasa yang digunakan. Oleh karena itu, penentuan tingkat elaborasi berdasarkan panjang teks dalam berbagai penelitian cenderung bersifat kontekstual dan bergantung pada karakteristik data yang digunakan.

Gambar II.15. Contoh Elaborasi Narasi Feedback

Keempat, relevansi topik memastikan bahwa konten narasi tidak menyimpang dari aspek rubrik yang menjadi fokus pertanyaan assessment. Feedback yang membahas aspek di luar pertanyaan yang diajukan, baik aspek rubrik lain maupun konten yang sama sekali tidak berkaitan, mengurangi nilai informatif feedback bagi penerimanya (Sun et al., 2023; Zhang & Schunn, 2023), diilustrasikan pada [Gambar](#page-5-1)  [II.16.](#page-5-1)

Gambar II.16. Contoh Relevansi Tidak Terpenuhi

Keempat indikator dipilih berdasarkan satu prinsip seleksi yaitu seluruhnya dapat diimplementasikan secara komputasional dari teks yang tersedia tanpa penilaian subjektif manusia, memungkinkan deteksi otomatis secara real-time sebagai dasar sistem conditional-prompt dalam penelitian ini. Operasionalisasi komputasional dari keempat indikator ini, yaitu model embedding, fungsi cosine similarity, dan metode kalibrasi threshold dijelaskan secara rinci pada Tabel III.3.

**II.1.9.1 Dekomposisi Rubrik**

Feedback literacy yang dijelaskan pada II.1.9 bersifat konseptual, keempatnya mendeskripsikan kapasitas kognitif yang seharusnya tercermin dalam narasi feedback. Untuk memungkinkan deteksi komputasional terhadap manifestasi tekstual evaluative expression pada narasi feedback, deskripsi rubrik perlu diterjemahkan menjadi unit-unit evaluatif yang dapat dibandingkan secara sistematis oleh pipeline NLP. Proses penerjemahan ini disebut sebagai dekomposisi rubrik.

Dekomposisi rubrik merupakan proses memecah sebuah deskripsi penilaian atau kompetensi yang kompleks menjadi kriteria-kriteria atau dimensi yang lebih spesifik dan terpisah. Dalam literatur pendidikan dan desain assessment, proses mengurai deskripsi holistik menjadi kriteria-kriteria tunggal ini sejalan dengan prinsip pengembangan analytic rubric. Berbeda dengan rubrik holistik yang menilai performa secara keseluruhan dan simultan, rubrik analitik merinci dan mengevaluasi setiap kriteria (dimensi atau sifat) secara terpisah (Brookhart, 2013). Pendekatan dekomposisi dalam pengembangan rubrik analitik dinilai memiliki relevansi pedagogis yang tinggi karena memungkinkan penyediaan informasi evaluatif yang lebih terperinci mengenai capaian kompetensi peserta didik pada setiap dimensi penilaian, sehingga mendukung identifikasi area kekuatan maupun aspek yang memerlukan intervensi pengembangan lebih lanjut (Jonsson & Svingby, 2007).

Secara teoretis, dekomposisi rubrik menerapkan pendekatan top-down, yaitu proses yang dimulai dari kerangka konseptual mengenai tujuan atau kompetensi pembelajaran, kemudian diturunkan secara sistematis ke dalam dimensi-dimensi penilaian yang lebih spesifik, operasional, dan dapat diamati. (Brookhart, 2013). [Gambar II.17](#page-7-0) mengilustrasikan konsep dekomposisi ini secara hierarkis.

Gambar II.17. Illustrasi Konseptual Dekomposisi Rubrik

Dalam penelitian ini, dekomposisi rubrik dilakukan pada dua tingkat representasi karena indikator feedback literacy yang dievaluasi beroperasi pada level analitis yang berbeda. [Tabel II.3](#page-7-1) menjabarkan perbedaan kedua tingkat dekomposisi tersebut dengan menggunakan rubrik pada Tabel II.1.

Tabel II.3. Tingkatan Dekomposisi Rubrik pada Pipeline

Tingkat  |  Fokus Pemecahan  |  Kegunaan pada  |  Contoh Unit Hasil
Representasi  |  Indikator Feedback  |  Dekomposisi
Tingkat 1:  |  Memecah satu aspek  |  Mengevaluasi  |  "Jumlah Iklan",
Dekomposisi Aspek  |  target menjadi  |  Cakupan Rubrik dan  |  "Platform".
kriteria-kriteria: Relevansi Topik
independen.
Tingkat2:  |  Memecah deskripsi  |  Mengevaluasi  |  "Mengumpulkan
Dekomposisi  |  pada setiap level skor  |  Koherensi Skor, yaitu  |  sedikit iklan" untuk
Performa  |  menjadi karakteristik  |  mengidentifikasi  |  skor 1.
narasinya.: apakah justifikasi teks
sesuai dengan skor: "Mengumpulkan
kuantitatif.: banyak iklan" untuk
skor 5.

Pada lingkup Aritifical Intelligence, dekomposisi rubrik secara manual merupakan tahapan knowledge acqusition dalam kerangka knowledge engineering. Tahapan ini mencakup ekstraksi, strukturisasi dan formalisasi pengetahuan evaluatif dari sumber manusia maupun dokumen ke bentuk representasi yang dapat diproses oleh sistem komputasional (Negnevitsky, 2005) di mana dalam konteks penelitian yaitu pipeline digital scaffolding yang akan dibangun. Konsep dekomposisi rubrik digunakan dalam penelitian ini untuk mengubah deskripsi holistik dari institusi menjadi unit-unit kriteria independen. Langkah ini esensial untuk memungkinkan komponen cosine similarity mengukur pemenuhan indikator cakupan rubrik dan relevansi topik secara spesifik terhadap masing-masing kriteria.

**II.1.10 Zone of Proximal Development**

Teori sosiokultural Vygotsky mendefinisikan Zone of Proximal Development  (ZPD) sebagai jarak antara kemampuan pemecahan masalah secara mandiri dengan kemampuan yang dapat dicapai melalui bimbingan dengan pihak yang lebih kompeten, pembelajaran optimal terjadi pada tugas yang berada dalam area ini dengan proses mediasi bersifat sementara serta kondisional. Secara teoritis, tugas menulis feedback menuntut beban kognitif tingkat tinggi yang mencakup penerapan kriteria rubrik, serta diagnosis masalah pada hasil kerja teman sejawat (Carless & Boud, 2018; Gu et al., 2026). Tingginya beban kognitif ini menempatkan penulisan feedback sebagai tugas yang umumnya berada di atas kemampuan mandiri mahasiswa di dalam area ZPD, sehingga memerlukan mediasi eksternal. Karena alasan inilah proses penulisan feedback membutuhkan dukungan berupa scaffolding (Kollar & Fischer, 2010). Ilustrasi mengenai kerangka kerja ZPD ini disajikan pada [Gambar II.18.](#page-9-0)

Gambar II.18 Ilustrasi kerangka ZPD

Dalam konteks penelitian ini, mahasiswa berada pada level aktual di mana mereka mampu memberikan skor numerik secara mandi. Meskipun tingkat pemberian skor sudah mampu dilakukan, temuan Setiawan (2026a) menunjukkan adanya tingkat ketidakselarasan skor yang tinggi. Kondisi tersebut mengindikasikan bahwa mahasiswa belum mampu mengartikulasikan justifikasi naratif yang selaras dengan kriteria rubrik secara konsisten. Setiawan (2026a) melaporkan bahwa hanya 18,4 % narasi yang selaras dengan skor yang diberikan oleh mahasiswa.

Kemampuan untuk menyelaraskan justifikasi narasi dengan skor feedback tersebut termasuk dalam area ZPD. Permasalahan tersebut dapat diatasi secara komputasional menggunakan conditional prompt untuk mengarahkan mahasiswa melengkapi komponen rubrik yang belum tercakup, memperbaiki skor yang belum koheren, menghindari narasi yang singkat (tingkat elaborasi), serta mencegah topik narasi feedback yang tidak relevan dengan rubrik penilaian yang sedang diajukan. Sistem pada penelitian ini berperan sebagai alat bantu yang memungkinkan mahasiswa mencapai level potensial tersebut selama sesi penulisan aktif. Konsep ZPD digunakan dalam penelitian ini untuk menjustifikasi pemberian bantuan scaffolding hanya ketika mahasiswa terdeteksi belum memenuhi indikator tekstual tertentu. Teori ini menjadi landasan komponen rule-based yang memutuskan kapan intervensi perlu diberikan dan ditarik.

**II.1.11 Scaffolding**

Konsep scaffolding sebagai strategi instruksional diperkenalkan oleh Wood et al. (1976) merupakan mekanisme yang menjembatani teori ZPD Vygotsky. Scaffolding merujuk pada dukungan terstruktur yang diberikan selama proses penyelesaian tugas dan ditarik secara bertahap seiring meningkatnya kompetensi peserta didik. Scaffolding memiliki sifat contingent dan fading, yaitu bantuan hanya diberikan ketika peserta didik tidak dapat melanjutkan tugas secara mandiri, dan dikurangi secara bertahap (Pea, 2004).

Dalam konteks penulisan feedback, sifat contingent ini memiliki implikasi langsung. Dukungan yang diberikan secara terus-menerus tanpa mempertimbangkan kondisi aktual peserta didik berpotensi menimbulkan ketergantungan, sehingga siswa tidak mengembangkan kemampuan evaluatif secara mandiri (Ding et al., 2025; Pea, 2004). Dalam penelitian ini, prinsip scaffolding dioperasionalisasikan melalui teknologi sebagai digital scaffolding, yaitu implementasi komputasional dari fungsi scaffolding yang dieksekusi secara real-time oleh pipeline NLP. Teori scaffolding diperlukan untuk memberikan kerangka instruksional bagaimana intervensi diberikan secara adaptif (contigent) tanpa menimbulkan ketergantungan. Konsep ini mendukung desain komponen rule-based yang menampilkan dan menarik prompt berdasarkan hasil deteksi keempat indikator tekstual.

**II.1.12 Digital Scaffolding**

Digital scaffolding merupakan implementasi prinsip scaffolding melalui mekanisme komputasional yang mampu mendeteksi kondisi input siswa secara otomatis dan memberikan panduan adaptif tanpa keterlibatan manusia secara langsung. Digital scaffolding juga memiliki sifat contingent dan fading melalui pemrosesan terhadap output yang dapat diobservasi secara komputasional, seperti teks narasi dan nilai numerik (Ding et al., 2025).

Arsitektur digital scaffolding dalam penelitian ini memisahkan dua tugas sehingga intervensi, yaitu tindakan komputasional berupa conditional-prompt berbasis template tekstual untuk memandu mahasiswa, dapat dikontrol tanpa bergantung pada AI generatif yang tidak dapat diprediksi. Pendekatan generasi teks untuk instrumen intervensi ini dieksplorasi lebih lanjut pada subbab [II.1.13](#page-11-0). Secara operasional, komponen NLP bertugas mengekstraksi empat indikator komputasi dari teks berbahasa Indonesia, sedangkan komponen rule-based berupa aturan eksplisit yang telah ditentukan sebelumnya memiliki tugas untuk memutuskan apakah indikator yang terdeteksi memerlukan intervensi tersebut. Mekanisme fading diimplementasikan dalam satu sesi penulisan aktif, di mana conditionalprompt hanya dimunculkan ketika nilai indikator berada di bawah threshold yang telah dikalibrasi dari distribusi data historis, dan berhenti secara otomatis ketika kondisi target terpenuhi.

**II.1.13 Pendekatan Generasi Teks untuk Scaffolding**

Sistem intervensi adaptif yang beroperasi secara real-time memerlukan komponen yang menghasilkan teks arahan berdasarkan hasil deteksi kondisi input. Dalam bidang Natural Language Generation, terdapat beberapa pendekatan yang secara teknis dapat digunakan untuk tugas ini, masing-masing dengan asumsi arsitektur dan karakteristik output yang berbeda, yaitu penggunaan LLM, fine-tuning dan zero-shot, Retrieval-Augmented Generation¸dan penggunaan template.

Pendekatan pertama yaitu menggunakan LLM, bergantung pada pola teks berdasarkan probabilistik yang dipelajari dari data skala besar. Dalam konteks feedback dalam pendidikan, LLM mampu menghasilkan respons yang adaptif dan menyerupai bahasa manusia tanpa memerlukan perancangan aturan eksplisit (Mazzullo et al., 2025). Namun, karena bersifat probabilistik dan tidak memiliki jaminan struktur, output yang dihasilkan dapat bervariasi dan berpotensi mengandung ketidaktepatan faktual atau penyimpangan dari tujuan instruksional. (Mazzullo et al., 2025; Stamper et al., 2024). [Gambar II.19](#page-12-0) menggambarkan bagaimana LLM melakukan generasi teks menggunakan fungsi probabilitas, di mana hasil probabilitas dapat berbeda dalam setiap percobaan.

Gambar II.19. Cara Kerja LLM dalam Generasi Teks

Pendekatan lain yang memanfaatkan LLM yaitu fine-tuning dan zero-shot/few-shot prompting memanfaatkan fleksibilitas model bahasa untuk menyesuaikan output dengan kebutuhan spesifik tanpa atau dengan training tambahan. Fine-tuning memungkinkan model mempelajari pola narasi feedback dari data yang telah dilakukan pre-processing (Mazzullo et al., 2025), sedangkan zero-shot dan few-shot memungkinkan penerapan langsung melalui instruksi atau contoh dalam prompt (M. Gao et al., 2025; Kim et al., 2023), diilustrasikan pada [Gambar II.20](#page-13-0), di mana letak perbedaan implementasi kedua pendekatan tersebut terletak dari contoh question dan answer sebelum diberikan question yang sesungguhnya, yang hanya disediakan pada metode few-shot prompting. Ketiga pendekatan ini menawarkan fleksibilitas tinggi, tetapi tetap bergantung pada mekanisme probabilistik yang tidak memberikan jaminan determinisme output.

Gambar II.20. Contoh Penggunaan Few-Shot dan Zero-Shot

(Sumber: Wan et al. (2023))

Pendekatan lain adalah Retrieval-Augmented Generation (RAG), yang menggabungkan model bahasa dengan sumber pengetahuan eksternal. Dalam skema ini, teks yang dihasilkan didasarkan pada parameter model dan informasi yang diambil dari dokumen atau database yang relevan. Diilustrasikan pada [Gambar II.21](#page-14-0), pendekatan ini meningkatkan keterkaitan konten dengan sumber referensi dan mengurangi ketidaktepatan faktual, meskipun tetap mempertahankan sifat generatif dari model bahasa yang mendasarinya. Meskipun begitu, pendekatan RAG bergantung pada pengetahuan domain yang dimiliki, sehingga hasil generasi teks memiliki kemungkinan bias. Selain itu, arsitektur RAG dapat mengalami fenomena retrieval collapse, yaitu kondisi di mana komponen retrieval gagal menyesuaikan diri dengan variasi input dan cenderung mengambil dokumen yang sama secara berulang. Ketika hal ini terjadi, informasi yang diambil menjadi tidak relevan, dan model generatif cenderung mengabaikannya, sehingga sistem berperilaku serupa dengan model bahasa umum tanpa grounding eksternal. (Lewis et al., 2021).

Gambar II.21. Arsitektur RAG

Pendekatan berbasis template dalam konteks Natural Language Generation merupakan metode yang melakukan mapping input nonlinguistic seperti data, variable, atau konstanta pada lapisan lingusitik menggunakan struktur yang sudah terdefinisi yang berisikan gap atau placeholder. Ilustrasi pendekatan ini disajikan pada Gambar II.22. Konsekuensi dari mekanisme ini adalah ruang output sistem bersifat terbatas dan dapat dienumerasi secara lengkap sebelum runtime. Setiap kemungkinan teks merupakan kombinasi dari template yang tersedia dan domain nilai slot yang diizinkan. Properti ini menghasilkan sistem yang deterministik dan reproducible, sehingga setiap input identik akan selalu menghasilkan output yang sama. Dalam konteks sistem instruksional, determinisme ini memungkinkan verifikasi eksplisit terhadap seluruh kemungkinan output, memastikan kesesuaian dengan tujuan pedagogis tanpa ketergantungan pada proses sampling (Deemter et al., 2005).

Gambar II.22. Ilustrasi Penggunaan Template untuk Output Teks

Dalam konteks penelitian ini, berbagai pendekatan generasi teks tersebut menjadi landasan untuk memahami bagaimana teks scaffolding dapat dihasilkan sebagai respons terhadap kondisi feedback mahasiswa. Setiap pendekatan merepresentasikan cara yang berbeda dalam memetakan hasil evaluasi terhadap narasi feedback menjadi bentuk teks yang dapat dikomunikasikan kembali kepada pengguna. Dengan demikian, kerangka konseptual untuk menempatkan mekanisme generasi teks dalam sistem yang dirancang, khususnya dalam kaitannya dengan kebutuhan akan kesesuaian instruksional, konsistensi respons, serta keterhubungan antara hasil evaluasi dan teks yang dihasilkan. Pemahaman mengenai pendekatan generasi teks ini diperlukan untuk menjustifikasi pemilihan arsitektur sistem. Dalam penelitian ini, pendekatan berbasis template statis digunakan untuk memastikan komponen output prompt beroperasi secara deterministik, konsisten, dan memitigasi risiko halusinasi generatif.

**II.1.14 Desain Eksperimen dan Evaluasi Statistik**

Penelitian ini menerapkan metode kuantitatif berskala pilot study dengan desain randomized posttest-only control group dan alokasi acak (Campbell et al., 1963; Shadish et al., 2002). Penelitian ini menggunakan random assignment terhadap partisipan individual ke dalam kelompok treatment dan kelompok kontrol.

Pemilihan Desain 6 didasarkan pada tujuan penelitian untuk mengevaluasi penggunaan digital scaffolding dalam kondisi pembelajaran yang mendekati praktik penggunaan aktual. Dalam konteks implementasi nyata, mahasiswa tidak menjalani pengukuran awal sebelum menggunakan digital scaffolding. Oleh karena itu, desain posttest-only dipilih agar proses penulisan narasi feedback dan penggunaan bantuan digital scaffolding dapat berlangsung secara alami tanpa intervensi tambahan berupa pre-test.

Penggunaan desain posttest-only berbasis random assignment juga bertujuan menghindari testing effect atau bias yang muncul akibat interaksi partisipan dengan instrumen pre-test sebelum perlakuan diberikan (Campbell et al., 1963). Tanpa adanya pre-test, potensi partisipan mengalami efek jenuh maupun pengaruh pengukuran awal yang dapat mengubah cara mereka menyusun narasi feedback  sebelum menerima bantuan digital scaffolding dapat diminimalkan..

Secara metodologis, Shadish et al. (2002) menegaskan bahwa random assigment merupakan instrumen paling kuat untuk menjamin kesetaraan karakteristik antar kelompok sebelum manipulasi dilakukan. Oleh karena itu, setiap perbedaan signifikan yang ditemukan pada post-test lebih mungkin dapat diatribusikan sebagai efek dari intervensi karena pengaruh perbedaan karakteristik awal antar kelompok telah diminimalkan antar kelompok melalui random assignment.

Selain itu kontrol terhadap confounding variables diperkuat dengan memastikan kedua kelompok berada dalam ekosistem akademik yang identik, meliputi mata kuliah, periode pengerjaan tugas, dan instrumen rubrik yang seragam. [Gambar II.23](#page-2-0) menyajikan desain eksperimen post-test only dalam penelitian ini. Perbedaan utama hanyalah terdapat keberadaan bantuan digital scaffolding yang diberikan kepada kelompok treatment.

Gambar II.23. Ilustrasi Eksperimen Post-Test Only

**II.2 Karya Ilmiah Sejenis**

Tabel II.1 Literatur sejenis dan penulisnya

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Penelitian mengenai feedback literacy menunjukkan bahwa kualitas feedback tidak hanya ditentukan oleh kemampuan mahasiswa memberikan penilaian, tetapi juga oleh kemampuan mengomunikasikan penilaian tersebut dalam bentuk narasi yang dapat dipahami dan ditindaklanjuti. Dalam konteks PjBL, aktivitas self assessment dan peer assessment menempatkan mahasiswa sebagai pemberi sekaligus penerima feedback sehingga kemampuan menyusun narasi evaluatif menjadi bagian penting dari proses pembelajaran. Kajian Setiawan (2026a) yang mengungkapkan bahwa dalam ekosistem PjBL di Indonesia, sebagian besar mahasiswa mampu memberikan skor numerik tinggi tetapi kesulitan menyusun narasi feedback yang selaras dengan rubrik. Temuan tersebut menunjukkan masalah mendasar dalam kemampuan mahasiswa mengekspresikan evaluasi secara eksplisit dalam bentuk feedback bermakna, sehingga intervensi diperlukan saat proses penulisan berlangsung, bukan sekadar deteksi pasca-penulisan.

Berbagai penelitian telah mengidentifikasi sejumlah karakteristik tekstual yang digunakan untuk menganalisis narasi feedback. Penelitian menekankan pentingnya cakupan terhadap aspek-aspek dalam rubrik penilaian (Camarata & Slieman, 2020), Zhang & Schunn (2023) menunjukkan pentingnya koherensi antara skor numerik dan narasi pendukung, Curtis et al. (2024) menggunakan panjang narasi sebagai pendekatan operasional untuk merepresentasikan tingkat elaborasi, sedangkan , Sun et al. (2023) membahas relevansi topik sebagai indikator kesesuaian isi feedback  terhadap aspek yang sedang dievaluasi. Keempat karakteristik tersebut memiliki kesamaan, yaitu dapat diidentifikasi melalui informasi tekstual yang tersedia pada narasi feedback sehingga berpotensi dioperasionalkan menjadi indikator komputasional.

Pada sisi intervensi, sejumlah penelitian menunjukkan bahwa Aritificial Intelligence (AI) dapat membantu dalam pemberian intervensi memberikan bantuab berupa digital scaffolding. Ding et al. (2025) mengajukan model scaffolding yang mengintegrasikan kontekstualisasi dan logika prosedural, di mana scaffolding memberikan dukungan dinamis yang selaras dengan tahapan kognitif pembelajaran. Gu et al. (2026) menemukan bahwa AI Generatif (GenAI) mampu memberikan umpan balik instan dan adaptif yang secara efektif menopang proses regulasi diri (Self-Regulated Learning) mahasiswa. Namun, penggunaan AI juga memunculkan tantangan kontrol pedagogis yang serius. Seperti yang diperingatkan oleh Gu et al. (2026) dan didukung oleh temuan Mohammad et al. (2025) ketergantungan mahasiswa pada saran instan dari Large Language Models (LLM) dapat memicu cognitive scaffloding atau kemalasan metakognitif, di mana mahasiswa melemahkan pemikiran kritisnya sendiri dan menerima rekomendasi AI secara otomatis. Selain itu sebagian besar pendekatan masih beroperasi secara sumatif, algoritma hanya memproses data setelah mahasiswa mengirimkan feedback (Omotehinwa et al., 2025; Rahimi et al., 2017).

Perkembangan NLP dalam analisis feedback menunjukkan pergeseran dari pendekatan yang berfokus pada evaluasi hasil akhir menuju ekstraksi berbagai karakteristik tekstual yang semakin beragam. Pada konteks PjBL, Setiawan et al. (2026) meneliti pendekatan seperti dictionary-based matching, ekstraksi fitur wacana, analisis sentimen, maupun klasifikasi speech acts menunjukkan bahwa informasi yang terkandung dalam narasi self assessment dan peer assessment. Setiawan (2026b) juga memvalidasi penggunaan model berbasis bahasa Indonesia (seperti IndoBERT dan IndoRoBERTa) untuk mengekstraksi polaritas sentimen dan mengklasifikasikan speech acts dari ribuan teks self assessment dan peer assessment mahasiswa. Pendekatan ini memungkinkan sistem untuk mendeteksi persistensi dan perjuangan kognitif mahasiswa di balik ekspresi yang secara kultural cenderung netral atau menahan diri. Meskipun demikian, sebagian besar penelitian masih memanfaatkan hasil analisis tersebut sebagai sarana evaluasi atau visualisasi setelah mahasiswa menyelesaikan proses penulisan (post-hoc analysis). Dengan kata lain, keluaran NLP belum secara langsung digunakan sebagai dasar pengambilan keputusan pedagogis selama proses penulisan berlangsung. Kesenjangan inilah yang menjadi landasan penelitian ini, yaitu mengintegrasikan hasil deteksi NLP dengan mekanisme rule-based untuk menentukan kebutuhan bantuan dan memicu digital scaffolding secara real-time ketika mahasiswa sedang menyusun narasi self assessment dan peer assessment.

Berdasarkan sintesis tersebut, dapat diidentifikasi dua kesenjangan penelitian. Pertama, meskipun berbagai penelitian telah mengidentifikasi karakteristik feedback yang berkaitan dengan kualitas narasi, belum banyak penelitian yang mengoperasionalkan karakteristik tersebut menjadi indikator tekstual yang dapat dideteksi secara otomatis selama proses penulisan berlangsung. Kedua, meskipun AI telah dimanfaatkan sebagai digital scaffolding, sebagian besar pendekatan masih memberikan bantuan setelah proses penulisan selesai atau belum mengintegrasikan mekanisme pengambilan keputusan berbasis aturan untuk menentukan kebutuhan bantuan secara konsisten. Kesenjangan inilah yang menjadi dasar pengembangan arsitektur digital scaffolding berbasis rubrik pada penelitian ini, yang mengintegrasikan pemrosesan NLP dengan mekanisme rule-based untuk memberikan conditional prompt secara real-time selama mahasiswa menyusun feedback pada aktivitas self assessment dan peer assessment di lingkungan PjBL.

**BAB III**

**METODOLOGI PENELITIAN**

Bab ini menjelaskan metodologi penelitian termasuk, objek, variabel, data yang ada dalam penelitian serta metodologi yang dilakukan.

Pada penelitian ini, hubungan antar istilah teknis yang digunakan dalam metodologi dipetakan sebagai berikut: (1) SAPA adalah aplikasi self dan peer assessment berbasis web yang sudah ada dan dikembangkan secara terpisah dari penelitian ini. Aplikasi ini berfungsi sebagai platform pengisian feedback mahasiswa. (2) Aplikasi pendukung eksperimen adalah modifikasi dari SAPA yang mengintegrasikan fitur digital scaffolding sebagai ekstensi, dikembangkan khusus untuk keperluan eksperimen penelitian ini. (3) Pipeline digital scaffolding adalah komponen analitik yang memproses narasi feedback secara real-time untuk mendeteksi pemenuhan keempat indikator tekstual menggunakan pendekatan sentence embedding dan cosine similarity. (4) Rule-based system adalah mekanisme pengambilan keputusan berbasis tabel kondisional yang memetakan vektor hasil deteksi indikator ke dalam keputusan intervensi secara deterministik. (5) Template scaffolding adalah output batuan berupa teks prompt yang ditampilkan kepada mahasiswa ketika sistem mendeteksi satu atau lebih indikator yang belum terpenuhi.

**III.1 Penjelasan Penelitian**

Penelitian yang dilaksanakan menggunakan metode kuantitatif dengan desain posttest-only control group dan alokasi treatment-kontrol secara acak, sebagaimana didefinisikan pada subbab [II.1.14.](#page-0-0) Penelitian ini dilakukan selama periode Januari 2026 hingga Juni 2026. Waktu yang dialokasikan mencakup tahap perbandingan arsitektur NLP, pembuatan pipeline, integrasi sistem scaffolding ke dalam sistem existing, hingga pelaksanaan eksperimen pengujian langsung terhadap subjek penelitian, serta proses analisis hasil data statistik.

Pendekatan kuantitatif eksperimental dengan desain post-test-only beserta kelompok kontrol dan treatment dipilih sebagaimana telah dijustifikasi pada subbab [II.1.14](#page-0-0).

Untuk merepresentasikan esensi penelitian secara matematis dan mendefinisikan batasan dari artefak yang diusulkan, sistem digital scaffolding dirancang secara hybrid, komponen NLP yang telah dijelaskan pada subbab II.1.7 bertugas mengukur kualitas semantik teks narasi secara komputasional, sedangkan komponen rule-based yang telah didefinisikan pada subbab II.1.8 menentukan apakah kualitas tersebut melewati threshold atau memerlukan intervensi. Tiga komponen utama dalam arsitektur ini adalah sebagai berikut:

1. Rubrik (ℛ): Kumpulan kriteria evaluasi yang tidak dapat diubah dan telah ditetapkan sebelumnya oleh institusi, didefinisikan sebagai ℛ = ?2@, 2A, … , 2<sup>B</sup> C.
2. Pertanyaan kuantitatif dan kualitatif feedback (D): Instruksi yang dihasilkan dari rubrik, didefinisikan sebagai fungsi dari rubrik: D = ℛ .
3. Respons siswa (): Feedback, atau variabel yang dapat berubah, didefinisikan sebagai tuple yang terdiri dari skor numerik kuantitatif BEF dan narasi teks kualitatif +,+ , yang ditandai sebagai = BEF, +,+ . Di mana BEF ∈ 1, dengan 1 merepresentasikan himpunan skala yang digunakan, yaitu ?1,2,3,4,5C, sementara +,+ adalah teks narasi berbahasa Indonesia. Feedback literacy  diimplementasikan melalui fungsi penilaian I yang memetakan satu instance feedback ke vektor empat indikator.

Korelasi dari ketiga komponen tersebut disajikan pada [Gambar III.1](#page-8-0) menggunakan rubrik pada Tabel II.1.

Gambar III.1. Korelasi Rubrik, Pertanyaan, dan Feedback

Untuk merepresentasikan sistem secara formal, penelitian ini menggunakan notasi matematis berikut. Rubrik direpresentasikan sebagai himpunan kriteria statis (ℛ). Pertanyaan assessment diturunkan dari rubrik (D). Respons mahasiswa direpresentasikan sebagai pasangan skor numerik dan teks narasi (). Setiap respons dievaluasi oleh empat fungsi pengukur (@ − J), masing-masing menghasilkan nilai dalam rentang [0,1] yang dibandingkan terhadap threshold similarity (KLF,) untuk memutuskan apakah intervensi diperlukan.

Seluruh simbol dan definisi operasional yang digunakan dalam sistem dan analisis statistik dirangkum dalam [Tabel III.1](#page-8-1).

Tabel III.1. Notasi Matematis

Simbol  |  Domain  |  Deskripsi
ℛ  |  Himpunan  |  Kumpulan kriteria rubrik statis yang ditetapkan institusi.
D  |  Fungsi dari R  |  Pertanyaan assessment yang diturunkan dari rubrik.

Simbol  |  Domain  |  Deskripsi
F  |  Tuple $(s_{num}, s_{txt})$  |  Respons mahasiswa berupa skor dan narasi feedback.
S  |  Himpunan  |  Skala rubrik yang digunakan, yaitu {1,2,3,4,5}.
Ф  |  Fungsi  |  Fungsi penilaian sistematis yang memetakan <i>F</i> ke vektor indikator.
$f_i$  |  $F \rightarrow [0,1]$  |  Fungsi pengukur indikator kualitas ke-i
$\theta_{sim,i}$  |  Skalar [0,1]  |  Threshold similarity komputasional untuk indikator ke i, dikalibrasi dari data historis.
$\theta_i$  |  Skalar [0,1]  |  Threshold keputusan intervensi untuk indikator ke-i, dalam penelitian ini bernilai mutlak 1 untuk memastikan pemenuhan indikator secara total.
$d_i$  |  {0,1}  |  Keputusan biner intervensi per indikator, dengan: 1. 0: Tidak membutuhkan intervensi. 2. 1: Membutuhkan intervensi.
D  |  $\{0,1\}^4$  |  Ruang keputusan biner berdimensi empat, dengan total 16 kombinasi. Merepresentasikan kombinasi hasil identifikasi indikator komputasi.
d(F)  |  D  |  Vektor keputusan aktual hasil evaluasi empat indikator pada <i>renspons</i> mahasiswa <i>F</i> .
$\mathcal{P}$  |  Himpunan  |  Kumpulan template conditional-prompt.
М  |  $D \to \mathcal{P} \cup \{\emptyset\}$  |  Fungsi <i>rule-based</i> yang memetakan vektor keputusan ke <i>template prompt</i> .
V  |  Tuple $(v_{komponen}, s_{num})$  |  Variabel kontekstual dinamis untuk pengisian template.
FE  |  Fungsi  |  Hasil operasi untuk dekomposisi rubrik.
$T_{pillai}$  |  Skalar  |  Nilai statistik Pillai's Trace dari uji MANOVA.
$\delta_i$  |  Skalar  |  Nilai effect size Cohen's d untuk indikator ke-i.
$\alpha_{adj}$  |  Skalar (0,0125)  |  Signifikansi statistik dengan Bonferroni correction.

Alur arsitektur data bersifat searah, yaitu  $\mathcal{R} \to Q \to F$ , sejalan dengan ilustrasi yang telah disajikan pada Gambar III.1. Artefak digital scaffolding yang diusulkan beroperasi sepenuhnya dalam batas variabel F, sistem tidak mengubah, menghasilkan, atau memodifikasi parameter  $\mathcal{R}$  maupun Q untuk menjaga instrumen evaluasi feedback yang telah ditetapkan. Setiap instance feedback direpresentasikan sebagai pasangan dua modalitas.

III.1.2 Formulasi Sistem dan Pengukuran

Feedback literacy dievaluasi melalui fungsi penilaian Φ yang memetakan feedback mahasiswa ke dalam empat indikator komputasi sesuai dengan rumus III.7.

$$\Phi(F) = [f_1(F), f_2(F), f_3(F), f_4(F)]$$
 (III.7)

Di mana  $f_1$ mengukur cakupan rubrik,  $f_2$  mengukur koherensi skor dan naratif,  $f_3$  mengukur kedalaman elaborasi, dan  $f_4$  mengukur relevansi topik, dengan  $f_i$ :  $F \rightarrow$

[0,1] untuk setiap  $i \in \{1,2,3,4\}$ . Dengan kata lain, sistem menghasilkan empat nilai dalam satu respons mahasiswa untuk setiap indikator dengan masing-masing dalam rentang 0 hingga 1. Gambar III.2 menyajikan ilustrasi pemetaan feedback kepada keempat indikator komputasi.

Gambar III.2. Pemetaan Feedback kepada Indikator Komputasi

Sistem menetapkan vektor threshold  $\theta_{sim} = [\theta_{sim,1}, \theta_{sim,2}, \theta_{sim,3}, \theta_{sim,4}]$  di mana setiap  $\theta_{sim,i}$  dikalibrasi dari distribusi data historis sebagai threshold komputasi pemenuhan indikator, dan  $\theta = [\theta_1, \theta_2, \theta_3 \theta_4]$  yang masing-masing bernilai 1 sebagai threshold keputusan intervensi scaffolding. Keputusan intervensi per indikator didefinisikan pada rumus III.8.

$$d_i(F) = \begin{cases} 1 & \text{jika } f_i(F) < \theta_i \\ 0 & \text{sebaliknya} \end{cases}, i \in \{1,2,3,4\}$$
 (III.8)

Dengan kata lain, sistem memberikan nilai 1, merepresentasikan bahwa intervensi diperlukan pada indikator ke-i apabila hasil komputasi pemenuhan indikator ke-i berada di bawah threshold  $\theta$ , dan nilai 0 apabila indikator telah terpenuhi sehingga tidak membutuhkan intervensi. Gambar III.3 menyajikan alur feedback ditransformasi menjadi  $f_i$  sebelum dilakukan komputasi keputusan intervensi pada  $d_i$  dalam rumus III.8.

Gambar III.3. Alur Komputasi Indikator dan Keputusan Intervensi

Tujuan dari penelitian ini adalah merancang intervensi rule-based digital scaffolding yang mengevaluasi feedback () secara real-time. Jika fungsi mendeteksi rendahnya feedback literacy yang didefinisikan pada rumus [III.9](#page-11-1), sistem memicu prompt (7) berbasis rule-based dan adaptif pada antarmuka yang telah dijelaskan pada subbab II.1.8.

$$If \exists i: d_i(F) = 1 \to P \tag{III.9}$$

Fungsi pengambilan keputusan intervensi direpresentasikan melalui fungsi aturan Q: ?0,1C<sup>J</sup> → P ∪ ?∅C, yang memetakan 16 kemungkinan kombinasi vektor keputusan biner ke dalam himpunan template prompt P yang selaras. Untuk memberikan gambaran operasional mengenai alur transformasi data dari nilai kontinu hasil pemrosesan NLP hingga menjadi keputusan intervensi, Tabel II.2 menyajikan simulasi data pada beberapa kondisi respons mahasiswa.

Tabel III.2. Simulasi Alur Data dan Keputusan Intervensi Sistem

Tahapan Evaluasi Komputasional  |  Kasus Simulasi A (Kondisi Melanggar)  |  Kasus Simulasi B (Kondisi Ideal)
1. Input Feedback ()  |  Skor: 3  |  Skor: 5
Narasi: "Bagus": Narasi: "Rekan saya
mengumpulkan banyak sekali
iklan dari berbagai platform,

dan semua iklannya sangat relevan tanpa ada kendala sama sekali. Dia langsung mengerjakan dengan sangat mudah"
2. Vektor Indikator kualitas  |  $[f_1 = 0.20, f_2 = 0, f_3 =$  |  $[f_1 = 1.00, f_2 = 1, f_3 =$
$(\Phi(F) = [f_1, f_2, f_3, f_4])$  |  $[1, f_4 = 0]$  |  $[0, f_4 = 1]$
3. Vektor <i>Threshold</i>  |  $[\theta_1, \theta_2]$  |  $[\theta_3, \theta_4]$
4. Vektor Keputusan Biner  |  $[d_1 = 1, d_2 = 1, d_3 =$  |  $[d_1 = 0, d_2 = 0, d_3 =$
$d(F) = [d_1, d_2, d_3, d_4]$  |  $[1.d_4 = 1]$  |  $0, d_4 = 0]$
(Terjadi Pelanggaran): (Memenuhi Seluruh
Indikator)
5. Aksi Sistem: Memicu Template Prompt
6. Output Antarmuka  |  Menampilkan teks panduan  |  adaptif ataupun fading sesuai
dengan template prompt.

Melalui mekanisme sekuensial yang digambarkan pada Tabel II.2, tujuan komputasi utama untuk melakukan intervensi kontingensi selama fase penulisan aktif dapat berjalan selama real-time, mengarahkan mahasiswa untuk merevisi narasinya hingga kondisi kriteria  $\forall i: f_i(F) \geq \theta_i$  terpenuhi secara mutlak.

Pengaruh sistem diukur pada dua level analisis. Level pertama menguji keempat indikator sebagai vektor multivariat menggunakan MANOVA, menghasilkan Pillai's Trace sebagai ukuran efek keseluruhan. Level kedua menguji per indikator secara independen menggunakan analisis follow-up dengan Bonferroni correction. Kriteria indikasi efektivitas sistem didefinisikan pada rumus III.10.

$$\text{Efektivitas} = \begin{cases} \textit{Terkonfirmasi, Jika $T_{pillai}$ signifikan $pada $\alpha = 0.05$ dan $\sum_{i=1}^{4} 1[\delta_i \geq 0.5] \geq 3$ \\ \textit{Parsial,Jika salah satu kondisi terpenuhi} \\ \textit{Tidak terkonfirmasi,Jika keduanya tidak terpenuhi} \end{cases} \tag{III.10}$$

Di mana  $T_{Pillai}$  adalah Pillai's Trace dari MANOVA dengan keempat indikator sebagai variabel dependen,  $\delta_i$  adalah Cohen's d untuk indikator ke-i pada analisis follow-up, dan  $\alpha_{adjusted} = 0.0125$  berlaku untuk setiap uji per indikator. Definisi operasional Pillai's Trace dan Cohen's d, beserta justifikasi pemilihannya sebagai effect size, dijabarkan pada tahap Evaluasi dalam subbab III.6.6.2.

**III.2 Variabel Penelitian**

Variabel penelitian pada tahap eksperimen disusun berdasarkan konfigurasi pipeline evaluasi yang telah dikembangkan pada RQ1. Dalam konteks eksperimen, pipeline berperan sebagai instrumen pengukuran untuk menghasilkan nilai keempat indikator tekstual yang selanjutnya digunakan sebagai variabel terikat pada analisis statistik:

1. Variabel bebas (*independent variable*)

Variabel bebas dalam penelitian adalah keberadaan intervensi digital scaffolding yang bersifat biner, yaitu aktif dan tidak aktif.

2. Variabel terikat (*dependent variable*)

Variabel terikat dalam penelitian ini adalah tingkat pemenuhan empat indikator tekstual narasi feedback, yaitu cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, serta relevansi topik. Keempat indikator tersebut diukur menggunakan pipeline digital scaffolding yang dikembangkan pada RQ1 dan merepresentasikan aspek-aspek konstruk evaluative judgement dalam feedback literacy yang dapat dioperasionalkan secara komputasional berdasarkan narasi feedback.[Tabel III.3.](#page-13-0)

Tabel III.3. Indikator Tekstual yang Dapat Dikomputasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Keempat indikator tersebut merupakan variabel terikat pada tahap eksperimen. Nilainya diperoleh melalui pipeline evaluasi yang dikembangkan pada RQ1. Pemilihan indikator tersebut merepresentasikan aspek-aspek konstruk evaluative judgement dalam feedback literacy yang dikenalkan oleh Carless & Boud (2018) yang dapat dioperasionalkan secara komputasi berdasarkan narasi feedback, hal tersebut telah dijelaskan lebih dalam pada subbab II.1.9. Sementara, variabel bebas bersifat biner karena penelitian membandingkan kondisi dengan dan tanpa bantuan digital scaffolding ketika mengisi narasi feedback.

**III.3 Data Penelitian**

Data yang digunakan dalam penelitian ini dikategorikan ke dalam dua kelompok, yaitu: (1) data historis untuk pengembangan dan validasi pipeline , dan (2) data eksperimental sebagai perbandingan evaluasi perbedaan tingkat pemenuhan keempat indikator tekstual narasi feedback antara kelompok kontrol dan kelompok treatment yang menerima bantuan digital scaffolding. Kedua data penelitian didefinisikan pada subbab [III.3.1](#page-0-0) hingga [III.3.2](#page-4-0).

Penggunaan dataset dari Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung dipilih karena relevansi langsung dengan fenomena rendahnya feedback literacy yang telah diidentifikasi sebelumnya, serta untuk memastikan kontinuitas temuan dengan studi Setiawan (2026a) yang menggunakan konteks institusional serupa.

**III.3.1 Data Pengembangan dan Validasi Pipeline Scaffolding**

Data pengembangan dan validasi pipeline berasal dari data historis yang telah dikumpulkan dalam mata kuliah yang menerapkan PjBL di Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung pada tahun akademik 2025/2026. Data ini terdiri dari dua bagian, yaitu (1) data feedback yang didefinisikan pada subbab [III.3.1.1](#page-1-0) dan (2) data rubrik pada subbab [III.3.1.2](#page-3-0). Rubrik yang digunakan pada data ini telah didefinisikan pada Tabel II.1.

Dalam konteks text classification pada machine learning, setiap instance data direpresentasikan sebagai satu objek analisis yang memiliki fitur dan label target (C. D. Manning et al., 2009). Dalam penelitian ini, satu objek analisis adalah satu pasangan narasi feedback dengan kriteria rubrik. Fitur dari objek ini adalah representasi semantik teks dalam ruang vektor yang dihasilkan oleh model sentence embedding yang telah dijelaskan pada subbab II.1.7.1. Label yang diprediksikan adalah keputusan biner TRUE/FALSE yang menyatakan apakah narasi tersebut diindikasikan membahas aspek rubrik. Skema ini mengikuti paradigma multi-label binary classification di mana satu objek dapat memiliki lebih dari satu label (Tsoumakas & Katakis, 2009) yang telah dijelaskan pada subbab II.1.6, mengingat satu narasi feedback dapat memenuhi atau tidak memenuhi beberapa kriteria feedback literacy secara simultan dan independen satu sama lain.

**III.3.1.1 Data Narasi Feedback**

Bagian pertama dari data pengembangan adalah data feedback. Data ini merupakan hasil self dan peer assessment dengan populasi data sebanyak 10.098 baris yang dihasilkan oleh mahasiswa jenjang D3 pada pertengahan dan akhir semester pada mata kuliah "Proyek 1: Pemanfaatan Aplikasi Perkantoran", mencakup 8.118 peer assessment dan 1.980 self assessment.

Dari jumlah populasi tersebut, diambil sampel berupa 384 baris data untuk diberi anotasi secara manual. Volume data ini ditentukan menggunakan formula Cochran dengan tingkat confidence 95% (z = 1,96), margin of error sebesar 5% (e = 0,05), serta proporsi populasi (}) ditetapkan sebesar 0,5 untuk memaksimalkan ukuran sampel dalam kondisi varians yang tidak diketahui. Perhitungan dilakukan menggunakan rumus [III.11.](#page-1-1)

$$n_0 = \frac{z^2 \cdot p \cdot (1 - p)}{e^2}$$
 (III.11)

Parameter yang digunakan dalam formula dipertimbangkan untuk hal berikut confidence 95% dipilih sebagai standar minimum yang diterima. Margin of error tujuan anotasi adalah menghasilkan estimasi distribusi feedback literacy yang representatif.

Perhitungan komputasional menggunakan parameter tersebut menghasilkan nilai estimasi 8<sup>Ñ</sup> = 384,16. Sesuai dengan konversi standar dalam statistik terapan, jumlah sampel final yang ditarik untuk anotasi ditetapkan sebanyak 8 = 384 narasi. Jumlah ini merupakan batas kecukupan statistik untuk mencapai margin of error 5%, sehingga menjamin reliabilitas estimasi distribusi tanpa bergantung pada asumsi varians awal. Untuk memastikan seluruh karakteristik data terwakili secara proporsional, penarikan sampel dilakukan secara acak dari total populasi historis.

Data ini digunakan mengevaluasi arsitektur pipeline pada tahap pengembangan, dengan memuat komponen penilaian kuantitatif dan kualitatif mahasiswa. [Tabel](#page-2-0)  [III.4](#page-2-0) dan [Tabel III.5](#page-2-1) menyajikan struktur data self dan peer assessent yang digunakan pada penelitian ini.

Tabel III.4. Struktur Data Peer Assessment

Atribut  |  Deskripsi  |  Tipe data
class_id  |  Kelas dari mahasiswa penulis feedback. Contoh: 1A  |  String
assesor_id  |  Nomor induk mahasiswa penulis feedback. Contoh: 221524003  |  String
group_id  |  Kelompok mahasiswa dalam PjBL. Contoh: 1  |  Integer
No. urut rekan tim yang akan dinilai  |  Nomor urut siswa penerima feedback pada kelompok PjBL. Contoh: 1  |  Integer
assessee_id  |  Nomor induk mahasiswa penerima feedback. Contoh: 221524021  |  String
timepoint  |  Waktu pengambilan feedback. Berisi mid/end. Contoh: mid  |  String
indicator  |  Pertanyaan kuantitatif pada feedback. Contoh: Seberapa baik rekan Anda dalam mengumpulkan iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)  |  String
question  |  Pertanyaan kualitatif pada feedback. Contoh: Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  String
peer_score  |  Skor kuantitatif yang diberikan penulis feedback. Contoh: 5  |  Integer
peer_comment  |  Narasi kualitatif yang diberikan penulis feedback. Contoh: Siswa sangat baik dalam mengumpulkan iklan baik di platform seperti linkedin dan instagram  |  String

Tabel III.5. Struktur Data Self Assessment

Atribut  |  Deskripsi  |  Tipe data
class_id  |  Kelas dari mahasiswa penulis feedback. Contoh: 1A  |  String
student_id  |  Nomor induk mahasiswa penulis feedback. Contoh: 221524003  |  String
group_id  |  Kelompok mahasiswa dalam PjBL. Contoh: 1  |  Integer
timepoint  |  Waktu pengambilan feedback. Berisi mid/end. Contoh: mid  |  String
indicator  |  Pertanyaan kuantitatif pada feedback.  |  String

Atribut  |  Deskripsi  |  Tipe data
Contoh: Seberapa baik rekan Anda dalam mengumpulkan iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)
question  |  Pertanyaan kualitatif pada feedback. Contoh: Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  String
self_score  |  Skor kuantitatif yang diberikan penulis feedback. Contoh: 5  |  Integer
self_comment  |  Narasi kualitatif yang diberikan penulis feedback. Contoh: Siswa sangat baik dalam mengumpulkan iklan baik di platform seperti linkedin dan instagram  |  String

Data dikumpulkan secara resmi oleh pihak pengajar PjBL melalui google form sebagai instrumen self dan peer assessment yang telah digunakan sebagai komponen pembelajaran.

**III.3.1.2 Data Rubrik**

Bagian kedua dari data pengembangan adalah data rubrik. Data ini mencakup aspek penilaian, kriteria, serta hubungan dengan skor yang digunakan sebagai dasar pertanyaan kuantitatif dan kualitatif pada feedback dengan struktur data yang disajikan pada [Tabel III.6](#page-3-1).

Tabel III.6. Struktur Data Rubrik

Atribut  |  Deskripsi  |  Tipe data
Aspek  |  Aspek spesifik dari kriteria penilaian.  |  String
Contoh: Pengumpulan Iklan Lowongan Kerja
Kriteria  |  Deskripsi kriteria yang dinilai.  |  String
Contoh: Banyaknya iklan dan keragaman platform
yang digunakan.
Pertanyaan Kuantitatif  |  Pertanyaan kuantitatif pada feedback.  |  String
Contoh: Seberapa baik rekan Anda dalam
mengumpulkan iklan lowongan kerja dari platform
yang ditugaskan? (Nilai dari skala 1-5)
Pertanyaan Kualitatif  |  Pertanyaan kualitatif pada feedback.  |  String
Contoh: Mengapa? (Berikan contoh spesifik
kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam
mengumpulkan iklan)
Skala 1 (Sangat Kurang)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 1.
Contoh: Mengumpulkan sedikit iklan.

Atribut  |  Deskripsi  |  Tipe data
Skala 3 (Cukup)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 3.
Contoh: Mengumpulkan cukup iklan.
Skala 5 (Sangat Baik)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 5.
Contoh: Mengumpulkan banyak dan relevan dari
platform yang bervariasi.

Penelitian ini menggunakan rubrik pada Tabel II.1 sebagai dasar evaluasi sistem digital scaffolding pada tahap pengembangan, dengan tambahan tahap feature extraction yang dijelaskan pada subbab II.1.9.1 sebagai dekomposisi dari rubrik tersebut. Implementasi feature extraction didasarkan pada beberapa pertimbangan berikut.

1. Memastikan setiap eksekusi pipeline menghasilkan output yang konsisten untuk input yang sama sebagai upaya reproducibility
2. Literatur educational data mining Romero & Ventura (2020) menegaskan bahwa preprocessing dan penataan data pendidikan sering kali menjadi kontribusi penelitian yang berdiri sendiri, mengingat kompleksitas spesifik domain, seperti struktur hierarkis dan longitudinal, dalam konteks pendidikan.

**III.3.2 Data Evaluasi Scaffolding**

Data evaluasi adalah data primer yang dikumpulkan dari subjek penelitian dengan menggunakan sistem digital scaffolding, didefinisikan pada subbab [III.3.2.1](#page-5-0) dan menghasilkan data interaksi sebagai ekstensi, sebagaimana didefinisikan pada subbab [III.3.2.2](#page-5-1).

Data evaluasi dikumpulkan menggunakan metode post-test only, yaitu data dikumpulkan hanya pada satu sesi yang sama. Detail desain eksperimen telah dijabarkan pada subbab II.1.14. Data tersebut didapatkan dari dua kelompok eksperimen, yaitu (1) kelompok treatment yang mengisi feedback dengan scaffolding aktif, dan (2) kelompok kontrol yang mengisi feedback tanpa scaffolding. Secara operasional, kelompok treatment menerima bantuan scaffolding secara real-time selama proses penulisan narasi feedback berlangsung, sedangkan kelompok kontrol menyelesaikan penulisan tanpa intervensi scaffolding apapun. Setelah seluruh jawaban tersebut dianalisis menggunakan pipeline digital scaffolding yang sama untuk menghasilkan skor pemenuhan keempat indikator tekstual narasi feedback. Hasil analisis inilah yang digunakan sebagai data perbandingan antara kelompok kontrol dan treatment. Gambar II.4 menyajikan ilustrasi pemetaan intervensi digital scaffolding pada kedua kelompok subjek eksperimen.

Gambar III.4. Pemetaan Scaffolding pada Kelompok Eksperimen

**III.3.2.1 Data Evaluasi**

Merupakan data yang berfungsi untuk mengukur kemampuan scaffolding yang didasarkan pada besar pengaruh (effect size) dan nilai signifikansi Pillai's Trace dari MANOVA. Data akhir ini lebih lanjut akan digunakan pada tahapan III.6.6.3B.

**III.3.2.2 Data Interaksi**

Merupakan data interaksi mahasiswa kelompok treatment yang menerima scaffolding. Setiap narasi feedback yang ditulis mahasiswa dan respon/output dari pipeline digital scaffolding akan dicatat. Data akhir ini lebih lanjut akan digunakan pada tahapan III.6.6.3C.

**III.3.2.3 Data Kuesioner**

Merupakan data respon kuesioner yang didapatkan dari kelompok treatment yang telah menerima bantuan scaffolding saat sesi perancangan skenario eksperimen. Data ini lebih lanjut didapatkan dan dirancang pada tahapan III.6.6.1C.

**III.4 Objek Penelitian**

Dalam penelitian ini, objek penelitian terbagi menjadi dua kelompok, yaitu objek material dan fungsional yang disajikan pada subbab [III.4.1](#page-6-0) hingga [III.4.2.](#page-7-0)

**III.4.1 Objek Material**

Objek material penelitian adalah teks narasi dan skor numerik hasil self dan peer assessment berbahasa Indonesia dalam konteks PjBL. Data ini merepresentasikan output feedback literacy mahasiswa yang dapat diamati sebagai target intervensi pipeline NLP.

Unit analisis ditetapkan pada level mahasiswa sebagai penulis feedback atau assessor. Hasil komputasi empat indikator yang telah didefinisikan pada Tabel III.3 diagregasi menjadi vektor indikator individu. Agregasi ini menjaga independensi observasi dalam analisis statistik. [Gambar III.5](#page-6-1) menyajikan visualisasi terhadap pemetaan unit analisis, objek material, dan agregasi vektor indikator individu.

Gambar III.5. Pemetaan Unit Analisis, Objek Material, dan Vektor Indikator

Keputusan untuk mengagregasi komputasi empat indikator ke level individu mahasiswa sebagai unit analisis didasarkan pada dua pertimbangan. Pertama, analisis pada level untuk setiap pertanyaan akan menghasilkan observasi yang tidak independen. Hal tersebut disebabkan karena satu mahasiswa dapat menghasilkan beberapa feedback dalam peer assessment untuk setiap rekan sejawat (assessee). Kedua, unit analisis yang relevan adalah mahasiswa sebagai individu, bukan pertanyaan sebagai unit. Keputusan tersebut didasarkan oleh intervensi scaffolding yang dirancang untuk mempengaruhi perilaku penulisan mahasiswa secara keseluruhan, dengan konsekuensi bahwa variasi antar-pertanyaan dalam satu mahasiswa tidak dianalisis secara terpisah.

**III.4.2 Objek Fungsional**

Objek fungsional dalam penelitian ini adalah arsitektur pipeline digital scaffolding pada pengisian self dan peer assessment. Objek dipilih karena sistem evaluasi otomatis konvensional beroperasi secara sumatif tidak bisa memberikan intervensi real-time ketika penulisan feedback berlangsung, yang telah dijelaskan pada subbab I.2. Arsitektur yang diusulkan memastikan intervensi tidak hanya akurat secara semantik tetapi juga dikontrol melalui rule-based.

**III.5 Perangkat Pendukung**

Penelitian ini memanfaatkan berbagai alat, teknologi, dan library untuk mendukung dua tahapan utama, yaitu eksperimen dalam pemodelan NLP dan pengembangan pipeline digital scaffolding. Dengan rincian pada [Tabel III.7](#page-7-1).

Tabel III.7. Perangkat Pendukung

Teknologi  |  Versi  |  Fungsi
Python  |  3.10  |  Bahasa pemrograman utama yang digunakan untuk memproses data teks, mengeksekusi model NLP, serta melakukan perhitungan untuk mengevaluasi model.
FastAPI  |  0.x  |  Framework web Python yang memiliki performa tinggi untuk membangun endpoint dari sistem digital scaffolding.
Vue.js & Inertia.js  |  3.x  |  Framework frontend yang dikombinasikan dengan Inertia.js untuk membangun antarmuka digital scaffolding.
Laravel  |  10.x  |  Framework yang digunakan untuk mengelola antarmuka bisnis self dan peer assessment.
Tailwind CSS  |  3.x  |  Framework CSS utility-first untuk merancang antarmuka pengguna.

Teknologi  |  Versi  |  Fungsi
Sentence Transformer + PyTorch  |  2.x  |  Library utama yang digunakan untuk mengunduh, memuat, dan mengeksekusi model NLP, serta mengekstraksi representasi numerik (embedding) dari teks mahasiswa berbahasa Indonesia untuk keperluan pengukuran kesamaan semantik.
ChromaDB  |  -  |  Vector database yang digunakan secara spesifik untuk menyimpan dan melakukan komputasi pencarian kedekatan vektor antar teks mahasiswa dengan rubrik evaluasi.
Google Gemini API  |  -  |  Generative AI Service yang digunakan untuk proses dekomposisi rubrik sebagai bagian dari APE SAPA.
Scikit-learn  |  1.3.x  |  Library yang digunakan untuk menghitung kesamaan kosinus antar vektor rubrik dan teks mahasiswa, serta untuk menghasilkan metrik performa model.
Pandas + NumPy  |  -  |  Library yang digunakan untuk membersihkan serta memproses data mentah.
Google Colab atau Kaggle notebook  |  -  |  Digunakan untuk mempercepat proses benchmarking model melalui cloud dengan memanfaatkan GPU seperti NVIDIA T4 atau P100.
Microsoft Excel atau Google Spreadsheet  |  -  |  Alat bantu untuk melakukan anotasi manual terhadap dataset, sesuai dengan rubrik yang telah ditentukan sebelum proses evaluasi dilakukan.
Aplikasi SAPA  |  -  |  Lingkungan eksperimen yang merupakan aplikasi internal yang sudah dikembangkan sebelumnya dan terpisah dari penelitian ini. Integrasi sistem scaffolding ke dalam aplikasi dilakukan atas persetujuan pengembang aplikasi sebagai fitur tambahan yang diaktifkan secara selektif berdasarkan kelompok eksperimen.

**III.6 Tahapan Pelaksanaan Penelitian**

Subbab ini membahas tahapan yang dilakukan selama penelitian untuk menjawab kedua pertanyaan penelitian. Secara keseluruhan tahapan terbagi menjadi tahapan yang berfokus pada RQ 1, yaitu perancangan, implementasi, dan evaluasi pipeline digital scaffolding untuk mendeteksi empat indikator tekstual narasi feedback. Pipeline digital scaffolding yang dihasilkan, kemudian digunakan sebagai mekanisme intervensi sekaligus instrumen pengukuran pada tahap kedua untuk menjawab RQ 2, yaitu mengevaluasi bagaimana tingkat pemenuhan keempat indikator tekstual narasi feedback melalui desain eksperimen yang dirancang. Tahapan pelaksanaan penelitian pada [Gambar III.6](#page-9-0) dirancang secara sistematis agar setiap tahap saling mendukung dan menghasilkan output yang dapat digunakan untuk menjawab permasalahan penelitian.

Gambar III.6. Tahapan Pelaksanaan Penelitian

**III.6.1 Identifikasi Masalah dan Studi Pendahuluan**

Tahap ini bertujuan memperoleh pemahaman awal mengenai karakteristik permasalahan yang menjadi dasar perancangan digital scaffolding. Kegiatan dilakukan melalui dua proses yang saling melengkapi, yaitu analisis konseptual terhadap karakteristik objek penelitian dan analisis empiris terhadap data historis self dan peer assessment. Data historis yang digunakan berasal dari 95 mahasiswa pada mata kuliah Proyek 1: Pemanfaatan Aplikasi Perkantoran yang dilaksanakan pada rentang Agustus–Desember 2024 sebagaimana dijelaskan pada III.3.1.

Hasil dari tahap ini tidak digunakan sebagai evaluasi performa sistem, melainkan sebagai dasar dalam merumuskan kebutuhan sistem, menentukan pendekatan komputasional yang sesuai, serta menyusun spesifikasi pipeline yang akan dikembangkan. Seluruh hasil analisis dipaparkan pada BAB IV.

**III.6.1.1 Identifikasi Karakteristik Indikator Tekstual Narasi**

Analisis konseptual dilakukan untuk mengidentifikasi karakteristik objek penelitian sebelum sistem dikembangkan. Analisis berfokus pada dua aspek.

Pertama, mengidentifikasi karakteristik narasi feedback sebagai objek pemrosesan bahasa alami berdasarkan teori feedback literacy Carless & Boud (2018), beserta karakteristik data tekstual yang digunakan dalam penelitian.

Kedua, karakteristik tekstual pada data historis yang dimiliki berdasarkan keempat indikator tekstual narasi feedback (Camarata & Slieman, 2020; Curtis et al., 2024; Sun et al., 2023; Zhang & Schunn, 2023). Analisis ini digunakan untuk memahami jenis penalaran yang diperlukan pada masing-masing indikator serta menjadi dasar dalam menentukan pendekatan komputasional yang sesuai.

**III.6.1.2 Kuantifikasi Skala Masalah dam Urgensi Intervensi**

Analisis empiris dilakukan menggunakan korpus historis sebanyak 10.098 narasi feedback yang terdiri atas 8.118 peer assessment dan 1.980 self assessment. Analisis bertujuan mengidentifikasi pola aktual penulisan feedback mahasiswa sebagai dasar perumusan kebutuhan sistem.

Analisis dilakukan menggunakan pendekatan Exploratory Data Analysis (EDA) dan statistik deskriptif terhadap karakteristik narasi, distribusi skor, panjang teks, hubungan antara skor dan narasi, serta berbagai pola yang berkaitan dengan keempat indikator tekstual yang digunakan dalam penelitian. Selain analisis kuantitatif, dilakukan pula penelaahan terhadap contoh-contoh narasi untuk mengidentifikasi bentuk penyimpangan yang muncul pada masing-masing indikator.

**III.6.2 Studi Literatur dan Pendefinisian Objektif Solusi**

Tahap ini bertujuan untuk menerjemahkan masalah empiris yang telah dipaparkan pada tahap studi pendahuluan menjadi spesifikasi teknis formal yang dapat diimplementasikan pada arsitektur software. Kajian literatur difokuskan secara terpadu pada tiga domain teoritis dengan output komponen desain sistem yang spesifik, sebagaimana diilustrasikan pada [Gambar III.7.](#page-11-0)

Gambar III.7. Peta Sintesis Studi Literatur

Pertama, domain teori pedagogi untuk menelaah kerangka kerja feedback literacy  (Tai et al., 2018), aspek evaluative judgement (Tai et al., 2018), serta hambatan sosiopragmatis dalam interaksi sosiokultural kolektivistik (Brown & Levinson, 1987; Setiawan, 2026a). Output dari domain ini adalah batasan konseptual untuk mengisolasi parameter indikator kualitas tertulis dari proses kognitif internal, yang menghasilkan pendefinisian empat kriteria manifestasi tekstual evaluative expression terbatas yang dapat diobservasi tanpa memerlukan interpretasi manusia.

Kedua, domain NLP untuk menelaah arsitektur artificial neural network Transformer, pemodelan sentence embedding berbasis pendekatan bi-encoder (Reimers & Gurevych, 2019) serta metrik eksploitasi ruang vektor melalui cosine similarity. Output dari domain ini adalah kodifikasi dan transformasi empat indikator tekstual narasi feedback menjadi fungsi matematis kontinu yang dapat dihitung secara real-time.

Ketiga, domain rule based untuk menelaah penggunaan kondisional decision table (Negnevitsky, 2005) serta metode template-based natural language generation (Deemter et al., 2005). Keluaran dari domain ini adalah spesifikasi pemetaan biner antar-indikator dan perancangan struktural sentence frames yang berfungsi mereduksi tahapan generatif penulisan sesuai prinsip kontingensi scaffolding.

Sintesis dari ketiga domain literatur tersebut dirumuskan menjadi batasan operasional dan objektif solusi. Dokumentasi menjadi landasan formal bagi pemodelan pipeline NLP, perancangan basis data, dan implementasi komponen digital scaffolding pada aplikasi pendukung eksperimen.

**III.6.3 Pemodelan Konfigurasi Pipeline**

Tahapan ini bertujuan untuk memodelkan konfigurasi model NLP yang digunakan untuk komputasi indikator tekstual narasi pada sistem digital scaffolding, mencakup proses anotasi dataset yang didefinisikan pada subbab [III.6.3.1](#page-13-0), serta evaluasi dan kalibrasi model pada subbab III.6.3.2.

**III.6.3.1 Anotasi Dataset**

Tahap ini bertujuan untuk menghasilkan ground truth yang menjadi dasar objektif bagi seluruh evaluasi pipeline. Pipeline NLP yang dirancang menggunakan pendekatan komputasional yang telah didefinisikan pada subbab II.1.7.3, bahwa tidak ada model yang dilakukan training. Namun, evaluasi performa pipeline tetap memerlukan ground truth dari dataset yang telah dianotasi untuk mengukur seberapa akurat sistem mendeteksi indikator cakupan rubrik, koherensi skor-narasi, dan relevansi topik. Anotasi juga diperlukan untuk kalibrasi threshold untuk menentukan nilai cosine similarity yang mengindikasikan bahwa sebuah narasi memenuhi atau tidak memenuhi indikator tersebut (KLF,). Sementara itu, indikator kedalaman elaborasi diimplementasi secara langsung menggunakan threshold heuristik jumlah kata, sehingga tidak membutuhkan anotasi. [Gambar III.8](#page-13-1) menyajikan pemetaan dataset tersebut untuk menghasilkan threshold komputasi indikator (KLF,).

Gambar III.8. Pemetaan Dataset untuk Evaluasi

Dari total populasi 10.098 baris data feedback historis, proses anotasi dilakukan terhadap sampel sebanyak 384 data. Jumlah sampel ini dihitung dan dijelaskan representasinya menggunakan Cochran formula pada rumus [III.11](#page-1-1) sebagaimana dijelaskan pada subbab III.3.1. Formulasi ini direpresentasikan sebagai standar metodologis yang teruji untuk penelitian cross sectional design populasi berskala besar (COCHRAN, 1977). Pada domain riset software engineering, formula Cochran secara empiris telah diaplikasikan untuk menentukan ukuran sampel minimum yang representatif dari populasi terbatas (Zul et al., 2024), serta digunakan secara aktif untuk mereduksi volume dataset teks berskala besar menjadi sampel representatif sebelum tahapan anotasi atau ekstraksi fitur berbasis Natural Language Processing (Ghali et al., 2025).

Pengambilan sampel dilakukan secara acak berdasarkan semester dilaksanakannya assessment untuk memastikan representasi proporsional dari seluruh subkelompok populasi, sehingga dataset tidak didominasi oleh satu class atau satu periode semester pembelajaran tertentu. Selanjutnya, untuk memastikan ecological validity dari dataset (Lücking et al., 2022), distribusi sampel dievaluasi dengan cara menghitung proporsi narasi yang tidak memenuhi empat indikator tekstual narasi feedback. Evaluasi distribusi ini dilakukan di awal untuk memverifikasi bahwa sampel secara akurat merepresentasikan fenomena tekstual aktual di dunia nyata sebelum proses pelabelan dilanjutkan.

**B. Dekomposisi Rubrik sebagai Pre Processing**

Penelitian ini tidak menerapkan tahapan data cleaning seperti stemming, lowercasing, atau penghapusan tanda baca pada narasi feedback mahasiswa. Pendekatan ini merupakan keputusan untuk menjaga ecological validity. Teks dipertahankan dalam bentuk mentah sebagaimana adanya untuk merepresentasikan kondisi lingkungan dunia nyata, sehingga performa model yang dievaluasi benarbenar merepresentasikan keandalannya saat beroperasi secara real-time.

Oleh karena itu, tahapan pre-processing dalam penelitian ini difokuskan secara eksklusif pada struktural dekomposisi rubrik sebagai feature extraction dengan memecah unit-unit kriteria atomik rubrik. Pemisahan ini merupakan prerequirement agar model embedding dapat melakukan komputasi kesamaan semantik antara narasi mahasiswa terhadap satu dimensi evaluasi spesifik tanpa

bias dari informasi yang overlapping, hal ini didasari pada subbab II.1.9.1. [Gambar](#page-0-0)  [III.9](#page-0-0) menyajikan visualisasi pemetaan dekomposisi rubrik terhadap dataset anotasi.

Gambar III.9. Pemetaan Dekomposisi Rubrik pada Anotasi Dataset

Dekomposisi rubrik mengubah bentuk rubrik holistik menjadi unit-unit atomik diskrit yang dapat diproses secara independen oleh pipeline NLP, sebagaimana dijelaskan oleh subbab II.1.9.1.

Secara formal, rubrik dianotasikan sebagai ℛ yang memiliki satu atau lebih aspek (I ), sebagaimana dinyatakan pada rumus [III.12.](#page-0-1)

$$\mathcal{R} = \{A_1, A_2, \dots, A_n\} \tag{III.12}$$

Di mana ∈ ?1,2, … , 8C. Sebagai contoh, beberapa aspek dalam rubrik yang didefinisikan pada Tabel II.1 adalah "Manajemen Waktu" dan "Kontribusi dalam Kelompok".

Setiap aspek (I ) memiliki satu atau lebih kriteria penilaian (-, ), sebagaimana direpresentasikan dalam rumus [III.13.](#page-0-2)

$$A_i = \{ K_{i,1}, K_{i,2}, \dots, K_{i,m} \}$$
 (III.13)

Dengan i merupakan aspek ke-i, dan ∈ ?1,2, . . , 8C. Sebagai contoh, aspek "Pembuatan Struktur Data" dalam rubrik pada Tabel II.1, memiliki kriteria "Banyaknya iklan dan keragaman platform yang digunakan."

Dalam rubrik penilaian, setiap kriteria (-, ) memiliki komponen tingkat skor (<sup>V</sup> ∈ 1), dengan f merupakan deret nilai yang memetakan rentang penilaian, contohnya f = ?1,2,3,4,5C. Komponen skor tersebut dihubungkan dengan deskripsi performa spesifik (-, ,L<sup>à</sup> ), sebagaimana direpresentasikan pada rumus [III.14](#page-1-0).

$$K_{i,j} = \{K_{i,j,s_1}, K_{i,j,s_2}, \dots, K_{i,j,s_n}\}$$
 (III.14)

Sebagai visualisasi, [Gambar III.10](#page-2-0) menyajikan pemetaan notasi terhadap rubrik historis yang telah didefinisikan pada Tabel II.1. Setelah proses dekomposisi, dilakukan validasi terhadap isi konten hasil dekomposisi dengan domain expertise.

Gambar III.10. Pemetaan Rubrik dalam Notasi Dekomposisi

Dari setiap kriteria -, , dihasilkan dua feature set yang melayani indikator berbeda, ditetapkan dengan notasi pada rumus [III.15](#page-3-0).

$$FE(K_{i,j}) = (COV(K_{i,j}), COH(K_{i,j}))$$
(III.15)

Di mana åçU-, ! merupakan feature set untuk indikator cakupan (@) dan relevansi topik (J), didefinisikan pada subbab [III.6.3.1C](#page-3-1). Di sisi lain, åçé-, merupakan feature set untuk indikator koherensi skor narasi (A) yang didefinisikan pada subbab [III.6.3.1D](#page-4-0).

**C. Cakupan dan Relevansi Feature-Set**

Feature set ini merepresentasikan seluruh dimensi substantif yang seharusnya hadir dalam narasi feedback, didefinisikan pada rumus [III.16.](#page-3-2)

$$COV(K_{i,j}) = \{c_{cov,1}, c_{cov,2}, \dots, c_{cov,n}\}$$
 (III.16)

Di mana setiap 2èW%,B merupakan satu unit teks yang merepresentasikan satu dimensi evaluatif dari kriteria ke-e pada aspek ke-. Unit teks tersebut diturunkan dari tiga sumber, yaitu: (1) deskripsi performa spesifik dari setiap skor (-, ,L<sup>à</sup> ), (2) pertanyaan kuantitatif, dan (3) pertanyaan kualitatif. Dengan komponen pertanyaan kuantitatif dan kualitatif hanya digunakan jika terdapat komponen penilaian yang tidak disebutkan dalam deskripsi performa spesifik (-, ,L<sup>à</sup> ).

Ketiga sumber tersebut dilebur menjadi satu kumpulan kriteria atomik karena ketiganya merepresentasikan dimensi yang seharusnya terdapat dalam narasi feedback. Contoh proses dekomposisi untuk feature set ini disajikan pada [Tabel](#page-3-3)  [III.8](#page-3-3) dengan menggunakan rubrik pada Tabel II.1 untuk aspek "Pengumpulan iklan lowongan kerja".

Tabel III.8 Contoh Proses Dekomposisi Cakupan dan Relevansi Topik

Sumber  |  Isi Konten Asli  |  Kriteria yang diekstraksi
Deskripsi  |  Mengumpulkan sedikit iklan.  |  "jumlah iklan"
performa skor 1
(-, ,Lâ )
Deskripsi  |  Mengumpulkan cukup iklan.  |  "jumlah iklan"
performa skor 3
(-, ,Lê )

Sumber  |  Isi Konten Asli  |  Kriteria yang diekstraksi
Deskripsi  |  Mengumpulkan banyak dan relevan dari  |  "jumlah iklan", "keragaman
performa skor 5  |  platform yang bervariasi.  |  platform", "relevansi iklan yang
(-, ,Lë ): dikumpulkan"
Pertanyaan  |  Seberapa baik rekan Anda dalam  |  -
Kualitatif: mengumpulkan iklan lowongan kerja
dari platform yang ditugaskan? (Nilai
dari skala 1-5)
Pertanyaan  |  Mengapa?  |  "kesulitan dalam pengumpulan
Kuantitatif  |  (Berikan contoh spesifik kontribusi  |  data", "kemudahan dalam
rekan Anda dalam pengumpulan data.: pengumpulam data"
Apakah rekan Anda menghadapi
kesulitan dalam mengumpulkan iklan)

**D. Koherensi Feature-Set**

Untuk mengukur koherensi antara narasi dengan skor yang diberikan, sistem harus mengekstrak deskripsi performa spesifik (-, ,L<sup>à</sup> ) menjadi unit-unit kriteria evaluasi yang lebih atomik. Proses ini dilakukan secara manual untuk setiap tingkat skor (<sup>V</sup> ∈ 1), menghasilkan notasi pada rumus [III.17](#page-4-1).

$$COH(K_{i,j,s_k}) = \{ c_{coh,1}, c_{coh,2}, \dots, c_{coh,q} \}$$
 (III.17)

Di mana setiap 2èWí,î merupakan unit teks yang telah didekomposisi untuk kriteria ke-j, aspek ke- untuk skor ke-f.

[Tabel III.9](#page-4-2) menyajikan contoh proses dekomposisi dengan menggunakan rubrik pada Tabel II.1, pada aspek "Pengumpulan iklan lowongan kerja" (I@), dengan pasangan kriteria rubrik "Banyaknya iklan dan keragaman platform yang digunakan" (-@,@).

Tabel III.9. Contoh Proses Dekomposisi untuk Koherensi Skor dan Narasi

Skala Skor: Dekomposisi
Skor 1 (Sangat Kurang): åçé-@,@,Lâ ! =
?"58 Ç}Ç;f:8 5fÅ f;:8"C
Skor 3 (Cukup): åçé-@,@,Lê ! =
?"58 Ç}Ç;f:8 2ÇfÇ} f;:8"C
Skor 5 (Sangat Baik): åçé-@,@,Lë ! =
?"58 Ç}Ç;f:8 h:8i:f f;:8",
"f;:8 45;5:8",
"};:Å34 h54:4:"C

Seluruh unit dekomposisi kemudian digabungkan menjadi satu himpunan besar, sebagaimana direpresentasikan pada rumus [III.18.](#page-5-0)

$$\mathcal{U}(K_{i,j}) = \bigcup_{s_k \in S} COH(K_{i,j,s_k})$$
 (III.18)

Sehingga ñ-, berisi: "iklan relevan", "platform bervariasi", "mengumpulkan banyak iklan", "mengumpulkan cukup iklan", dan "mengumpulkan sedikit iklan".

Namun, karena satu kriteria penilaian sering kali mengandung beberapa dimensi evaluasi yang berbeda, unit dekomposisi ini diklasifikasikan ke dalam himpunan (ô<sup>F</sup> yang bersifat mutually exclusive, direpresentasikan pada rumus [III.19](#page-5-1).

$$COH(K_{i,j}) = \{G_1, G_2, ..., G_m\}$$
 (III.19)

Di mana ôF merupakan himpunan untuk memartisi unit kriteria yang lebih atomik yang bersaing dalam satu dimensi yang sama. Anggota di dalam himpunan bersifat mutually exclusive, sehingga tidak mungkin sebuah narasi secara logis memenuhi lebih dari satu unit dalam himpunan yang sama secara bersamaan. Sebaliknya, unit dari himpunan yang berbeda bersifat independen. Contoh himpunan disajikan pada [Tabel III.10](#page-5-2).

Tabel III.10. Contoh Himpunan Koherensi Feature Set

Himpuna  |  Unit  |  Irisa  |  Unit Irisan Skor
n: n
Skor
G@  |  ?"58 Ç}Ç;f:8 5fÅ f;:8",  |  Skala  |  ?"58 Ç}Ç;f:8 5fÅ f;:8"C
"58 Ç}Ç;f:8 2ÇfÇ} f;:8", ... 1
"58 Ç}Ç;f:8 h:8i:f f;:8"C  |  Skala  |  ?"58 Ç}Ç;f:8 2ÇfÇ} f;:8"C
3
Skala: ?"58 Ç}Ç;f:8 h:8i:f f;:8"C
5
ôA  |  ?"f;:8 45;5:8"C  |  Skala  |  ?"f;:8 95;5:8"C
5
ô`  |  ?"};:Å34 h54:4:"C  |  Skala  |  ?};:Å34 h54:4:C
5

Berdasarkan [Tabel III.10](#page-5-2), ô@ merupakan grup yang mengevaluasi dimensi kriteria jumlah iklan, ôA mengevaluasi dimensi relevansi iklan, sementara ô` mengevaluasi keberagaman platform. Sifat mutual exclusive berlaku untuk setiap himpunan, narasi yang mendeskripsikan "mengumpulkan sedikit iklan" sekaligus "iklan yang dikumpulkan relevan" secara adalah kondisi yang valid, sehingga kedua unit tersebut dapat bernilai "TRUE" dalam hasil anotasi. Constraint tersebut dinotasikan dalam rumus [III.20.](#page-6-0)

$$\left| COH(K_{i,j,s_k}) \cap G_v \right| = 1, \forall G_v \in COH(K_{i,j}) \, \forall s_k \in S$$
 (III.20)

Di mana constraint ini menjaga bahwa setiap himpunan ô% hanya dapat memberikan tepat satu anggota kepada himpunan åçé-, ,L<sup>à</sup> !. Elemen dalam ô% yang berkorespondensi dengan tingkat skor f dinotasikan sebagai |%,V, sebagaimana disajikan pada rumus [III.21](#page-6-1).

$$g_{v,k} = G_v \cap COH(K_{i,j,s_k}), g_{v,k} \in G_v$$
 (III.21)

Berdasarkan constraint pada rumus [III.20,](#page-6-0) irisan ini menghasilkan tepat satu elemen, sehingga |%,V terdefinisi dengan baik.

Selain sifat mutual exclusive, setiap unit hanya dapat berada dalam satu anggota himpunan ôF, sehingga setiap himpunan merepresentasikan dimensi evaluatif yang independen, sebagaimana direpresentasikan pada rumus [III.22](#page-6-2).

$$G_m \cap G_{m'} = \emptyset \ \forall G_m, G_{m'} \in COH(K_{i,j}), m \neq m'$$
 (III.22)

Di mana ôF dan ôFü adalah dua himpunan yang berbeda dalam åçé-, .

Untuk mengilustrasikan proses dekomposisi feature set ini, [Gambar III.11](#page-7-0) menyajikan alur dekomposisi untuk koherensi skor berdasarkan rubrik historis yang telah didefinisikan pada Tabel II.1.

Gambar III.11 Alur Dekomposisi dan Pengelompokan Mutual Exclusive

**E. Pembuatan Panduan Anotasi**

Setiap baris data yang dianotasi merepresentasikan satu pasangan antara narasi feedback dan satu aspek rubrik tertentu. Skema ini mengadopsi multi-label binary classification yang telah dibahas pada subbab II.1.6, di mana anotator memberikan label TRUE atau FALSE untuk setiap kriteria berdasarkan aspek yang sedang dievaluasi. Label TRUE diberikan apabila narasi secara eksplisit membahas atau mengindikasikan pemenuhan kriteria pada aspek target tersebut, sedangkan label FALSE diberikan apabila aspek tersebut tidak dibahas dalam narasi feedback. Dalam kerangka ini, coverage dievaluasi secara lokal pada masing-masing aspek rubrik, sehingga hanya menilai apakah aspek spesifik yang menjadi target muncul dalam narasi. [Gambar III.12](#page-8-0) menyajikan alur anotasi dataset untuk cakupan rubrik.

Gambar III.12. Alur Anotasi Dataset Cakupan Rubrik

Relevansi memiliki fungsi yang berbeda dari cakupan. Jika narasi membahas aspek rubrik lain di luar aspek target, maka aspek target tetap diberi label FALSE untuk cakupan, tetapi kondisi tersebut juga menandakan deviasi relevansi secara global karena perhatian mahasiswa bergeser ke dimensi evaluasi yang tidak sedang dinilai. Alur anotasi disajikan pada [Gambar III.13](#page-9-0). Dengan demikian, cakupan mengukur keberadaan konten yang sesuai pada aspek spesifik, sementara relevansi mengevaluasi kesesuaian fokus narasi terhadap ruang lingkup pertanyaan atau aspek yang seharusnya dibahas. Distingsi ini memungkinkan sistem membedakan antara ketiadaan informasi, kekurangan fokus, dan penyimpangan topik secara lebih presisi.

Gambar III.13. Alur Anotasi Dataset Relevansi Topik

Untuk indikator koherensi skor, di mana hanya satu skala dapat bernilai TRUE dalam satu kelompok rubrik guna mempertahankan sifat ordinal skor, dengan visualisasi alur anotasi dataset yang disajikan pada [Gambar III.14](#page-10-0). Skema anotasi biner ini dipilih dibandingkan rating skala Likert karena tujuan utama pipeline adalah menghasilkan keputusan deterministik per indikator. Oleh karena itu, format ground truth harus selaras secara struktural dengan output prediksi agar evaluasi metrik tetap langsung, konsisten, dan mudah diinterpretasikan.

Gambar III.14. Alur Anotasi Dataset Koherensi Skor dan Narasi

**F. Proses Anotasi**

Anotasi dilakukan oleh dua anotator yang merupakan peneliti dengan pemahaman komprehensif mengenai struktur rubrik PjBL dan definisi operasional indikator tekstual narasi feedback. Proses anotasi dilakukan secara kolaboratif, kedua anotator bekerja bersama dalam saru sesi untuk mengevaluasi dan mendiskusikan setiap baris data.

Selama proses kolaboratif tersebut, panduan anotasi formal memuat definisi operasional setiap label, aturan penanganan kasus ambigu, daftar kata yang berpotensi menimbulkan ambiguitas penilaian, dan contoh berlabel untuk setiap aspek rubrik digunakan sebagai acuan mutlak.

Mengingat proses pelabelan bersifat kolaboratif dan sling membantu, setiap perbedaan interpretasi diselesaikan secara langsung melalui diskusi. Sebagai contoh disagreement, ketika menghadapi narasi "Rekan saya sangat rajin membantu tugas kelompok", satu anotator mungkin menganggap ini memenuhi kriteria rubrik "Kemampuan bekerja sama dengan anggota kelompok lain.", satu anotator

mungkin menganggapnya terlalu umum. Penyelesaian dilakukan dengan merujuk kembali pada aturan di panduan anotasi. Apabila diskusi kolaboratif menemui jalan buntu pada kasus yang sangat ambigu, data tersebut ditandai untuk diputuskan pada tahap validasi. Alur proses anotasi disajikan pada [Gambar III.15.](#page-11-0)

Gambar III.15. Alur Anotasi Dataset oleh Annotator

**G. Validasi Anotasi**

Tahap terakhir dari proses anotasi adalah validasi konfirmatif oleh dosen pengampu PjBL selaku domain expert. Sampel acak dari data yang telah dianotasi diserahkan kepada dosen untuk dievaluasi. Dosen exepertise memberikan penilaian akhir mengenai apakah label hasil konsensus kedua anotator telah merepresentasikan sesuai yang diharapkan. Selain itu, dosen juga memberikan keputusan final terhadap narasi edge-case yang sebelumnya tidak dapat disepakati oleh anotator.

Hasil validasi dari dosen inilah yang kemudian mengunci status dataset dan menetapkannya menjadi ground truth final untuk eksperimen pemodelan. Proses ini memastikan bahwa seluruh label anotasi yang dijadikan ground truth konsisten secara logis dan valid serta dapat dipertanggungjawabkan secara pedagogis menurut standar evaluasi dosen. Alur validasi anotasi dataset disajikan pada [Gambar III.16.](#page-11-1)

Gambar III.16. Alur Validasi Dataset

**III.6.3.2 Evaluasi dan Kalibrasi Model NLP**

Tahap ini merancang dan menguji pipeline NLP untuk mendeteksi setiap indikator secara matematis, dengan alur pemetaan yang disajikan pada [Gambar III.17](#page-12-0). Pipeline yang dirancang menggunakan representasi vektor dari model pre-trained berbasis arsitektur Transformer yang telah dijelaskan pada subbab II.1.7. Representasi ini sepenuhnya bergantung pada model yang dipilih, di mana model yang dilatih pada korpus multilingual akan menghasilkan representasi yang berbeda secara fundamental dibandingkan model multilingual atau bahasa Indonesia. Demikian pula, threshold (KLF,) harus dikalibrasi secara empiris terhadap data ground truth.

Gambar III.17. Pemetaan Eksperimen dan Kalibrasi Model

Kandidat model dipilih berdasarkan dua acuan literatur, yaitu studi NLP multilingual pada bahasa dengan resource parameter model yang terbatas, dan benchmark seperti IndoNLU (Wilie et al., 2020) serta MMTEB (Enevoldsen et al., 2025). Setiap kandidat dievaluasi menggunakan dataset yang telah dianotasi sebagai hasil dari proses pada subbab III.6.3.1. Proses evaluasi menghitung cosine  similarity dilakukan pada indikator cakupan rubrik (@), koherensi skor (A), dan relevansi topik (J) untuk setiap pasangan narasi-kriteria, kemudian hasil prediksi dibandingkan terhadap label ground truth. Metrik utama yang digunakan untuk membandingkan performa antar model adalah F1-Score pada setiap indikator. Output dari tahapan ini adalah konfigurasi model NLP terbaik beserta nilai threshold optimalnya (KLF,).

Untuk menentukan nilai threshold optimal (KLF,) pada indikator @, A, dan J, pengujian dilakukan secara sistematis menggunakan metode grid search. Proses grid-search ini mengeksplorasi rentang nilai similarity secara menyeluruh dari nilai 0,00 hingga 1,00 dengan akurasi interval sebesar 0,01. Sistem mengevaluasi performa prediksi model pada setiap titik interval tersebut, lalu mengisolasi nilai threshold yang menghasilkan metrik F1-Score tertinggi terhadap ground truth. Kombinasi antara parameter model dengan skor tertinggi dan threshold hasil pengujian iteratif ini ditetapkan sebagai konfigurasi akhir. Output dari tahapan ini adalah konfigurasi model NLP terbaik beserta nilai threshold optimalnya (KLF,).

Proses pencarian konfigurasi terbaik ini dieksekusi melalui tiga skenario evaluasi komparatif, yaitu: (1) eksperimen whole-text embedding untuk mengukur performa baseline model dalam memproses teks narasi secara utuh terhadap feature-set rubrik, (2) eksperimen semantic chunking untuk mengukur dampak segmentasi narasi menjadi unit-unit kalimat independen terhadap akurasi deteksi, dan (3) evaluasi aturan mutually exclusive untuk mengukur efektivitas penerapan batasan deterministik pada feature-set koherensi skor-narasi (A) untuk mempersempit ruang prediksi model terhadap gradasi skor yang berdekatan.

Seluruh rangkaian pengujian komparatif antar-model, pengujian teknik pemrosesan teks, serta penentuan threshold optimal melalui grid-search ini diposisikan sebagai skenario eksperimen utama untuk menjawab RQ 1. Evaluasi kuantitatif ini digunakan untuk membuktikan sejauh mana pipeline digital scaffolding yang dirancang memiliki akurasi dan keandalan dalam mendeteksi manifestasi keempat indikator tekstual pada dokumen narasi feedback.

Berbeda dari ketiga indikator lainnya yang dikalibrasi menggunakan cosine similarity terhadap data anotasi, indikator kedalaman elaborasi (`) dikalibrasi secara langsung dari distribusi statistik data historis. Analisis distribusi jumlah kata leksikal dilakukan untuk mengidentifikasi titik infleksi distribusi, yaitu batas di mana frekuensi narasi bertransisi dari zona kluster padat ke distribusi yang jarang. Titik tersebut ditetapkan sebagai threshold (KLF,`).

**III.6.4 Formulasi Pendekatan Scaffolding**

Tahapan ini berfokus pada transformasi konstruk pedagogis abstrak menjadi sistem komputasional yang terukur, operasional, dan dapat dievaluasi secara empiris. Langkah dari tahapan ini adalah perumusan logika inferensi pada subbab [III.6.4.1](#page-14-0), dan perancangan teks dan template scaffolding pada subbab III.6.4.2.

**III.6.4.1 Perumusan Logika Inferensi**

Tahap ini merumuskan logika inferensi deterministik yang menerjemahkan output prediksi komputasional dari NLP menjadi keputusan intervensi pedagogis. Pendekatan rule based digunakan untuk memetakan kombinasi biner kondisi feedback liteacy yang spesifik.

Karena sistem mengevaluasi empat indikator tekstual narasi feedback, sistem mendefinisikan tepat 2 <sup>J</sup> = 16 kombinasi kondisi operasional. Output dari tahapan ini adalah rule-set yang memastikan setiap kombinasi indikator feedback literacy memiliki target pemetaan intervensi yang akurat serta struktural tanpa memerlukan mekanisme intervensi tambahan.

**III.6.4.2 Perancangan Teks dan Template Scaffolding**

Berdasarkan rule-set yang telah disusun, tahap ini merancang instrumen intervensi pedagogis berupa teks prompt scaffolding. Sistem menggunakan pendekatan template-based sebagaimana dijelaskan pada subbab II.1.13.

Teks disusun untuk memberikan panduan yang seragam, tetap relevan dengan kondisi feedback yang sedang dievaluasi, serta dapat menampilkan lebih dari satu arahan apabila terdapat beberapa indikator yang belum terpenuhi. Setiap template dirancang agar bersifat sugestif, yaitu mengarahkan mahasiswa untuk memperbaiki narasi feedback sebagai bentuk jawaban dari pertanyaan kualitatif dalam konteks self dan peer assessment di lingkungan PjBL. Output dari tahapan ini adalah himpunan template prompt yang siap diintergasikan dengan logika rule-based ke dalam sistem digital scaffolding.

**III.6.5 Pembuatan APE**

Tahap ini menguraikan bagaimana sistem digital scaffolding dikembangkan dan diintegrasikan ke dalam lingkungan aplikasi existing, yaitu SAPA (Self & Peer Assessment). Proses ini memodifikasi sistem yang berjalan agar dapat berfungsi sebagai instrumen eksperimen.

**III.6.5.1 Analisis Sistem Berjalan**

Langkah awal dilakukan dengan menganalisis arsitektur, database, dan antarmuka dari aplikasi SAPA yang telah berjalan. Analisis ini difokuskan pada identifikasi titik integrasi di mana modul NLP dan rule-based engine dapat disisipkan tanpa mengganggu fungsi utama aplikasi. Metode yang digunakan meliputi analisis requirements, source code review, basis data, class diagram, desain antarmuka dan pemetaan alur proses menggunakan BPMN.

**III.6.5.2 Perancangan dan Integrasi Komponen**

Setelah titik integrasi terpetakan, proses dilanjutkan dengan merancang arsitektur software yang menggabungkan pipeline NLP backend dengan aplikasi frontend

SAPA. Perancangan ini didokumentasikan menggunakan UML seperti use case diagram, class digram, dan sequence diagram untuk mendeskripsikan interaksi antara pengguna, sistem SAPA, dan digital scaffolding service.

**III.6.5.3 Pengujian Sistem**

Sebelum digunakan dalam eksperimen, APE yang telah diintegrasi diuji secara internal.. Pengujian fungsional sistem dilakukan menggunakan pendekatan blackbox testing. Perancangan skenario pengujian ini menerapkan teknik Equivalence Partitioning dan Boundary Value Analysis untuk memetakan setiap kemungkinan input teks dan transisi antarmuka secara sistematis. Rangkaian test case dari hasil perancangan tersebut dieksekusi untuk memastikan bahwa conditional prompt muncul ketika narasi yang ditulis mahasiswa tidak memenuhi indikator feedback literacy dan menghilang saat kriteria telah terpenuhi. Pengujian non-functional juga diterapkan untuk memverifikasi latensi pemrosesan NLP agar respons sistem tetap real-time dan tidak mengganggu pengalaman pengguna dalam menulis feedback

**III.6.5.4 Perbaikan Aplikasi Pendukung Eksperimen (APE)**

Tahap ini merupakan tindak lanjut dari temuan yang diperoleh setelah pelaksanaan eksperimen berdasarkan masukan pengguna untuk memperbaiki beberapa aspek pengalaman yang teridentifikasi selama sesi assessment.

Perubahan yang dilakukan dibatasi pada aspek antarmuka dan mekanisme interaksi pengguna, perubahan tersebut tidak mengubah model NLP, aturan deteksi, threshold, maupun mekanisme pengambilan keputusan yang digunakan dalam evaluasi penelitian.

Seluruh data eksperimen yang digunakan untuk menjawab pertanyaan penelitian tetap berasal dari versi sistem yang digunakan selama pelaksanaan eksperimen. Oleh karena itu, revisi APE dilakukan sebagai tindak lanjut hasil evaluasi pengguna dan tidak memengaruhi hasil analisis yang dilaporkan pada penelitian ini.

Luaran tahap ini adalah versi APE yang telah direvisi berdasarkan temuan penggunaan pada eksperimen dan disiapkan sebagai dasar pengembangan lanjutan.

**III.6.6 Perancangan Skenario Eksperimen**

Tahap ini bertujuan untuk menetapkan seluruh parameter eksperimen sebelum data eksperimental dikumpulkan, mencakup penentuan subjek, alur interaksi, prosedur statistik dan kriteria interpretasi hasil. Secara umum rancangan skenario eksperimen dapat dilihat pada [Gambar III.18.](#page-3-0)

Penjelasan detail mengenai masing-masing komponen skenario eksperimen tersebut dijabarkan secara terstruktur pada subbab [III.6.6.1](#page-4-0) hingga subbab [III.6.6.3](#page-11-0).

Gambar III.18 Rancangan Eksperimen

**III.6.6.1 Pre-Eksperimen**

Subbab ini membahas aktivitas persiapan lingkungan eksperimen, termasuk subjek eksperimen, rubrik yang digunakan, serta pembuatan kuesioner. Sesuai dengan karakteristik randomized posttest-only control group design yang telah dijelaskan pada II.1.14, penelitian ini tidak menggunakan pre-test pada kelompok treatment  maupun kontrol.

**A. Penentuan Subjek Eksperimen**

Subjek eksperimen adalah mahasiswa JTK POLBAN yang sedang menjalani mata kuliah PjBL pada semester pelaksanaan penelitian. Penentuan subjek mengikuti prosedur yang digambarkan pada [Gambar III.19](#page-6-0), dengan rincian:

1. Kriteria Inklusi, yaitu mahasiswa aktif yang terdaftar dalam satu mata kuliah yang menerapkan PjBL dan bersedia berpartisipasi secara sukarela tanpa konsekuensi nilai akademik.
2. Random Assignment. Mahasiswa yang memenuhi kriteria didaftarkan ke dalam kelompok treatment dan kontrol, sebagaimana didefinisikan pada subbab II.1.14. Penentuan kelompok dilakukan secara acak menggunakan random assignment pada level individu untuk menghindari clustering effect. Proses random assignment dilakukan dengan menghasilkan nilai acak untuk setiap partisipan menggunakan fungsi randomisasi pada aplikasi Spreadsheet, sehingga setiap subjek memiliki probabilitas yang asma untuk masuk ke dalam kelompok treatment atau kontrol. Partisipan dialokasikan secara proporsional ke dalam kelompok treatment dan kontrol sehingga jumlah partisipan pada kedua kelompok tetap seimbang.
3. Ukuran Sampel. Eksperimen ini diposisikan sebagai pilot study dengan target minimal n ≈ 10 per kelompok. Ukuran ini belum memenuhi syarat untuk analisis konfirmatif, namun cukup untuk menghasilkan estimasi effect size awal yang dapat digunakan sebagai masukan dalam perencanaan penelitian. Hal ini didukung oleh Hertzog (2008) yang menyatakan bahwa sampel 10 hingga 20 partisipan per kelompok sudah memadai untuk mengevaluasi parameter feasibility dan mengestimasi varian awal. Selain itu, Julious (2005)

merekomendasikan 12 subjek per kelompok sebagai rule of thumb untuk pilot study. Menyadari keterbatasan populasi dan risiko statictical power yang rendah, hasil ekspermen diposisikan sebagai bukti awal yang berfokus pada effect size serta pola temuan yang muncul dibandingkan dipandang sebagai pengujian konfirmatif.

Eksperimen dilaksanakan pada mata kuliah Manajemen Kualitas Terpadu yang merupakan mata kuliah pada semester delapan di program Sarjana Terapan Teknik Informatika, Politeknik Negeri Bandung yang sedang diikuti oleh mahasiswa angkatan 2022. Berbeda dengan data historis yang digunakan pada tahap pengembangan pipeline dan berasal dari mata kuliah Proyek 1: Pemanfaatan Aplikasi Perkantoran, konteks eksperimen pada penelitian ini menggunakan aktivitas Project Based Learning (PjBL) dalam bentuk proyek penerapan kerangka kerja manajemen kualitas, seperti ISO 9001, ITIL v4, dan COBIT. Mahasiswa bekerja dalam kelompok yang terdiri atas 5-6 orang untuk menyelesaikan studi kasus berbasis role-play serta menyusun laporan proyek sebagai luaran pembelajaran.

Pemilihan konteks ini didasarkan pada kesamaan karakteristik pedagogis dengan lingkungan PjBL yang digunakan pada tahap pengembangan, yaitu adanya kolaborasi tim, pembagian peran, serta penerapan mekanisme self assessment dan peer assessment sebagai sarana evaluasi kontribusi anggota kelompok. Sehingga meskipun domain proyek yang digunakan berbeda, aktivitas evaluatif yang menjadi target bantuan digital scaffolding tetap dipertahankan.

Gambar III.19. Alur Penentuan dan Pengacakan Subjek Eksperimen

**B. Pembuatan Kuesioner**

Kuesioner dirancang sebagai instrumen evaluasi eksplanatori dengan pendekatan metode campuran untuk melengkapi data kuantitatif dari hasil pengujian statistik. Data kuesioner berfungsi untuk memvalidasi penerimaan intervensi secara psikologis dan operasional oleh pengguna. Skala pengukuran kuantitatif diseragamkan menggunakan skala Likert 5 poin, dengan nilai 1 merepresentasikan "Tidak Setuju", sedangkan nilai 5 merepresentasikan "Setuju" untuk menjaga konsistensi komputasi data. Instrumen dirancang eksklusif untuk kelompok treatment.

Kuesioner difokuskan pada evaluasi pengalaman interaksi mahasiswa terhadap fitur prompt scaffolding. Penyusunan instrumen ini diadaptasi dari dua kerangka teoritism, yaitu:

1. Evaluasi technology acceptance model (Davis, 1989) untuk mengukur secara spesifik perceived ease of use dari prompt yang muncul guna mengetahui sejauh mana panduan tersebut membantu mahasiswa dalam memperbaiki narasi feedback.
2. Evaluasi cognitive load theory (Mestre & Ross, 2011) untuk mengukur apakah kemunculan teks prompt scaffolding berhasil memandu pemikiran mahasiswa (Intrinsic Load) atau menambah beban visual yang tidak perlu (Extraneous Load).

Pemilihan ketiga kerangka evaluasi tersebut didasarkan pada karakteristik pilot study yang berfokus pada persepsi specific task utilization, serta memiliki relevansi langsung dengan kerangka pedagogis ZPD yang dijelaskan pada subbab II.1.10. Kuesioner ini juga memuat open-ended questions untuk menggali opini mahasiswa mengenai akurasi deteksi sistem.

**C. Pembuatan Rubrik**

Instrumen rubrik yang diterapkan dalam tahap eksperimen tidak menggunakan rubrik spesifik proyek pada Tabel II.1. Hal ini dilakukan untuk mengeliminasi bias kompleksitas tugas teknik antar kelompok mahasiswa.

Untuk menjamin validitas instrumen pengujian secara akademis, penelitian ini mengadopsi dan mengadaptasi rubrik standar internasional CATME (Comprehensive Assessment of Team Member Effectiveness) yang dikembangkan khusus untuk peer assessment mahasiswa pada pendidikan tinggi (Ohland et al., 2012). Kerangka instrumen ini dipilih karena secara empiris dirancang berdasarkan taksonomi efektivitas tim yang valid untuk lingkungan kolaboratif mahasiswa.

Berdasarkan struktur aslinya, CATME memuat lima dimensi evaluasi. Namun, untuk mempertahankan netralisasi instrumen terhadap domain teknis proyek, penelitian ini secara terukur mengeliminasi dimensi keterampilan teknis, yaitu knowledge, skill, serta abilities sehingga kriteria rubrik meliputi:

1. Kontribusi terhadap pekerjaan tim untuk menilai dedikasi, alokasi waktu, dan penyelesaian bagian tugas secara mandiri.
2. Interaksi dengan rekan tim untuk menilai kemampuan komunikasi, penyampaian ide, dan penerimaan feedback secara konstruktif.
3. Menjaga fokus dan dinamika tim untuk menilai kesadaran terhadap kemajuan tim dan kemampuan memberikan feedback perbaikan kepada sesama rekan.
4. Komitmen terhadap kualitas untuk menilai tingkat motivasi, ketelitian, dan usaha mahasiswa dalam menghasilkan yang terbaik.

Merujuk pada prinsip perancangan rubrik formatif dari Brookhart (2013), keempat kriteria CATME tersebut diimplementasi menggunakan model Behavioral Anchored Rating Scale (BARS). Dalam implementasinya, model BARS pada CATME menetapkan deskriptor perilaku tekstual yang eksplisit pada anchor skala 1, skala 3, dan skala 5, sedangkan skala 2 dan 4 tidak memiliki behavioral anchors, tetapi digunakan sebagai pilihan bagi siswa untuk memberikan skor di antara skala yang diberikan, sebagaimana diilustrasikan pada [Tabel III.11.](#page-8-0)

Tabel III.11. Contoh Implementasi BARS pada Rubrik CATME

Skala 1  |  Skala 2  |  Skala 3  |  Skala 4  |  Skala 5
Tidak menyelesaikan  |  -  |  Menyelesaikan bagian  |  -  |  Melakukan lebih
tugas yang diberikan  |  tugas yang diberikan  |  banyak dari tugas yang
atau menyerahkan  |  dengan kualitas yang  |  diberikan dengan
pekerjaan dengan  |  memadai dan tepat  |  kualitas melebihi
kualitas buruk. Sering  |  waktu. Berkontribusi  |  ekspektasi. Mengambil
terlambat atau tidak  |  proporsional.  |  inisiatif mengisi
berkontribusi.: kekosongan peran.

**III.6.6.2 Eksperimen**

Subbab ini membahas kegiatan yang dilakukan selama dilaksanakannya alur eksperimen yang mencakup pembuatan instruksi, pengisian self dan peer assessment, serta kuesioner. Fase dieksekusi secara independen sebelum interaksi subjek dimulai.

**A. Pemberian Instruksi**

Tahapan ini bertujuan untuk memberikan instruksi yang seragam kepada kedua kelompok, meliputi penyampaian konteks penelitian, prosedur pengerjaan assessment, serta protokol keamanan data terkait jawaban assessment dan respons kuesioner yang diberikan subjek eksperimen. Dalam pelaksanaan assessment, subjek eksperimen diminta menyusun narasi feedback berdasarkan pengalaman mereka pada proyek yang sedang dikerjakan dalam mata kuliah berbasis yang menerapkan PjBL. Dengan demikian, narasi yang dihasilkan merepresentasikan evaluasi terhadap aktivitas proyek yang benar-benar dialami selama proses pembelajaran. Penyampaian instruksi dilakukan tanpa mengungkapkan keberadaan modul scaffolding guna meminimalkan potensi bias selama eksperimen.

Kedua kelompok eksperimen melaksanakan sesi pengisian assessment secara serentak pada periode waktu dan lingkungan kelas yang sama. Pengaturan ini dilakukan untuk memastikan kelompok treatment dan kontrol mengalami kondisi eksternal yang setara selama proses pengisian assessment, sehingga potensi pengaruh faktor eksternal di luar konteks eksperimen terhadap hasil pengukuran dapat diminimalkan.

Untuk memperjelas perbedaan perlakuan antar kelompok, berikut adalah alur yang diterapkan dalam eksperimen ini:

1. Kelompok treatment menerima bantuan scaffolding secara real-time selama proses penulisan narasi feedback berlangsung, setiap kali terjadi pelanggaran indikator, sistem menampilkan prompt panduan berbasis template.
2. Kelompok kontrol tidak menerima scaffolding apapun selama proses penulisan, subjek menyelesaikan seluruh assessment tanpa intervensi sistem.
3. Setelah seluruh jawaban dari kedua kelompok dikirimkan, jawaban tersebut dianalisis menggunakan pipeline digital scaffolding yang sama untuk menghasilkan skor pemenuhan keempat indikator tekstual narasi feedback pada setiap baris pertanyaan assessment.

4. Hasil analisis inilah yang digunakan sebagai data perbandingan antar kelompok treatment dan kontrol.

**B. Operasionalisasi untuk Kelompok Kontrol**

Subjek eksperimen kelompok kontrol dihadapkan antarmuka asessment SAPA tanpa scaffolding. Subjek mengisi assessment dengan modalitas skor kuantitatif dan narasi kualitatif. Subjek eksperimen menyelesaikan seluruh assessment tanpa intervensi scaffolding, sehingga merepresentasikan kondisi penulisan feedback tanpa intervensi scaffolding.

Meskipun kelompok kontrol tidak menerima scaffolding, setiap jawaban dari pertanyaan assessment yang dikirimkan tetap dianalisis menggunakan pipeline digital scaffolding yang sama dengan yang digunakan oleh kelompok treatment. Analisis ini dilakukan untuk memperoleh tingkat pemenuhan keempat indikator tekstual narasi feedback. Hasil analisis tersebut berupa data tingkat pemenuhan pada keempat indikator tekstual narasi feedback dan digunakan sebagai data pengukuran pada kelompok kontrol untuk keperluan perbandingan dengan kelompok treatment yang mendapatkan bantuan digital scaffolding pada proses penulisan.

**C. Operasionalisasi untuk Kelompok Treatement**

Subjek eksperimen kelompok treatment dihadapkan antarmuka assessment SAPA dengan intervensi scaffolding. Kelompok treatment mendapatkan antarmuka SAPA yang identik, di mana perbedaan terletak pada scaffolding yang muncul ketika terjadi pelanggaran terhadap keempat indikator tekstual narasi feedback. Selama proses penyusunan narasi feedback, sistem secara otomatis melakukan evaluasi terhadap keempat indikator tekstual pada setiap perubahan jawaban. Ketika terdeteksi indikator yang belum terpenuhi, sistem menghasilkan scaffolding berbasis template untuk membantu mahasiswa melakukan revisi narasi.

Pada kelompok treatment, sesuai yang dijelaskan pada subbab III.3.2, selain menyimpan hasil akhir dari setiap jawaban assessment, sistem menyimpan data setiap perubahan yang dilakukan oleh mahasiswa. Perubahan dalam konteks ini yaitu, setiap jawaban yang diproses oleh digital scaffolding direkam, sehingga memungkinkannya menangkap proses interaksi mahasiswa dengan teks scaffolding  yang diberikan.

**D. Terminasi Eksperimen**

Setelah waktu yang diberikan selesai, subjek eksperimen diberikan kuesioner yang telah dirancang pada tahapan [III.6.6.1B](#page-6-1) melalui platform Google Form kepada kelompok treatment untuk merekam pengalaman menggunakan aplikasi SAPA.

**III.6.6.3 Pasca Eksperimen**

Setelah eksperimen selesai, dilakukan ekstraksi data hasil eksperimen yang selanjutnya dilanjutkan dengan pengolahan data untuk penarikan kesimpulan.

**A. Ekstraksi Data Hasil Eksperimen**

Tahap ini bertujuan untuk mengumpulkan dan mengagregasi seluruh data yang dihasilkan selama pelaksanaan eksperimen dari kelompok treatment maupun kelompok kontrol. Proses ekstraksi dilakukan langsung dari basis data SAPA dan log yang merekam seluruh interaksi pengguna selama sesi pengerjaan self assessment dan peer assessment.

Data yang diekstraksi terdiri atas dua kategori utama. Kategori pertama adalah data evaluasi hasil assessment yang tersedia untuk kedua kelompok eksperimen. Khusus untuk data kelompok kontrol di mana dalam kondisi tidak menerima scaffolding,  dilakukan langkah tambahan untuk mendapatkan tingkat pemenuhan keempat indikator tekstual narasi feedback yang dilakukan oleh peneliti untuk setiap baris pertanyaan assessment pada kelompok kontrol. Sehingga, baik kelompok treatment  maupun kontrol memiliki data pemenuhan keempat indikator tekstual narasi feedback.

Kategori kedua adalah data interaksi pengguna yang hanya tersedia pada kelompok treatment. Data ini berasal dari log aktivitas sistem yang merekam proses penggunaan digital scaffolding selama penulisan narasi feedback. Informasi yang diekstraksi meliputi waktu pengiriman narasi, status indikator sebelum dan sesudah revisi, jumlah revisi yang dilakukan, riwayat bantuan yang diberikan sistem, serta respons mahasiswa terhadap scaffolding yang muncul selama sesi penulisan.

**B. Pengolahan Data Evaluasi Hasil Eksperimen**

Sebagaimana didefinisikan pada subbab III.3.2.1, pengolahan data evaluasi bertujuan untuk mengetahui ukuran dan signifikansi perbedaan antara kelompok treatment dan kelompok kontrol. Pengolahan ini terdiri dari tiga tahapan, yaitu: (1) verifikasi asumsi, (2) pengujian multivariat, dan (3) pengujian univariat pada setiap indikator yang diikuti dengan perhitungan effect size untuk mengukur besaran perbedaan.

Khusus untuk data hasil eksperimen kelompok kontrol dilakukan terlebih dahulu pengukuran untuk setiap indikator tekstual narasi feedback. Pengukuran ini dilakukan untuk mendapatkan status pemenuhan terhadap setiap indikator berdasarkan skor dan narasi yang telah disubmit oleh mahasiswa dari kelompok kontrol.

Sebelum analisis utama dilaksanakan, verifikasi asumsi dilakukan untuk setiap indikator. Uji Shapiro-Wilk digunakan untuk memverifikasi normalitas distribusi setiap indikator pada kedua kelompok. Pemilihan uji ini didasarkan pada tingkat sensitivitasnya yang lebih tinggi terhadap ukuran sampel kecil dalam konteks pilot study. Selanjutnya, uji Levene digunakan untuk mengevaluasi homogenitas varians antar kelompok treatment dan kontrol. Hasil verifikasi asumsi dilaporkan sesuai dengan format pada [Tabel III.12.](#page-13-0)

Tabel III.12 Format Tabel Pelaporan Verifikasi Asumsi

Jenis Asssessment  |  Indikator  |  Normalitas Kelompok Treatement  |  Normalitas Kelompok Kontrol  |  Homogenitas
Self Assessment: (Cakupan) @
(Koherensi) A
(Elaborasi) `
(Relevansi) J
Peer Assessment: (Cakupan) @
(Koherensi) A
(Elaborasi) `
(Relevansi) J

Jika hasil uji mengonfirmasi normalitas per indikator pada setiap kelompok, yang ditunjukkan dengan nilai } > 0,05, analisis statistik dilanjutkan pada dua tingkat. Tingkat pertama adalah pengujian multivariat untuk mengevaluasi empat indikator yang didefinisikan pada Tabel III.3 sebagai satu konstruk komprehensif. Tingkat kedua adalah analisis follow-up univariat untuk melihat fenomena pada masingmasing indikator.

Tingkat pertama menggunakan Multivariate Analysis of Variance (MANOVA) untuk menguji efek intervensi terhadap vektor keempat indikator secara simultan, dengan format pelaporan pada [Tabel III.13.](#page-13-1) Penggunaan MANOVA diterapkan karena keempat indikator berkorelasi dalam konteks assessment yang sama. Analisis univariat terpisah tanpa koreksi akan mengabaikan interdependensi ini. Pillai's Trace digunakan sebagai effect size multivariat karena bersifat robust terhadap pelanggaran asumsi normalitas multivariat.

Tabel III.13. Format Pelaporan Uji Manova (Pillai's Trace)

Jenis  |  P-value  |  Pillai  |  Signifikan
Assessment  |  Value  |  (Ya/Tidak)

Jika MANOVA menghasilkan } < 0.05, terdapat efek multivariat yang signifikan dari intervensi terhadap keempat indikator secara keseluruhan. Analisa kemudian dilanjutkan ke tingkat indikator individu untuk mengidentifikasi indikator spesifik yang berkontribusi.

Sebaliknya, jika MANOVA menghasilkan } ≥ 0,05, tidak terdapat efek multivariat yang signifikan pada tingkat signifikansi yang ditetapkan. Karena penelitian ini diklasifikasikan sebagai pilot study dengan ukuran sampel ≈ 10 partisipan untuk setiap kelompok, hasil tidak signifikan ini tidak dapat langsung disimpulkan sebagai bukti ketiadaan efek, melainkan indikasi tidak cukupnya statistical power untuk mendeteksi efek yang ada. Atas dasar ini, analisis follow-up pada tingkat indikator tetap dilaksanakan dengan tujuan utama untuk mengestimasi effect size.

Secara keseluruhan, analisis statistik pada penelitian ini difokuskan pada outcome, yaitu tingkat pemenuhan indikator tekstual pada mahasiswa. Data interaksi yang terekam selama proses penyusunan narasi feedback tidak digunakan sebagai dasar pengujian hipotesis utama. Data tersebut difungsikan secara eksklusif sebagai sumber interpretasi tambahan untuk mendeskripsikan mekanisme kerja digital scaffolding.

Tingkat kedua adalah analisis follow-up yang dilaksanakan secara terpisah per indikator. Karena setiap indikator dapat memiliki status asumsi yang berbeda berdasarkan hasil tahap pertama dalam verifikasi asumsi, prosedur statistik yang digunakan per indikator ditentukan oleh kombinasi status normalitas dan homogenitas varians indikator tersebut. Alur pengambilan keputusan uji statistik ini divisualisasikan pada Gambar III.20.

Gambar III.20. Flowchart Keputusan Uji Statistik Per Indikator

Rincian lebih lanjut mengenai kriteria pengambilan keputusan, penentuan metrik effect size yang bersesuaian dengan setiap uji, serta justifikasi penggunaannya dirangkum pada [Tabel III.14](#page-0-0).

Tabel III.14 Tabel Interpretasi Keputusan Uji Asumsi

Hasil Uji  |  Hasil Uji  |  Keputusan Uji  |  Effect Size  |  Catatan
Normalitas  |  Homogenitas  |  yang Digunakan  |  yang Digunakan
Kedua kelompok normal } > 0.05  |  Homogen (} > 0.05)  |  Independent samples t test  |  Cohen's d  |  Kondisi parametrik penuh
Kedua kelompok normal } > 0.05  |  Tidak homogen (} ≤ 0.05)  |  Welch's T test  |  Cohen's d  |  Robust terhadap heterogenitas varians
Salah satu kelompok tidak normal } ≤ 0.05  |  Tidak dipertimbangkan  |  Mann Whitney U Test  |  Rank biserial correlation (r)  |  Alternatif non parametrik

Dengan demikian, dalam satu analisis follow-up, dimungkinkan bahwa sebagian indikator diuji menggunakan t-test atau Welch's t-test sementara indikator lain diuji menggunakan Mann-Whitney U.

Untuk mengontrol family-wise error rate akibat pengujian empat indikator secara paralel, digunakan prosedur Bonferroni correction. Dengan empat indikator, tingkat signifikansi yang disesuaikan adalah:

$$a_{adjusted} = \frac{0.05}{4} = 0.0125$$
 (III.23)

Interpretasi uji follow up per indikator dapat dilihat pada [Tabel III.15.](#page-2-0)

Cohen's d digunakan sebagai effect size per indikator untuk membedakan signifikansi statistik dari signifikansi praktis. Interpretasi nilai effect size merujuk pada Cohen (1988) dan Fiel Peres (2026), yang disajikan pada [Tabel III.16.](#page-2-1)

Setiap uji dan effect size yang digunakan dilaporkan pada tabel dalam format yang disajikan pada [Tabel III.17](#page-2-2).

Tabel III.15 Interpretasi Uji Follow Up Per Indikator

Jenis  |  Uji  |  Kriteria  |  Interpretasi
Parametrik  |  Independent t test/  |  $p < \alpha_{adjusted}$  |  Signifikan
Parametrik  |  Welch's t test  |  $p \geq \alpha_{adjusted}$  |  Tidak Signifikan
N D  |  n Parametrik Mann-Whitney U Test  |  $p < \alpha_{adjusted}$  |  Distribusi indikator berbeda signifikan
Non Parametrik  |  $p \geq \alpha_{adjusted}$  |  Tidak signifikan

Tabel III.16 Interpretasi Effect Size

Effect Size  |  Kriteria  |  Interpretasi
0.00 - 0.19: Trivial
Cohon's d (Dogometails)  |  d = 0.20  |  Small Effect
Cohen's d (Parametrik)_  |  d = 0.50  |  Medium
d = 0.80 or higher: Large
$r \ge 0.11$: Small
Rank Biserial Corelation (Non Parametrik)  |  $r \ge 0.28$  |  Medium
$r \ge 0.43$: Large

Tabel III.17. Format Pelaporan Uji Univariat dan Effect Size

Iı  |  ndikator  |  Uji yang digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect size (Cohen's d atau rank bisserinal correlation)

**C. Pengolahan Data Interaksi Kelompok Treatment**

Pengolahan data pada tahap ini memanfaatkan rekaman data interaksi yang dijelaskan pada subbab III.3.2.2. Data tersebut mencakup kondisi indikator, intervensi yang diberikan, serta perbaikan narasi pada setiap siklus penulisan feedback. Tujuan proses ini adalah mengevaluasi dinamika interaksi mahasiswa dengan instrumen scaffolding. Untuk mencapai tujuan tersebut, pengolahan data dibagi ke dalam lima tahapan analisis, yaitu: (1) Analisis distribusi kebutuhan, (2) evaluasi respons mahasiswa, (3) klasifikasi karakteristik revisi teks, (4) pemetaan pola revisi, dan (5) evaluasi resolusi akhir. Alur pengolahan data interaksi ini disajikan pada [Gambar III.21.](#page-3-0)

Gambar III.21. Flowchart Tahapan Pengolahan Data Interaksi

Tahap pertama mengukur distribusi pemenuhan dan persistensi indikator untuk memetakan frekuensi kemunculan scaffolding. Kebutuhan bantuan didefinisikan sebagai kondisi saat indikator tekstual berada pada status "membutuhkan intervensi" sebelum mahasiswa melakukan perbaikan/revisi terhadap narasi. Setiap kondisi ini dihitung sebagai satu kesempatan bagi sistem untuk memberikan scaffolding. Distribusi dihitung berdasarkan frekuensi kemunculan setiap indikator pada konteks self dan peer assessment untuk mengidentifikasi indikator yang paling sering memicu intervensi.

Tahap kedua mengevaluasi respons mahasiswa terhadap kebutuhan scaffolding yang muncul. Analisis ini menggunakan metrik implementation rate dan persitence rate yang merujuk pada konsep Nelson & Schunn (2008) serta Zhang et al. (2024). Implementation rate menghitung proporsi perbaikan yang berhasil memenuhi indikator dibandingkan dengan total kesempatan scaffolding yang dipicu. Perhitungan metrik ini dirumuskan dalam rumus [III.24](#page-4-0).

$$Implementation Rate = \frac{Implemented Opportunities}{Scaffolding Opportunities}$$
 (III.24)

Pada rumus tersebut, implemented opportunities adalah jumlah revisi mahasiswa yang berhasil mengubah status indikator menjadi terpenuhi. Scaffolding  opportunities adalah total kejadian indikator berada pada status "membutuhkan intervensi". Metrik pendampingnya adalah persisetence rate yang menghitung proporsi kebutuhan scaffolding yang tetap tidak terpenuhi meskipun intervensi telah diberikan. Perhitungan ini dirumuskan pada rumus [III.25](#page-4-1).

$$Persistence Rate = \frac{Persistence Opportunities}{Scaffolding Opportunities}$$
 (III.25)

Tahap ketiga menganalisis karakteristik perbaikan teks pada setiap revisi. Perubahan narasi dievaluasi dengan membandingkan teks sebelum dan setelah intervensi menggunakan metode Levenshtein Distance (Levenshtein, 1966). Metode ini mengklasifikasikan modifikasi teks ke dalam tiga jenis operasi yang disajikan pada [Tabel III.18](#page-4-2).

Tabel III.18 Karakteristik Perubahan pada Narasi Feedback

Jenis  |  Definisi  |  Contoh
Perubahan
Tanpa  |  Tidak mengubah narasi feedback setelah  |  -
Perubahan (No: menerima bantua scaffolding
Change

Jenis  |  Definisi  |  Contoh
Perubahan
Penambahan  |  Menambahkan satu karakter baru ke dalam  |  "bap" menjadi "bapak"
(Insertion)  |  teks yang salah agar menjadi kata yang  |  (menambahkan huruf 'k')
benar.
Penghapusan  |  Menghapus atau membuang satu karakter  |  "bapakk" menjadi "bapak"
(Deletion)  |  yang berlebih atau salah dari sebuah teks.  |  (menghapus satu huruf 'k')
Penggantian  |  Mengganti satu karakter yang salah pada  |  "bapok" menjadi "bapak"
(Substitution /  |  teks dengan satu karakter yang benar.  |  (mengganti huruf 'o' menjadi
Replacement): 'a')

Tahap keempat memetakan dampak setiap revisi terhadap tingkat pemenuhan indikator tekstual. Berdasarkan transisi status dari narasi pada kondisi awal hingga kondisi akhir, lintasan revisi mahasiswa diklasifikasikan ke dalam empat pola deskriptif. Rincian keempat pola revisi tersebut disajikan pada

Tabel III.19. Klasifikasi Pola Revisi

(Nelson & Schunn, 2008; Pea, 2004; Zhang et al., 2024)

Pola  |  Definisi  |  Interpretasi
Konsisten  |  Indikator terpenuhi sejak kondisi  |  Menunjukkan bahwa narasi telah memenuhi
Memenuhi  |  narasi awal hingga akhir tanpa  |  indikator sejak kondisi awal dan tidak
Indikator  |  memicu intervensi.  |  memicu intervensi.
Pemenuhan
Berhasil  |  Indikator bermasalah pada kondisi  |  Merepresentasikan keberhasilan
Memenuhi  |  narasi awal namun berhasil  |  implementasi scaffolding yang
Indikator  |  dipenuhi.  |  ditindaklanjuti mahasiswa ke dalam revisi.
Belum  |  Indikator memicu intervensi dan  |  Menunjukkan bahwa kebutuhan bantuan
Memenuhi  |  tetap bermasalah hingga kondisi  |  yang terdeteksi tidak terselesaikan hingga
Indikator  |  akhir narasi feedback.  |  versi akhir narasi.
Tidak  |  Status pemenuhan indikator  |  "Merefleksikan dinamika revisi narasi yang
Konsisten  |  berubah secara fluktuatif antara  |  belum menghasilkan kondisi pemenuhan
Pola  |  "terpenuhi" dan "tidak terpenuhi".  |  indikator secara stabil.
Lainnya

Tahap kelima mengevaluasi hasil kumulatif dari seluruh proses revisi untuk melihat apakah kebutuhan bantuan berhasil diselesaikan pada versi final narasi feedback. Pendekatan ini sejalan dengan konsep closing the feedback loop. Efektivitas intervensi dinilai dari kondisi akhir dokumen, tidak hanya mengukur ada atau tidaknya respons mahasiswa pada satu siklus tertentu. Suatu indikator dinyatakan berhasil diselesaikan apabila indikator tersebut pernah aktif memicu scaffolding pada salah satu tahap revisi, tetapi tidak lagi aktif pada versi final narasi feedback

mahasiswa. Sebaliknya, indikator yang tetap aktif hingga versi final dikategorikan sebagai kebutuhan bantuan yang belum terselesaikan.

**D. Pengolahan Data Kuesioner Evaluasi Pengguna**

Pengolahan data pada tahap ini memanfaatkan respons dari kuesioner pascaeksperimen yang diisi oleh subjek pada kelompok treatmet. Sesuai dengan pendekatan metode campuran eksplanatori yang ditetapkan pada subbab III.6.6.1B, pengolahan data kuesioner bertujuan untuk memvalidasi penerimaan intervensi secara operasional dan mengukur beban kognitif pengguna. Proses pengolahan data dibagi ke dalam tiga tahapan analisis berdasarkan jenis instrumen pertanyaan, yaitu: (1) analisis metrik penerimaan dan beban kognitif, (2) distribusi preferensi komponen, dan (3) analisis saran kualitatif.

Tahap pertama adalah mengolah data kuantitatif yang mengukur preceived usefullness dan tingkat extraneous cognitive load. Data bersumber dari instrumen skala Likert 5 poin, di mana skor 1 merepresentasikan "Sangat tidak setuju" dan skor 5 merepresentasikan "Sangat Setuju". Pengolahan dilakukan menggunakan statistik deskriptif dengan menghitung nilai rata-rata pada setiap metrik pertanyaan untuk menentukan tendensi sentral dari persepsi pengguna terhadap intervensi scaffolding.

Tahap kedua memetakan evaluasi pengguna teradap komponen antarmuka spesifik. Data bersumber dari instrumen checkboxes yang mengidentifikasi elemen sistem yang dirasa paling membantu dan elemen yang paling membutuhkan perbaikan. Data diolah dengan menghitung frekuensi pemilihan setiap komponen oleh responden, yang kemudian dikonversi menjadi persentase proporsi. Metrik ini digunakan untuk memetakan area antarmuka yang memiliki utilitas tertinggi serta mengisolasi fitur yang menjadi sumber gangguan visual.

Tahap ketiga menganalisis data kualitatif yang diperoleh dari open-ended responses. Teks evaluasi pengguna dioleh menggunakan analisis tematik untuk mengidentifikasi pola keluhan teknis atau kendala operasional selama penulisan narasi. Hasil ekstraksi tema kualitatif ini diposisikan sebagai fungsi eksplanatori untuk menjelaskan penyebab anomali atau tren dominan yang ditemukan pada data kuantitatif.

**E. Interpretasi Data Hasil Eksperimen**

Untuk menjawab RQ 2, hasil eksperimen diinterpretasikan menggunakan kombinasi analisis statistik pada metrik evaluasi dan analisis triangulasi pada kuesioner evaluasi pengguna. Analisis multivariat, analisis univariat, dan ukuran efek. Analisis multivariat menggunakan MANOVA digunakan untuk mengevaluasi apakah terdapat perbedaan profil keempat indikator tekstual secara simultan antara kelompok treatment dan kontrol. Selanjutnya, analisis univariat digunakan untuk mengidentifikasi indikator yang berkontribusi terhadap perbedaan tersebut. Selain signifikansi statistik, interpretasi juga mempertimbangkan ukuran efek sebagai dasar untuk menilai besarnya perbedaan yang diamati, mengingat penelitian ini merupakan pilot study dengan ukuran sampel yang terbatas. Pendekatan ini dipilih agar interpretasi hasil tidak bergantung pada satu ukuran statistik saja. Di sisi lain, interpretasi kuesioner digunakan untuk menjelaskan mekanisme operasional sistem, memvalidasi penerimaan fungsional, dan mengidentifikasi limitasi desain antarmuka berdasarkan tingkat beban kognitif yang dilaporkan pengguna.

**III.6.7 Penarikan Kesimpulan dan Perumusan Saran**

Tahap terakhir dalam penelitian ini adalah menarik kesimpulan dan merumuskan saran untuk penelitian lanjut, sebagai manifestasi dari proses "Analisis Hasil Eksperimen". Proses penarikan kesimpulan dilakukan secara deduktif dengan melakukan sintesis hasil analisis statistik hasil eksperimen untuk secara langsung menjawab RQ yang telah ditetapkan pada subbab I.3. Kesimpulan akan difokuskan pada interpretasi awal mengenai hubungan antara penggunaan digital scaffolding dan tingkat pemenuhan indikator tekstual feedback pada kelompok treatment dibandingkan kelompok kontrol.

Sementara itu, perumusan saran pengembangan lanjutan diformulasikan melalui identifikasi limitasi atau anomali komputasional yang ditemukan pada performa model NLP selama pengujian berlangsung. Saran dirumuskan untuk merekomendasikan perbaikan arsitektur atau parameter pada studi mendatang, sehingga murni berbasis pada batasan observasi sistem.

**BAB IV**

**HASIL PENGEMBANGAN APLIKASI PENDUKUNG EKSPERIMEN**

Bab ini menjelaskan hasil yang diperoleh dari proses pembuatan dan pengembangan sistem digital scaffolding. Struktur pembahasan pada bab ini dimulai dengan penjelasan mengenai konteks desain yang berfungsi sebagai dasar justifikasi sistem, yang menampilkan skema arsitektur pada tingkat makro. Bagian utama dalam bab ini kemudian menjelaskan secara rinci proses pengembangan artefak melalui penerapan aplikasi SAPA.

**IV.1 Analisis Problem Domain**

Berdasarkan langkah identifikasi dan studi pendahuluan yang telah diuraikan pada subbab III.6.1, subbab ini menyajikan analisis terhadap karakteristik permasalahan yang ditemukan pada data historis Self Assessment dan Peer Assessment sebagai dasar perancangan pipeline digital scaffolding. Analisis dilakukan untuk mengidentifikasi bagaimana mahasiswa mengartikulasikan penilaian ke dalam bentuk narasi feedback serta bentuk penyimpangan yang muncul terhadap indikator tekstual narasi feedback yang telah dirumuskan pada BAB II. Selain karakteristik kualitatif, subbab ini juga menyajikan kuantifikasi kondisi aktual berdasarkan data historis sehingga kebutuhan pengembangan sistem dapat dijustifikasi secara empiris sebelum proses perancangan pipeline dilakukan.

**IV.1.1 Karakteristik Data Narasi** *Feedback*

Analisis dilakukan secara manual terhadap sampel acak dari data historis untuk mengisolasi karakteristik kemunculan pola dari penyimpangan terhadap keempat indikator tekstual narasi feedback, sebagaimana didefinisikan pada Tabel III.3. Narasi feedback yang dianalisis memiliki karakteristik sebagai teks bahasa alami yang ditulis secara bebas oleh mahasiswa. Berbeda dengan data terstruktur, narasi dapat menggunakan berbagai variasi ekspresi untuk menyampaikan penilaian yang sama sehingga evaluasi kualitas feedback tidak dapat dilakukan hanya berdasarkan keberadaan kata tertentu. Oleh karena itu, analisis pada subbab ini difokuskan pada pola penyimpangan terhadap empat indikator tekstual yang telah didefinisikan sebelumnya.

**IV.1.1.1 Karakteristik Indikator Cakupan Rubrik.**

Pelanggaran pada indikator cakupan rubrik (A) ditunjukkan oleh pola dimana mahasiswa kerap dapat menuliskan narasi kualitatif, namun gagal menyebutkan kriteria spesifik yang tertera pada instrumen rubrik. Sebagaimana ditunjukkan pada [Tabel IV.1](#page-10-0) berdasarkan data historis yang dimiliki, dengan rubrik yang telah didefinisikan pada Tabel II.1 untuk aspek manajemen waktu.

Tabel IV.1. Kasus narasi bersifat generik

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel IV.1](#page-10-0) menunjukkan fenomena pada data historis aktual dengan narasi "Sangat baik". Narasi tersebut tidak menjawab komponen penilaian rubrik, yaitu (1) apakah tugas diselesaikan tepat waktu ataupun (2) eksistensi tugas yang terlambat yang dapat dikejar. Alih-alih, narasi hanya berupa pernyataan afektif generik dan tidak memuat referensi terhadap rubrik. Karakteristik teks ini sejalan dengan temuan (Setiawan, 2026a) yang menekankan bahwa teks generik dan afektif mereduksi fungsi evaluasi menjadi sekadar gestur sosial. Kondisi ini pada akhirnya menghilangkan seluruh informasi yang berguna bagi penerima feedback (assessee) untuk mengidentifikasi kualitas kerja mereka (Nicol et al., 2014).

Kasus lainnya yaitu mahasiswa berhasil mengidentifikasi satu kriteria rubrik, tetapi gagal menuliskan kriteria substantif lainnya dalam aspek rubrik yang sama, fenomena ini merupakan contoh cakupan parsial, sebagaimana disajikan pada [Tabel](#page-11-0)  [IV.2.](#page-11-0)

Tabel IV.2. Kasus Cakupan Parsial

Skor: 5 Narasi: Rekan : dibutuhkan kh  |  Legend:  |  Tidak dibahas Dibahas
Aspek  |  Kriteria  |  Pertanyaan Kuantitatif  |  Pertanyaan Kualitatif  |  Skala 1 (Sangat Kurang)  |  Skala 3 (Cukup)  |  Skala 5 (Sangat Baik)
Pengumpulan Iklan Lowongan Kerja  |  Banyaknya iklan dan keragaman platform yang digunakan.  |  Seberapa baik rekan Anda dalam mengumpulka n iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)  |  Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  Mengumpulka n sedikit iklan.  |  Mengumpulkan cukup iklan.  |  Mengumpulka n banyak dan relevan dari platform yang bervariasi.

Narasi pada [Tabel IV.2](#page-11-0) yaitu "Rekan saya mampu mengumpulkan iklan sebanyak yang dibutuhkan khususnya di platform facebook.", secara eksplisit menyinggung dimensi rubrik (1) banyaknya iklan yang dikumpulkan dan (2) platform sumber yang digunakan, namun gagal membahas dimensi (1) relevansi iklan yang diberikan dan (2) kesulitan yang dihadapi ketika mengumpulkan iklan. Kemunculan pola cakupan parsial ini menegaskan bahwa identifikasi cakupan rubrik memerlukan mekanisme yang mampu mengenali hubungan antara narasi mahasiswa dan deskriptor rubrik meskipun keduanya menggunakan formulasi bahasa yang berbeda dengan menetapkan threshold deteksi indikator cakupan rubrik (KLF,@).

**IV.1.1.2 Karakteristik Indikator Koherensi**

Pelanggaran pada indikator koherensi skor narasi (A) ditunjukkan oleh pola kontradiksi semantik antara skor kuantitatif (dalam skala 1 sampai 5) dengan narasi kualitatif yang diberikan. Sebagaimana disajikan pada [Tabel IV.3,](#page-12-0) mahasiswa memberikan skor kuantitatif rendah namun dengan narasi cenderung tinggi positif.

Tabel IV.3. Kasus Skor Tidak Koheren dengan Narasi yang ditulis

Asp  |  ek  |  Kriteria  |  Pertanyaan Kuantitatif  |  Pertanyaan Kualitatif  |  Skala 1 (Sangat Kurang)  |  Skala 3 (Cukup)  |  Skala 5 (Sangat Baik)
Pengum Iklan Lowong Kerja  |  •  |  Banyaknya iklan dan keragaman platform yang digunakan.  |  mengumpulka n iklan  |  Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  Mengumpulka n sedikit iklan.  |  Mengumpulkan cukup iklan.  |  Mengumpulka n banyak dan relevan dari platform yang bervariasi.

[Tabel IV.3](#page-12-0) menunjukkan mahasiswa yang memberikan skor 1 untuk aspek rubrik "Pengumpulan Iklan Lowongan Pekerjaan.", dengan narasi "dia sangat rajin melebihi seluruh rekan tim.". Terjadi ketidakselarasan antara skor 1 yang pada idealnya menunjukkan kinerja yang rendah, namun disini narasi cenderung menggambarkan kinerja yang baik.

Ketidakselarasan tersebut membuktikan terjadinya pemisahan terhadap mekanisme pemberian skor dengan narasi yang menjustifikasi nilai yang diberikan, menimbulkan diskrepansi antara skor kuantitatif dan narasi feedback. Mahasiswa umumnya mampu menghasilkan skor kuantitatif, namun mengalami kesulitan dalam menulis narasi kualitatif, ataupun kondisi sebaliknya, sebagaimana disajikan pada [Tabel IV.4.](#page-13-0)

Tabel IV.4. Kasus Inkoherensi Skor secara Parsial

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel IV.4](#page-13-0) menyajikan contoh inkoherensi di mana mahasiswa memilih skor kuantitatif 5, tetapi dengan narasi yang sebatas menyatakan "Baik dalam kontribusinya.". Jika mengacu pada rubrik, skor 5 berpasangan dengan standar deskriptif "Sangat baik.", tidak munculnya kata penguat "Sangat." dalam narasi menunjukkan artikulasi skor 5 yang belum memenuhi standar rubrik. Kondisi tersebut dapat dikategorikan sebagai kasus dimana teks mengalami penurunan akurasi penilaian sebesar satu hingga dua tingkat di bawah standar rubrik. Temuan ini menunjukkan bahwa proses identifikasi koherensi tidak hanya memerlukan pengenalan topik yang sama, tetapi juga kemampuan membedakan tingkat kualitas yang direpresentasikan dalam narasi

**IV.1.1.3 Karakteristik Indikator Kedalaman Elaborasi**

Pelanggaran pada indikator elaborasi (`) ditunjukkan oleh narasi feedback yang sangat pendek, sehingga tidak memungkinkan untuk memuat informasi bermakna, dengan contoh yang disajikan pada [Tabel IV.5](#page-14-0). Kasus ini mengonfirmasi bahwa adanya hambatan mahasiswa dalam mengartikulasikan penilaian mereka ke dalam bentuk narasi yang sesuai dengan rubrik.

Tabel IV.5. Kasus Feedback dengan Elaborasi Singkat

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Selain kasus yang disajikan pada [Tabel IV.5,](#page-14-0) tercatat adanya fenomena inflasi tekstual tanpa makna. Sebagai contoh, kasus yang muncul dengan narasi "Rekan saya sangat baik dalam pengumpulan dan pengekstakan data karena ia sangat cepat bahkan nomor 1 tercepat dalam kelompok kami dalam pengumpulan dan pengekstrakan data, saking cepat nya dia juga membantu saya dalam mengumpulan data di Facebook karena tugas yang dia kerjakan sudah selesai.". Dalam contoh tersebut, narasi memiliki panjang 36 kata yang bersifat repetitif dan berputar-putar menggunakan struktur kalimat pengisi tanpa menambah substansi baru.

Fenomena tersebut menjadi kelemahan jika sistem hanya melakukan perhitungan kuantitas jumlah kata secara murni, karena teks dapat dianggap memenuhi indikator elaborasi (`) meskipun tidak memiliki bobot substansi. Hal ini membuktikan bahwa indikator kedalaman elaborasi (`) tidak dapat digunakan sebagai tolak ukur tunggal, melainkan harus dipadukan dengan indikator lainnya untuk mendeteksi kesesuaian antara volume teks dan substansi yang dapat diobservasi tanpa memerlukan interpretasi manusia.

**IV.1.1.4 Karakteristik Indikator Relevansi Topik**

Pelanggaran pada indikator relevansi topik (J) ditunjukkan oleh munculnya penyimpangan isi narasi feedback dengan aspek rubrik yang sedang dinilai. Pada

contoh yang disajikan dalam [Tabel IV.6](#page-0-0) untuk aspek rubrik penilaian "Penggabungan Data dengan Kelompok Lain.", mahasiswa menuliskan narasi: "Saya memang kurang berkomunikasi namun saya mencoba menjadi pendengar yang baik.". Teks tersebut tidak membahas sama sekali terkait penggabungan data yang telah dilakukan, alih-alih membahas mengenai aspek "Komunikasi", yaitu kriteria rubrik lain yang tidak relevan dengan pertanyaan.

Tabel IV.6. Kasus Narasi Tidak Relevan dengan Aspek Rubrik Pertanyaan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Kasus lain yang disajikan pada [Tabel IV.7](#page-0-1) merupakan fenomena dimana relevansi terjadi secara parsial ketika terdapat overlap terminologi dalam rubrik yang digunakan pada Tabel II.1.

Tabel IV.7. Kasus Narasi Feedback Tidak Relevan Sebagian

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dalam [Tabel IV.7](#page-0-1), aspek rubrik yang sedang dinilai adalah "Penggabungan Data dengan Kelompok Lain.", namun mahasiswa menuliskan narasi "Dia sudah mengumpulkan sebagian iklan lowongan kerja.". Narasi tersebut secara substansi berisikan mengenai aspek lain, yaitu "Pengumpulan iklan lowongan pekerjaan". Ketidaksesuaian ini disebabkan oleh pertanyaan yang berfokus pada penggabungan data, yang secara tidak langsung berhubungan dengan proses pengumpulan data.

Kondisi tersebut menegaskan bahwa deteksi relevansi (J) tidak dapat dilakukan melalui pencocokan kata kunci sederhana, melainkan memerlukan mekanisme yang mampu membedakan kesamaan terminologi dasar dari kesesuaian semantik terhadap aspek rubrik yang sedang dinilai.

Secara keseluruhan, analisis terhadap data historis menunjukkan bahwa permasalahan kualitas feedback mahasiswa tidak hanya ditandai oleh rendahnya volume narasi, tetapi juga oleh ketidaklengkapan informasi, ketidaksesuaian antara skor dan justifikasi, serta penyimpangan topik terhadap aspek rubrik yang dinilai. Temuan tersebut menunjukkan bahwa setiap indikator merepresentasikan karakteristik permasalahan yang berbeda sehingga kebutuhan deteksinya tidak dapat diasumsikan bersifat seragam. Karakteristik tersebut selanjutnya menjadi dasar untuk menganalisis konsekuensi komputasional dari setiap indikator dan menentukan pendekatan yang sesuai pada perancangan pipeline digital scaffolding sebagaimana dibahas pada subbab berikutnya.

**IV.1.2 Hasil Kuantifikasi Masalah**

Analisis kuantifikasi dilakukan dengan mengamati 10.098 data feedback historis dengan detail yang disajikan pada [Tabel IV.8](#page-2-0). Setiap data digunakan untuk mengidentifikasi kesenjangan yang terjadi pada pengisian assessment di tengah semester dan akhir semester pembelajaran, distribusi panjang teks narasi, perbandingan self dengan peer assessment, serta selisih skor pada self dan peer assessment.

Tabel IV.8. Detail Data Historis Assessment sebelum Dikomputasi

Jenis Assesment  |  Fase  |  Jumlah Mahasiswa yang Merespons (Assessor)  |  Jumlah Jawaban  |  Rata-Rata Skor yang diberikan (Skala 1-5)  |  Standar Deviasi
Self  |  Tengah Semester  |  94  |  1.034  |  4,156  |  0,531
Akhir Semester  |  86  |  946  |  4,012  |  0,485
Peer  |  Tengah Semester  |  95  |  4.455  |  4,292  |  0,427
Akhir Semester  |  95  |  3.663  |  4,119  |  0,565

Berdasarkan detail yang disajikan pada [Tabel IV.8,](#page-2-0) rata-rata skor peer assessent  memiliki nilai yang jauh lebih tinggi dibandingkan dengan self assessment. Meskipun demikian, skor peer assessment memiliki variasi yang lebih tinggi pada akhir semester, ditunjukan dengan standar deviasi yang menyentuh nilai 0,565. Selain itu, terjadi fenomena reduksi jumlah assessor seiring waktu yang menjadi sinyal penurunan keterlibatan mahasiswa, mengakibatkan penyusutan 792 data pada peer assessment, dan 88 data pada self assessment.

[Gambar IV.1](#page-3-0) menyajikan perbandingan rata-rata jumlah kata dalam narasi feedback self dan peer assessment pada periode pengisian tengah semester dan akhir semester.

Gambar IV.1 Perbandingan Rata-Rata Jumlah Kata antar Self dan Peer

Berdasarkan [Gambar IV.1,](#page-3-0) tercatat bahwa self assessment pada periode tengah semester memiliki volume narasi tertinggi dengan rata-rata 31 kata, yang kemudian menurun menjadi 24 kata pada akhir semester. Pada sisi lain, peer assessment secara konstan menunjukkan volume yang lebih rendah, yakni dengan rata-rata 14 kata pada tengah semester, sebelum terjadi penurunan hingga 11 kata pada akhir semester.

Kesenjangan yang persisten antara self dan peer assessment di kedua periode pengisian mengindikasikan adanya asimetri sistemik, di mana mahasiswa cenderung menginvestasikan elaborasi yang lebih dalam ketika mengevaluasi diri sendiri dibandingkan teman sejawat. Lebih lanjut, penurunan volume pada kedua instrumen mengisyaratkan adanya efek kelelahan seiring akumulasi beban akademik.

[Gambar IV.2](#page-4-0) menyajikan karakteristik sebaran jumlah kata di balik nilai rata-rata pada [Gambar IV.1](#page-3-0) sebelumnya untuk self dan peer assessment pada setiap periode pengisian.

Gambar IV.2 Sebaran Jumlah Kata antar Peer dan Self Assessment

Berdasarkan [Gambar IV.2,](#page-4-0) seluruh kluster data menunjukkan pola distribusi miring ke kanan (positive skewness), dengan konsentrasi frekuensi tertinggi pada rentang 0 hingga 20 kata. Pada fase tengah semester, self assessment mencatat mean 30,6 kata dan median 24 kata, yang menurun menjadi mean 23,7 kata dan median 19 kata pada fase akhir semester. Di sisi lain, peer assessment menunjukkan sebaran yang lebih rendah secara konsisten, dengan mean 13,3 kata dan median 12 kata pada fase tengah semester, sebelum terjadi degradasi dengan mean 11,3 kata dan median 10 kata pada fase akhir semester.

Kondisi median yang secara konsisten berada di bawah mean pada seluruh kluster mengonfirmasi bahwa distribusi didominasi oleh narasi pendek, dengan nilai ratarata yang tinggi dipengaruhi oleh sebagian kecil narasi panjang. Pola ini memiliki implikasi terhadap indikator kedalaman elaborasi, yaitu jika mayoritas respons berada di bawah 20 kata, terdapat risiko bahwa feedback yang diberikan bersifat superfisial dan kurang memuat elaborasi diagnostik yang bermakna bagi penerima feedback (assessee). Kondisi ini menjadi landasan empiris untuk penentuan threshold indikator kedalaman elaborasi (KLF,`) pada tahapan eksperimen selanjutnya.

[Gambar IV.3](#page-5-0) menunjukkan bahwa panjang narasi tidak mengikuti pola peningkatan maupun penurunan yang konsisten terhadap skor kuantitatif. Distribusi panjang narasi pada skor 1 hingga skor 5 saling bertumpang tindih pada hampir seluruh kategori skor. Mahasiswa yang memberikan skor rendah (1–2) tidak selalu menulis narasi yang lebih singkat dibandingkan mahasiswa yang memberikan skor tinggi (4–5), demikian pula mahasiswa yang memberikan skor tinggi tidak secara konsisten menghasilkan narasi yang lebih panjang. Temuan ini menunjukkan bahwa besarnya skor numerik tidak dapat digunakan sebagai indikator tingkat elaborasi narasi feedback sendirian.

Gambar IV.3 Perbandingan Pola Assessment antar Skor dan Panjang Narasi

[Gambar IV.3](#page-5-0) mengindikasikan bahwa kemampuan mahasiswa dalam memberikan skor, tidak selalu diikuti dengan kemampuan mengartikulasikannya ke dalam narasi yang bermakna dan sesuai dengan skor yang diberikan.

Lebih lanjut, [Gambar IV.3](#page-5-0) memperjelas bahwa narasi self assessment secara konsisten lebih panjang dibanding peer assessment, dengan selisih 10-30 kata. Didukung oleh konteks budaya kolektivits di Indonesia, pola ini mengindikasikan bahwa mahasiswa cenderung berhati-hati untuk memberikan penilaian rekan sejawat, sehingga feedback cenderung berisikan deskripsi umum dan menghindari evaluasi yang mengancam harmoni kelompok.

Lebih jauh, [Gambar IV.4](#page-6-0) menyajikan perbandingan skor dan panjang narasi berdasarkan periode pengisian assessment. Ditemukan bahwa degradasi panjang narasi terjadi secara relatif merata pada seluruh rentang skor, baik pada self maupun peer assessment.

Gambar IV.4 Pola Periode Pengisian antar Skor dan Panjang Narasi

Pola pada [Gambar IV.4](#page-6-0) mengindikasikan bahwa penurunan panjang narasi bersifat struktural, konsisten dan tidak terbatas pada rentang skor tertentu. Penurunan volume narasi tersebut dapat diinterpretasikan sebagai indikasi adanya perubahan dalam keterlibatan mahasiswa terhadap proses assessment, meskipun penelitian ini tidak secara langsung mengukur aspek keterlibatan kognitif tersebut.

[Gambar IV.5](#page-7-0) menyajikan distribusi frekuensi rata-rata skor penilaian untuk setiap mahasiswa dalam self dan peer assessment untuk seluruh periode pengisian.

Gambar IV.5 Distribusi Skor Antara Self dan Peer Assessment

Berdasarkan [Gambar IV.5](#page-7-0), ditemukan distribusi peer assessment dominan pada skor 4 dan 5, sementara self assessment memiliki sebaran pada skor yang lebih rendah. Hal tersebut menunjukkan bahwa mahasiswa cenderung memberikan skor yang lebih tinggi pada rekan sejawat dibandingkan dengan diri sendiri. Berdasarkan framework feedback litracy yang telah dijelaskan pada subbab II.1.9, pola ini dipahami sebagai leniency bias yang didorong oleh dinamika interpersonal, khususnya bias pertemanan pada kelompok (Panadero et al., 2017). Kondisi ini sejalan dengan temuan sebelumnya bahwa narasi pada peer assessment cenderung lebih singkat dan kurang mendalam.

Temuan tersebut menjadi semakin krusial jika dihubungkan dengan data penurunan volume narasi di akhir semester. Mahasiswa tampak terbiasa mengeksekusi penilaian kuantitatif secara instan dengan memberikan skor tinggi, meskipun terdapat subjektivitas dan ketidakselarasan. Namun, tidak terdapat peningkatan dalam menguraikan narasi yang menjadi dasar pertimbangan angka tersebut. Hal tersebut menegaskan bahwa kemudahan mahasiswa dalam mendistribusikan angka tidak diiringi oleh kemampuan mengartikulasikan alasan evaluatif secara naratif.

Kondisi tersebut menunjukkan adanya ruang urgensi untuk intervensi yang dapat membantu mahasiswa secara kognitif sehingga dapat menghubungkan penilaian kuantitatif dengan justifikasi naratif yang lebih representatif.

Seluruh temuan yang telah dipaparkan mengonfirmasi tiga hasil utama, yaitu (1) adanya asimetri alokasi effort atau usaha antara self assessment dan peer assessment, (2) ditemukannya penurunan kuantitas narasi lintas waktu antara tengah semester dan akhir semester, serta (3) ditemukannya fenomena yang terisolasi antara nilai numerik dengan kedalaman eksplorasi teks. Ketiga hal tersebut memperkuat motivasi penelitian, di mana kemampuan mahasiswa dalam mengartikulasi skor ke dalam bentuk narasi feedback tidak berkembang secara alami tanpa adanya intervensi, dan hanya melalui pengulangan proses pengisian instrumen.

**IV.1.3 Spesifikasi dan Objektif Solusi**

Subbab ini adalah manifestasi dari tahapan yang didefinisikan pada subbab III.6.2. Spesifikasi dan objektif dari solusi didefinisikan berdasarkan temuan pada subbab IV.1.1 hingga [IV.1.2](#page-1-0) yang menunjukkan bahwa skor kuantitatif dan narasi pendukung tidak selalu berkembang secara selaras selama proses assessment. Hal ini terlihat dari semakin kecilnya perbedaan skor antara self assessment dan peer assessment menjelang akhir semester, sementara panjang narasi yang menyertainya justru mengalami penurunan.

Berdasarkan temuan tersebut, solusi dirancang dengan spesifikasi sebagai berikut:

1. Sistem mampu mendeteksi keempat indikator tekstual narasi feedback yaitu cakupan rubrik, koherensi skor, kedalaman elaborasi dan relevansi topik yang dijelaskan lebih lanjut pada subbab

2. Sistem mampu memicu teks scaffolding secara real-time dalam sesi penulisan ketika narasi feedback melanggar keempat indikator tekstual dan diberikan teks scaffolding berdasarkan vektor keputusan intervensi di mana setiap keputusan didasarkan pada threshold yang telah dikalibrasi berdasarkan sample data historis.
3. Sistem mampu menghentikan pemberian scaffolding secara otomatis ketika seluruh indikator tekstual telah terpenuhi pada sesi penulisan yang sama..

Batasan operasional sistem ditetapkan pada evaluasi keempat indikator tekstual narasi feedback. Dengan demikian, sistem hanya mengevaluasi indikator yang dapat dioperasionalkan secara komputasional berdasarkan teks narasi, dan tidak mencakup aspek linguistik maupun evaluatif yang masih memerlukan interpretasi manusia sebagaimana dijelaskan pada subbab I.7.

Objektif solusi difokuskan pada penyediaan scaffolding selama proses penulisan narasi berlangsung untuk membantu mahasiswa menghasilkan narasi yang lebih selaras dengan indikator tekstual yang digunakan sebagai dasar pemberian scaffolding.

Keberhasilan solusi dievaluasi melalui dua tahapan yang selaras dengan pertanyaan penelitian. Tahap pertama menjawab RQ1, yaitu mengevaluasi kemampuan pipeline mendeteksi keempat indikator tekstual menggunakan metrik precision, recall, dan F1-score. Tahap kedua menjawab RQ2 melalui pilot study untuk mengukur perbedaan tingkat pemenuhan indikator tekstual antara kelompok treatment dan kelompok kontrol menggunakan analisis multivariat, analisis univariat, dan estimasi effect size.

**IV.2 Hasil Anotasi Dataset**

Subbab ini merupakan hasil akhir dari metodologi anotasi dataset yang telah didefinisikan pada subbab III.6.3.1. Sebagaimana dijelaskan, proses anotasi terdiri dari beberapa tahapan, yaitu: (1) pre-processing untuk melakukan dekomposisi terhadap rubrik, hasil tahapan ini disajikan pada subbab [IV.2.1.](#page-10-0) Kemudian, untuk menjaga konsistensi, (2) implementasi panduan anotasi disajikan pada subbab [IV.2.2](#page-12-0) sebelum dilakukan proses anotasi. Setelah itu, (3) sampel hasil anotasi disajikan pada subbab [IV.2.3,](#page-13-0) sebelum dilakukan (4) validasi pada subbab IV.2.3.3.

**IV.2.1 Hasil Dekomposisi Rubrik**

Sebagai manifestasi hasil dari pre-processing, sebagaimana didefinisikan pada subbab III.6.3.1B, tahapan ini menghasilkan dua feature set, yaitu: (1) cakupan dan relevansi topik (åçé-, ) yang disajikan pada subbab [IV.2.1.1,](#page-10-1) serta feature set koherensi skor narasi (åçU-, ) yang disajikan pada subbab [IV.2.1.2](#page-11-0).

**IV.2.1.1 Hasil Feature Set Cakupan dan Relevansi Topik**

Berdasarkan proses yang didefinisikan pada subbab III.6.3.1C, dekomposisi akhir yang diperoleh disajikan pada [Tabel IV.9.](#page-10-2) Feature set ini memiliki total 26 unit yang digunakan sebagai komponen utama indikator cakupan rubrik (@) dan relevansi topik (J) dalam melakukan vector embedding dan cosine similarity, sebagaimana dijelaskan dalam subbab II.1.7.1 dan II.1.7.2.

Tabel IV.9 Hasil Akhir Dekomposisi Rubrik untuk Cakupan dan Relevansi

Kriteria: Unit hasil dekomposisi
Banyaknya iklan dan keragaman: Jumlah Iklan yang Dikumpulkan
platform yang digunakan.: Keragaman Platform Pengumpulan
Kesulitan dalam Pengumpulan Data
Kemudahan dalam Pengumpulan Data
Relevansi Iklan yang Dikumpulkan
Pemahaman informasi penting dari: Tingkat Pemahaman Konten Iklan
iklan yang dikumpulkan.: Identifikasi Informasi Penting
Kesesuaian dan kejelasan struktur data: Kesesuaian Struktur dengan Kebutuhan
untuk memuat informasi.: Kelengkapan Struktur Data
Struktur memadai atau tidak
Ketelitian dan keakuratan penginputan: Ketelitian dalam Penginputan
data.: Keakuratan Data yang Diinput
Ada atau tidaknya kesalahan dalam penginputan
Partisipasi dalam menggabungkan data: Aktif atau tidaknya dalam keterlibatan penggabungan
kelompok.: Kontribusi dalam Menyelesaikan Penggabungan
Kemampuan bekerja sama dengan: Sikap Kooperatif terhadap Tim
anggota kelompok lain.: Dukungan terhadap Anggota Tim
Partisipasi dalam Diskusi Kelompok
Efektivitas dalam menyampaikan ide: Efektivitas Berkomunikasi
dan berdiskusi.: Kemampuan Menyampaikan Ide

Kriteria: Unit hasil dekomposisi
Konsistensi Komunikasi Selama Proyek
Kemampuan mengidentifikasi dan  |  dan  |  Tingkat Inisiatif dan Proaktivitas
menyelesaikan masalah.: Kemampuan Menyelesaikan Masalah
Respons terhadap Kendala dan Masalah
Kemampuan  |  menyelesaikan  |  tugas  |  Ketepatan Memenuhi Deadline
sesuai tenggat waktu.  |  _  |  Kemampuan Mengelola Waktu

IV.2.1.2 Hasil Feature Set Koherensi Skor

Dengan menggunakan proses yang telah didefinisikan pada subbab III.6.3.1D, hasil dekomposisi disajikan pada Tabel IV.10 dengan total 46 unit. Setiap unit digunakan sebagai komponen utama dalam melakukan komputasi indikator koherensi skor dan narasi  $(f_2)$ .

Tabel IV.10. Hasil Dekomposisi Rubrik Untuk Koherensi Skor dan Narasi

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
Banyaknya iklan dan  |  Skala 1 (Sangat  |  $G_1$  |  Mengumpulkan sedikit iklan
keragaman platform  |  Kurang)  |  $G_2$  |  Iklan tidak relevan
yang digunakan.  |  $G_3$  |  Platform tidak bervariasi
Skala 3 (Cukup)  |  $G_1$  |  Mengumpulkan cukup iklan
$G_2$: Iklan cukup relevan
$G_3$: Platform cukup bervariasi
Skala 5 (Sangat Baik)  |  $G_1$  |  Mengumpulkan banyak iklan
$G_2$: Iklan sangat relevan
$G_3$: Platform sangat bervariasi
Pemahaman  |  Skala 1 (Sangat  |  $G_1$  |  Tidak memahami isi iklan
informasi penting dari: Kurang)
iklan yang  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup memahami isi iklan
dikumpulkan.  |  Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat memahami informasi
penting dari iklan
Kesesuaian dan  |  Skala 1 (Sangat  |  $G_1$  |  Struktur data tidak sesuai
kejelasan struktur  |  Kurang)  |  $G_2$  |  Struktur data tidak lengkap
data untuk memuat  |  Skala 3 (Cukup)  |  $G_1$  |  Struktur data cukup sesuai
informasi.  |  $G_3$  |  Struktur data memiliki beberapa
kekurangan
Skala 5 (Sangat Baik)  |  $G_1$  |  Struktur data sangat baik
$G_2$: Struktur data lengkap
Ketelitian dan  |  Skala 1 (Sangat  |  $G_1$  |  Banyak kesalahan dalam data
keakuratan  |  Kurang)  |  yang diinput
penginputan data.  |  $G_2$  |  Tidak teliti dalam penginputan
Skala 3 (Cukup)  |  $G_1$  |  Cukup akurat dengan sedikit
kesalahan
Skala 5 (Sangat Baik)  |  $G_1$  |  Data sangat akurat
$G_2$: Sangat teliti dalam penginputan
Partisipasi dalam  |  Skala 1 (Sangat  |  $G_1$  |  Tidak banyak terlibat dalam
menggabungkan data  |  Kurang)  |  penggabungan data
kelompok.  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup terlibat namun tidak
signifikan

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat terlibat dan membantu menyelesaikan penggabungan
Kemampuan bekerja sama dengan anggota  |  Skala 1 (Sangat Kurang)  |  $G_1$  |  Tidak banyak bekerja sama
kelompok lain.  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup kooperatif, namun kontribusi terbatas
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat kooperatif dan banyak membantu tim
Efektivitas dalam  |  Skala 1 (Sangat  |  $G_1$  |  Tidak efektif dalam komunikasi
menyampaikan ide dan berdiskusi.  |  Kurang)  |  $G_2$  |  Ide tidak tersampaikan dengan jelas
Skala 3 (Cukup)  |  $G_1$  |  Cukup efektif dalam komunikasi
$G_2$: Ide cukup tersampaikan dengan jelas
$G_3$: Komunikasi tidak konsisten
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat efektif dalam komunikasi
$G_2$: Ide sangat tersampaikan dengan jelas
Kemampuan  |  Skala 1 (Sangat  |  $G_1$  |  Tidak memiliki inisiatif
mengidentifikasi dan menyelesaikan  |  Kurang)  |  $G_2$  |  Tidak memberikan solusi untu menyelesaikan masalah
masalah.  |  Skala 3 (Cukup)  |  $G_2$  |  Cukup memberikan solusi
$G_3$: Memberikan solusi hanya dalam beberapa situasi
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat proaktif
$G_2$: Memberikan solusi untuk menyelesaikan masalah
Kemampuan menyelesaikan tugas  |  Skala 1 (Sangat Kurang)  |  $G_1$  |  Banyak tugas yang terlambat diselesaikan
sesuai tenggat waktu.  |  Skala 3 (Cukup)  |  $G_1$  |  Beberapa tugas terlambat
. 1/  |  $G_2$  |  Tugas yang terlambat masih terkejar
Skala 5 (Sangat Baik)  |  $G_1$  |  Semua tugas diselesaikan tepat waktu

IV.2.2 Implementasi Panduan Anotasi

Sebagai manifestasi dari subbab III.6.3.1E, panduan anotasi telah diimplementasikan pada Lampiran 1. Panduan ini digunakan sebagai acuan operasional dalam seluruh proses pelabelan dataset. Setiap anotator menggunakan definisi kriteria, aturan keputusan, dan contoh yang tercantum dalam panduan sebagai dasar dalam menentukan label, sehingga proses anotasi tidak bergantung pada interpretasi individual yang bersifat ad-hoc.

Selama proses anotasi, panduan berfungsi sebagai single source of truth yang memastikan konsistensi antar anotator pada kasus-kasus yang memiliki potensi ambiguitas. Dalam situasi di mana interpretasi terhadap suatu narasi bersifat tidak jelas, keputusan pelabelan ditelusuri kembali ke aturan eksplisit dalam panduan, sehingga menjaga keseragaman penerapan kriteria pada seluruh dataset.

Penggunaan panduan ini juga menjadi dasar dalam proses validasi oleh domain expert, di mana kesesuaian label tidak hanya dinilai terhadap intuisi penilai, tetapi terhadap definisi formal yang telah dikodifikasi. Dengan demikian, implementasi panduan anotasi berkontribusi langsung terhadap konsistensi, traceability, dan validitas ground truth yang dihasilkan.

**IV.2.3 Sampel Hasil Anotasi**

Berdasarkan metodologi dan skema multi-label binary classification yang telah diuraikan pada subbab III.6.3.1E, proses anotasi dilaksanakan terhadap sampel acak sebanyak 384 narasi feedback menggunakan hasil dekomposisi rubrik pada subbab [IV.2](#page-10-3), serta panduan yang telah didefinisikan pada [IV.2.2](#page-12-0). Untuk menjaga kerahasiaan data feedback, subbab ini hanya menyajikan sampel dari hasil anotasi dataset.

Anotasi menghasilkan dua dataset berbeda berdasarkan feature set yang didefinisikan pada subbab [IV.2.1](#page-10-0). Dataset yang pertama merupakan manifestasi dari cakupan dan relevansi feature set (åçé-, ), dengan sampel anotasi disajikan pada subbab [IV.2.3.1.](#page-13-1) Dataset kedua merupakan manifestasi feature set koherensi skor dan narasi (åçU-, ), dengan sampel anotasi yang disajikan pada subbab IV.2.3.2.

**IV.2.3.1 Sampel Anotasi Feature Set Cakupan dan Relevansi Topik**

Dataset ini dibuat berdasarkan feature-set cakupan dan relevansi (åçU-, ) yang didefinisikan pada subbab [IV.2.1.1](#page-10-1). Anotasi pada dataset ini digunakan sebagai acuan utama evaluasi kinerja model NLP untuk indikator cakupan rubrik (@) dan relevansi topik (J).

Tabel IV.11 menyajikan sampel dataset yang telah dianotasi untuk kriteria "Banyaknya iklan dan keragaman platform yang digunakan" dan "Pemahaman informasi penting dari iklan yang dikumpulkan". Setiap narasi feedback (+,+) dibandingkan dengan seluruh unit pada feature set, hubungannya dengan unit memiliki nilai "TRUE" jika narasi membahas kriteria penilaian dalam unit tersebut, dan memiliki nilai "FALSE" jika unit penilaian tidak dibahas dalam narasi.

Proses anotasi untuk dataset ini bergantung sepenuhnya pada narasi feedback (+,+), tanpa menggunakan sumber data lain seperti skor (BEF) ataupun pertanyaan spesifik. yang diberikan.

Tabel IV.11. Sampel Data Anotasi Dataset Cakupan Rubrik dan Relevansi

Bany: Pemahaman informasi penting dari iklan yang dikumpulkan.
Narasi Feedback (S <sub>txt</sub> )  |  Jumlah Iklan yang Dikumpulkan  |  Keragaman Platform Pengumpulan  |  Kesulitan dalam Pengumpulan Data  |  Kemudahan dalam Pengumpulan Data  |  Relevansi Iklan yang Dikumpulkan  |  Tingkat Pemahaman Konten Iklan  |  Identifikasi Informasi Penting
Saya berperan aktif dalam menyamakan format data, menyesuaikan header kolom yang akan dipakai dalam struktur kelompok apa saja. Masalah yang dihadapi adalah banyaknya struktur data yang berbeda atau salah penginputan sehingga harus mem validasi ulang  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Rekan saya memahami dengan baik isi iklan yang dikumpulkannya. Ia bisa mengenali informasi penting seperti posisi, persyaratan, dan lokasi kerja, sehingga data yang ia kumpulkan mudah diproses lebih lanjut.  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  TRUE  |  TRUE
Dia sangat aktif karena dia ketua juga  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Karena rekan saya bagian platform TikTok juga (sama dengan rekan saya yang satunya) mereka jadi lebih cepat dan mudah dalam mencari loker  |  FALSE  |  TRUE  |  FALSE  |  TRUE  |  FALSE  |  FALSE  |  FALSE
Rekan saya menyelesaikan 50 data facebook dengan baik dan tepat waktu  |  TRUE  |  TRUE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Rekan saya teliti dalam penginputan data  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE

**IV.2.3.2 Sampel Anotasi Feature Set Koherensi Skor Narasi**

Dataset ini merupakan manifestasi dari feature-set koherensi (åçé-, ) yang didefinisikan pada subbab [IV.2.3.2.](#page-1-0) Dataset digunakan sebagai acuan dalam komputasi indikator koherensi skor dan narasi (A).

Pelabelan pada dataset ini memetakan narasi feedback (+,+) secara langsung terhadap unit dalam feature-set sesuai dengan pasangan kriteria yang ditanyakan. Relasi ini diberi nilai "TRUE" apabila narasi merepresentasikan deskripsi performa pada skala tertentu, dan nilai "FALSE" untuk skala yang tidak relevan. [Tabel IV.12](#page-2-0) dan [Tabel IV.13](#page-3-0) menyajikan contoh dataset pada kriteria "Banyaknya iklan dan keragaman platform yang digunakan." dan "Pemahaman informasi penting dari iklan yang dikumpulkan.".

Tabel IV.12. Sampel Dataset Koherensi Skor Narasi 1

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Tabel IV.13. Sampel Dataset Koherensi Skor Narasi 2

Pemahaman informasi penting dari iklan yang dikumpulkan.
Narasi  |  Vuitauia Vang Ditanyakan  |  Skala 1 (Sangat Kurang)  |  Skala 3 (Cukup)  |  Skala 5 (Sangat Baik)
Ivarasi  |  Kriteria Yang Ditanyakan  |  Cukup memahami isi iklan  |  Sangat memahami informasi penting dari iklan
Rekan saya memahami dengan baik isi iklan yang dikumpulkannya. Ia bisa mengenali informasi penting seperti posisi, persyaratan, dan lokasi kerja, sehingga data yang ia kumpulkan mudah diproses lebih lanjut.  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  FALSE  |  TRUE
data yang di kumpulkan rekan saya sudah rapih dan mudah dibaca: Ketelitian dan keakuratan penginputan data.
dia dapat memahami informasi dengan sangat baik  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  FALSE  |  TRUE
Sudah memabahami tentang informasi yang penting dalam iklan  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  FALSE  |  TRUE
Saya pertama-tama menganalisa atau mencari posisinya terlebih dahulu kemudian nama perusahaanya, skill/requirement, dan terakhir link/kontak untuk menghubungi HRD.  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  FALSE  |  FALSE
dia memahami cukup baik tentang data yang cukup penting untuk dikumpulkan  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  TRUE  |  FALSE
karena , ia selalu tepat waktu: Kemampuan menyelesaikan tugas sesuai tenggat waktu
Cukup memahami namun ia tidak bisa mengungkapkannya  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE  |  TRUE  |  FALSE

**IV.2.3.3 Statistik Dataset**

Sebagai hasil akhir dari prosedur anotasi bersumber dari 384 baris data feedback yang dijelaskan pada subbab III.6.3.1F, setiap baris narasi dipasangkan dengan beberapa unit kriteria rubrik untuk dievaluasi secara independen. Proses kombinasi ini mentransformasi 384 narasi menjadi volume data komputasional dengan distribusi sebagai berikut:

1. 1.100 pasangan data untuk indikator cakupan rubrik (@). Narasi dipasangkan secara eksklusif dengan unit kriteria dari aspek yang sedang menjadi fokus penilaian untuk mendeteksi kehadiran elemen penilaian spesifik dalam narasi.
2. 1.990 pasangan data untuk indikator koherensi skor dan narasi (A). Volume ini didapatkan oleh hubungan narasi feedback dengan deskripsi capaian spesifik (-, ,L<sup>à</sup> ) pada skala skor 1, 3, dan 5 secara terpisah.
3. 9.984 pasangan data untuk indikator relevansi topik (J). Jilah ini mencapai titik tertinggi karena metode deteksi yang bersifat global. Setiap narasi dilakukan komputasi silang terhadap total 26 unit dekomposisi kriteria untuk mengidentifikasi apakah narasi menyimpang ke aspek lain di luar pertanyaan.

Distribusi label "TRUE" dan "FALSE" dari hasil anotasi kombinasi pasangan tersebut disajikan pada [Gambar IV.6.](#page-4-0)

Gambar IV.6. Distribusi label TRUE dan FALSE pada Dataset

Dataset ini mencakup sembilan aspek rubrik evaluasi dari mata kuliah yang menerapkan PjBL, yaitu pengumpulan iklan lowongan kerja, pemahaman terhadap isi iklan, pembuatan struktur data, penginputan data ke Excel, penggabungan data dengan kelompok lain, kolaborasi dan kerjasama tim, komunikasi, inisiatif dan pemecahan masalah, serta manajemen waktu. Sebagaimana didefinisikan pada Tabel II.1. Seluruh dataset ini dianalisis lebih lanjut pada subbab [IV.2.3.3A](#page-5-0) dan [IV.2.3.3B](#page-6-0).

**A. Representasi Dataset**

Sebagai hasil dari prosedur penarikan sampel yang telah ditetapkan pada subbab III.6.3.1, distribusi data pada sampel anotasi dievaluasi untuk memastikan ecological validity dari dataset tersebut. [Gambar IV.7](#page-5-1) mengilustrasikan hasil distribusi narasi yang tidak memenuhi indikator cakupan rubrik (@), koherensi skor dan narasi (A), serta relevansi topik pada sampel yang telah dianotasi (J).

Gambar IV.7. Distribusi Tiga Indikator Pada Sampel Anotasi

Berdasarkan [Gambar IV.7,](#page-5-1) terindikasi bahwa terdapat 328 feedback yang tidak memenuhi cakupan rubrik (@), 266 narasi feedback yang tidak selaras dengan skor kuantitatif (A), serta 90 feedback memiliki narasi yang tidak relevan (J). Hal ini secara langsung mengonfirmasi temuan Setiawan (2026a) mengenai tingginya angka ketidakselarasan antara skor narasi dalam kondisi aktual di lapangan.

Di sisi lain, [Gambar IV.8](#page-6-1) menyajikan distribusi jumlah kata pada keseluruhan dataset. Sumbu X merepresentasikan jumlah kata untuk setiap narasi, dan sumbu Y merepresentasikan frekuensi kemunculan narasi dengan panjang kata spesifik.

Gambar IV.8. Histogram Jumlah Kata Pada Dataset Anotasi

[Gambar IV.8](#page-6-1) menyajikan distribusi jumlah kata pada seluruh narasi feedback. Distribusi menunjukkan pola right-skewed dengan konsentrasi terbesar pada narasi yang relatif pendek. Secara visual, terlihat adanya titik perubahan distribusi pada kisaran 25 kata, yaitu batas ketika frekuensi narasi mulai bergeser dari kluster padat menuju distribusi yang lebih jarang. Berdasarkan karakteristik distribusi tersebut, threshold indikator kedalaman elaborasi ` ditetapkan sebesar 25 kata. Nilai ini merepresentasikan karakteristik aktual data yang digunakan dalam penelitian dan menjadi dasar operasional untuk membedakan narasi pendek dan narasi panjang pada analisis selanjutnya.

**B. Analisis Komplementaritas Antar Indikator**

Analisis ini bertujuan untuk memverifikasi tiga hal secara empiris, yaitu: (1) apakah skala masalah pada data aktual sesuai dengan yang diidentifikasi pada studi pendahuluan, (2) apakah keempat indikator komputasi yang didefinisikan pada Tabel III.3 bersifat komplementer dan tidak redundan, serta apakah threshold elaborasi (KLF,`) bernilai 25 kata memiliki justifikasi empiris terhadap kualitas cakupan rubrik.

[Gambar IV.9](#page-7-0) menyajikan distribusi indikator komputasi tekstual narasi feedback. Dengan sumbu X merepresentasikan indikator cakupan rubrik (@), koherensi skor

dan narasi (A), serta relevansi topik (J), sebagaimana didefinisikan pada Tabel III.3.

Gambar IV.9 Distribusi Empat Indikator Tekstual Narasi Feedback

Berdasarkan [Gambar IV.9,](#page-7-0) menunjukkan distribusi pemenuhan indikator tekstual pada seluruh narasi feedback. Berdasarkan visualisasi tersebut, indikator cakupan rubrik @ memiliki tingkat ketidakterpenuhan tertinggi, yaitu 328 dari 384 narasi (85,4%). Indikator koherensi skor dan narasi <sup>A</sup> menunjukkan tingkat ketidakterpenuhan sebesar 69,3%, sedangkan indikator relevansi topik J memiliki tingkat pemenuhan tertinggi dengan proporsi narasi yang masih berada pada topik yang sesuai mencapai 76,6%. Distribusi ini menunjukkan bahwa permasalahan utama pada feedback mahasiswa lebih banyak berkaitan dengan kualitas justifikasi dan kelengkapan evaluasi dibandingkan dengan penyimpangan topik pembahasan.

[Gambar IV.10](#page-8-0) menyajikan kontigensi berpasangan pada distribusi pemenuhan indikator. Dengan pemetaan cakupan rubrik (@) & relevansi topik (J), cakupan rubrik (@) & koherensi skor dan narasi (A), serta relevansi topik (J) & koherensi skor dan narasi (A). Pemetaan tersebut mengungkap pola hubungan yang memvalidasi desain keempat indikator sebagai konstruk yang komplementer.

Gambar IV.10 Hubungan Antar Indikator

Berdasarkan [Gambar IV.10](#page-8-0) pada pasangan indikator cakupan rubrik dan relevansi topik, ditemukan bahwa 246 dari 384 narasi yang tidak memenuhi cakupan rubrik tetap memenuhi indikator relevansi topik. Temuan ini menunjukkan bahwa mahasiswa umumnya masih membahas aspek yang sedang dinilai, namun belum mengembangkan seluruh dimensi evaluasi yang tercantum dalam rubrik. Dengan demikian, indikator cakupan rubrik dan relevansi topik merepresentasikan dua konstruk yang berbeda dan saling melengkapi. Relevansi topik mengukur kesesuaian fokus pembahasan terhadap aspek yang ditanyakan, sedangkan cakupan rubrik mengukur kelengkapan dimensi evaluatif yang muncul dalam narasi.

Pada pasangan cakupan rubrik dan koherensi skor-narasi, tercatat bahwa 237 dari 384 narasi yang tidak memenuhi cakupan rubrik juga tidak memenuhi indikator koherensi. Pola ini menunjukkan bahwa keterbatasan cakupan sering disertai dengan lemahnya justifikasi terhadap skor yang diberikan. Ketika narasi hanya memuat sedikit informasi mengenai kriteria rubrik, ruang bagi narasi untuk merepresentasikan tingkat pencapaian yang sesuai dengan skor juga menjadi terbatas. Temuan ini menjelaskan tingginya co-occurency kegagalan kedua indikator sekaligus mengindikasikan adanya hubungan substantif antara kelengkapan evaluasi dan kemampuan narasi dalam mendukung skor yang diberikan.

Pada pasangan relevansi topik dan koherensi skor-narasi, tidak ditemukan hubungan yang signifikan. Sebagian besar narasi yang relevan terhadap aspek yang ditanyakan tetap dapat gagal memenuhi koherensi skor-narasi. Temuan ini menunjukkan bahwa membahas topik yang benar tidak secara otomatis menghasilkan justifikasi yang sesuai terhadap tingkat skor yang diberikan. Dengan demikian, relevansi topik dan koherensi skor-narasi merepresentasikan dua dimensi indikator tekstual narasi feedback yang relatif independen.

Pola co-occurency ini menjelaskan mengapa kombinasi kegagalan cakupan dan koherensi mendominasi distribusi, dengan analisis yang disajikan pada [Gambar](#page-9-0)  [IV.11.](#page-9-0)

Gambar IV.11 Pola Overlap Indikator Tidak Terpenuhi

Berdasarkan [Gambar IV.11,](#page-9-0) overlap antara kegagalan indikator cakupan rubrik @ dan koherensi skor-narasi A merupakan pola yang paling dominan dengan 177 narasi. Pola ini diikuti oleh narasi yang hanya gagal pada indikator cakupan rubrik sebanyak 69 narasi (18,0%), serta narasi yang gagal pada ketiga indikator secara bersamaan sebanyak 60 narasi (15,6%). Sebaliknya, kegagalan yang hanya melibatkan indikator relevansi topik relatif jarang ditemukan, dengan hanya 3 narasi yang gagal pada indikator tersebut secara terisolasi. Distribusi ini menunjukkan bahwa permasalahan pada dataset lebih banyak berkaitan dengan cakupan aspek evaluasi dan keselarasan antara skor dan narasi dibandingkan dengan kesesuaian topik pembahasan.

Temuan ini memberikan bukti empiris bahwa ketiga indikator menangkap pola kegagalan yang berbeda dan tidak bersifat redundan. Sebagian narasi hanya gagal pada satu indikator tertentu, sementara sebagian lainnya menunjukkan kombinasi kegagalan pada dua atau tiga indikator sekaligus. Variasi pola tersebut mengindikasikan bahwa kualitas feedback mahasiswa tidak dapat direpresentasikan secara memadai oleh satu indikator tunggal. Oleh karena itu, penggunaan pendekatan multi-indikator sebagaimana dirancang pada penelitian ini memperoleh justifikasi empiris dari distribusi data aktual yang diamati.

[Gambar IV.12](#page-10-0) menyajikan jumlah narasi feedback yang termasuk ke dalam kategori panjang (≥ 25 kata) dan kategori pendek (< 25 kata). Lebih jauh, gambar tersebut mengaitkan hubungan jumlah kata dengan pemenuhan indikator cakupan rubrik (@).

Gambar IV.12 Pemenuhan Indikator Cakupan Rubrik berdasarkan Panjang

Sebagaimana diungkapkan pada [Gambar IV.12](#page-10-0) menunjukkan distribusi panjang narasi berdasarkan threshold 25 kata yang digunakan pada indikator kedalaman elaborasi `. Dari 384 narasi yang dianalisis, sebanyak 328 narasi (85,4%) termasuk dalam kategori pendek (<25 kata), sedangkan hanya 56 narasi (14,6%) yang termasuk kategori panjang (≥25 kata). Distribusi ini menunjukkan bahwa sebagian besar mahasiswa memberikan feedback dalam bentuk narasi yang relatif singkat.

Untuk mengevaluasi apakah panjang narasi berkaitan dengan kualitas isi yang lebih baik, dilakukan perbandingan terhadap pemenuhan indikator cakupan rubrik (@). Hasil analisis menunjukkan bahwa narasi pendek memiliki coverage pass rate sebesar 13,1%, sedangkan narasi panjang mencapai 23,2%. Meskipun perbedaannya tidak terlalu besar, pola ini menunjukkan bahwa narasi yang lebih panjang memiliki peluang yang lebih tinggi untuk memuat elemen rubrik yang relevan.

Namun demikian, sebagian besar narasi panjang tetap tidak memenuhi indikator cakupan rubrik. Temuan ini menunjukkan bahwa panjang narasi tidak identik dengan kualitas isi narasi. Mahasiswa dapat menghasilkan narasi yang panjang tanpa membahas dimensi evaluasi yang diminta rubrik. Sebaliknya, narasi yang sangat singkat memiliki keterbatasan ruang untuk menjelaskan alasan penilaian secara rinci. Oleh karena itu, indikator kedalaman elaborasi ` merepresentasikan dimensi yang berbeda dari indikator lainnya, yaitu kecukupan ruang informasi dalam narasi, bukan kualitas semantik dari isi narasi tersebut.

**IV.2.4 Validasi Hasil Anotasi**

Sesuai dengan prosedur yang didefinisikan pada subbab III.6.3.1G, validasi ground truth dilakukan melalui random sampling terhadap 384 data anotasi yang kemudian dilakukan review oleh dosen dengan keahlian pada Project-Based Learning.

Hasil validasi menegaskan bahwa proses pelabelan telah dilakukan sesuai dengan definisi dan kriteria rubrik yang ditetapkan. Didukung oleh buku panduan anotasi pada Lampiran 1 yang berperan sebagai acuan, sehingga setiap keputusan label dapat ditelusuri kembali ke aturan yang eksplisit.

**IV.3 Hasil Pemodelan dan Pengembangan Sistem Scaffolding**

Subbab ini merupakan manifestasi dari metodologi pemodelan sistem digital scaffolding yang telah didefinisikan pada subbab III.6.3.2. Pembahasan mencakup definisi fungsi, representasi semantik teks, mekanisme evaluasi yang digunakan untuk menghasilkan sinyal kuantitatif dari narasi terhadap rubrik, pengembangan rule-based system, serta perancangan teks dan template scaffolding.

Berdasarkan subbab III.6.3.2, langkah pertama dalam pemodelan sistem adalah seleksi pendekatan komputasional untuk klasifikasi teks narasi feedback sebelum mendapatkan kandidat model. Proses ini dilakukan dengan mempertimbangkan kebutuhan rubrik yang bersifat dinamis, detail kandidat yang disajikan pada [Tabel](#page-13-0)  [IV.14](#page-13-0).

[Tabel IV.14](#page-13-0) mendefinisikan bahwa pendekatan komputasional yang digunakan dalam penelitian adalah metode semantic text similarity dalam ruang vektor untuk melakukan klasifikasi teks. Desain pipeline dan seleksi kandidat model pada pendekatan ini ditelusuri lebih lanjut pada subbab IV.3.2 hingga IV.3.2.1.

Tabel IV.14. Pemilihan Pendekatan Komputasional

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Pendekatan  |  Penelitian Terdahulu  |  Karakteristik Metode  |  Justifikasi Pemilihan
Pendekatan LLM  |  Penelitian Terdahulu  Penelitian mengenai LLM untuk mengklasifikasikan teks tidak jarang dilakukan. Hal ini disebabkan oleh prosedur training dan fine-tuning yang bersidat opsional. Model dapat melakukan klasifikasi secara akurat menggunakan metode zeroshot, few-shot prompting, ataupun dynamic exemplar selection (Lan et al., 2024; Liu & Shi, 2020; Tripp, 2025).  |  Rarakteristik Metode Pendekatan ini menggunakan LLM sepenuhnya melakukan proses klasifikasi pada teks.  |  Meskipun performanya yang tinggi, pendekatan ini tidak sesuai dengan karakteristik tugas klasifikasi dan implikasi operasional karena membutuhkan sumber saya yang besar.  Dengan asumsi terdapat 96 mahasiswa yang mengisi masing-masing 10 pertanyaan dalam skema self dan peer assessment, total permintaan mencapai sekitar 5.280 API call untuk satu kali assessment. Jika diasumsikan rata-rata konsumsi 1.000 token per permintaan, maka total penggunaan mencapai sekitar 5,28 juta token.  Mengacu pada skema harga model berbiaya rendah (± \$0,15 per 1 juta token input dan ± \$0,60 per 1 juta token output), estimasi biaya operasional berada pada kisaran \$1,5–\$3 atau sekitar Rp25.950–Rp51.900 per satu kali assessment (asumsi kurs Rp17.300/USD).  Meskipun nilai tersebut relatif kecil pada satu siklus, biaya meningkat secara linear terhadap jumlah pengguna, jumlah pertanyaan, serta frekuensi interaksi seperti iterasi revisi atau multi-step scaffolding. Selain itu, pendekatan berbasis
API memperkenalkan ketergantungan eksternal serta biaya berulang yang dinamis.
Semantic Text Similiarity in Embedding Space  |  Pendekatan semantic text similarity di ruang embedding telah dikembangkan dan divalidasi secara luas melalui beberapa penelitian berikut:  1. Reimers & Gurevych (2019) mengusulkan Sentence-BERT, sebuah modifikasi dari model pre-trained BERT  |  Pendekatan ini bekerja dengan cara mengukur jarak kedekatan dua buah vektor yang merepresentasikan kalimat.  |  Pendekatan semantic similarity berbasis SBERT dengan cosine similarity dipilih sebagai metode utama dalam penelitian ini karena memiliki keunggulan performa yang stabil, efisiensi tinggi, dan kesesuaian penuh dengan karakteristik data rubrik penilaian.  Secara empiris, Reimers & Gurevych (2019) menunjukkan bahwa arsitektur siamese network pada SBERT
yang menggunakan arsitektur siamese dan triplet untuk menghasilkan sentence: menghasilkan <i>sentence embeddings</i> yang bermakna secara semantik dan dapat dibandingkan langsung melalui <i>cosine</i>

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**IV.3.2 Desain Pipeline Digital Scaffolding**

Dengan menggunakan pendekatan semantic text similarity, sebagaimana dijelaskan pada Tabel IV.14, arsitektur digital scaffolding dibangun sepenuhnya menggunakan model SBERT sebagai alat embedding. Mekanisme dari arsitektur ini disajikan pada [Gambar IV.13](#page-2-0).

Direpresentasikan pada [Gambar IV.13](#page-2-0), langkah pertama dalam pipeline digital scaffolding adalah melakukan embedding terhadap kriteria rubrik yang telah dilakukan proses dekomposisi, sebagaimana didefinisikan pada subbab III.6.3.1B. Kemudian, selama mahasiswa menulis feedback, narasi diproses secara real-time untuk dilakukan embedding dalam menentukan semantic similarity dengan kriteria rubrik.

Nilai semantic similarity digunakan sebagai landasan komputasi indikator cakupan rubrik (@), koherensi skor dan narasi (A), elaborasi (`), dan relevansi topik (J). Komputasi tersebut menghasilkan variabel kontekstual yang digunakan untuk memproduksi teks scaffolding akhir yang diberikan kepada mahasiswa.

Gambar IV.13 Desain Pipeline yang Dibangun

**IV.3.2.1 Kandidat Model Embedding**

Untuk mendukung proses eksperimen yang dipetakan pada subbab III.6.3.2 dan pendekatan komputasional yang didefinisikan pada Tabel IV.14, pemilihan model sentence embedding didasarkan pada tiga kriteria, yaitu: (1) dukungan multilingual dengan performa yang terverifikasi pada bahasa Indonesia, (2) ukuran model di bawah satu miliar parameter untuk kompabilitas dengan deployment real-time, dan (3) ketersediaan bukti empiris pada benchmark multilingual.

Seluruh model kandidat yang dievaluasi dikelompokkan ke dalam tiga kategori berdasarkan arsitektur dan pendekatan training, sebagaimana disajikan pada [Tabel](#page-3-0)  [IV.15](#page-3-0).

Tabel IV.15. Kandidat Model Sentence Embedding

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dalam mengimplementasi model "intfloat/multilingual-e5-large-instruct" yang didefinisikan pada [Tabel IV.15,](#page-3-0) instruksi yang digunakan disajikan pada [Tabel](#page-5-0)  [IV.16.](#page-5-0)

Tabel IV.16. Instruksi Model Untuk Indikator

Indikator: Instruksi
Cakupan Rubrik (@ ): Temukan teks feedback yang secara eksplisit membahas kriteria rubrik
berikut
Koherensi Skor dan: Temukan teks feedback yang konsisten dengan tingkat penilaian
Narasi (A ): berikut
Relevansi Topik (J ): Temukan teks feedback yang relevan dengan aspek rubrik ini dan tidak
membahas aspek rubrik lainnya

**IV.3.3 Landasan Formal dan Pemodelan Pipeline**

Subbab ini mendukung pengembangan pipeline digital scaffolding dengan menjelaskan perumusan matematis keempat indikator tekstual narasi, sebagaimana didefinisikan pada Tabel III.3. Bagian ini berfungsi untuk memetakan definisi formal dari setiap komputasi yang dilakukan sistem, dimulai dari semantic chunking yang didefinisikan pada subbab [IV.3.3.2,](#page-8-0) sebelum mekanisme analisa narasi feedback yang dijabarkan pada subbab [IV.3.3.3](#page-10-0).

**IV.3.3.1 Part-of-Speech Tagging**

Untuk mencegah narasi feedback yang berisi teks acak tanpa makna, sistem menerapkan mekanisme identifikasi struktur gramatikal klausa. Menurut Moeliono (2017), syarat minimal terbentuknya sebuah kalimat independen dalam bahasa Indonesia adalah terpenuhinya fungsi subjek dan predikat.

Dalam mendukung hal tersebut, identifikasi diimplementasikan menggunakan NLP toolkit Stanza (Qi et al., n.d.) melalui teknik Part-of-Speech (POS) tagging. Sistem mengekstraksi representasi leksikal dari setiap narasi feedback dan memvalidasi keberadaan kelas kata pengganti subjek, yang umumnya didominasi oleh nomina (NOUN), pranomina (PRON), atau nomina propria (PROPN). Selanjutnya, sistem memvalidasi eksistensi predikat.

Dalam bahasa Indonesia, terdapat variasi kalimat berpredikat non-verbal Moeliono (2017). Oleh karena itu, aturan filter pada sistem dirancang untuk menerima verba (VERB), auxiliary (AUX), adjektiva (ADJ), dan adverba (ADV) sebagai parameter validasi predikat. Apabila representasi POS tag dari narasi feedback gagal memenuhi struktur hierarkis subjek-predikat ini, sistem menolak teks tersebut sebelum dilanjutkan ke tahap komputasi indikator tekstual narasi. Metode ini sejalan dengan kaidah dasar NLP untuk memfilter struktur noise tanpa makna (Jurafsky & Martin, 2009).

Validasi input dievaluasi pada setiap teks narasi feedback (+,+). Melalui proses tokenisasi, teks +,+ dipecah menjadi himpunan token . Setiap token Å ∈ memiliki atribut kelas kata (ÅXWL) dan panjang karakter (|Å+Y,+|). Berdasarkan tata bahasa baku, sistem mengekstraksi dua himpunan syarat fungsi dari +,+, yaitu: (1) himpunan kandidat predikat (7), dan (2) himpunan kandidat subjek (1).

Syarat pertama, yaitu himpunan kandidat predikat (7), diimplementasikan dengan mengisolasi token dari +,+ yang kelas katanya merepresentasikan tindakan, keadaan, atau keterangan, sebagaimana disajikan pada rumus [IV.26.](#page-6-0)

$$P = \{t \in T | t_{pos} \in \{VERB, AUX, ADJ, ADV\}\}$$
 (IV.26)

Syarat kedua, yaitu himpunan kandidat subjek (S), direalisasikan dengan mengisolasi token pronomina, atau nonima atau nomina propria dengan batasan panjang karakter di atas 1 untuk menggugurkan teks dengan satu huruf, sebagaimana disajikan pada rumus IV.27.

$$S = \{t \in T | t_{pos} = PRON \lor (t_{pos} \in (NOUN, PROPN) \land |t_{text}| > 1)\} \quad \text{(IV.27)}$$

Teks narasi feedback ( $s_{txt}$ ) ditetapkan valid apabila memenuhi eksistensi minimal satu elemen subjek dan satu elemen predikat, sebagaimana direpresentasikan pada rumus IV.28.

$$POS(s_{txt}) = \begin{cases} Valid, jika \ (|S| \ge 1) \land (|P| \ge 1) \\ Invalid, jika \ lainnya \end{cases}$$
 (IV.28)

Tabel IV.17 menyajikan contoh skenario evaluasi narasi feedback menggunakan mekanisme dan rumus yang telah dipetakan.

Ekstraksi POS Skenario Input Teks Evaluasi Status Alasan Tag Himpunan Input Klausa "Saya merevisi Saya (PRON), S = 2Valid Memiliki laporan" P = 1Verbal merevisi (VERB), subjek dan Sempurna laporan (NOUN) predikat Klausa "Aplikasi ini Aplikasi (NOUN), S = 2Valid Memiliki Adjektivial lambat" ini (PRON), lambat P = 1subjek dan Sempurna predikat non-(ADJ) verbal "asdf hjkl" S = 0Input acak Invalid Tidak P = 0terdapat kelas kata baku

Tabel IV.17. Skenario Evaluasi Part-of-Speech Taging

Untuk menyederhanakan komputasi, Gambar IV.14 menyajikan representasi identifikasi part-pf-speech tagging melalui notasi flowchart.

Gambar IV.14. Flowchart Part-of-Speech Tagging

**IV.3.3.2 Semantic Chunking**

Teks narasi feedback mahasiswa, terutama yang memiliki volume teks yang panjang umumnya bersifat multi-aspek, di mana terdapat beberapa dimensi penilaian berbeda yang dibahas dalam satu narasi. Apabila keseluruhan teks narasi dilakukan embedding sebagai satu kesatuan, representasi vektor yang dihasilkan merupakan agregasi dari seluruh kalimat, dilakukan melalui mekanisme mean  pooling pada level token. Kondisi ini dapat menyebabkan embedding dilution, yaitu informasi spesifik terhomogenisasi oleh informasi dari kalimat lain, sehingga menurunkan nilai cosine similarity pada kriteria target (L. Wang et al., 2024).

Sebagai solusi terhadap masalah tersebut, diusulkan teknik semantic chunking berbasis kalimat yang menggunakan library SpaCy dari sentencizer sebagai komponen segmentasi. Library ini bekerja dengan cara memecah teks secara deterministik berdasarkan himpunan karakter penanda akhir kalimat (stop words), sebagaimana disajikan [Gambar IV.15.](#page-9-0)

Gambar IV.15 Mekanisme Semantic Chunking menggunakan Sentencizer Secara formal, fungsi segmentasi dinyatakan pada rumus [IV.29.](#page-9-1)

$$U(s_{txt}) = \{u_1, u_2, \dots, u_k\} = sentencizer(s_{txt})$$
 (IV.29)

Di mana +,+ adalah teks narasi utuh dari feedback, dan setiap Ç adalah kalimat hasil segmentasi. Kemudian, untuk mengagregasikan similarity dari level kalimat ke level narasi, digunakan operator maksimum, yaitu:

$$sim_{splitmax}(x_1, x_2) = \max_{\{u_m \in U(x_1)\}} sim(x_1, x_2)$$
 (IV.30)

Di mana sim. , . merupakan fungsi cosine similarity yang didefinisikan pada subbab II.1.7.2. @ dan A merupakan pasangan teks yang dikomputasi, dalam penelitian ini, @ merupakan narasi feedback (+,+). Hal ini dilakukan untuk mendukung nilai similarity yang tinggi pada satu kalimat dalam merepresentasikan keseluruhan narasi.

Pemilihan kalimat sebagai unit segmentasi didasarkan pada prinsip otomisitas semantik, yaitu bahwa kalimat merupakan unit terkecil yang memuat proposisi independen secara gramatikal dan semantik (Quirk et al., 1985).

Berbeda dengan pendekatan fixed-size chunking yang memotong teks berdasarkan panjang karakter atau token secara arbiter, segmentasi berbasis kalimat memastikan bahwa setiap unit teks memiliki makna yang utuh. Hal ini selaras dengan argumen Qin et al. (2017) mengenai pentingnya menjaga batas kalimat dalam pemrosesan teks, di mana sistem memastikan bahwa fitur yang diekstraksi berasal dari konteks yang lengkap. Lebih jauh, metode semantic chunking dibandingkan secara empiris terhadap whole-text embedding pada eksperimen di subbab IV.3.4.2 untuk memverifikasi apakah keunggulan teoretis ini terkonfirmasi pada data aktual.

**IV.3.3.3 Representasi Vektor dan Metrik Semantik**

Subbab ini mendefinisikan formulasi fungsi evaluasi operasional dari keempat indikator tekstual narasi feedback pada Tabel III.3. Seluruh fungsi dirumuskan berdasarkan mekanisme embedding dan cosine similiarity yang telah dijelaskan pada subbab II.1.7.1 hingga II.1.7.2. Fungsi tersebut diimplementasikan sebagai acuan utama dalam evaluasi dan eksperimen model, sebagaimana dijabarkan pada subbab 0.

Evaluasi dilakukan pada tingkat pasangan narasi feedback (+,+) dengan himpunan feature-set åçé-, serta åçU-, yang telah didefinisikan pada subbab IV.2.1.1 dan IV.2.1.2. Setiap pasangan tersebut diasosiasikan dengan label anotasi TRUE/FALSE yang dihasilkan pada subbab IV.2.3. Evaluasi dilakukan untuk memprediksi nilai label anotasi dalam membangun mekanisme deteksi keempat indikator tekstual pada Tabel III.3.

Formulasi keempat nilai indikator tekstual tersebut didefinisikan pada subbab [IV.3.3.3A](#page-11-0) hingga IV.3.3.3D. Hasil komputasi direpresentasikan sebagai = [@ , <sup>A</sup> , ` , <sup>J</sup> ] yang membentuk vektor pemenuhan indikator sebagai acuan utama dalam rule-based system pada subbab IV.3.5.

Lebih jauh, subbab ini mendefinisikan penggunaan fungsi similarity whole-text embedding dengan semantic chunking yang telah didefinisikan pada subbab [IV.3.3.2](#page-8-0). Dengan evaluasi performa pendekatan kedua embedding tersebut disajikan pada subbab IV.3.4.2.

**A. Cakupan Rubrik (**Ø°**)**

Indikator pertama berfokus untuk mengevaluasi sejauh mana narasi feedback membahas kriteria rubrik. Secara komputasional, indikator didefinisikan melalui fungsi similiarity antara narasi feedback (+,+) dengan feature-set cakupan dan relevansi topik (åçU-, ) yang didefinisikan pada subbab IV.2.1.1, sebagaimana disajikan pada rumus [IV.31](#page-11-1).

$$\tilde{y}(s_{txt}, c_{cov,i}) = \begin{cases} 1, & sim_x(s_{txt}, c_{cov,i}) \ge \theta_{sim,1} \\ 0, & sebaliknya \end{cases}$$
(IV.31)

Di mana KLF,@ adalah threshold cosine similarity indikator cakupan rubrik yang didapatkan melalui evaluasi pada subbab 0. Di sisi lain,. 2èW%, merupakan unit dekomposisi kriteria rubrik yang didefinisikan pada subbab IV.2.1.1. Fungsi ,. , . merujuk pada salah satu dari dua varian fungsi similarity yang dievaluasi, yaitu whole-text cosine similarity (. , . ) atau semantic chunking (LX[+F\,. , . ), sebagaimana didefinisikan pada subbab II.1.7.2 dan [IV.3.3.2](#page-8-0). Pemilihan varian dilakukan berdasarkan hasil eksperimen komparatif pada subbab IV.3.4.2.

Selanjutnya, nilai cakupan  $f_1$  dihitung sebagai proporsi kriteria yang terdeteksi. Sebagaimana disajikan pada rumus IV.32.

$$f_1(s_{txt}, COV(K_{i,j})) = \frac{\sum_{c_{cov,i} \in COV(K_{i,j})} \check{y}(s_{txt}, c_{cov,i})}{|COV(K_{i,j})|}$$
(IV.32)

Dengan  $COV(K_{i,j})$  merupakan feature-set untuk cakupan dan relevansi topik, didefinisikan pada subbab IV.2.1.1. Fungsi ini menghasilkan nilai bilangan real dengan nilai 0 hingga 1  $(f_1(.,.) = x \in \mathbb{R} | 0 \le x \le 1)$ , dengan 1 merepresentasikan bahwa indikator terpenuhi sempurna. Seluruh alur komputasi indikator ini disajikan pada Gambar IV.16.

Sebagai contoh komputasi indikator ini, Tabel IV.18 menyajikan perhitungan menggunakan rumus IV.31 dan IV.32 yang telah didefinisikan.

Tabel IV.18. Contoh Perhitungan Indikator Cakupan Rubrik

Narasi:  |  "Saya selalu mengelola waktu dengan baik  |  :''
$\theta_{sim,i}$ :: 0,7
Unit Dekomposisi  |  Isi Narasi yang Relevan  |  Similarity  |  ž
Unit Dekomposisi Ketepatan Memenuhi Deadline  |  Isi Narasi yang Relevan Tidak disebutkan  |  Similarity 0,5  |  <b>y</b> 0

Berdasarkan Tabel IV.18, narasi "Saya selalu mengelola waktu dengan baik" dengan threshold 0,7 memiliki pemenuhan indikator sebesar 0,5, sebagaimana disajikan pada rumus IV.33.

$$f_1 = \frac{0+1}{2} = \frac{1}{2} = 0.5$$
 (IV.33)

Gambar IV.16. Flowchart Komputasi Indikator Cakupan Rubrik

B. Koherensi Skor dan Narasi $(f_2)$

Indikator ini mengukur keselarasan antara skor numerik  $(s_{num})$  dan makna evaluatif dalam narasi feedback  $(s_{txt})$  menggunakan koherensi skor feature-set yang didefinisikan pada subbab IV.2.1.2.

Sebagaimana telah diuraikan pada subbab III.6.3.1D, kriteria rubrik koherensi yang telah didekomposisi ke dalam himpunan grup memiliki sifat mutually exclusive, direpresentasikan sebagai  $COH(K_{i,j}) = \{G_1, G_2, ..., G_m\}$ . Di dalam setiap grup  $G_v$ , dengan  $v \in \{1,2,...,m\}$ , terdapat deskripsi fitur  $g_{v,k}$  yang berkorespondensi dengan tingkat skor  $k \in S$ .

Komputasi indikator ini dilakukan melalui dua tahapan. Tahap pertama adalah mengumpulkan kandidat skor pada setiap  $G_v$  yang memiliki nilai cosine similarity melampaui threshold indikator ( $\theta_{sim,2}$ ). Sebagaimana disajikan pada rumus IV.34.

$$C_{\nu}(s_{txt}) = \{k \in S | sim_{x}(s_{txt}, g_{\nu,k}) \ge \theta_{sim,2}\}$$
 (IV.34)

Dengan  $sim_x(.,.)$  merujuk pada salah satu fungsi  $cosine\ similarity$ , yaitu  $wholetext\ embedding\ dan\ semantic\ chunking\ yang\ diuji\ pada\ subbab\ IV.3.4.2.$  Mengingat unit di dalam satu grup bersifat  $mutual\ exclusive$ , fungsi argmax diaplikasikan secara lokal pada himpunan kandidat  $C_v$  untuk mengekstrak prediksi skor tertinggi pada dimensi tersebut. Fungsi ini disajikan pada rumus IV.35.

$$\hat{s}_v(s_{txt}) = \arg \max_{k \in C_v(s_{txt})} sim_x(s_{txt}, g_{v,k})$$
 (IV.35)

Pada tahap kedua, sistem mengakumulasikan seluruh prediksi skor lokal dari masing-masing grup dimensi menjadi satu himpunan prediksi global  $(\hat{S})$  melalui operasi union, sebagaimana disajikan pada rumus IV.36. Hal ini memungkinkan sistem untuk mengakomondasi narasi mahasiswa yang memuat kondisi silang antar dimensi:

$$\hat{S}(s_{txt}) = \bigcup_{v=1}^{m} {\{\hat{s}_v(s_{txt})\}}$$
 (IV.36)

Sebagai tahap akhir, dilakukan verifikasi apakah skor aktual mahasiswa  $(s_{num})$  merupakan anggota dari himpunan prediksi global  $(\hat{S}(s_{txt}))$ , sebagaimana disajikan pada rumus IV.37.

$$f_2(F) = \begin{cases} 1, jika \ s_{num} \in \hat{S}(s_{txt}) \\ 0, sebaliknya \end{cases}$$
 (IV.37)

Di mana 1 merepresentasikan bahwa skor dan narasi dalam kondisi selaras, sedangkan nilai 0 merepresentasikan ketidakselarasan.

Gambar IV.17 menyajikan contoh komputasi indikator koherensi skor dan narasi menggunakan narasi "Iklan yang saya kumpulkan jumlahnya sedikit tetapi relevan" dengan  $\theta_{sim,3} = 0.8$ . Komputasi pada contoh tersebut mencangkup rumus IV.34 hingga IV.36.

Gambar IV.17. Contoh Komputasi Indikator Koherensi Skor dan Narasi

Berdasarkan hasil yang didapatkan pada Gambar IV.17,  $f_2$  bernilai 1 jika mahasiswa memberikan skor 1 ataupun 5. Sebaliknya, jika skor yang diberikan adalah 2,3, ataupun 4, maka  $f_2$  akan bernilai 0.

C. Indikator Kedalaman Elaborasi ( $f_3$ )

Indikator kedalaman elaborasi mengukur panjang teks narasi sebagai prasyarat sehingga feedback bersifat informatif.

Didefinisikan fungsi panjang teks  $L(s_{txt})$  yang mengekstraksi jumlah kata leksikal narasi feedback. Evaluasi kedalaman elaborasi diformulasikan sebagai fungsi biner yang membandingkan panjang narasi dengan threshold kata  $(\theta_{sim,3})$ :

$$f_{3} = \begin{cases} 1, & apabila L(s_{txt}) \ge \theta_{sim,3} \\ 0, & sebaliknya \end{cases}$$
 (IV.38)

Di mana  $\theta_{len}$  ditetapkan sebagai 25 kata, sebagaimana didefinisikan pada subbab IV.2.3.3. Nilai 1 mengindikasikan bahwa narasi memiliki panjang yang memadai, sedangkan 0 mengindikasikan narasi terlalu pendek.

Pendekatan ini tidak mengasumsikan bahwa panjang teks secara langsung merepresentasikan yang bersifat informatif, tetapi menetapkan batas minimal sebagai kondisi bagi keberadaan elaborasi. Dengan demikian, indikator ini berfungsi sebagai penyaring awal terhadap skor kualitatif/narasi yang terlalu singkat untuk memberikan nilai instruksional. Tabel IV.19 menyajikan contoh komputasi indikator elaborasi dalam berbagai skenario.

Tabel IV.19. Contoh Komputasi Indikator Elaborasi

Narasi  |  Panjang Teks  |  $f_3$
$(L(s_{txt}))$
Baik  |  1  |  0
Saya mengumpulkan banyak iklan. Setiap iklannya sangat relevan. Saya  |  24  |  0
menggunakan banyak sekali platform, mulai dari instagram, twitter,
linkedin, facebook, WhatsApp, dan platform platform lainnya
Saya mengumpulkan banyak iklan. Setiap iklannya sangat relevan. Saya  |  25  |  1
menggunakan banyak sekali platform, mulai dari instagram, twitter,
linkedin, facebook, WhatsApp, dan platform platform lainnya, banyak.
Saya mengumpulkan banyak iklan. Setiap iklannya sangat relevan. Saya  |  35  |  1
menggunakan banyak sekali platform, mulai dari instagram, twitter,
linkedin, facebook, WhatsApp, dan platform platform lainnya, banyak.
Bahkan saya membantu teman saya mencari iklan dari platform
glassdoor

D. Indikator Relevansi Topik $(f_4)$

Indikator ini mengevaluasi apakah narasi fokus pada aspek penilaian yang dituju. Feedback terdeteksi tidak relevan apabila narasi memiliki nilai similarity setara atau di atas treshold terhadap kriteria lain yang tidak sedang dinilai dari rubrik. Hal ini mengindikasikan bahwa mahasiswa salah sasaran dalam memberikan justifikasi evaluatif.

Didefinisikan  $\mathcal{K}$  sebagai himpunan seluruh kriteria rubrik, diturunkan dari definisi pada rumus III.12 dan III.13. Sebagaimana disajikan pada rumus IV.39, dengan  $A_i$  merepresentasikan aspek ke-i.

$$\mathcal{K} = \bigcup_{i=1}^{n} A_i \tag{IV.39}$$

Kriteria rubrik yang menjadi fokus penilaian dinotasikan sebagai  $K_{i,j}$ . Di sisi lain,  $K_{other}$  merepresentasikan himpunan seluruh unit dekomposisi yang tidak termasuk ke dalam kriteria yang sedang dinilai, disajikan pada rumus IV.41.

$$K_{other}(K_{i,j}) = \bigcup_{K' \in \mathcal{K} \setminus K_{i,j}} COV(K')$$
(IV.40)

Dengan COV(.) didefinisikan pada rumus III.16.

Secara konseptual, fungsi indikator relevansi topik dievaluasi menggunakan rumus IV.41.

$$f_4(F) = \begin{cases} 0, & apabila \ \exists c \in K_{other}(K_{i,j}) : sim_x(s_{txt}, c) \ge \theta_{sim,4} \\ 1, & sebaliknya \end{cases}$$
(IV.41)

Di mana  $\theta_{sim,4}$  adalah threshold semantic similarity untuk indikator koherensi skor dan narasi. Nilai 0 mengindikasikan bahwa narasi membahas kriteria lain di luar kriteria penilaian. Di sisi lain, nilai 1 mengindikasikan bahwa narasi telah berfokus pada kriteria yang dinilai. Dengan  $sim_x(.,.)$  merepresentasikan salah satu fungsi cosine similarity, yaitu whole-text embedding yang didefinisikan pada subbab II.1.7.2, dan semantic chunking yang disajikan pada subbab IV.3.3.2. Contoh alur komputasi indikator ini disajikan pada Gambar IV.18.

Gambar IV.18. Contoh Komputasi Indikator Relevansi Topik

**IV.3.4 Hasil Evaluasi dan Kalibrasi Model**

Subbab ini merupakan manifestasi dari tahap pengembangan sistem yang didefinisikan pada subbab III.6.3.2, dilakukan dengan mengevaluasi performa setiap kandidat model yang telah diseleksi pada subbab IV.3.2.1 serta instruksi pada Tabel IV.16 menggunakan kode yang dieksekusi melalui google colab. Evaluasi dilakukan dengan membandingkan hasil prediksi model berdasarkan mekanisme grid-search yang telah didefinisikan pada subbab II.1.7.4 feature-set dan hasil anotasi dataset sebagai ground truth pada subbab IV.2.1 dan IV.2.3.

[Gambar IV.19](#page-5-0) menyajikan mekanisme kalibrasi dalam evaluasi performa model. Indikator yang dievaluasi adalah cakupan rubrik (@), koherensi skor dan narasi (A), serta relevansi topik (J). Dalam mengevaluasi indikator koherensi skor dan narasi (A), digunakan feature-set koherensi skor (åçé-, ) pada subbab IV.2.1.2 sebagai pasangan narasi feedback. Di sisi lain, evaluasi indikator cakupan rubrik (@) dan relevansi topik (J) dilakukan dengan menggunakan feature-set åçU-, yang didefinisikan pada subbab IV.2.1.1.

Eksperimen dilakukan dengan tiga metode implementasi yang berbeda. Metode pertama adalah komputasi cosine similarity dengan whole-text embedding, sebagaimana didefinisikan pada subbab II.1.7.1 dan II.1.7.2, disajikan pada subbab [IV.3.4.1](#page-6-0). Metode kedua adalah realisasi dari semantic chunking pada subbab IV.3.3.2, disajikan pada subbab [IV.3.4.2.](#page-8-0) Metode ketiga adalah implementasi dari aturan mutual exclusive dari feature-set koherensi skor dan narasi yang didefinisikan pada subbab III.6.3.1D, disajikan pada subbab [IV.3.4.3.](#page-10-0)

Output akhir dari tahap evaluasi dan kalibrasi model adalah konfigurasi model, threshold, dan metode implementasi terbaik untuk indikator cakupan rubrik (@), koherensi skor dan narasi (A), serta relevansi topik (J), disajikan pada subbab [IV.3.4.4.](#page-11-0) Lebih jauh, implikasi performa hasil kalibrasi disajikan pada subbab IV.3.4.6 sebagai analisis kemampuan analisis indikator komputasional.

Gambar IV.19. Mekanisme Kalibrasi Model

**IV.3.4.1 Evalauasi Performa Whole-Text Embedding**

Whole-text embedding digunakan sebagai konfigurasi dasar (baseline) dalam rangkaian eksperimen kalibrasi model. Pada tahap ini, seluruh kandidat model embedding dievaluasi menggunakan representasi narasi secara utuh tanpa penerapan teknik pemrosesan tambahan, seperti semantic chunking maupun aturan mutual exclusivity. Evaluasi baseline ini bertujuan menyediakan acuan performa awal sehingga pengaruh setiap teknik tambahan terhadap masing-masing kandidat model dapat dibandingkan secara konsisten pada tahap eksperimen berikutnya.

Metode ini bekerja dengan merepresentasikan keseluruhan narasi feedback sebagai satu embedding yang kemudian dibandingkan dengan feature-set hasil dekomposisi pada Whole-text embedding merupakan metode pertama yang dievaluasi, sebagaimana didefinisikan pada subbab II.1.7.1 dan II.1.7.2. Metode ini bekerja dengan cara memproses embedding dari narasi feedback utuh dengan feature-set hasil dekomposisi pada subbab IV.2.1.

[Tabel IV.20](#page-6-1) menyajikan performa seluruh kandidat model pada indikator cakupan rubrik (@) menggunakan whole-text embedding. Performa yang diukur tidak mencakup fungsi semantic chunking yang dijabarkan pada subbab IV.3.3.2.

Tabel IV.20. Performa Model pada Indikator Cakupan Rubrik (@)

Model  |  Optimal Threshold (ª£lº,°)  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet-base-v2  |  0,27  |  0,5822  |  0,4415  |  0,8545
intfloat/multilingual-e5-base  |  0,81  |  0,5926  |  0,4604  |  0,8314
intfloat/multilingual-e5-base dengan query / passage prefix  |  0,81  |  0,5760  |  0,4315  |  0,8661
intfloat/multilingual-e5-large-instruct  |  0,84  |  0,6131  |  0,5323  |  0,7229
denaya/indoSBERT-large  |  0,36  |  0,6002  |  0,4940  |  0,7644
paraphrase-multilingual-MiniLM-L12-v2  |  0,16  |  0,5706  |  0,4166  |  0,9053

[Tabel IV.20](#page-6-1) menunjukkan bahwa model "intfloat/multilingual-e5-large-instruct" memiliki F1 tertinggi di antara seluruh kandidat, dengan nilai 0,6131. Hal ini mengkonfirmasi keunggulan instruksi tuning eksplisit untuk task retrieval semantik berbasis rubrik. Di sisi lain, model spesifik bahasa Indonesia "denaya/indoSBERT-

large" menempati posisi kedua dengan F1 sebesar 0,6002. Temuan ini membuktikan bahwa meskipun indoSBERT-large dilatih secara eksklusif dan dioptimasi pada korpus bahasa Indonesia, kemampuannya dalam memetakan cakupan rubrik masih belum mampu melampaui arsitektur multilingual berparameter besar yang dikombinasikan dengan instruksi tugas yang spesifik.

Indikator koherensi skor dan narasi (A) memiliki pola yang serupa, sebagaimana disajikan pada [Tabel IV.21](#page-7-0). Evaluasi performa tersebut menggunakan feature-set åçU-, yang diperoleh pada subbab IV.2.1.2, namun tidak mengimplementasikan sifat mutual exclusivity yang telah didefinisikan pada subbab III.6.3.1D. Hal tersebut dilakukan guna mengukur performa model tanpa aturan spesifik dari indikator koherensi skor dan narasi (A).

Tabel IV.21. Performa Model pada Indikator Koherensi Skor dan Narasi

Model  |  Optimal Threshold (££lº,ø)  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet-base-v2  |  0,44  |  0,4193  |  0,3129  |  0,6353
intfloat/multilingual-e5-base  |  0,84  |  0,3751  |  0,2778  |  0,5775
intfloat/multilingual-e5-base dengan query / passage prefix  |  0,83  |  0,3958  |  0,3011  |  0,5775
intfloat/multilingual-e5-large-instruct  |  0,89  |  0,5020  |  0,4458  |  0,5745
denaya/indoSBERT-large  |  0,45  |  0,4139  |  0,3226  |  0,5775
paraphrase-multilingual-MiniLM-L12-v2  |  0,48  |  0,3722  |  0,3189  |  0,4468

Berdasarkan [Tabel IV.21](#page-7-0), model "intfloat/multilingual-e5-large-instruct" kembali mendominasi dengan nilai F1 sebesar 0,5020. Model "denaya/indoSBERT-large" mencatatkan F1 sebesar 0,4139, bersaing ketat dengan "paraphrase-multilingualmpnet-base-v2" (0,4193). Hasil ini menunjukkan bahwa untuk tugas mencocokkan koherensi skor yang membutuhkan pemahaman gradasi makna secara presisi, kapabilitas instruction tuning pada e5-large-instruct memberikan keuntungan komputasional yang lebih krusial dibandingkan lokalisasi pelatihan pada satu bahasa spesifik.

Pola yang sama terjadi pada indikator relevansi topik (J), sebagaimana disajikan pada [Tabel IV.22.](#page-8-1) Performa pada indikator ini menunjukkan bahwa model "intfloat/multilingual-e5-large-instruct" berhasil mencapai F1 tertinggi. Model "denaya/indoSBERT-large" kembali menyusul pada posisi kedua dengan F1 sebesar 0,3605.

Tabel IV.22. Performa Model pada Indikator Relevansi Topik

Model  |  Optimal Threshold ª£lº,«  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet-base-v2  |  0,53  |  0,3071  |  0,3209  |  0,2944
intfloat/multilingual-e5-base  |  0,84  |  0,2924  |  0,2418  |  0,3698
intfloat/multilingual-e5-base dengan query / passage prefix  |  0,83  |  0,3188  |  0,2421  |  0,4668
intfloat/multilingual-e5-large-instruct  |  0,85  |  0,4296  |  0,4265  |  0,4327
denaya/indoSBERT-large  |  0,48  |  0,3605  |  0,2981  |  0.4560
paraphrase-multilingual-MiniLM-L12-v2  |  0,40  |  0,2575  |  0,1824  |  0,4381

Secara keseluruhan, sintesis dari ketiga pengujian whole-text ini secara konklusif menggugurkan asumsi awal bahwa spesialisasi model monolingual bahasa Indonesia akan selalu mengungguli model multilingual. Arsitektur berparameter raksasa yang mendukung intervensi instruction tuning terbukti lebih superior dalam menangani kompleksitas semantik narasi feedback mahasiswa.

**IV.3.4.2 Evaluasi Semantic Chunking**

Sebagai ekstensi dari pengukuran performa model yang dilakukan pada subbab [IV.3.4.1](#page-6-0), subbab ini mengevaluasi implementasi semantic chunking yang telah didefinisikan pada subbab IV.3.3.2. Hal tersebut dilakukan untuk mengukur dampak metode tersebut terhadap setiap indikator komputasi untuk setiap model embedding.

[Tabel IV.23](#page-9-0) menyajikan nilai F1 untuk setiap indikator komputasi pada seluruh kandidat model embedding, dengan ΔF1(%) merepresentasikan selisih performa dibandingkan dengan metode whole-text embedding pada subbab [IV.3.4.1.](#page-6-0)

Tabel IV.23. Peningkatan Performa Model dengan Semantic Chunking

Model  |  Cakupan Rubrik (f <sub>1</sub> )  |  Koherensi Skor dan Narasi (f <sub>2</sub> )  |  nsi Topik f <sub>4</sub> )
F1Score  |  ΔF1(%)  |  F1Score  |  ΔF1(%)  |  F1Score  |  ΔF1(%)
paraphrase-multilingual- mpnet-base-v2  |  0,5820  |  -0,034%  |  0,4216  |  0,549%  |  0,3200  |  4,201 %
intfloat/multilingual-e5- base  |  0,6002  |  1,282%  |  0,3829  |  2,079%  |  0,2966  |  1,436 %
intfloat/multilingual-e5- base + Prefix  |  0,5826  |  1,146%  |  0,3922  |  -0,910%  |  0,3202  |  0,439 %
intfloat/multilingual-e5- large-instruct  |  0,6140  |  0,147%  |  0,4974  |  -0,916%  |  0,4155  |  -3,282 %
denaya/indoSBERT- large  |  0,6096  |  1,566%  |  0,4195  |  1,353%  |  0,3705  |  2,774%
paraphrase-multilingual- MiniLM-L12-v2  |  0,5720  |  0,245%  |  0,3837  |  3,090%  |  0,2586  |  0,427 %

Berdasarkan Tabel IV.23, peningkatan performa akibat semantic chunking tidak terjadi secara seragam pada seluruh model. Model spesifik bahasa Indonesia, "denaya/indoSBERT-large", menunjukkan tren eskalasi yang paling konsisten di seluruh indikator, dengan puncak peningkatan +2,774% pada relevansi topik. Fenomena ini mengindikasikan bahwa model tersebut cukup rentan terhadap embedding dilution, di mana informasi penting tenggelam oleh noise saat memproses paragraf panjang, sehingga segmentasi kalimat sangat membantu mengisolasi fitur semantiknya secara lebih presisi.

Di sisi lain, model "intfloat/multilingual-e5-large-instruct" justru mengalami degradasi performa pada indikator relevansi topik (-3,282%) dan koherensi skor (-0,916%). Namun, terlepas dari dinamika peningkatan dan penurunan tersebut, nilai absolut dari model "intfloat/multilingual-e5-large-instruct" secara konsisten tetap mempertahankan performa tertinggi dibandingkan dengan kandidat model lain pada seluruh indikator.

Merujuk pada temuan tersebut, untuk konfigurasi model "intfloat/multilingual-e5-large-instruct" yang dipilih sebagai pipeline akhir, penerapan semantic chunking tidak mengubah performa indikator cakupan rubrik secara berarti ( $\Delta$ F1 = +0,147%),

namun terbukti berhasil menjaga stabilitas deteksi kriteria mencapai F1 0,6140. Sebaliknya, penerapan semantic chunking menurunkan performa pada indikator koherensi skor dan narasi serta relevansi topik. Oleh karena itu, semantic chunking hanya dipertahankan pada indikator cakupan rubrik yang secara konseptual berorientasi pada identifikasi keberadaan unit informasi spesifik di dalam teks. Detail performa seluruh model pada indikator ini disajikan pada [Tabel IV.24.](#page-10-1)

Tabel IV.24. Performa Cakupan Rubrik dengan Semantic Chunking

Model  |  Optimal Threshold (ª£lº,°)  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet-base-v2  |  0,27  |  0,5820  |  0,4406  |  0,8568
intfloat/multilingual-e5-base  |  0,81  |  0,6002  |  0,4646  |  0,8476
intfloat/multilingual-e5-base dengan query / passage prefix  |  0,81  |  0,5826  |  0,4327  |  0,8915
intfloat/multilingual-e5-large-instruct  |  0,84  |  0,6140  |  0,5312  |  0,7275
denaya/indoSBERT-large  |  0.37  |  0,6096  |  0,5000  |  0,7806
paraphrase-multilingual-MiniLM-L12-v2  |  0,16  |  0,5720  |  0,4167  |  0,9122

Penurunan performa yang terjadi pada indikator relevansi topik (J) dan koherensi skor (A) pada pipeline utama merupakan dampak langsung dari metode segmentasi yang menghilangkan global context dari narasi utuh. Kedua indikator tersebut membutuhkan pemahaman terhadap sentimen dan alur teks secara keseluruhan, mengingat justifikasi evaluatif mahasiswa seringkali dibangun melalui kohesi antarkalimat. Sebaliknya, indikator cakupan rubrik (@) murni menelusuri eksistensi informasi spesifik, sehingga isolasi kalimat sangat menguntungkan indikator ini karena mereduksi embedding dilution tanpa merusak parameter evaluasinya.

**IV.3.4.3 Evaluasi Dampak Sifat Mutual Exlusivity pada Koherensi Skor dan Narasi**

Evaluasi yang dilakukan pada subbab ini merupakan manifestasi dari sifat mutual exclusivity yang didefinisikan pada subbab III.6.3.1D dan IV.3.3.3B. Hal tersebut dilakukan untuk mengukur dampak terhadap aturan eksplisit dalam memprediksi label pasangan narasi dengan feature-set koherensi skor dan narasi (åçU-, ) yang didapatkan pada subbab IV.2.1.2. Hasil eksperimen disajikan pada Tabel [IV.25,](#page-11-1) dengan ΔF1(%) merepresentasikan selisih nilai F1 dengan whole-text embedding dalam subbab [IV.3.4.1.](#page-6-0)

Tabel IV.25. Performa Sifat Mutual Exclusivity pada <sup>A</sup>

Model  |  Opitmal Threshold (ª£lº,ø)  |  F1  |  ∆F1 (%)  |  Precision  |  Recall
paraphrase-multilingual-mpnet base-v2  |  0,35  |  0,4315  |  2,910 %  |  0,3422  |  0,5836
intfloat/multilingual-e5-base  |  0,84  |  0,3954  |  5,412 %  |  0,3717  |  0,4225
intfloat/multilingual-e5-base dengan query / passage prefix  |  0,83  |  0,3932  |  -0,657 %  |  0,3700  |  0,4195
intfloat/multilingual-e5-large instruct  |  0,87  |  0,5314  |  5,857 %  |  0,4409  |  0,6687
denaya/indoSBERT-large  |  0,4  |  0,4386  |  5,968%  |  0,3879  |  0,5046
paraphrase-multilingual-MiniLM L12-v2  |  0,23  |  0,4024  |  8,114 %  |  0,3008  |  0,6079

[Tabel IV.25](#page-11-1) menunjukkan bahwa peningkatan performa tidak terjadi secara konsisten pada seluruh model. Ditemukan bahwa model "paraphrase-multilingual-MiniLM-L12-v2" mendapatkan manfaat terbesar dengan selisih nilai F1 sebesar 8,114%, diikuti oleh model spesifik bahasa Indonesia "denaya/indoSBERT-large" yang mencatatkan peningkatan sebesar 5,968%, dan model "intfloat/multilinguale5-large-instruct" dengan peningkatan sebesar 5,857%.

Lonjakan performa pada "denaya/indoSBERT-large" ini kembali mengindikasikan bahwa model tersebut sangat terbantu oleh aturan mutually exclusive untuk membedakan gradasi skor rubrik secara presisi. Meskipun demikian, setelah mendapatkan intervensi aturan yang sama, model "intfloat/multilingual-e5-largeinstruct" tetap kokoh mempertahankan posisinya sebagai model dengan performa absolut tertinggi (F1: 0,5314). Hal ini menegaskan bahwa kombinasi antara arsitektur instruction-tuning yang mumpuni dengan kontrol logika yang membatasi ruang prediksi menghasilkan kualitas deteksi koherensi yang optimal.

**IV.3.4.4 Konfigurasi Akhir Model & Temuan Eksperimen**

Ketiga eksperimen sebelumnya tidak dimaksudkan sebagai evaluasi yang [berdiri](#page-11-1)  sendiri, melainkan sebagai proses seleksi konfigurasi pipeline. Oleh karena itu, konfigurasi akhir ditentukan berdasarkan sintesis hasil ketiga eksperimen dengan mempertimbangkan performa pada masing-masing indikator, bukan berdasarkan satu metode yang diterapkan secara seragam pada seluruh pipeline.

Hasil eksperimen pada subbab [IV.3.4.1](#page-6-0) hingga [IV.3.4.3](#page-10-0) menunjukkan bahwa model "intfloat/multilingual-e5-large-instruct" secara konsisten mencapai nilai F1 tertinggi di antara seluruh kandidat. Rangkaian pengujian komparatif ini menghasilkan satu temuan, yaitu bahwa spesialisasi korpus pada bahasa Indonesia melalui model indoSBERT-large tidak mampu melampaui performa model multilingual yang dilengkapi dengan instruction-tuning eksplisit. Arsitektur yang dikendalikan oleh instruksi tugas spesifik memiliki performa yang lebih tinggi dalam menangani kompleksitas dan ambiguitas semantik pada narasi feedback mahasiswa. Keunggulan ini mengindikasikan kemampuan model dalam menangkap kesamaan semantik yang lebih presisi pada konteks rubrik berbahasa alami, sehingga "intfloat/multilingual-e5-large-instruct" dipilih sebagai representasi embedding utama dalam pipeline.

Pada indikator cakupan rubrik (@), penerapan strategi semantic chunking yang didefinisikan pada subbab IV.3.3.2 menunjukkan peningkatan performa dibandingkan representasi whole-text embedding pada sebagian besar model. Oleh karena itu, pendekatan ini dipilih sebagai mekanisme operasional untuk menghitung similarity pada indikator tersebut.

Pada indikator koherensi skor dan narasi (A), integrasi sifat mutual exclusivity yang didefinisikan pada subbab [IV.3.3.3D](#page-2-2) dipilih sebagai konfigurasi akhir, integrasi aturan mutual exclusivity meningkatkan F1-score dibandingkan pendekatan similarity murni. Oleh karena itu, aturan tersebut dipertahankan sebagai bagian dari pipeline akhir untuk indikator koherensi skor dan narasi.

Berdasarkan sintesis tersebut, konfigurasi akhir pipeline ditetapkan sebagai kombinasi dari:

1. Model "embedding intfloat/multilingual-e5-large-instruct" untuk komputasi indikator cakupan rubrik  $(f_1)$ , koherensi skor dan narasi  $(f_2)$ , serta relevansi topik  $(f_4)$ .
2. Strategi semantic chunking untuk komputasi indikator cakupan rubrik  $(f_1)$ .
3. Mekanisme mutual exclusivity untuk indikator koherensi skor dan narasi  $(f_2)$ , dan
4. Aturan heuristik berbasis jumlah kata leksikal untuk indikator kedalaman elaborasi  $(f_3)$  dengan nilai minimum 25 kata, sebagaimana didefinisikan pada subbab IV.2.3.3.

Performa akhir pada dataset disajikan pada Tabel IV.26.

Tabel IV.26. Performa Akhir Model untuk Setiap Indikator

intfloat/multilingual-e5-large-instruct
Indikator: $ \begin{array}{c ccccccccccccccccccccccccccccccccccc$
Cakupan Rubrik $(f_1)$  |  0.84  |  0.6140  |  0.5312  |  0.7275
Koherensi Skor dan Narasi $(f_2)$  |  0.87  |  0.5314  |  0.4409  |  0.6687
Kedalaman Elaborasi $(f_3)$  |  25 kata  |  -  |  -  |  -
Relevansi Topik $(f_4)$  |  0.85  |  0.4296  |  0.4265  |  0.4327

Berdasarkan Tabel IV.26, indikator relevansi topik ( $f_4$ ) memiliki performa yang rendah dibandingkan dengan indikator lainnya. Hal tersebut merupakan dampak langsung dari distribusi kelas pada dataset anotasi dalam feature-set yang disajikan pada subbab IV.2.3.1. Sebagaimana analisis yang dilakukan pada subbab IV.2.3.3B, hanya terdapat 23,4% narasi feedback yang tidak memenuhi indikator relevansi topik, menyebabkan model cenderung underpredict terhadap kelas minoritas. Temuan tersebut didukung oleh Albattah & Khan (2025) yang mengonfirmasi bahwa dataset yang tidak seimbang akan mempengaruhi model  $machine\ learning\ sehingga\ terdapat\ bias\ terhadap\ kelas\ mayoritas.$

IV.3.4.5 Justifikasi Penentuan Threshold

Setiap threshold yang ditetapkan pada Tabel IV.26 merupakan keputusan desain yang mempengaruhi keseimbangan kinerja sistem. Untuk indikator berbasis embedding  $(f_1, f_2, f_4)$ , penentuan threshold similarity  $(\theta_{sim,i})$  dilakukan melalui

eksperimen metode grid-search pada rentan nilai [0,1] dengan interval 0,01. Titik threshold optimal dipilih berdasarkan nilai yang menghasilkan F1-Score tertinggi saat divalidasi terhadap dataset ground truth. Pendekatan data-driven ini memastikan bahwa threshold merepresentasikan cut-off matematis paling ideal antara sensitivitas model dan ketepatan prediksi untuk lingkungan Project-Based Learning.

Pemilihan threshold komputasional ini berdampak langsung pada konsekuensi False Positive (FP) dan False Negative (FN) dalam implementasi real-time. Pada sistem yang beroperasi dalam Zone of Proximal Development (ZPD), keseimbangan ini bersifat krusial. Jika threshold diatur teralu tinggi, risiko FN akan meningkat, sehingga mahasiswa kehilangan kesempatan untuk mendapatkan arahan. Sebaliknya, threshold yang terlalu rendah meningkatkan risiko FP, yang dapa menimbulkan kebingungan atau gangguan konsentrasi akibat scaffolding redundan. Nilai threshold optimal pada [Tabel IV.26](#page-13-0) dipilih karena secara statistik menyeimbangkan risiko tersebut, sehingga intensitasscaffolding yang muncul tidak membebani cognitive load mahasiswa secara berlebihan.

Di sisi lain, threshold untuk kedalaman elaborasi (`) diimplementasikan menggunakan aturan heuristik batas leksikal sebesar 25 kata. Penentuan threshold ini diperoleh dari analisis distribusi right-skewed panjang narasi pada 10.098 data historis. Analisis tersebut mengidentifikasi angka 25 kata sebagai titik infleksi di mana peluang pemenuhan cakupan rubrik meningkat. Konsekuensi dari threshold struktural ini adalah sifatnya yang absolut, yaitu narasi dengan 24 kata memicu False Negative untuk scaffolding elaborasi, meskipun narasi tersebut mungkin sangat padat. Namun, threshold 25 kata ini dipertahankan karena sifat pengukurannya yang deterministik dan komputasinya yang ringan.

**IV.3.4.6 Implikasi Performa terhadap Validitas Intervensi Scaffolding**

Subbab ini menganalisis lebih jauh dampak performa model pada subbab [IV.3.4.4](#page-11-0) untuk setiap indikator, sebagaimana disajikan pada Tabel IV.27

Tabel IV.27 Analisis Implikasi Performa Hasil Evaluasi dan Eksperimen

Indikator  |  Risiko Prediksi False Positive  |  Risiko Prediksi False Negative
Cakupan  |  Terdapat kemungkinan di mana  |  Terdapat kemungkinan di mana model
Rubrik (@ )  |  mahasiswa telah menulis narasi  |  memprediksi bahwa narasi feedback
feedback yang telah mencakup seluruh: telah memenuhi indikator cakupan
komponen penilaian rubrik, namun: rubrik meskipun terdapat komponen
model prediksi tetap mendeteksi: penilaian yang hilang pada narasi.
adanya komponen penilaian yang
terlewatkan.: Hal tersebut sangat berbahaya karena
mahasiswa akan mengirimkan
Hal tersebut akan berdampak pada mahasiswa yang menerima teks: feedaback yang tidak membahas seluruh komponen penilaian secara
scaffolding yang tidak diperlukan dan: lengkap.
tidak akurat.
Koherensi  |  Terdapat kemungkinan di mana narasi  |  Terdapat kemungkinan bahwa narasi
Skordan  |  feedback dianggap tidak koheren  |  dan skor yang diberikan siswa tidak
Narasi (A )  |  dengan skor yang diberikan, meskipun  |  koheren, namun sistem tidak dapat
kenyataannya sudah sesuai.: menangkap kesalahan terebut.
Hal tersebut akan membuat: Hal ini berbahaya karena feedback akhir
mahasiswa kebingungan karena: mahasiswa akan memiliki skor
mendapatkan peringatan bahwa skor: kuantitatif yang tidak selaras dengan
dan narasi tidak koheren, meskipun: narasi kualitatif yang ditulis.
faktanya berkata sebaliknya.
Relevansi  |  Terdapat kemungkinan di mana  |  Terdapat kemungkinan di mana model
Topik (J )  |  mahasiswa mendapatkan peringatan  |  tidak dapat memprediksi narasi yang
bahwa narasi tidak relevan, meskipun: tidak relevan. Hal tersebut berbahaya
faktanya sudah terfokus kepada: karena mengakibatkan mahasiswa
komponen rubrik yang dinilai.: mengirimkan feedback yang tidak
relevan dengan komponen penilaian.

Sebagaimana didefinisikan pada subbab IV.3.4.4, indikator relevansi topik (J) memiliki performa yang paling rendah di antara seluruh indikator lainnya. Meskipun demikian, hal tersebut dapat dimitigasi oleh tiga indikator lainnya yang bekerja secara kolaboratif. Narasi yang benar-benar tidak relevan umumnya juga tidak memenuhi indikator cakupan rubrik (@ , sehingga intervensi tetap dipicu melalui jalur alternatif meskipun indikator relevansi topik (J) menghasilkan false negative. Dalam konteks pilot study, performa pipeline saat ini dianggap memadai sebagai proof-of-concept untuk mengevaluasi feasibility arsitektur.

**IV.3.4.7 Analisis Keterbatasan Model**

Subbab ini merupakan ekstensi dari analisa yang diakukan pada subbab IV.3.4.6. Meskipun hasil evaluasi telah mencapai tingkat klasifikasi yang memadai untuk implementasi tahap awal, pengujian terhadap edge cases mengungkapkan beberapa keterbatasan fundamental dari representasi semantic embedding. Keterbatasan ini memberikan pandangan mengenai batasan komputasional sistem.

**A. Kelemahan Pemetaan Kuantitas Numerik Terhadap Semantik Abstrak**

Model prediksi menunjukkan sensitivitas yang rendah dalam memetakan angka kuantitatif pasti ke dalam kategori ordinal abstrak murni. Pengujian dilakukan dengan menggunakan narasi "5 iklan hari ini, yang mana itu kurang dari target" terhadap aspek "Pengumpulan Iklan Lowongan Kerja" dalam rubrik yang didefinisikan pada Tabel II.1.

Narasi tersebut menghasilkan nilai cosine similarity sebesar 0,8921 pada skala 1, dan 0,8964 pada skala 3. Margin 0,004 mengindikasikan bahwa representasi vektor kesulitan melakukan penalaran matematis-komparatif. Keterbatasan ini mengakibatkan sistem sangat rentan terhadap prediksi false positive ataupun false negative.

**B. Kegagalan Disambiguasi Overlapping Topik**

Ditemukan bahwa sistem rentan mengalami kegagalan klasifikasi pada indikator relevansi topik (J) ketika mengevaluasi narasi yang mengandung irisan kosakata antar aspek rubrik.

Pengujian dilakukan terhadap aspek "Kolaborasi dan Kerjasama Tim" pada rubrik dalam Tabel II.1, dengan narasi "membantu kami menggabungkan data". Ditemukan bahwa sistem menghasilkan nilai cosine similarity sebesar 0,8695 pada aspek "Penggabungan Data dengan Kelompok Lain". Nilai cosine similarity tersebut melebihi threshold (KLF,J) yang telah ditetapkan pada Tabel IV.26.

Hal tersebut mengakibatkan model mendeteksi bahwa narasi tidak terfokus pada aspek yang dinilai, yaitu "Kolaborasi dan Kerjasama Tim", meskipun narasi tersebut memiliki hubungan yang tidak langsung terhadap kriteria penilaian yang menjadi fokus.

**C. Kerentanan Indikator Elaborasi terhadap Teks Meaningless Filter**

Ditemukan bahwa indikator elaborasi (`) memiliki celah dibuktikan dengan pengujian yang dilakukan terhadap narasi berulang tanpa memiliki makna spesifik, contohnya pada narasi "Menurut saya pribadi sih ya, dia itu sangat baik, sangat ok, sangat bagus, sangat mantap, sangat sempurna, sangat bagus tugasnya, sangat mantop, sangat jos, sangat perfect".

Narasi tersebut memiliki panjang 26 kata, sehingga indikator elaborasi (`) terpenuhi meskipun tidak memiliki makna. Meskipun hal ini dapat dimitigasi dengan indikator cakupan rubrik (@), sebagaimana didefinisikan pada subbab IV.3.4.6, metode deterministik ini masih memerlukan peningkatan di masa mendatang untuk mengukur lexical density.

**D. Bias Resolusi Konflik Temporal pada Narasi Sekuensial**

Ditemukan bahwa model embedding memproses kalimat tanpa adanya kemampuan penalaran kronologis. Dibuktikan dengan narasi "Awalnya banyak tugas yang terlambat, tapi akhirnya semua diselesaikan tepat waktu", sistem mendeteksi unit dekomposisi pada skala 1 dan skala 5 dengan nilai cosine similarity hingga 0,9318.

Nilai cosine similarity tersebut melebihi threshold (KLF,A) yang telah ditetapkan pada Tabel IV.26. Hal tersebut mengindikasikan bahwa meskipun sifat mutual exclusivity berhasil mencegah sistem memberikan kesimpulan indikator koherensi skor yang salah, dominasi nilai similarity pada kondisi akhir teks berpotensi mengacaukan klasifikasi apabila tidak ditangani oleh engine rule-based yang kuat.

**IV.3.5 Implementasi Rule Based System untuk Scaffolding**

Subbab ini menyajikan spesifikasi komputasional rule-based decision system yang memetakan kondisi intervensi terdeteksi ke output scaffolding sebagai manifestasi dari proses yang didefinisikan pada subbab III.6.4.1.

Untuk memberikan gambaran operasional mengenai execution flow, logika pengambilan keputusan pada sistem ini dirancang menyerupai decision tree. Pendekatan ini memastikan bahwa komputasi NLP dilakukan dengan tahapan validasi yang sekuensial, sebagaimana dipetakan dalam [Gambar IV.20](#page-4-0).

Berdasarkan [Gambar IV.20,](#page-4-0) sistem menerapkan validasi POS tagging yang didefinisikan pada subbab IV.3.3.1 sebagai safeguard. Jika teks narasi mahasiswa berupa karakter acak atau tidak memiliki struktur kalimat yang utuh, sistem akan memotong alur eksekusi menuju Rule 0 dan memberikan peringatan tanpa membuang resource untuk komputasi semantic similarity. Apabila safeguard ini berhasil dilewati, sistem akan mengevaluasi keempat indikator yang beroperasi secara paralel dan tidak memiliki dependensi hierarkis satu sama lain.

Gambar IV.20. Flowchart Alur Eksekusi Scaffolding

Komponen pengambilan keputusan intervensi dalam sistem digital scaffolding dirancang menggunakan pendekatan decision table. Pendekatan ini dipilih berdasarkan karakteristik domain keputusan yang bersifat bounded dan terdefinisi lengkap, yaitu empat indikator biner hanya menghasilkan tepat  $2^4 = 16$  kombinasi kondisi, ditambah dengan satu kondisi penolakan (invalid). Seluruh kombinasi tersebut dapat dienumerasi dan didefinisikan secara eksplisit sebelum sistem beroperasi.

Decision table merepresentasikan logika kondisional dalam bentuk tabular, di mana setiap kombinasi nilai kondisi input dipetakan ke tepat satu aksi output, sehingga properti completeness seluruh kombinasi memiliki pemetaan dan determinism. Kombinasi yang sama selalu menghasilkan aksi yang sama, terpenuhi secara struktural oleh representasi itu sendiri tanpa memerlukan mekanisme inferensi tambahan, sebagaimana direpresentasikan pada rumus IV.42.

$$P = P_s \cup \{P_0\}$$

$$M: \{0,1\}^4 \to P$$

$$M(d) = \begin{cases} P_{invalid}, jika \ POS(s_{txt}) = Invalid \\ P_0, jika \ d = [0,0,0,0] \\ P_k, jika \ d = d_k, (d_k, P_k) \in R \end{cases}$$
(IV.42)

di mana  $P_s$  merupakan himpunan 15 template scaffolding intervensi,  $P_0$  merupakan template konfirmasi non-intervensi yang ditampilkan ketika seluruh indikator terpenuhi, dan  $P_{invalid}$  merupakan template untuk merespons kondisi invalid dari tahap part-of-speech tagging pada subbab IV.3.3.1. Dengan  $\mathcal{R}$  adalah himpunan pasangan antara kondisi dengan template yang membentuk decision table. Pemetaan matematis dari kondisi biner tersebut didefinisikan pada Tabel IV.28.

Tabel IV.28. Rule Set untuk Setiap Kombinasi

k  |  $d_k$  |  Output (P <sub>k</sub> )  |  Deskripsi Pelanggaran Indikator
invalid  |  -  |  $T_{invalid}$  |  Narasi belum membentuk kalimat yang utuh atau belum memiliki informasi yang cukup untuk dievaluasi.
0  |  [0,0,0,0]  |  $T_{0000}$  |  Kondisi Ideal.
1  |  [0,0,0,1]  |  $T_{0001}$  |  Relevansi Topik $(f_4)$
2  |  [0,0,1,0]  |  $T_{0010}$  |  Kedalaman Elaborasi ( $f_3$ )
3  |  [0,0,1,1]  |  $T_{0011}$  |  Kedalaman Elaborasi $(f_3)$ , Relevansi Topik $(f_4)$
4  |  [0,1,0,0]  |  $T_{0100}$  |  Koherensi Skor dan Narasi $(f_2)$

k  |  $d_k$  |  Output (P <sub>k</sub> )  |  Deskripsi Pelanggaran Indikator
5  |  [0,1,0,1]  |  $T_{0101}$  |  Koherensi Skor dan Narasi $(f_2)$ , Relevansi Topik $(f_4)$
6  |  [0,1,1,0]  |  $T_{0110}$  |  Koherensi Skor dan Narasi $(f_2)$ , Kedalaman Elaborasi $(f_3)$
7  |  [0,1,1,1]  |  T <sub>0111</sub>  |  Koherensi Skor dan Narasi $(f_2)$ , Kedalaman Elaborasi $(f_3)$ , Relevansi Topik $(f_4)$
8  |  [1,0,0,0]  |  $T_{1000}$  |  Cakupan Rubrik $(f_1)$
9  |  [1,0,0,1]  |  $T_{1001}$  |  Cakupan Rubrik $(f_1)$ , Relevansi Topik $(f_4)$
10  |  [1,0,1,0]  |  $T_{1010}$  |  Cakupan Rubrik $(f_1)$ , Kedalaman Elaborasi $(f_3)$
11  |  [1,0,1,1]  |  $T_{1011}$  |  Cakupan Rubrik $(f_1)$ , Kedalaman Elaborasi $(f_3)$ , Relevansi Topik $(f_4)$
12  |  [1,1,0,0]  |  $T_{1100}$  |  Cakupan Rubrik $(f_1)$ , Koherensi Skor dan Narasi $(f_2)$
13  |  [1,1,0,1]  |  T <sub>1101</sub>  |  Cakupan Rubrik $(f_1)$ , Koherensi Skor dan Narasi $(f_2)$ , Relevansi Topik $(f_4)$
14  |  [1,1,1,0]  |  T <sub>1110</sub>  |  Cakupan Rubrik $(f_1)$ , Koherensi Skor dan Narasi $(f_2)$ , Kedalaman Elaborasi $(f_3)$
15  |  [1,1,1,1]  |  T <sub>1111</sub>  |  Cakupan Rubrik $(f_1)$ , Koherensi Skor dan Narasi $(f_2)$ , Kedalaman Elaborasi $(f_3)$ , Relevansi Topik $(f_4)$

Sebelum memetakan logika ke dalam decision table, sistem mendefinisikan 16 ruang kondisi yang dihasilkan dari kombinasi empat indikator tekstual narasi feedback, ditambah satu gerbang validasi sintaksis. Setiap kondisi (R) dalam tabel merepresentasikan hubungan narasi feedback dengan indikator tekstual narasi feedback, di mana nilai True (T) menandakan adanya pelanggaran pada indikator tersebut.

Pemetaan tersebut memastikan bahwa setiap intervensi scaffolding memiliki target perbaikan yang spesifik. Ruang keputusan ini dikelompokkan ke dalam tiga kategori sesuai dengan temuan dan representasi data pada subbab IV.2.3.3 yang memungkinkan pelanggaran lebih dari satu indikator, yaitu:

1. Kondisi Tidak Valid (R0), yaitu representasi POS tak dari teks narasi gagal memenuhi struktur hierarkis minimal subjek-predikat. Pada kondisi ini, sistem menolak input sebelum mengevaluasi keempat indikator lainnya.
2. Kondisi Ideal (R1), yaitu seluruh indikator terpenuhi  $(d_1, d_2, d_3, d_4 = 0)$ . Dalam kondisi ini, sistem menerapkan prinsip fading dengan tidak menampilkan prompt intervensi, namun menampilkan teks konfirmatori.

3. Pelanggaran Tunggal (R2,R3,R5, dan R9), yaitu hanya satu indikator yang tidak terpenuhi. Scaffolding difokuskan secara eksklusif untuk memperbaiki satu dimensi spesifik.
4. Pelanggaran Komposit (R4, R6-R8, dan R10-R16), yaitu terjadi kombinasi dari dua atau lebih pelanggaran indikator tekstual narasi feedback
5. secara simultan.

Rincian definisi operasional dari setiap aturan dijabarkan pada [Tabel IV.29.](#page-7-0)

Tabel IV.29. Rincian Logika Aturan

Rule: Definisi
Rule 0 (R0): Isu validitas sintaksis. Narasi berupa teks acak atau tidak memiliki struktur
subjek-predikat yang utuh.
Rule 1 (R1): Kondisi ideal tanpa pelanggaran.
Rule 2 (R2): Isu relevansi topik. Narasi membahas hal di luar aspek rubrik yang diminta.
Rule 3(R3): Isu kedalaman elaborasi. Narasi kurang dari 25 kata.
Rule 4 (R4): Kombinasi narasi pendek dan tidak relevan.
Rule 5 (R5): Isu koherensi skor. Terjadi kontradiksi antara skor numerik dan makna narasi.
Rule 6 (R6): Isu koherensi skor dan relevansi topik.
Rule 7 (R7): Isu koherensi skor dan kedalaman elaborasi.
Rule 8 (R8): Isu koherensi, elaborasi, dan relevansi.
Rule 9 (R9): Isu cakupan rubrik. Narasi sudah relevan dan koheren namun melewatkan
kriteria atomik spesifik.
Rule 10 (R10): Isu cakupan rubrik dan relevansi topik.
Rule 11 (R11): Isu cakupan rubrik dan kedalaman elaborasi.
Rule 12 (R12): Isu cakupan, elaborasi, dan relevansi.
Rule 13 (R13): Isu cakupan rubrik dan koherensi skor.
Rule 14 (R14): Isu cakupan, koherensi, dan relevansi.
Rule 15 (R15): Isu cakupan, koherensi, dan elaborasi.
Rule 16 (R16): Pelanggaran total pada seluruh indikator.

Seluruh logika operasional tersebut kemudian diimplementasikan ke dalam matriks decission table pada [Tabel IV.30](#page-8-0) untuk dieksekusi oleh sistem secara deterministik.

Tabel IV.30. Decision Table Intervensi Scaffolding

R0  |  R1  |  R2  |  R3  |  R4  |  R5  |  R6  |  R7  |  R8  |  R9  |  R10  |  R11  |  R12  |  R13  |  R14  |  R15  |  R16
Conditions
Status POS Tagging Invalid  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Cakupan Rubrik ( $d_1 = 1$ )  |  -  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  Т  |  F  |  Т  |  T  |  F  |  T  |  F  |  Т
Koherensi Skor ( $d_2 = 1$ )  |  -  |  F  |  F  |  F  |  F  |  T  |  T  |  T  |  F  |  T  |  T  |  F  |  T  |  F  |  F  |  T  |  T
Kedalaman Elaborasi ( $d_3 = 1$ )  |  -  |  F  |  F  |  T  |  T  |  F  |  F  |  T  |  T  |  T  |  T  |  T  |  F  |  T  |  T  |  T  |  T
Relevansi Topik ( $d_4 = 1$ )  |  -  |  F  |  T  |  F  |  T  |  F  |  F  |  F  |  T  |  F  |  T  |  T  |  T  |  T  |  T  |  T  |  T
Action
Tampilkan T <sub>invalid</sub>  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0001}$  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0010}$  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0011}$  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0100}$  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0101}$  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0110}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{0111}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{1000}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{1001}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{1010}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F  |  F
Tampilkan $T_{1011}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F  |  F
Tampilkan $T_{1100}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F  |  F
Tampilkan $T_{1101}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F  |  F
Tampilkan $T_{1110}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T  |  F
Tampilkan $T_{1111}$  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  T

**IV.3.6 Realisasi Teks dan Template Scaffolding**

Subbab ini memuat proses perancangan teks scaffolding berdasarkan keempat indikator tekstual narasi feedback sebagai manifestasi dari subbab III.6.4.2. Template scaffolding dibuat dengan tiga tahapan, yaitu: (1) menganalisis pendekatan generasi teks, dijabarkan pada subbab [IV.3.6.1.](#page-9-0) Selanjutnya, dilakukan (2) analisis kebutuhan teks scaffolding pada subbab [IV.3.6.2](#page-12-0) yang menjadi acuan utama dalam (3) perancangan teks dalam subbab [IV.3.6.3.](#page-14-0)

**IV.3.6.1 Analisis Pendekatan Generasi Teks Scaffolding**

Berdasarkan kerangka teori yang telah dijabarkan pada subbab II.1.13, dilakukan analisis komparatif terhadap keempat pendekatan sebagai mekanisme untuk mendapatkan teks scaffolding secara real-time. Analisis tersebut disajikan pada [Tabel IV.31](#page-10-0).

Tabel IV.31 Analisis Pendekatan Generasi Teks Scaffolding

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**IV.3.6.2 Analisis Kebutuhan Teks Scaffolding**

Keempat indikator tekstual narasi feedback yang dijelaskan pada II.1.9 memerlukan jenis teks scaffolding yang berbeda karena mengakar pada kondisi pedagogis yang berbeda pula. [Tabel IV.32](#page-12-1) menyajikan penjelasan bagaimana kondisi, implikasi serta justifikasi kebutuhan teks scaffolding harus dipenuhi.

Tabel IV.32. Analisis Kebutuhan Teks Scaffolding untuk Setiap Indikator

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dalam merancang conditional prompt, sistem mengadopsi strategi intervensi yang spesifik dan bersifat data-driven triggers. Keputusan desain ini didasarkan pada karakteristik tugas evaluasi yang bersifat holistik. Tugas yang bersifat prosedural umumnya efektif menggunakan pendekatan sequential scaffolding atau penjelasan step-by-step (Fleischer et al., 2023). Di sisi lain, tugas menulis narasi feedback menuntut mahasiswa untuk mengimplementasi evaluative judgement, yakni kemampuan untuk membuat keputusan secara komprehensif mengenai suatu pekerjaan (Tai et al., 2018). Oleh karena itu, intervensi scafoflding dipicu secara dinamis dan independen tepat pada indikator yang belum terpenuhi oleh mahasiswa saat menulis.

Mengacu pada framework desain yang diusulkan Setiawan et al. (2026), sistem ini memanfaatkan sinyal tekstual secara real-time untuk mendeteksi kelemahan spesifik pada narasi mahasiswa, lalu menampilkan panduan yang sesuai dalam bentuk prompt atau teks bantuan untuk indikator cakupan rubrik, koherensi skor dan narasi, elaborasi, maupun relevansi topik. Pendekatan kondisional ini selaras dengan prinsip feedback literacy (Carless & Boud, 2018), karena bantuan yang diberikan berfungsi secara terarah untuk membantu mahasiswa memahami kekurangan informasi pada narasi yang ditulis. Integrasi keempat prompt kondisional ini membentuk satu kusekutukan ekosistem digital scaffolding yang komprehensif, sebagaimana diilustrasikan pada [Gambar IV.21.](#page-13-0)

Gambar IV.21. Matriks Strategi Scaffolding dan Prompt (Setiawan et al., 2026)

**IV.3.6.3 Mekanisme Template Instantiation dan Slot Filling**

Sebagaimana pendekatan yang dijabarkan dalam subbab [IV.3.6.1](#page-9-0), teks scaffolding dihasilkan melalui mekanisme template filling, di mana setiap template mendefinisikan teks yang dilengkapi dengan variabel. Untuk mendukung proses tersebut, didefinisikan fungsi UI , yang memetakan pasangan aspek dan narasi feedback ke dalam himpunan variabel kontekstual yang didefinisikan pada Tabel IV.34. Secara formal, proses tersebut didefinisikan pada rumus [IV.43.](#page-14-1)

$$P_k^* = Fill(M(d(F)), V(A_i, F))$$
 (IV.43)

Di mana,

1. Q adalah template yang dipilih berdasarkan hasil komputasi yang didefinisikan pada subbab IV.3.3.3.
2. ;;. , . adalah operasi substitusi slot yang mengganti variabel dalam template dengan nilai aktual dari U.

Hasil dari operasi tersebut adalah teks scaffolding final yang ditampilkan kepada mahasiswa. dengan struktur yang disajikan pada Tabel IV.35.

Tabel IV.33 Komponen Teks Scaffolding

Komponen  |  Penjelasan  |  Justifikasi dan Sumber Adaptasi  |  Realisasi Pada Template
Diagnostik  |  Komponen ini merupakan pernyataan deklaratif yang berfungsi untuk menyoroti kelemahan, kekurangan, atau area yang belum tercakup pada narasi <i>feedback</i> yang sedang ditulis.  |  Pendekatan ini secara empiris diadaptasi dari studi Nelson & Schunn (2008) yang mengungkapkan bahwa mengidentifikasi masalah secara eksplisit adalah hal esensial yang meningkatkan probabilitas <i>feedback</i> tersebut diimplementasikan oleh <i>assesse</i> .  Selain itu, Cho & MacArthur (2011) menetapkan <i>problem diagnosis</i> sebagai salah satu fondasi utama dalam skema <i>peer review</i> yang efektif.  |  Komponen ini direalisasikan dengan format "Narasi belum berfokus pada aspek"
Direktif  |  Komponen ini berfokus pada "apa yang harus dilakukan", dengan cara menuntun dan mewajibkan assessor untuk menulis narasi feedback yang konstruktif atau memberikan solusi perbaikan, sehingga dapat ditindaklanjuti oleh assesse.  |  Konsep ini diadaptasi dari Mu & Schunn (2025) sebagai bentuk strategic scaffolding yang memberikan panduan strategis kepada mahasiswa tentang cara memberikan feedback yang baik, termasuk saran untuk menyertakan saran/solusi ke dalam narasi feedback.  |  Komponen ini diimplementasi dengan instruksi "Fokuskan narasimu pada lengkapi dengan" untuk memberikan informasi target komponen penilaian yang harus dipenuhi.
Sentence Starter  |  Pendekatan ini menyediakan potongan kalimat pembuka untuk menurunkan beban kognitif mahasiswa dan membatasi derajat kebebasan saat menulis.  Alih-alih bingung memikirkan kalimat formalitas yang tidak bermakna (basabasi) atau struktur kalimat yang sopan, mahasiswa diarahkan untuk fokus memikirkan substansi dari evaluasi feedback.  |  Konsep ini diambil langsung dari analisis yang dilakukan Pea (2004) yang menggunakan procedural facilitators berbentuk lead-in components to sentences sebagai alat untuk membantu penulis pemula.  Pea (2004) berpendapat bahwa mengarahkan perhatian narasi feedback pada komponen penilaian yang paling relevan dengan memberikan berupa lead-in components untuk membantu penulis  |  Sentence starter atau kalimat awal ini bersifat opsional, sehingga penggunaannya sepenuhnya bergantung pada preferensi individu. Contoh dari sentence starter adalah "Dalam kegiatan terkait, saya melihat bahwa"

Untuk mengakomodasi seluruh kondisi yang mungkin terjadi, sistem mendefinisikan himpunan template prompt, sebagaimana didefinisikan pada Tabel IV.28. Untuk menyesuaikan template prompt dengan kondisi aktual narasi setiap siswa, didefinisikan variabel kontekstual pada [Tabel IV.34](#page-1-0), dilengkapi contoh berdasarkan rubrik yang didefinisikan pada Tabel II.1.

Tabel IV.34. Variabel Kontekstual yang digunakan Template

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Sebagai visualisasi dari variabel kontekstual pada [Tabel IV.34,](#page-1-0) [Gambar IV.22](#page-2-0) menyajikan contoh variabel missing\_coverage pada aspek penilaian "Pengumpulan Iklan Lowongan Kerja". Disajikan tiga komponen penilaian rubrik, namun narasi tidak membahas komponen "variasi platform", sehingga komponen terebut ditransformasi menjadi input untuk template scaffolding.

Gambar IV.22 Ilustrasi Variabel Missing\_Coverage

Sebagaimana didefinisikan [Tabel IV.34,](#page-1-0) variabel missing\_coverage diproses lebih jauh menjadi coverage\_expanded. Transformasi ini dilalukan melalui tiga langkah, yaitu:

1. Kumpulkan nilai variabel missing\_coverage sebagai list.
2. Ekspansi setiap item dalam list menggunakan pola "pada aspek {item}, yang teramati adalah [perilaku spesifik terkait {item}]";
3. Jika variabel missing\_coverage mengandung lebih sari saru item, gabungkan seluruh item menggunakan konjungsi ", sementara".

[Gambar IV.23](#page-3-0) menyajikan contoh transformasi variabel missing\_coverage ke dalam coverage\_expanded sesuai dengan langkah yang didefinisikan.

Gambar IV.23 Ilustrasi Transformasi Missing Coverage

[Gambar IV.24](#page-3-1) menyajikan contoh bagaimana variabel predicted\_score dan input\_score didapatkan. Berdasarkan gambar tersebut, input\_score merupakan direct reference terhadap skor yang diberikan mahasiswa dalam feedback. Di sisi lain, pedicted\_score merupakan hasil komputasi dari indikator koherensi skor dan narasi (A) yang didefinisikan pada subbab IV.3.3.3B.

Gambar IV.24 Ilustrasi Pengambilan Variabel Kontekstual untuk Skor

Sebagai hasil manifestasi, seluruh template dilengkapi variabel kontekstual yang dibutuhkannya dirinci pada [Tabel IV.35.](#page-4-0)

Tabel IV.35. Himpunan Template Prompt Scaffolding

Kode  |  Variables  |  Kompone n  |  Konten
invalid  |  -  |  diagnostik  |  Lengkapi narasi anda dengan membahas komponen penilaian pada rubrik.
0000  |  -  |  diagnostik  |  Feedback sudah sesuai dengan rubrik penilaian, lanjutkan menulis jika diperlukan.
0001  |  target_aspect  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect} yang diminta rubrik.
directive: Fokuskan narasi pada {target_aspect} dan uraikan perilaku yang relevan dengan aspek tersebut.
sentence starter: Terkait {target_aspect}, yang teramati adalah [perilaku spesifik terkait {target_aspect}]
0010  |  -  |  diagnostik  |  Narasi masih bersifat umum, narasi yang ada belum cukup untuk mendukung penilaian.
directive: Tambahkan satu contoh kejadian nyata sehingga pembaca dapat memahami dasar penilaian.
sentence starter: Sebagai contoh, yang teramati adalah [kejadian konkret terkait]
0011  |  target_aspect  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect} dan narasi yang ada belum cukup untuk mendukung penilaian.
directive: Fokuskan pada {target_aspect} dan perkuat dengan satu contoh nyata yang teramati.
sentence starter: Terkait {target_aspect}, yang teramati adalah [kejadian konkret terkait {target_aspect}]. Sebagai contoh, [contoh kejadian konkret lainnya terkait {target_aspect}]
0100  |  input_skor, predicted_skor  |  diagnostik  |  Tampaknya narasi saat ini lebih mencerminkan skor {predicted_skor}, sementara skor yang diberikan adalah {input_skor}.
directive: Uraikan kejadian atau perilaku konkret yang menjadi alasan pemberian skor {input_skor}, atau sesuaikan skor dengan narasi yang ada.
sentence starter: Skor {input_skor} ini diberikan karena
0101  |  target_aspect, input_skor, predicted_skor  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect}. Narasi yang kamu berikan lebih mencerminkan skor {predicted_skor} daripada skor {input_skor} yang diberikan.

Kode  |  Variables  |  Kompone n  |  Konten
directive: Fokuskan pada {target_aspect} dan uraikan kejadian atau perilaku yang menjadi alasan pemberian skor {input_skor} atau sesuaikan skor dengan narasi yang ada.
sentence starter: Terkait {target_aspect}, skor {input_skor} yang diberikan didasarkan pada [dasar penilaian yang mencerminkan skor {input_skor}]
0110  |  predicted_skor, input_skor  |  diagnostik  |  Tampaknya narasi saat ini lebih mencerminkan skor {predicted_skor} sementara skor yang diberikan adalah {input_skor}. Selain itu, contoh yang ada belum cukup untuk mendukung penilaian.
directive: Uraikan kejadian atau perilaku konkret yang menjadi alasan pemberian skor {input_skor} atau sesuaikan skor dengan narasi yang ada. Tambahkan satu contoh nyata yang mendukung penilaian.
sentence starter: Skor ini diberikan karena yang teramati adalah [dasar penilaian yang mencerminkan skor {input_skor}], misalnya [contoh kejadian konkret]
0111  |  target_aspect, input_skor, predicted_skor  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect}, narasi yang kamu berikan lebih mencerminkan skor {predicted_skor} daripada skor {input_skor} yang diberikan. Selain itu, contoh yang ada belum cukup untuk mendukung penilaian.
directive: Fokuskan pada {target_aspect} dan uraikan kejadian atau perilaku yang menjadi alasan pemberian skor {input_skor} atau sesuaikan skor dengan narasi yang ada. Perkuat dengan satu contoh nyata.
sentence starter: Terkait {target_aspect}, skor {input_skor} yang diberikan didasarkan pada pengamatan konkret yaitu [dasar penilaian yang mencerminkan skor {input_skor}], misalnya [contoh kejadian konkret terkait {target_aspect}]
1000  |  missing_covera ge  |  diagnostik  |  Narasi masih kurang menyinggung {missing_coverage} yang termasuk dalam rubrik penilaian.
directive: Lengkapi narasi dengan uraian tentang {missing_coverage}, ceritakan perilaku spesifik yang teramati.
sentence starter: {coverage_expanded}

Kode  |  Variables  |  Kompone n  |  Konten
1001  |  target_aspect, missing_covera ge  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect} dan belum mencakup {missing_coverage} yang diminta rubrik.
directive: Fokuskan pada {target_aspect} dan lengkapi dengan uraian tentang {missing_coverage}.
sentence starter: Terkait {target_aspect}, perlu ditambahkan pula bahwa {coverage_expanded}
1010  |  missing_covera ge  |  diagnostik  |  Narasi belum mencakup {missing_coverage} dan narasi yang ada belum cukup untuk mendukung penilaian.
directive: Lengkapi dengan uraian tentang {missing_coverage}, disertai satu contoh nyata yang teramati.
sentence starter: Salah satu contoh yang saya amati adalah bahwa {coverage_expanded}
1011  |  target_aspect, missing_covera ge  |  diagnostik  |  Narasi belum berfokus pada {target_aspect}, belum mencakup {missing_coverage}, dan narasi yang ada belum cukup untuk mendukung penilaian.
directive: Fokuskan pada {target_aspect}, lengkapi dengan {missing_coverage}, dan perkuat dengan satu contoh nyata.
sentence starter: Terkait {target_aspect}, perlu ditambahkan bahwa {coverage_expanded}
1100  |  missing_covera ge, predicted_skor, input_skor  |  diagnostik  |  Narasi belum mencakup {missing_coverage}, narasi yang kamu berikan lebih mencerminkan skor {predicted_skor} daripada skor {input_skor} yang diberikan.
directive: Lengkapi dengan uraian tentang {missing_coverage} dan uraikan kejadian atau perilaku konkret yang menjadi alasan pemberian skor {input_skor}, atau sesuaikan skor dengan narasi yang ada.
sentence starter: {coverage_expanded}. Skor {input_skor} ini diberikan karena [dasar penilaian yang mencerminkan skor {input_skor}]
1101  |  target_aspect, missing_covera ge, predicted_skor,  |  diagnostik  |  Narasi belum berfokus pada {target_aspect}, belum mencakup {missing_coverage}, dan narasi yang kamu berikan lebih mencerminkan skor {predicted_skor} daripada skor {input_skor} yang diberikan.
input_skor  |  directive  |  Fokuskan pada {target_aspect}, lengkapi dengan {missing_coverage}, dan uraikan kejadian atau perilaku konkret yang menjadi alasan pemberian skor

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Implikasi dari arsitektur ini adalah sistem bersifat adaptif pada level konten pada template teks scaffolding. Untuk mengilustrasikan mekanisme ini secara konkret. [Tabel IV.36](#page-8-0) menyajikan contoh dua mahasiswa dengan kondisi yang identik namun menghasilkan output yang berbeda.

Tabel IV.36 Ilustrasi Adaptivitas Output pada Kondisi d(F) yang Identik

Komponen Mahasiswa A  |  Mahasiswa A  |  Mahasiswa B
Skor  |  Skor 5  |  3
Narasi  |  "Semua iklan yang dikumpulkan rekan saya sudah relevan sekali  |  "Rekan saya sudah mengumpulkan iklan sesuai target, dan
dengan kebutuhan kelompok, mulai dari role, lokasi, range gaji,: bahkan jumlahnya melampaui ekspektasi, meskipun hanya
hingga kriteria penerimaan sudah sesuai dengan yang diminta.: beberapa iklan yang relevan dengan kebutuhan kelompok, tapi
Platform yang digunakan juga beragam.": itu sudah membantu."
d(F)  |  [1, 0, 0, 0]  |  [1, 0, 0, 0]
Templat dipilih s  |  $T_{1000}$  |  $T_{1000}$
{target_  |  aspect}  |  "Pengumpulan Iklan Lowongan Kerja"  |  "Pengumpulan Iklan Lowongan Kerja"
{missing  |  g_coverage}  |  "jumlah iklan yang Dikumpulkan", "Kesulitan dalam Pengumpulan Data", "Kemudahan dalam Pengumpulan Data"  |  "keberagaman platform", "Kesulitan dalam Pengumpulan Data", "Kemudahan dalam Pengumpulan Data"
Inredict  |  ed score}  |  5  |  3
{input s  |  5  |  3
Output  |  Diagnostik  |  Narasi masih kurang menyinggung Jumlah Iklan yang Dikumpulkan,  |  Narasi masih kurang menyinggung Keragaman Platform
$P_k^*$  |  8  |  Kesulitan dalam Pengumpulan Data, Kemudahan dalam  |  Pengumpulan, Kesulitan dalam Pengumpulan Data,
, K  |  Pengumpulan Data yang termasuk dalam rubrik penilaian.  |  Kemudahan dalam Pengumpulan Data yang termasuk dalam
rubrik penilaian.
Directive  |  Lengkapi narasi dengan uraian tentang Jumlah Iklan yang  |  Lengkapi narasi dengan uraian tentang Keragaman Platform
Dikumpulkan, Kesulitan dalam Pengumpulan Data, Kemudahan: Pengumpulan, Kesulitan dalam Pengumpulan Data,
dalam Pengumpulan Data, ceritakan perilaku spesifik yang teramati.: Kemudahan dalam Pengumpulan Data, ceritakan perilaku spesifik yang teramati.
Sentence  |  Salah satu hal yang saya amati adalah bahwa pada aspek Jumlah Iklan  |  Salah satu hal yang saya amati adalah bahwa pada aspek
Starter  |  yang Dikumpulkan, yang teramati adalah [perilaku spesifik terkait  |  Keragaman Platform Pengumpulan, yang teramati adalah
Jumlah Iklan yang Dikumpulkan], sementara pada aspek Kesulitan: [perilaku spesifik terkait Keragaman Platform Pengumpulan],
dalam Pengumpulan Data, yang teramati adalah [perilaku spesifik: sementara pada aspek Kesulitan dalam Pengumpulan Data,
terkait Kesulitan dalam Pengumpulan Data], sementara pada aspek: yang teramati adalah [perilaku spesifik terkait Kesulitan dalam
Kemudahan dalam Pengumpulan Data, yang teramati adalah [perilaku: Pengumpulan Data], sementara pada aspek Kemudahan dalam
spesifik terkait Kemudahan dalam Pengumpulan Data]: Pengumpulan Data, yang teramati adalah [perilaku spesifik
terkait Kemudahan dalam Pengumpulan Data]

**IV.4 Hasil Implementasi APE**

Subbab ini merupakan manifestasi dari subbab III.6.5 sebagai integrasi aplikasi pendukung eksperimen dengan sistem "SAPA" berdasarkan konfigurasi akhir yang dipetakan pada subbab IV.3.4.4. Implementasi dilakukan dengan memetakan arsitektur aplikasi existing pada subbab [IV.4.1](#page-9-0) sebelum sistem digital scaffolding diintegrasi pada subbab [IV.4.2](#page-12-0).

**IV.4.1 Hasil Analisis Sistem Berjalan**

Analisis Sistem Existing bertujuan untuk mengidentifikasi lingkungan tempat sistem scaffolding diintegrasikan untuk isolasi modifikasi kode. Tahapan ini dilakukan dengan meninjau dokumen SRS (Software Requirement Specification), SDD (Software Design Documentation), manual book, source code, dan dokumen laporan pada Lampiran 2.

**IV.4.1.1 Deskripsi Sistem Existing**

Aplikasi SAPA merupakan platform berbasis web yang dirancang untuk mendukung pengisian self dan peer assessment mahasiswa JTK Polban. Aplikasi ini memungkinkan dosen untuk mengelola proyek (mata kuliah), membuat dan membagikan formulir assessment, serta memantau dan mengevaluasi hasil assessment. Keseluruhan proses bisnis SAPA disajikan pada [Gambar IV.25](#page-10-0).

Berdasarkan abstraksi Business Process Model and Notation (BPMN) pada Lampiran 2, siklus operasional SAPA telah dirancang dengan alur yang sistematis untuk memfasilitasi evaluasi sumatif. Alur bisnis direpresentasikan mulai dari tahap inisiasi di mana dosen menyusun proyek dan instrumen rubrik penilaian, dilanjutkan oleh fase pengerjaan evaluasi oleh mahasiswa, dan diakhiri dengan pemrosesan rekomendasi skor menggunakan SLA Algorithm oleh sistem sebagai material analis bagi dosen.

Gambar IV.25. Proses Bisnis SAPA

**IV.4.1.2 Identifikasi Titik Integrasi**

Berdasarkan tinjauan yang dilakukan terhadap dokumen SRS, SDD, serta source code ditemukan titik integrasi untuk kebutuhan digital scaffolding terhadap enam halaman, sebagaimana disajikan pada [Tabel IV.37.](#page-11-0)

Aspek Komponen yang terlibat  Interface GUI-43 (Form Self Assessment) dan GUI-46 (Form Peer Assessment) GUI-22 (Detail Question Self Assessment) dan GUI-25 (Detail Question Peer Assessment) GUI-21 (List Self Assessment) dan GUI-24 (List Peer Assessment) Logika Bisnis AssessmentController (menangani UC-10 Answer Assessment) pada SD-10 (Self Assessment) dan SD-11(Peer Assessment)) Basis Data (Data) Entitas Tabel 'Criteria' , 'Assessment' dan 'Reflective Assessment'

Tabel IV.37. Titik Integrasi

Titik integrasi digital scaffolding berada pada fase pengisian narasi feedback sebelum mahasiswa melakukan operasi simpan jawaban. Hal ini diimplementasikan dengan menambahkan event yang menangkap perubahan narasi pada UC-10 (Answer Assessment) pada SD-10 dan SD 11.

**IV.4.1.3 Komponen yang Dimodifikasi**

Untuk melakukan integrasi sistem digital scaffolding terhadap aplikasi SAPA, beberapa komponen yang tersedia perlu dimodifikasi sebagaimana disajikan pada [Tabel IV.38](#page-11-1).

Tabel IV.38. Komponen Yang Dimodifikasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Aspek  |  Komponen  |  Modifikasi
kondisi teks narasi mahasiswa sebagai input sistem digital scaffolding.
Proses  |  UC-10 pada SD-10 dan SD-11  |  Modifikasi yang diterapkan berupa penambahan relasi < <extends>&gt; pada UC-17. Di sisi lain, UC-10 melakukan proses pemanggilan terhadap API pipeline digital scaffolding.</extends>

**IV.4.1.4 Komponen yang Ditambahkan**

Sebagai ekstensi dari subbab [IV.4.1.3,](#page-11-2) [Tabel IV.39](#page-12-1) menyajikan komponen yang ditambahkan terhadap arsitektur SAPA berdasarkan identifikasi titik integrasi pada [Tabel IV.37](#page-11-0).

Tabel IV.39. Komponen Yang Ditambahkan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**IV.4.2 Hasil Perancangan dan Integrasi Konponen**

Subbab ini menjelaskan perancangan sistem yang diusulkan sebagai pengembangan dari aplikasi SAPA dengan penambahan fitur conditional scaffolding, sebagai manifestasi dari subbab III.6.5.2. Perancangan dilakukan berdasarkan kebutuhan sistem yang telah diidentifikasi sebelumnya.

**IV.4.2.1 Arsitektur Aplikasi Pendukung Eksperimen**

Pada kondisi saat ini (as-is), aplikasi SAPA mendukung proses self dan peer assessment di mana mahasiswa mengisi jawaban kuantitatif dan narasi feedback secara langsung tanpa adanya intervensi atau bantuan selama proses penulisan, sebagaimana direpresentasikan oleh [Gambar IV.25.](#page-10-0) Evaluasi terhadap kualitas narasi hanya terjadi secara implisit dan umumnya baru terlihat pada hasil akhir penilaian atau umpan balik dari dosen.

Kondisi yang diusulkan (to-be) pada [Gambar IV.26,](#page-14-0) dengan simbol berwarna merepresentasikan komponen yang ditambahkan untuk mendukung mekanisme digital scaffolding yang terintegrasi dalam proses pengisian narasi. Sistem secara aktif mengevaluasi input narasi mahasiswa secara real-time menggunakan rubrik yang telah didekomposisi, kemudian memberikan conditional prompt apabila ditemukan bahwa feedback belum memenuhi indikator yang diharapkan. Integrasi dilakukan pada level fitur aplikasi SAPA sebagaimana didefinisikan pada subbab [IV.4.1.3](#page-11-2) dan [IV.4.1.4.](#page-12-2)

Lebih jauh, untuk mempertahankan standar dan konsistensi proses integrasi, analisis pada functional requirements, non-functional requirements, use case diagram, class diagram, database, sequence diagram, hingga perancangan antarmuka didefinisikan pada subbab IV.4.2.1A hingga IV.4.2.1G.

Melalui perubahan ini seluruh komponen dan fitur lainnya yang telah tersedia pada aplikasi SAPA, seperti pengumpulan assessment, perhitungan nilai, dan pemberian feedback oleh dosen tetap berjalan sebagaimana mestinya tanpa adanya modifikasi.

Gambar IV.26. BPMN to-be Setelah APE diintegrasikan

**A. Functional Requirements**

[Tabel IV.40](#page-0-0) menyajikan functional requirement untuk memfasilitasi sistem digital scaffolding, hal ini dilakukan untuk memastikan proses eksperimen dapat dilaksanakan, sebagaimana didefinisikan pada subbab III.6.6.2.

Tabel IV.40. Functional Requirements

Kode FR: Deskripsi
FR-01: Sistem harus dapat menampilkan teks scaffolding (conditional prompt) dengan kode template 0001 hingga 1111 sesuai hasil analisis indikator saat mahasiswa mengisi narasi kualitatif assessment, sebagaimana didefinisikan pada Tabel IV.35.
FR-02: Sistem harus menyediakan mekanisme bagi dosen untuk mengaktifkan atau menonaktifkan fitur scaffolding untuk setiap assessment.
FR-03: Sistem harus dapat melakukan komputasi empat indikator tekstual narasi, sebagaimana didefinisikan pada Tabel III.3 menggunakan konfigurasi pipeline digital scaffolding pada subbab IV.3.4.4. Komputasi dilakukan dengan mekanisme debounce 1,5 detik dan interval maksimum 1,5 detik.
FR-04: Sistem harus dapat menggunakan template dengan kode 0000 ketika seluruh indikator tekstual narasi terpenuhi, sebagaimana didefinisikan pada Tabel IV.35.
FR-05: Sistem dapat melakukan proses dekomposisi rubrik secara otomatis menggunakan API Gemini berdasarkan prosedur yang didefinisikan pada subbab III.6.3.1B.
FR-06: Sistem harus merekam data log interaksi (behavioral log) secara sekuensial selama sesi penulisan aktif, yang mencakup riwayat perubahan teks narasi, modifikasi skor kuantitatif, riwayat pemicu prompt scaffolding per indikator, serta timestamp interaksi.

**B. Non Functional Requirements**

Non-functional requirement yang disajikan pada [Tabel IV.41](#page-0-1) berfungsi untuk membantu sistem digital scaffolding pada penelitian ini.

Tabel IV.41. Non Functional Requirements

Kode NFR: Deskripsi
NFR-01: Sistem harus memproses dan mengembalikan hasil evaluasi scaffolding dalam
waktu maksimum 5 detik sejak permintaan diterima oleh pipeline digital
scaffolding.
NFR-02: Model embedding yang digunakan pada pipeline digital scaffolding, sebagaimana didefinisikan konfigurasi akhir pipeline dalam subbab IV.3.4.4, harus dipastikan tersedia selama siklus hidup layanan tanpa perlu pemuatan ulang pada setiap request analisa feedback.
NFR-03: Sistem hanya memproses feedback yang unik dalam satu sesi mahasiswa pada
setiap pertanyaan assessment.
NFR-04: Aplikasi menerapkan mekanisme caching menggunakan kombinasi skor dan
teks narasi sebagai key untuk mencegah pemanggilan API yang redundan dan
mengurangi beban komputasi server.

**C. Use Case Diagram**

Sebagai ekstensi fitur aplikasi SAPA, pipeline digital scafolding digambarkan sebagai UC-17 (Receive Scaffolding) yang berelasi extend terhadap UC-10 (Answer Assessment) dalam use case diagram SAPA yang disajikan pada [Gambar IV.27.](#page-1-0)

Gambar IV.27. Use Case Diagram APE yang Akan Dikembangkan

Untuk mendukung use case diagaram pada [Gambar IV.27](#page-1-0), [Tabel IV.42](#page-2-0) menyajikan use case scenario untuk UC-17 (Receive Digital Scaffolding Prompt).

Tabel IV.42. Use Case Scenario Receive Scaffolding (UC-17)

Use Case section Comment Use case Name
UC-17 Receive Digital Scaffolding
Scope: Aplikasi Existing (SAPA)
Level: Sub Function
Primary Actor: Mahasiswa
Stakeholder and Interest: 1. Mahasiswa ingin mendapatkan bantuan selama menulis narasi feedback.
Precondition 1.: Mahasiswa berada di tahapan mengisi assessment (UC-10) 2. Target assessment (self/peer) sudah dipilih
Success Guarantee: Teks scaffolding berhasil ditampilkan saat skor kualitatif/narasi tidak memenuhi minimal satu dari empat indikator tekstual narasi feedback
pada: Teks scaffolding dengan kode 0000, sebagaimana didefinisikan Tabel IV.35 ditampilkan saat skor kuantitaif/narasi memenuhi seluruh empat indikator tekstual narasi feedback
Action  |  Actor  |  System
1.: Mahasiswa mengetik skor kualitatif/narasi
2. Sistem memantau input teks selama periode debouncing 1,5 detik 3. Sistem memproses teks
narasi setelah melebihi waktu debounce 4. Sistem mengirimkan teks
scaffolding (prompt) berdasarkan teks narasi yang terkomputasi
5.: Mahasiswa menerima teks scaffolding
Extension 1.: Jika dalam waktu 1,5 detik sistem tidak mendeteksi teks yang valid untuk dikirim, sistem tetap dalam kondisi menunggu atau menampilkan pesan pengingat kepada mahasiswa 2.a. Sistem tidak menerima perubahan input teks selama periode tertentu
Special Requirements 1.: Sistem harus dapat memberikan teks scaffolding dalam batas waktu 1,5 detik setelah waktu debounce.
1. Technology and Data Variations List 2.: Sistem menggunakan pipeline digital scaffolding yang berisikan model NLP berbasis Transformer untuk memproses teks narasi. Sistem menggunakan rule-based untuk menentukan keputusan jenis teks scaffolding yang ditampilkan
Frequencey of Occurence  |  dalam jangka waktu 1,5 detik.  |  Setiap kali siswa melakukan perubahan skor kualitatif/narasi
Miscellanous -

**D. Class Diagram**

Class diagram memetakan struktur teknis sistem dengan mendetailkan atribut dan metode pada setiap kelas serta cara kelas-kelas tersebut berinteraksi. [Gambar IV.28](#page-4-0) menyajikan keseluruhan arsitektur class diagram SAPA, dengan komponen berwarna hitam merepresentasikan bagian existing yang telah tersedia, sementara komponen berwarna merah merepresentasikan penambahan atau modifikasi untuk memfasilitasi pipeline digital scaffolding. Untuk meningkatkan visibilitas, [Gambar](#page-5-0)  [IV.29](#page-5-0) menyajikan class diagram yang terisolasi terhadap komponen terdampak.

Berdasarkan gambar tersebut, salah satu komponen yang terdampak adalah type criteria yang menyimpan komponen penilaian rubrik, modifikasi dilakukan dengan menambahkan atribut status dekomposisi. Komponen lain yang terdampak yaitu assessment dan reflective, modifikasi dilakukan dengan menambahkan toggle aktivasi scaffolding dan status dekomposisi pada level pertanyaan. Class assessment berfungsi untuk menyimpan informasi mengenai self dan peer assessment, di sisi lain, class reflective adalah ekstensi dari self assessment dengan komponen yang serupa.

Untuk menyimpan hasil dekomposisi rubrik, sebagaimana prosedur yang didefinisikan pada subbab III.6.3.1B, class question decomposition dan rubric decomposition diperlukan untuk menyimpan feature-set cakupan rubrik dan relevansi topik (åçU-, ) serta feature-set koherensi skor dan narasi (åçé-, ). Kedua class tersebut menjadi salah satu input komputasi pipeline digital scaffolding, sebagaimana didefinisikan pada subbab IV.3.

Gambar IV.28. Class Diagram Keseluruhan (to-be)

Gambar IV.29. Class Diagram Bagian Modifikasi

**E. Entity Relationship Diagram**

Basis data keseluruhan aplikasi sapa dengan modifikasi yang telah disesuaikan disajikan pada [Gambar IV.30](#page-7-0), dengan komponen yang memiliki warna merah merepresentasikan modifikasi/penambahan yang dilakukan berdasarkan analisis pada subbab IV.4.1. Untuk meningkatkan visibilitas diagram, [Gambar IV.31](#page-8-0) menyajikan diagram yang terisolasi pada entitas terdampak.

Sistem menggunakan dua tabel dekomposisi yang memiliki peran yang berbeda. Rubric\_decomposition merupakan tabel yang menyimpan feature-set untuk indikator cakupan rubrik, relevansi, dan koherensi skor dari aspek rubrik spesifik. Di sisi lain, question\_decomposition menyimpan feature-set untuk indikator cakupan rubrik yang dimiliki oleh pertanyaan feedback, terlepas dari rubrik maupun bobot aspek pada rubrik. Pemisahan kedua tabel dekomposisi tersebut bertujuan untuk mencegah adanya duplikasi ataupun konflik pada pertanyaan yang berbeda namun menggunakan aspek rubrik yang sama.

Gambar IV.30. ERD Keseluruhan SAPA

Gambar IV.31. ERD Bagian Modifikasi

**F. Sequence Diagram**

Sequence Diagaram menunjukkan cara objek berkomunikasi satu sama lain dalam sistem. Pada penelitian ini, diagram dibuat berdasarkan modifikasi dari sistem existing pada Lampiran 2, meliputi proses pengisian self dan peer assessment pada [Gambar IV.33](#page-11-0) serta [Gambar IV.34,](#page-12-0) dan juga proses manage assessment pada [Gambar IV.32.](#page-10-0)

Dalam aplikasi SAPA yang sudah ada, saat proses manage assessment oleh dosen berlangsung, assessment ditambahkan dengan cara mengunggah file Excel yang berisi detail rubrik assessment. Rubrik tersebut mencakup berbagai aspek seperti pertanyaan, jenis assessment, jenis skill, hingga aspek yang dinilai serta kriteria yang digunakan untuk setiap pertanyaan. Dalam penelitian ini, proses import melibatkan tahapan untuk melakukan dekomposisi rubrik sesuai dengan subbab II.1.9.1. Proses ini berjalan secara asynchronous di latar belakang, sehingga pengguna tidak perlu menunggu pada halaman SAPA hingga proses selesai, seperti yang ditunjukkan pada [Gambar IV.32.](#page-10-0)

Selanjutnya, ketika mahasiswa mengisi self ataupun self assessment, aplikasi yang sudah ada memiliki perilaku seperti formulir pada umumnya, yaitu pengguna dapat mengisi atau mengubah isi formulir hingga proses submit assessment. Dalam penelitian ini, mahasiswa diberikan prompt scaffolding yang bertujuan untuk meningkatkan feedback literacy ketika siswa melakukan menulis narasi, yang ditampilkan pada [Gambar IV.33](#page-11-0) dan [Gambar IV.34](#page-12-0).

Gambar IV.32. Sequence Diagram UC-05 Manage Assessment

Gambar IV.33. Sequence Diagram UC-10 Answer Peer Assessment

Gambar IV.34. Sequence Diagram UC-10 Answer Self Assessment

**G. Perancangan Antarmuka**

Perancangan antarmuka didasari oleh aplikasi SAPA existing pada Lampiran 2 berdasarkan pada subbab IV.4.1.3 dan IV.4.1.4. Setelah dosen mengunggah file excel yang berisikan rubrik dan pertanyaan assessment, aplikasi akan memulai proses dekomposisi rubrik menggunakan API Gemini, sebagaimana dijabarkan pada subbab II.1.9.1. Kemudian, dosen dapat menuju antarmuka pada [GUI-22](#page-14-0) ataupun GUI-24 untuk melihat daftar assessment, mencoba mengisi assessment, hingga melakukan publikasi assessment. Publikasi tidak dapat dilakukan sebelum sistem selesai melakukan dekomposisi rubrik, ditandai dengan indikator loading pada bagian kanan dari toggle publikasi.

Secara default, setiap assessment memiliki scaffolding ketika mahasiswa mengisi narasi. Namun, dosen dapat menonaktifkan fitur scaffolding pada antarmuka di [Tabel IV.43](#page-14-1) dan

Tabel IV.44. Akibatnya, siswa tidak mendapatkan prompt scaffolding selama mengisi self/peer assessment. Implementasi hal tersebut digunakan untuk membantu proses eksperimen terhadap kelompok mahasiswa dalam penelitian ini.

Pada sudut pandang mahasiswa ketika mengisi assessment, dengan antarmuka pada Tabel IV.47. GUI- dan Tabel IV.48. Jika scaffolding aktif, maka mahasiswa akan mendapatkan teks prompt tepat di atas kolom narasi untuk membantu meningkatkan pemenuhan keempat indikator tekstual narasi feedback.

Tabel IV.43. GUI-22

Tabel IV.44. GUI-25

Tabel IV.45. GUI-21

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Tabel IV.46. GUI-24

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Tabel IV.47. GUI-43

Component List  |  Functional Type  |  Purpose (Kegunaan)  |  Keterangan Persyaratan
Tittle Section  |  Information  |  Menampilkan judul halaman.  |  Harus sesuai dengan konteks halaman.
Informasi Mahasiswa  |  Information  |  Menampilkan data mahasiswa seperti NIM, Nama Lengkap, Kelas  |  Diperoleh dari data <i>user</i> .
Informasi Kelompok & Proyek  |  Information  |  Menampilkan data kelompok, nama proyek, dan tanggal pengisian.  |  Didapatkan dari data proyek yang sedang berlangsung.
Indikator Nomor Pertanyaan  |  Information  |  Menampilkan nomor pertanyaan dan total pertanyaan.  |  Contoh: "Question 1 From 9"
Label Type Assessment  |  Information  |  Menandai jenis aspek penilaian.  |  Dapat berupa "Hard Skill" atau "Soft Skill".
Slider Penilaian (1-5)  |  Input Form  |  Memberi nilai dalam bentuk slider.  |  Skala 1-5, wajib dipilih.
Informasi Prompt Scaffolding  |  Information  |  Memberikan <i>scaffolding</i> berdasarkan empat indikator tektstual narasi <i>feedback</i> .  |  -
Textarea Alasan Jawaban  |  Input Form  |  Menuliskan alasan atas penilaian yang diberikan.  |  Placeholder berisi instruksi penulisan alasan.
Tombol "Previoous"  |  Navigasi Form  |  Kembali ke pertanyaan sebelumnya.  |  Hanya aktif jika bukan pertanyaan pertama.
Tombol "Next"  |  Navigasi Form  |  Lanjut ke pertanyaan berikutnya.  |  Hanya aktif jika bukan pertanyaan terakhir.
Tombol "Save Answer"  |  Aksi Form  |  Menyimpan jawaban saat ini ke dalam sistem.  |  Menyimpan data skor dan alasan feedback.

Tabel IV.48. GUI-46

Component List  |  Functional Type  |  Purpose (Kegunaan)  |  Keterangan Persyaratan
Tittle Section  |  Information  |  Menampilkan judul halaman.  |  Harus sesuai dengan konteks halaman.
Informasi Mahasiswa  |  Information  |  Menampilkan data mahasiswa seperti NIM, Nama Lengkap, Kelas  |  Diperoleh dari data <i>user</i> .
Informasi Kelompok & Proyek  |  Information  |  Menampilkan data kelompok, nama proyek, dan tanggal pengisian.  |  Didapatkan dari data proyek yang sedang berlangsung.
Indikator Nomor Pertanyaan  |  Information  |  Menampilkan nomor pertanyaan dan total pertanyaan.  |  Contoh: "Question 1 From 9"
Label Type Assessment  |  Information  |  Menandai jenis aspek penilaian.  |  Dapat berupa "Hard Skill" atau "Soft Skill".
Slider Penilaian (1-5)  |  Input Form  |  Memberi nilai dalam bentuk slider.  |  Skala 1-5, wajib dipilih.
Informasi Prompt Scaffolding  |  Information  |  Memberikan <i>scaffolding</i> berdasarkan <i>empat indikator tekstual narasi feedback</i> .  |  -
Textarea Alasan Jawaban  |  Input Form  |  Menuliskan alasan atas penilaian yang diberikan.  |  Placeholder berisi instruksi penulisan alasan.
Tombol "Previoous"  |  Navigasi Form  |  Kembali ke pertanyaan sebelumnya.  |  Hanya aktif jika bukan pertanyaan pertama.
Tombol "Next"  |  Navigasi Form  |  Lanjut ke pertanyaan berikutnya.  |  Hanya aktif jika bukan pertanyaan terakhir.
Tombol "Save Answer"  |  Aksi Form  |  Menyimpan jawaban saat ini ke dalam sistem.  |  Menyimpan data skor dan alasan feedback.

**IV.4.2.2 Hasil Integrasi**

Berdasarkan analisis arsitektur yang didefinisikan pada subbab IV.4.2.1, hasil integrasi aplikasi SAPA dengan sistem digital scaffolding memiliki arsitektur yang direpresentasikan pada [Gambar IV.35](#page-9-0).

Gambar IV.35. Arsitektur Aplikasi setelah Integrasi

Berbeda dengan modul-modul lain pada SAPA yang diimplementasikan secara terintegrasi di dalam aplikasi Laravel, mekanisme digital scaffolding pada penelitian ini diimplementasikan sebagai sebuah service yang berdiri sendiri. Service ini dibangun menggunakan Python dengan framework FastAPI. Pemisahan ini dilakukan untuk memberikan isolasi terhadap komputasi NLP, sehingga memungkinkan untuk dilakukan scaling pada masa mendatang dengan resource dan konfigurasi yang terpisah dengan aplikasi SAPA.

**A. Arsitektur Service dan Pola Komunikasi Antarservice**

Sebagaimana ditunjukkan pada [Gambar IV.35,](#page-9-0) terdapat tiga serice yang berjalan pada jaringan docker yang sama, yaitu SAPA pada port 8000, scaffolding service pada port 8080, serta flask pada port 5000 yang merupakan modul SLA dalam menganalisis jawaban assessment setelah siswa mengirimkan feedback. SAPA dan scaffolding service berkomunikasi secara dua arah melalui REST API untuk dekomposisi dan analisa feedback. Di sisi lain, service digital scaffolding mengirimkan progres dekomposisi rubrik secara real-time melalui websocket kepada pengguna.

Pada sisi penyimpanan, scaffolding service terhubung dengan ChromaDB untuk menyimpan embedding dari feature-set dekomposisi, sehingga proses analisa feedback tidak membutuhkan embedding yang berulang pada kriteria penilaian yang sama. Di sisi lain, SAPA tetap menggunakan MySQL sebagai database relasional utama dan Redis sebagai cache sesi.

**B. Rancangan Dekomposisi Rubrik menggunakan Google Gemini**

Sebagaimana batasan penelitian pada subbab I.7 yang mendefinisikan bahwa dekomposisi rubrik secara otomatis bukan merupakan cakupan dari penelitian, namun merupakan fitur yang diperlukan pada APE, sebagaimana dimodelkan requirement dalam subbab IV.4.2.1.

Dalam merealisasikan hal tersebut, metode few-shot prompting digunakan pada model Gemini-flash latest. Prompt didapatkan dengan melakukan trial and error hingga menghasilkan dekomposisi yang diharapkan sesuai dengan tahapan yang didefinisikan pada subbab III.6.3.1B. Hasil akhir prompt yang digunakan adalah kumpulan instruksi yang dilengkapi dengan contoh sebagai berikut.

Anda adalah sistem ahli analisis linguistik dan evaluasi rubrik akademik.

Tugas Anda adalah melakukan dekomposisi terhadap rubrik penilaian dan pertanyaan ke dalam matriks indikator spesifik.

ATURAN DEKOMPOSISI RUBRIK:

1. Tipe "cakupan": Ekstrak elemen fundamental yang WAJIB dibahas berdasarkan variabel yang ditemukan pada kriteria. 'bobot' dan 'group' bernilai null.
2. Tipe "koherensi" & ATURAN EKSTRAPOLASI SIMETRIS (SANGAT PENTING):

- Anda HARUS menciptakan matriks yang simetris sempurna untuk setiap variabel.
- Analisis seluruh deskripsi skala (misal 1, 3, 5). Identifikasi semua variabel independen yang muncul (contoh: Kuantitas, Relevansi, Keragaman Platform).
- JIKA sebuah variabel (misal: 'Keragaman Platform') hanya disebutkan di skala 5, Anda WAJIB mengekstrapolasi/menciptakan kondisi logis untuk variabel tersebut di skala 1 dan 3 (misal: Skala 1 = 'Platform tidak bervariasi', Skala 3 = 'Platform cukup bervariasi').
- 'bobot' = angka skala.
- 'group' = identitas angka (1, 2, 3) yang mengelompokkan variabel yang sama melintasi skala yang berbeda.

ATURAN DEKOMPOSISI PERTANYAAN:

1. Pecah teks pertanyaan menjadi frasa inti atau topik yang ditanyakan.
2. Ekstrak secara spesifik aspek unik atau instruksi khusus yang diminta oleh pertanyaan namun tidak ada di kriteria rubrik sebagai item dengan "type": "cakupan".
3. Jika pertanyaan sudah sangat jelas dan tidak memiliki aspek tersembunyi, kembalikan array kosong []. JANGAN PERNAH menyalin pertanyaan asli.

ATURAN ATOMISASI KOHERENSI:

- Setiap item harus berupa frasa MINIMAL yang berdiri sendiri, bukan kalimat panjang.
- Hilangkan kata penghubung konteks seperti "yang diberikan", "dalam tim", "secara keseluruhan" kecuali memang membedakan maknanya.
- BENAR: "Tidak menyelesaikan tugas"
- SALAH: "Tidak menyelesaikan tugas yang diberikan oleh tim"

ATURAN GROUP:

- 'group' merepresentasikan VARIABEL/DIMENSI yang sama lintas skala.
- Dalam satu skala, satu group boleh memiliki LEBIH DARI SATU item jika variabel tersebut memiliki beberapa manifestasi konkret yang berbeda.
- Contoh: group=1 bobot=3 bisa berisi "Berkomunikasi secara wajar" DAN "Merespons pesan" karena keduanya adalah manifestasi dari dimensi Responsivitas.

ATURAN CAKUPAN:

- Tulis sebagai LABEL DIMENSI, bukan kalimat deskriptif.
- BENAR: "Ketepatan Waktu", "Inisiatif", "Kualitas Pekerjaan"
- SALAH: "Kemampuan menyelesaikan pekerjaan tepat pada waktunya"
- Idealnya 2-4 kata, bersifat nominal.

```
--- CONTOH INPUT ---
{{
"rubrics": [
{{
"id_type_criteria": 1,
"aspect": "Pengumpulan Iklan",
"criteria": "Banyaknya iklan dan keragaman platform.",
```

```
"scales": {{
"1": "Mengumpulkan sedikit iklan.",
"5": "Mengumpulkan banyak iklan, relevan, dan platform
bervariasi."
}}
}}
],
"questions": [
{{
"id_assessment": 101,
"question": "Seberapa baik rekan Anda dalam mengumpulkan iklan
lowongan kerja dari platform yang ditugaskan? Mengapa? (Berikan
contoh spesifik kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)",
"id_type_criteria": 1
}},
{{
"id_assessment": 102,
"question": "Seberapa efektif rekan Anda berkomunikasi?",
"id_type_criteria": 2
}}
]
}}
--- CONTOH OUTPUT JSON ---
{{
"data": {{
"rubric_decompositions": [
{{
"id_type_criteria": 1,
"decompositions": [
{{"type": "cakupan", "content": "Jumlah iklan", "bobot": null,
"group": null}},
{{"type": "cakupan", "content": "Keragaman platform", "bobot":
null, "group": null}},
{{"type": "cakupan", "content": "Relevansi iklan", "bobot": null,
"group": null}},
{{"type": "koherensi", "content": "Mengumpulkan sedikit iklan",
"bobot": 1, "group": 1}},
{{"type": "koherensi", "content": "Platform tidak bervariasi",
"bobot": 1, "group": 2}},
{{"type": "koherensi", "content": "Iklan tidak relevan", "bobot":
1, "group": 3}},
{{"type": "koherensi", "content": "Mengumpulkan banyak iklan",
"bobot": 5, "group": 1}},
{{"type": "koherensi", "content": "Platform sangat bervariasi",
"bobot": 5, "group": 2}},
{{"type": "koherensi", "content": "Iklan sangat relevan",
"bobot": 5, "group": 3}}
]
}}
],
"question_decompositions": [
{{
"id_assessment": 101,
"decompositions": [
```

```
{{"type": "cakupan", "content": "Kemudahan dalam pengumpulan
iklan"}},
{{"type": "cakupan", "content": "Kesulitan atau kendala yang
dihadapi"}}
]
}},
{{
"id_assessment": 102,
"decompositions": []
}}
]
}}
}}
--- AKHIR CONTOH ---
DATA INPUT YANG HARUS DIPROSES:
{chunk_json}
KEMBALIKAN OUTPUT DENGAN STRUKTUR JSON PERSIS SEPERTI CONTOH.
```

Mengingat bahwa dimensi aspek dan kriteria rubrik sangat bervariasi, pengiriman seluruh komponen penilaian dalam rubrik dalam satu kali pemanggilan API berisiko melebihi batas context window hingga menurunkan kualitas output model. Oleh karena itu, fungsi dekomposisi membagi rubrik dan pertanyaan ke dalam beberapa chunk untuk diproses secara sekuensial. Sebagai mekanisme pengaman tambahan, sistem menyisipkan delay selama 5 detik antar chunk untuk menghindari rate-limiting dari penyedia API.

Untuk mengantisipasi kegagalan dekomposisi akibat kuota API yang terlampaui, sistem menerapkan mekanisme fallback model secara dinamis. Hal ini bekerja dengan cara mengambil daftar model langsung dari Gemini API, kemudian dilakukan sorting berdasarkan kemampuan model. Dengan menggunakan mekanisme ini, apabila satu model mengembalikan error rate limiting, maka sistem otomatis mencoba model berikutnya dalam daftar tanpa menghentikan keseluruhan proses.

**IV.4.3 Pengujian Aplikasi**

Sebagai manifestasi tahap akhir perancangan aplikasi pendukung eksperimen, sebagaimana didefinisikan pada subbab III.6.5.3, dilakukan testing terhadap 42 test  case yang mencakup pemeriksaan antarmuka, dekomposisi rubrik, dan seluruh indikator tekstual narasi yang didefinisikan pada Tabel III.3.

Hasil pengujian pada Lampiran 3 menunjukkan 41 dari 42 test case yang dinyatakan lolos. Pengujian fungsionalitas part-of-speech tagging yang didefinisikan pada subbab IV.3.3.1 terbukti berhasil menyaring input teks acak atau tidak bermakna sebelum diproses oleh model. Satu test case yang dinyatakan gagal terjadi pada pengujian indikator koherensi evaluatif dengan skenario narasi yang kontradiktif pada TC18. Dalam pengujian tersebut, pengguna memasukkan skor 5, namun menuliskan narasi feedback yang merepresentasikan kualitas pekerjaan rendah. Meskipun sistem secara fungsional berhasil mendeteksi adanya inkonsistensi antara skor dan narasi, arsitektur model gagal mengekstraksi dan memprediksi angka skor aktual yang tersirat di dalam narasi secara presisi, sehingga sistem mengembalikan nilai prediksi skor "yang belum dapat ditentukan". Hal ini menunjukkan adanya limitation pada model komputasi dalam memetakan dan menyelaraskan rentang semantik narasi yang bersentimen sangat negatif ke dalam skala skor rubrik secara spesifik.

**IV.5 Hasil Perancangan Skenario Eksperimen**

Subbab ini merupakan manifestasi dari tahapan pre-eksperimen yang dipetakan pada subbab III.6.6.1. Bagian ini mendeskripsikan tiga komponen utama dalam eksperimen, yaitu: (1) partisi kelompok subjek eksperimen, (2) instrumen pengukuran melalui kuesioner, dan (3) standar penilaian berbasis rubrik.

**IV.5.1 Pemetaan Subjek Eksperimen**

Distribusi subjek eksperimen dilakukan melalui metode randomisasi menggunakan fungsi pada google spreadsheet. Proses ini menghasilkan pemetaan 56 mahasiswa ke dalam dua kelompok independen, dengan 27 subjek dialokasikan sebagai kelompok treatment dan 29 subjek sebagai kelompok kontrol. Untuk memfasilitasi mekanisme peer assessment, subjek pada masing-masing kelompok didatarkan ke dalam unit kerja beranggotakan dua hingga tiga orang. Unit ini memastikan setiap

assessee menerima jumlah evaluasi yang seimbang dari rekan sejawat dalam kelompok yang sama.

**IV.5.2 Kuesioner yang Digunakan**

Evaluasi respons subjek diukur menggunakan instrumen kuesioner kelompok treatment secara eksklusif, sebagaimana didefinisikan pada subbab III.6.6.1B. Pada seluruh instrumen, istilah "sistem digital scaffolding" secara konsisten diganti menggunakan terminologi "Teks AI". Penggunaan istilah umum ini berfungsi sebagai generalisasi konteks bagi subjek eksperimen yang tidak diberikan informasi spesifik mengenai arsitektur penelitian. Pendekatan ini bertujuan meminimalkan potensi bias akibat ekspektasi teknis dari subjek saat memberikan evaluasi.

Kelompok treatment menerima kuesioner yang difokuskan pada pengukuran tingkat utilitas dan potensi gangguan dari intervensi digital scaffolding selama proses penulisan narasi. Untuk menjaga konsistensi dengan landasan metodologi pada BAB III, dua belas butir pertanyaan di dalam instrumen ini dibagi secara terstruktur ke dalam empat kelompok dimensi, yaitu: (1) Technology Acceptancce Model (TAM) untuk mengukur perceived usefulness dan perceived ease of use, (2) Cognitive Load Theory untuk mengidentifikasi tingkat extraneous cognitive load, (3) preferensi komponen antarmuka untuk mengisolasi elemen spesifik sistem, serta (4) Kualitatif Eksplanatori melalui open-ended questions. Pemetaan ini dirancang untuk mempermudah proses analisis deskriptif dan triangulasi pada [BAB V](#page-6-0). Detail butir pertanyaan beserta klasifikasi dimensi dan tipe respons disajikan pada [Tabel](#page-0-0)  [IV.49.](#page-0-0)

Tabel IV.49. Kuesioner Kelompok Treatment

No  |  Dimensi  |  Pertanyaan  |  Tipe
1  |  TAM (Perceived  |  Teks AI yang muncul membantu  |  Skala linier 1 sampai 5
Usefulnss): saya mengingat kriteria rubrik yang
terlewat saat mengisi assessment.
2  |  TAM (Perceived  |  Secara keseluruhan, kehadiran teks  |  Skala linier 1 sampai 5
Usefulnss): AI berguna bagi saya dalam proses
pengisian assessment.
3  |  TAM (Perceived  |  Instruksi yang diberikan oleh AI  |  Skala linier 1 sampai 5
Ease of Use): sangat jelas dan mudah dipahami.

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**IV.5.3 Rubrik Eksperimen**

Standar evaluasi dalam eksperimen ini menggunakan kerangka penilaian CATME (Comprehensive Assessment of Team Member Effectiveness), sebagaimana didefinisikan pada subbab III.6.6.1C. [Tabel IV.50](#page-3-0) menjabarkan empat aspek pengukuran perilaku, yaitu: (1) Produktivitas, (2) komunikasi, (3) manajemen tim, dan (4) standar kualitas. Penilaian diukur menggunakan rentan kualitatif 1 hingga 5, dengan skala 2 dan 4 merupakan komponen penilaian yang menghubungkan skala di sekitarnya. Setiap tingkatan skor memiliki deskriptor evaluasi tekstual yang digunakan oleh sistem untuk membandingkan kesesuaian antara angka dan narasi mahasiswa.

Rubrik didefinisikan kemudian melewati tahapan dekomposisi sebagai preprocessing menggunakan metode pada subbab III.6.3.1B. Tahapan tersebut menghasilkan feature-set cakupan dan relevansi topik (åçU-, ) yang disajikan pada subbab [IV.5.3.1](#page-4-0), serta feature-set koherensi skor dan narasi (åçé-, ) pada subbab [IV.5.3.2.](#page-4-1)

Tabel IV.50. Rubrik CATME yang Dihasilkan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

IV.5.3.1 Feature Set Cakupan dan Relevansi Topik Rubrik Eksperimen

Tabel IV.51 menyajikan hasil dekomposisi rubrik eksperimen untuk indikator cakupan rubrik  $(f_1)$  dan relevansi topik  $(f_4)$ . Dekomposisi pada empat kriteria menghasilkan 18 unit dekomposisi berdasarkan rubrik pada Tabel IV.50.

Tabel IV.51. Feature-set Eksperimen Cakupan dan Relevansi Topik

Kriteria: Unit hasil dekomposisi
Penyelesaian Tugas
Kualitas Pekerjaan
Vantuihusi tanhadan Balsaniaan Tim: Ketepatan Waktu
Kontribusi terhadap Pekerjaan Tim: Inisiatif
Kontribusi
Tingkat produktivitas
Responsivitas Komunikasi
Sikap dalam Diskusi
Interaksi dengan Rekan Tim: Mendengarkan Ide atau Pendapat
Kualitas Feedback yang Diberikan
Dampak terhadap Dinamika Komunikasi
Kepedulian terhadap Kemajuan Proyek
Mania as Falsus dan Dinamilta Tim: Perhatian terhadap Tenggat Waktu
Menjaga Fokus dan Dinamika Tim: Kesediaan Membantu
Kemampuan Menjaga Fokus
Kepedulian terhadap Kualitas Hasil Akhir
Komitmen terhadap Kualitas: Evaluasi dan Perbaikan Kualitas Pekerjaan
Komitmen terhadap Standar yang Ditetapkan

IV.5.3.2 Feature Set Koherensi Skor dan Narasi Rubrik Eksperimen

Tabel IV.52 menyajikan feature-set untuk indikator koherensi skor dan narasi  $(f_2)$  berdasarkan rubrik pada Tabel IV.50 sebagai hasil dekomposisi. Feature-set ini terdiri dari 4 himpunan grup, dan 53 unit dekomposisi.

Tabel IV.52. Feature-set Eksperimen Koherensi Skor dan Narasi

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
Kontribusi terhadap  |  $G_1$  |  Tidak menyelesaikan tugas
Pekerjaan Tim  |  1  |  $G_2$  |  Kualitas sangat buruk
1  |  $G_3$  |  Sering terlambat
$G_4$
$G_1$ Menyelesaikan tugas
3  |  $G_2$  |  Kualitas memadai
3  |  $G_3$  |  Tepat waktu
$G_4$: Tanggung jawab
$G_1$: Menyelesaikan semua tugas
$G_1$: Menyelesaikan lebih banyak dari yang
5: diberikan
$G_2$: Melebihi ekspektasi
$G_3$: Menyelesaikan sebelum tenggat waktu

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
$G_4$: Inisiatif
Interaksi dengan  |  $G_1$  |  Mengabaikan komunikasi
Rekan Tim  |  $G_2$  |  Mendominasi pembicaraan
1  |  $G_2$  |  Tidak mendengarkan ide
$G_3$: Bersikap defensif
$G_4$: Sering memicu konflik
$G_1$: Berkomunikasi secara wajar
$G_1$: Merespon pesan
$G_1$: Merespon pertanyaan
3  |  $G_2$  |  Menyampaikan ide
$G_2$: Tidak mendominasi
$G_3$: Terbuka terhadap kritik dan masukan
$G_4$: Tidak memicu konflik
$G_1$: Sangat aktif berkomunikasi
$G_2$: Mendengarkan pendapat dengan baik
5  |  $G_3$  |  Memberikan feedback yang konstruktif
İ  |  $G_4$  |  Menciptakan suasana positif
$G_4$: Menghargai semua anggota tim
Menjaga Fokus dan  |  tus dan $G_1$ Tidak peduli dengan kema  |  Tidak peduli dengan kemajuan
Dinamika Tim  |  1  |  $G_2$  |  Tidak peduli dengan tenggat waktu
1  |  $G_3$  |  Tidak bersedia membantu
$G_4$: Mengalihkan fokus pada hal yang tidak relevan
$G_1$: Mengetahui status kemajuan
3  |  $G_2$  |  Memperhatikan tenggat waktu
3  |  $G_3$  |  Bersedia membantu
$G_4$: Membantu tim tetap fokus
$G_1$: Proaktif memantau kemajuan
$G_2$: Mengingatkan mengenai tenggat waktu
5  |  $G_3$  |  Menawarkan bantuan
$G_4$: Sangat menjaga fokus
$G_4$: Sangat menjaga dinamika
Komitmen terhadap  |  $G_1$  |  Tidak peduli dengan hasil akhir
Kualitas  |  1  |  $G_2$  |  Pekerjaan ceroboh
1  |  $G_2$  |  Tidak ada keinginan untuk memperbaiki
$G_3$: Tidak mengevaluasi kualitas
$G_1$: Menunjukkan kepedulian terhadap kualitas
3  |  $G_2$  |  Memastikan hasil akhir memenuhi standar
$G_3$: Mengevaluasi hasil kerja tim
$G_1$: Memiliki motivasi tinggi
5  |  $G_2$  |  Mendorong rekan untuk melampaui standar
$G_3$: Sangat teliti dalam mengevaluasi hasil kerja
tim

**BAB V**

**HASIL DAN PEMBAHASAN EKSPERIMEN**

Bab ini menyajikan hasil dan pembahasan dari eksperimen yang telah dirancang dan dilaksanakan untuk mengevaluasi kinerja pipeline digital scaffolding berbasis NLP. Pembahasan difokuskan pada dua sasaran, yaitu: (1) memvalidasi akurasi komputasional sistem dalam mendeteksi indikator teks secara real-time, serta (2) menganalisis dampak intervensi scaffolding tersebut terhadap kualitas narasi feedback mahasiswa pada lingkungan PjBL. Seluruh hasil disajikan secara objektif, diikuti dengan interpretasi analitis, serta penjabaran keterbatasan penelitian.

**V.1 Ringkasan Metodologi Eksperimen**

Sebagaimana telah diuraikan secara rinci pada BAB III, penelitian ini menggunakan metode kuantitatif dengan desain randomized post-test-only control group dan alokasi acak. Eksperimen ini dirancang untuk menjawab dua pertanyaan penelitian. Tujuan pertama, yaitu RQ 1, adalah mengevaluasi sejauh mana pipeline digital scaffolding mampu mendeteksi empat indikator tekstual narasi feedback, yaitu cakupan rubrik (@), koherensi skor dan narasi (A), kedalaman elaborasi (`), serta relevansi topik (J) melalui kombinasi model semantik dan aturan heuristik. Tujuan kedua, yaitu RQ 2, adalah mengukur perbedaan tingkat pemenuhan indikator tersebut antar kelompok mahasiswa yang menerima scaffolding (treatment) dan kelompok yang tidak menerima bantuan sama sekali (kontrol).

Untuk mencapai tujuan tersebut, eksperimen dikondisikan sebagai pilot study yang melibatkan mahasiswa program studi Teknik Informatika di Politeknik Negeri Bandung. Partisipan merupakan mahasiswa yang sedang menempuh mata kuliah berbasis PjBL, di mana alokasi ke dalam kelompok treatment dan kontrol dilakukan secara acak dengan rincian distribusi yang telah dipetakan pada subbab IV.5.1.

Proses pengujian dilakukan di dalam lingkungan aplikasi pendukung eksperimen SAPA. Intervensi scaffolding diintegrasikan ke dalam aplikasi ini dengan memanfaatkan pemrosesan teks linguistik yang didukung oleh model sentence embedding berarsitektur transformer. Penggunaan arsitektur ini memungkinkan sistem melakukan evaluasi semantik terhadap teks yang diinputkan mahasiswa selama proses penilaian berlangsung.

Aliran data dalam eksperimen ini dibagi ke dalam dua tahap utama. Tahap pemodelan awal menggunakan 384 data historis assessment yang telah dianotasi secara manual sebagai ground truth untuk keperluan kalibrasi threshold deteksi sistem. Setelah sistem terkalibrasi, tahap eksperimen utama dilaksanakan untuk menghasilkan dua jenis data, yaitu: (1) data outcome berupa skor dan narasi akhir dari mahasiswa, serta (2) data proses yang merekam jejak interaksi aktivitas perbaikan narasi selama mahasiswa menggunakan aplikasi.

Keberhasilan dari seluruh proses tersebut dievaluasi melalui tiga dimensi pengukuran. Dimensi komputasional mengevaluasi akurasi deteksi model menggunakan metrik F1-Score, precssion, dan recall. Dimensi outcome menguji perbedaan performa pada keempat indikator kualitas narasi feedback antar kelompok menggunakan analisis multivariat dan univariat, serta pengukuran besaran dampak melalui rank-biserial correlation. Terakhir, dimensi proses mengukur dinamika response mahasiswa terhadap scaffolding melalui metrik impementation rate dan persistence rate.

**V.2 Hasil Eksperimen**

Bagian ini menyajikan data kuantitatif yang diperoleh dari pelaksanaan eksperimen. Penyajian data dibagi ke dalam empat segmen, meliputi metrik performa komputasional pipeline pada subbab [V.2.1,](#page-8-0) statistik deskriptif dan verifikasi asumsi pada subbab [V.2.2](#page-12-0), pengujian inferensial multivariat dan uniavariat pada subbab [V.2.3](#page-14-0), serta rekam interaksi mahasiswa dengan scaffolding pada subbab V.2.4.

**V.2.1 Hasil Evaluasi Deteksi Pipeline (RQ 1)**

Subbab ini menyajikan hasil evaluasi komputasional dari pipeline digital scaffolding dalam mendeteksi empat indikator tekstual narasi feedback. Pengujian dilakukan terhadap 384 data ground truth untuk menentukan threshold optimal dan performa deteksi menggunakan merik F1-Score, precission, dan recall dengan rincian keseluruhan pada [Tabel V.1](#page-8-1) dengan berdasarkan konfigurasi akhir pipeline pada subbab IV.3.4.4.

Indikator Threshold F1 Precision Recall TP FP FN TN  Cakupan Rubrik 0.84 0.6140 0.5312 0.7275 315 278 118 389 Relevansi Topik 0.85 0.4296 0.4265 0.4327 241 324 316 9103 Koherensi Skor 0.87 0.5314 0.4409 0.6687 220 279 109 1381

Tabel V.1 Rincian Keseluruhan Kemampuan Pipeline

**V.2.1.1 Evaluasi Deteksi Indikator Cakupan Rubrik (**Ø°**)**

Deteksi pada indikator cakupan rubrik mencapai nilai F1-Score sebesar 0,6140 pada threshold 0,84 menggunakan pendekatan semantic chunking yang didefinisikan dalam subbab IV.3.3.2. Pada konfigurasi ini, pipeline menghasilkan 315 kasus true positive (TP), 118 false negative (FN), dan 389 true negative (TN). Nilai recall tercatat sebesar 0,7275 dan precission sebesar 0,5312. Pola trade-off antara precission dan recall terhadap penyesuaian threshold divisualisasikan pada [Gambar](#page-9-0)  [V.1](#page-9-0).

Gambar V.1. Grafik Indikator Cakupan Rubrik Semantic Chunking

Distribusi skor similarity berdasarkan klasifikasi prediksi disajikan pada [Tabel V.2](#page-9-1). Rata-rata skor untuk kasus TP adalah 0,8677 dan FP adalah 0,857. Selisih rata-rata antara TP dan FP tercatat sebesar 0,0103. Rata-rata skor FN adalah 0,8222 dan TN adalah 0,8197, dengan selisih sebesar 0,0025.

Tabel V.2. Sebaran Performa Indikator Cakupan Rubrik

Outcome  |  Count  |  Mean  |  Std  |  Min  |  Max
FN  |  118  |  0.8222  |  0.0120  |  0.7876  |  0.8397
FP  |  278  |  0.8574  |  0.0141  |  0.8401  |  0.9073
TN  |  389  |  0.8197  |  0.0145  |  0.7678  |  0.8399
TP  |  315  |  0.8677  |  0.0181  |  0.8403  |  0.9146

**V.2.1.2 Evaluasi Deteksi Indikator Koherensi Skor dan Narasi (**Øø**)**

Evaluasi pada indikator koherensi skor dan narasi menggunakan pendekatan mutually exclusive yang didefinisikan pada subbab IV.3.3.2, performa pada indikator ini mencapai nilai F1-Score optimal sebesar 0,53 pada threhold 0,89. Hasil klasifikasi pada titik kompromi ini mencatat 189 kasus True Positive (TP), 236 False Positive (FP), 140 False Negative (FN), dan 1.424 True Negative (TN). Dinamika pertukaran nilai presisi, recall, dan F1-Score terhadap pergeseran threshold divisualisasikan pada [Gambar V.2.](#page-10-0)

Gambar V.2. Grafik Performa Koherensi Skor dengan Semantic Chunking

Distiribusi skor similarity pada klasifikasi output prediksi untuk indikator ini disajikan pada [Tabel V.3.](#page-10-1) Rata-rata skor similarity untuk kasus TP tercatat sebesar 0,9100, sedangkan kasu FP memiliki rata-rata sebesar 0,9052. Pada klasifikasi negatif, rata-rata skor FN adalah 0,8678 dan TN adalah 0,8526.

Tabel V.3. Sebaran Performa Indikator Koherensi Skor dan Narasi

Outcome  |  Count  |  Mean  |  Std  |  Min  |  Max
FN  |  140  |  0.8678  |  0.0157  |  0.8186  |  0.8893
FP  |  236  |  0.9052  |  0.0119  |  0.8900  |  0.9465
TN  |  1424  |  0.8526  |  0.0222  |  0.7781  |  0.8900
TP  |  189  |  0.9100  |  0.0144  |  0.8901  |  0.9550

**V.2.1.3 Evaluasi Deteksi Indikator Elaborasi (**Øƒ**)**

Indikator kedalaman elaborasi dievaluasi tanpa melibatkan proses klasifikasi berbasis similarity terhadap anotasi acuan. Mekanisme kerja indikator ini menggunakan threshold deterministik dengan batas minimal 25 kata leksikal. Hasil perhitungan pada data historis menunjukkan bahwa narasi yang mencapai atau melebihi threshold 25 kata memiliki proporsi pemenuhan cakupan rubrik sebesar 23,2%. Sementara itu, narasi dengan panjang di bawah threshold tersebut mencatat tingkat pemenuhan cakupan rubrik yang rendah, yaitu sebesar 13,1%.

**V.2.1.4 Evaluasi Deteksi Indikator Relevansi Topik (**Ø«**)**

Deteksi relevansi topik dievaluasi menggunakan pendekatan whole-text embedding pada seluruh narasi. Pendekatan ini menghasilkan nilai F1-Score optimal sebesar 0,4296 pada threshold 0,85. Pada titik kalibrasi tersebut, metrik precission tercatat sebesar 0,4265 dan recall sebesar 0,4327. Hasil klasifikasi prediksi memuat 241 kasus true positive (TP), 324 false positive (FP)), 316 false negative (FN), dan 9.103 true negative (TN). Pola perubahan persisi dan recall terhadap penyesuaian threshold disajikan pada [Gambar V.3.](#page-11-0)

Gambar V.3. Grafik Performa Relevansi Topik dengan Whole-text-embedding

Distribusi skor similarity pada klasifikasi prediksi untuk indikator relevansi topik disajikan pada [Tabel V.4.](#page-11-1) Rata-rata skor untuk kasus RP adalah 0,8690, sedangkan FP adalah 0,8608. Untuk kasus klasifikasi negatif, rata-rata skor FN tercatat sebesar 0,8266 dan TN sebesar 0,8075.

Tabel V.4. Sebaran Nilai FN, FP, TN, TP untuk Indikator Relevansi Topik

Outcome  |  Count  |  Mean  |  Std  |  Min  |  25%  |  50%  |  75%  |  Max
FN  |  316  |  0.8266  |  0.0170  |  0.7703  |  0.8154  |  0.8293  |  0.8403  |  0.8500
FP  |  324  |  0.8608  |  0.0094  |  0.8501  |  0.8534  |  0.8585  |  0.8655  |  0.8979
TN  |  9103  |  0.8075  |  0.0196  |  0.7481  |  0.7941  |  0.8080  |  0.8216  |  0.8500
TP  |  241  |  0.8690  |  0.0152  |  0.8501  |  0.8569  |  0.8663  |  0.8787  |  0.9127

**V.2.2 Statistik Deskriptif dan Verifikasi Asumsi (RQ 2)**

Subbab ini menyajikan deskripsi partisipan, statistik deskriptif dari tingkat pemenuhan indikator tekstual narasi feedback, serta hasil verifikasi asumsi parametrik sebelum pengujian inferensial dilakukan.

Penentuan partisipan didasarkan pada kriteria inklusi mahasiswa aktif yang bersedia berpartisipasi secara sukarela tanpa konsekuensi terhadap penilaian akademik. Meskipun subjek eksperimen telah dipetakan pada subbab IV.5.1, tidak seluruh subjek eksperimen menyelesaikan kedua assessment . Beberapa mahasiswa hanya mengirimkan self assessment atau peer assessment, sedangkan sebagian lainnya tidak menyelesaikan salah satu komponen tersebut.

Penelitian ini tidak melakukan imputasi terhadap data yang tidak terkumpul tersebut. Analisis dilakukan menggunakan data yang benar-benar tersedia, sehingga jumlah observasi pada setiap jenis assessment mengikuti jumlah respons yang berhasil dikumpulkan dari masing-masing kelompok.

Distribusi partisipan yang dialokasikan ke dalam kelompok treatment dan kontrol, beserta total dokumen self dan peer assessment yang terkumpul disajikan pada [Tabel V.5.](#page-12-1)

Tabel V.5. Deskripsi Data Terkumpul dari Eksperimen yang Dilakukan

Kelompok  |  Jumlah Mahasiswa  |  Total Mahasiswa mengisi Self Assessment  |  Total Mahasiswa mengisi Peer Assessment  |  Total Jawaban Self  |  Total Jawaban Peer
Treatment  |  15  |  15  |  14  |  57  |  56
Kontrol  |  17  |  17  |  17  |  68  |  75

Berdasarkan [Tabel V.5](#page-12-1) terdapat satu data yang tidak terkumpul untuk peer assessment. Proporsi yang tidak terkumpul hanya satu relatif kecil jika dibandingkan dengan 32 subjek eksperimen. Dengan demikian, hasil eksperimen yang akan dipaparkan diinterpretasikan berdasarkan data yang tersedia.

Unit analisis pada pengujian ini adalah mahasiswa.Nilai evaluasi merupakan hasil agregasi tingkat pemenuhan indikator pada seluruh narasi feedback yang ditulis oleh setiap mahasiswa. Statistik deskriptif yang mencakup nilai mean, standar deviasi, median, nilai minimum, dan maksimum untuk kelompok treatment dan kontrol disajikan pada [Tabel V.6](#page-13-0) untuk self assessment dan [Tabel V.7](#page-13-1) untuk peer assessment.

Tabel V.6. Statistik Deskriptif Self Assessment

Indikator  |  Kelompok  |  Mean  |  Standar Deviasi  |  Median  |  Min  |  Max
Cakupan Rubrik  |  Treatment  |  0.267  |  0.258  |  0.25  |  0.0  |  0.75
Kontrol  |  0.132  |  0.219  |  0.00  |  0.0  |  0.75
Koherensi Skor  |  Treatment  |  0.467  |  0.297  |  0.50  |  0.0  |  0.75
Kontrol  |  0.426  |  0.351  |  0.50  |  0.0  |  1.00
Kedalaman  |  Treatment  |  0.433  |  0.458  |  0.25  |  0.0  |  1.00
Elaborasi  |  Kontrol  |  0.074  |  0.246  |  0.00  |  0.0  |  1.00
Treatment  |  0.633  |  0.339  |  0.75  |  0.0  |  1.00
Relevansi Topik  |  Kontrol  |  0.647  |  0.331  |  0.75  |  0.0  |  1.00

Tabel V.7. Statistik Deskriptif Peer Assessent

Indikator  |  Kelompok  |  Mean  |  Standar Deviasi  |  Median  |  Min  |  Max
Cakupan Rubrik  |  Treatment  |  0.286  |  0.275  |  0.25  |  0.0  |  0.75
Kontrol  |  0.191  |  0.188  |  0.25  |  0.0  |  0.75
Koherensi Skor  |  Treatment  |  0.446  |  0.369  |  0.375  |  0.0  |  1.00
Kontrol  |  0.603  |  0.386  |  0.75  |  0.0  |  1.00
Kedalaman  |  Treatment  |  0.357  |  0.389  |  0.25  |  0.0  |  1.00
Elaborasi  |  Kontrol  |  0.044  |  0.132  |  0.0  |  0.0  |  0.5
Treatment  |  0.571  |  0.372  |  0.625  |  0.0  |  1.00
Relevansi Topik  |  Kontrol  |  0.588  |  0.364  |  0.75  |  0.0  |  1.00

Sebelum pengujian multivarfiat dan univariat dilaksanakan, dilakukan verifikasi asumsi normalitas menggunakan uji Shapiro-Wilk dan homogenitas variant menggunakan uji Levene. Hasil uji asumsi untuk seluruh indikator pada kedua jenis assessment dilaporkan pada [Tabel V.8.](#page-13-2)

Tabel V.8. Hasil Uji Asumsi

Jenis Asssessment  |  Indikator  |  Normalitas Kelompok Treatement  |  Jenis Asssessment  |  Indikator
Self Assessment  |  (Cakupan) @  |  Tidak  |  Tidak  |  Ya
(Koherensi) A  |  Tidak  |  Tidak  |  Ya
(Elaborasi) `  |  Tidak  |  Tidak  |  Tidak
(Relevansi) J  |  Ya  |  Tidak  |  Ya

Jenis Asssessment  |  Indikator  |  Normalitas Kelompok Treatement  |  Jenis Asssessment  |  Indikator
Peer Assessment  |  (Cakupan) @  |  Tidak  |  Tidak  |  Ya
(Koherensi) A  |  Ya  |  Tidak  |  Ya
(Elaborasi) `  |  Tidak  |  Tidak  |  Tidak
(Relevansi) J  |  Ya  |  Tidak  |  Ya

Berdasarkan hasil pengujian tersebut, sebagian besar indikator pada self maupun peer assessment tidak memenuhi asumsi distribusi normal. Pada uji homogenitas, sebagian besar indikator memiliki varians yang homogen, kecuali indikator kedalaman elaborasi (`) yang menunjukkan pelanggaran homogenitas baik pada self maupun peer assessment.

**V.2.3 Hasil Pengujian Multivariat dan Univariat (RQ 2)**

Pengujian statistik infersial dilakukan secara bertahap, dimulai dari analisis multivariat untuk melihat efek keseluruhan, dilanjutkan dengan analisis univariat untuk setiap indikator. Pengujian multivariat menggunakan Multivariate Anaysis of Variance (MANOVA) dengan metrik Pillai's Trace. Hasil pengujian multivariat disajikan pada [Tabel V.9.](#page-14-1)

Tabel V.9. Hasil Pengujian Multivariat

Jenis Assessment  |  Pillai Value  |  p-value  |  Signifikan
Self  |  0.2677  |  0.0688  |  Tidak
Peer  |  0.3047  |  0.0441  |  Ya

Pada pengujian self assessment, nilai pillai's trace tercatat sebesar 0,2677 dengan nilai signifikansi } = 0,0688. Pada peer assessment, nilai Pillai's Trace tercatat sebesar 0,3047 dengan nilai signifikansi } = 0,0441.

Pengujian tahap kedua menggunakan analisis univariat Mann-Whitney U yang didampingi dengan pengukuran effect size menggunakan rank-biserial correlation. Keputusan penggunaan uji non parametrik ini didasarkan pada hasil verifikasi asumsi sebelumnya. Hasil pengujian univariat beserta besaran dampaknya disajikan pada Tabel V.10 untuk self assessment, dan Tabel V.11 untuk peer assessment.

Tabel V.10. Hasil Pengujian Univariat untuk Self Assessment

Indikator  |  Uji yang Digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect Size
(Cakupan) @  |  Mann-Whitney  |  0.0880  |  Tidak  |  0.329
(Koherensi) A  |  Mann-Whitney  |  0.6823  |  Tidak  |  0.086
(Elaborasi) `  |  Mann-Whitney  |  0.0054  |  Ya  |  0.49
(Relevansi) J  |  Mann-Whitney  |  0.9223  |  Tidak  |  -0.024

Tabel V.11. Hasil Pengujian Univariat untuk Peer Assessment

Indikator  |  Uji yang Digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect Size
(Cakupan) @  |  Mann-Whitney  |  0.3809  |  Tidak  |  0.176
(Koherensi) A  |  Mann-Whitney  |  0.2722  |  Tidak  |  -0.231
(Elaborasi) `  |  Mann-Whitney  |  0.0059  |  Ya  |  0.487
(Relevansi) J  |  Mann-Whitney  |  0.9189  |  Tidak  |  -0.025

Pada self assessment, pengujian univariat menunjukkan nilai } = 0,0054 pada indikator kedalaman elaborasi (`), dengan effect size sebesar 0,490. Indikator cakupan rubrik (@), koherensi skor (A), dan relevansi topik (J) mencatat nilai signifikansi di atas threshold ^ yang disesuaikan.

Pola seragam ditemukan pada peer assessment, di mana indikator kedalaman elaborasi (`) mencatat nilai signifikansi } = 0,0059 dengan effect size sebesar 0,487. Indikator lainnya tidak mencatat perbedaan yang signifikan secara statistik.

**V.2.4 Hasil Pengolahan Data Interaksi Scaffolding (RQ 2)**

Subbab ini menyajikan data proses interaksi mahasiswa dengan digital scaffolding selama penyusunan narasi feedback. Data yang disajikan mencakup frekuensi kebutuhan bantuan yang terdeteksi, tingkat resolusi dan persistensi indikator, serta klasifikasi operasi edit yang dilakukan mahasiswa pada setiap siklus revisi.

**V.2.4.1 Distribusi Kebutuhan Bantuan, Resolusi, dan Persistensi**

Sistem digital scaffolding mendeteksi kebutuhan bantuan setiap kali sebuah indikator teridentifikasi tidak terpenuhi pada awal siklus revisi. Frekuensi kemunculan kebutuhan bantuan pada setiap indikator diukur pada self assessment

dan peer assessment. Distribusi frekuensi ini divisualisasikan melalui heatmap pada [Gambar V.4.](#page-1-0)

Gambar V.4. Frekuensi Kebutuhan Bantuan yang Terdeteksi

Respons mahasiswa terhadap scaffolding dievaluasi menggunakan metrik tingkat resolusi, yaitu proporsi kebutuhan bantuan yang berhasil diselesaikan pada revisi berikutnya, dan tingkat persistensi, yaitu proporsi kebutuhan bantuan yang tetap bertahan pasca-intervensi. Data tingkat resolusi divisualisasikan pada [Gambar V.5](#page-2-0) dan tingkat persistensi disajikan pada [Gambar V.6.](#page-2-1)

Gambar V.5. Tingkat Resolusi Keempat Indikator

Gambar V.6. Tingkat Persistensi Antar Indikator

Berdasarkan data tersebut, indikator relevansi topik (J) mencatat tingkat resolusi tertinggi pada kedua assessment, yaitu 29,9% pada self assessment dan 33,3% pada peer assessment. Sebaliknya, indikator cakupan rubrik (@) mencatat tingkat resolusi terendah pada self assessment (5,1%) dengan tingkat persistensi yang tinggi, yaitu 93,4% pada self assessment dan 95,5% pada peer assessment. Indikator kedalaman elaborasi (`) mencatat resolusi sebesar 21,0% pada self assessment dan 9,7% pada peer assessment.

**V.2.4.2 Karakteristik Perbaikan Narasi**

Perubahan tekstual narasi pasca-intervensi dievaluasi menggunakan operasi Levenshtein pada tingkat token, yang mengklasifikasikan revisi ke dalam empat kategori, yaitu: (1) No Change (NC), (2) Insertion (INS), (3) Deletion (DEL), dan (4) Substitution (SUB). Distribusi klasifikasi operasi ini disajikan pada [Gambar](#page-3-0)  [V.7](#page-3-0).

Gambar V.7. Pola Revisi Perubahan

Operasi Insertion mendominasi pada kedua konteks penilaian, yaitu 61,6% pada self assessment dan 69,5% pada peer assessment. Operasi Substitution menempati urutan kedua dengan proporsi 23,2% pada self assessment dan 17,2% pada peer assessment. Operasi Deletion mencatat proporsi yang relatif kecil, yaitu 12,3% pada self dan 8,6% pada peer assessment. Kategori No Change berada pada proporsi terendah, yaitu 2,9% pada self assessment dan 4,7% pada peer assessment.

**V.2.4.3 Dinamika Pemenuhan Indikator Tekstual Narasi Feedback**

Analisis perubahan status indikator pada [Gambar V.8](#page-4-0) menunjukkan proporsi pemenuhan berbeda antar indikator.

Gambar V.8 Dinamika Pemenuhan Indikator Saat Sesi Eksperimen

Indikator kedalaman elaborasi, menunjukkan kondisi berhasil terpenuhi yang lebih sering ditemukan dibandingkan indikator lainnya. Sebaliknya, pada indikator cakupan rubrik, koherensi skor dan relevansi topik, keberadaan bantuan digital scaffolding tidak selalu diikuti oleh perubahan pemenuhan status indikator yang bertahan hingga akhir sesi eksperimen

**V.2.4.4 Penyelesaian Akhir Kebutuhan Scaffolding**

Pada [Gambar V.9](#page-5-0) disajikan kondisi kebutuhan bantuan digital scaffolding yang berhasil teratasi pada akhir sesi selalu lebih tinggi dibandingkan yang terpenuhi hanya melalui satu kali revisi setelah menerima bantuan digital scaffolding.

Gambar V.9 Perbandingan Pemenuhan Indikator Terpenuhi

[Gambar V.9](#page-5-0) menyajikan perbandingan antara tingkat penyelesaian kebutuhan bantuan setelah revisi pertama dan tingkat penyelesaian kebutuhan bantuan pada akhir sesi revisi. Pada seluruh indikator, tingkat penyelesaian pada akhir sesi lebih tinggi dibandingkan tingkat penyelesaian setelah revisi pertama.

Pada indikator cakupan rubrik, tingkat penyelesaian meningkat dari sekitar 7,6% menjadi 21,2%. Pada indikator koherensi skor dan narasi, tingkat penyelesaian meningkat dari sekitar 5,9% menjadi 15,9%. Sementara itu, indikator kedalaman elaborasi menunjukkan peningkatan dari sekitar 16,4% menjadi 43,9%, dan indikator relevansi topik meningkat dari sekitar 30,9% menjadi 50,0%.

Hasil tersebut menunjukkan adanya perbedaan antara tingkat penyelesaian kebutuhan bantuan yang terjadi segera setelah bantuan digital scaffolding diberikan dan tingkat penyelesaian yang tercapai pada akhir sesi revisi.

**V.2.5 Hasil Kuesioner Evaluasi Pengguna**

Subbab ini memaparkan hasil evaluasi kuesioner yang dirancang sebagai instrumen eksplanatori dengan pendekatan metode campuran, sebagaimana telah ditetapkan pada subbab III.6.6.1B, dengan jumlah responden yang disajikan pada [Tabel V.12](#page-6-0). Pengumpulan data kualitatif dan kuantitatif ini berfungsi untuk memvalidasi penerimaan intervensi secara psikologis dan operasional oleh pengguna. Sesuai dengan pedoman implementasi pada subbab IV.5.2. Pemaparan hasil difokuskan pada evaluasi penerimaan intervensi dalam kelompok treatment melalui subbab [V.2.5.1](#page-6-1).

Tabel V.12. Jumlah Responden Kuesioner

Kelompok: Jumlah Responden
Treatment: 11 Responden
Kontrol: 14 Responden
Total: 25 Responden

**V.2.5.1 Evaluasi Penerimaan dan Beban Kognitif**

Kuesioner pada kelompok treatment difokuskan pada pengukuran preceived usefullness dalam [Gambar V.10](#page-7-0) dan identifikasi cognitive load dari intervensi digital scaffolding selama proses penulisan dalam [Gambar V.11.](#page-7-1) Berdasarkan rancangan instrumen pada Tabel IV.49, mahasiswa diminta memberikan evaluasi menggunakan skala linier (1-5), di mana skor 1 merepresentasikan "Sangat Tidak Setuju" dan skor 5 merepresentasikan "Sangat Setuju". Data ini dihimpun dari 11 subjek yang secara aktif menggunakan sistem.

Gambar V.10. Rata-rata Skor Evaluasi Penerimaan (TAM)

Gambar V.11. Rata-rata Skor Evaluasi Beban Kognitif

Berdasarkan nilai rata-rata dari skala Likert 5 poin, fitur intervensi menunjukkan penerimaan utilitas yang positif. Responden menilai bahwa intervensi digital scaffolding berhasil membantu mereka mengingat kriteria rubrik yang terlewat dengan skor rata-rata tertinggi yaitu 4,00. Aspek kegunaan keseluruhan dan fleksibilitas interaksi memiliki rata-rata 3,91, diikuti oleh kejelasan instruksi dan kemudahan memahami struktur penilaian dengan skor 3,82. Namun, data juga menunjukkan kehadiran distorsi kognitif. Pertanyaan yang mengukur extraneous cognitive load, yaitu perasaan pusing akibat informasi yang terlalu padat dan gangguan konsentrasi saat mengetik, masing-masing mencatat skor yang cukup signifikan, yaitu 3,45.

Untuk memetakan secara spesifik elemen antarmuka yang berdampak pada utilitas maupun beban kognitif tersebut, responden ditugaskan untuk mengidentifikasi komponen yang dirasa paling membantu yang disajikan pada [Gambar V.12](#page-8-0), sekaligus paling mengganggu yang disajikan pada [Gambar V.13](#page-9-0). Data dikumpulkan melalui instrumen checkboxes yang mengizinkan pilihan lebih dari satu.

Gambar V.12. Komponen Scaffolding yang Dinilai Paling Membantu

Hasil pemetaan komponen yang paling membantu menunjukkan bahwa "Arahan mengenai apa yang harus ditulis dalam narasi" menjadi preferensi utama yang dipilih oleh 7 responden (38,9%). Komponen "Peringatan kekurangan narasi yang ditulis" berada pada posisi kedua, dipilih oleh 6 responden (33,3%). Indikator status warna dan sentence starter masing-masing dipilih sebayak dua kali (11,1%). Terdapat pula satu responden yang menambahkan opsi khusus berupa pandan rentang angka/skor (5,6%).

Gambar V.13. Komponen Scaffolding yang Dinilai Mem9utuhkan Perbaikan

Di sisi lain, hasil identifikasi komponen tang membutuhkan perbaikan atau dinilai mengganggu, menunjukkan pola distribusi yang ironis. Komponen "Arahan mengenai apa yang harus ditulis dalam narasi" justru menduduki peringkat teratas sebagai fitur yang paling mengganggu oleh 6 responden (42,3%), diikuti oleh "Peringatan diagnosis kekurangan narasi yang ditulis" oleh 3 responden (21,4%) dan "Contoh kalimat pembuka" oleh 2 responden (14,3%). Selain itu, terdapat masukan kualitatif spesifik dari beberapa responden mengenai mekanisme UI. Tiga entri respons menyoroti isu teknis pergeseran layar otomatis, di mana pembaruan teks scaffolding saat mahasiswa sedang mengetik menyebabkan layar bergulir ke bawah, sehingga membingungkan dan mengganggu fokus visual.

**V.3 Pembahasan Hasil Eksperimen**

Subbab ini menginterpretasikan hasil pengujian komputasional dan statistik inferensial yang telah dipaparkan pada subbab sebelumnya untuk menjawab dua research questions. Pembahasan menstrukturkan temuan empiris ke dalam dua fokus analisis utama. Fokus pertama mengevaluasi kapabilitas teknis pipeline digital scaffolding dalam mendeteksi indikator tekstual narasi feedback di lingkungan PjBL untuk menjawab RQ 1. Fokus kedua menganalisis dampak pedagogis dari intervensi tersebut terhadap pemenuhan indikator tekstual narasi feedback, yang ditinjau melalui sintesis komprehensif antara luaran statistik, dinamika proses revisi mahasiswa, dan implikasi beban kognitif pengguna untuk menjawab RQ 2.

**V.3.1 Pembahasan Kemampuan Deteksi Pipeline (Menjawab RQ 1)**

Research question pertama mengevaluasi sejauh mana pipeline digital scaffolding mampu mendeteksi keempat indikator tekstual narasi feedback melalui kombinasi model semantik terhadap ground truth anotasi dan aturan heuristik. Jawaban atas pertanyaan ini diinterpretasikan melalui tiga kerangka evaluasi, sebagaimana divisualisasikan pada [Gambar V.14.](#page-10-0)

Gambar V.14. Kerangka untuk Menjawab RQ 1

Kerangka evaluasi pertama berfokus pada capaian komputasional menggunakan metrik performa F1-Score yang telah dieksekusi terhadap 384 data ground truth. Kerangka kedua meninjau justifikasi fungsional berdasarkan rasio risiko antar False Positive dan False Negative secara spesifik untuk setiap indikator tekstual. Kerangka ketiga menggunakan standar komparatif empiris yang menunjuk pada rentang performa pipeline NLP dalam konteks domain pendidikan.

Berdasarkan keseluruhan hasil evaluasi, keempat indikator menunjukkan karakteristik deteksi yang berbeda. Cakupan rubrik menghasilkan performa yang relatif stabil untuk mengidentifikasi keberadaan aspek-aspek rubrik. Koherensi skor dan narasi merupakan indikator yang paling menantang karena memerlukan penalaran terhadap tingkat kualitas jawaban. Kedalaman elaborasi dioperasionalkan menggunakan pendekatan deterministik berbasis jumlah kata sehingga tidak dievaluasi sebagai tugas klasifikasi semantik. Sementara itu, relevansi topik masih mampu mengenali domain pembahasan, namun performanya menurun ketika hubungan antara narasi dan aspek rubrik harus disimpulkan secara implisit.

**V.3.1.1 Pembahasan Indikator Cakupan Rubrik (**Ø°**)**

Berdasarkan hasil evaluasi komputasional pada indikator cakupan rubrik dalam subbab 0, nilai recall (0,7275) tampak lebih tinggi dibandingkan precision (0,5312). Hal ini merepresentasikan sensitivitas pipeline yang lebih tinggi terhadap kebenaran unit dekomposisi di dalam narasi mahasiswa. Konsekuensi dari sensitivitas ini adalah meningkatnya jumlah deteksi positif yang kurang tepat (FP).

Ruang pemisahan class menggunakan threshold 0,84 tergolong sangat sempit. Selisih rata-rata skor similarity antara TP dan FP hanya sebesar 0,0103. Distribusi nilai yang sempit ini memperlihatkan bahwa pasangan narasi dan dekomposisi rubrik yang berstatus FALSE pada ground truth masih dapat menghasilkan skor similarity yang tinggi, ditunjukkan pada [Gambar V.15](#page-11-0).

Gambar V.15. Distribusi FP dan FN pada Rubrik

Varians false positive terkonsentrasi pada kriteria yang menuntut abstraksi tinggi, seperti "Kemampuan Mengelola Waktu", "Kemampuan Menyampaikan Ide", dan "Kelengkapan Struktur Data". Kriteria-kriteria ini mencatat 19 hingga 25 kasus FP. Model embedding cenderung mengaitkan kosakata umum mahasiwa dengan kriteria tersebut. Pipeline menganggap suatu kriteria telah dibahas meskipun mahasiswa belum mengevaluasi aspek tersebut secara eksplisit.

[Tabel V.13](#page-12-0) menunjukkan bahwa model sering memberikan skor cosine similarity tinggi (0,89 hingga 0,9) pada narasi yang hanya menyebutkan istilah terkait rubrik tanpa penjelasan memadai. Sebagai contoh, kalimat "menginputkan data dengan teliti" memperoleh skor tinggi terhadap kriteria "Keakuratan Data yang Diinput". Narasi tersebut belum menyertakan alasan atau proses evaluasi yang mendukung pertanyaan terkait. Temuan ini mengindikasikan bahwa model lebihi mudah mengenali kesamaan topik dibandingkan memverifikasi substansi kriteria. Narasi yang sangat singkat dan superfisial masih terdeteksi memenuhi kriteria.

Tabel V.13. Sampel data False Positive

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Menyarankan struktur data yang memadai dengan data yang ada
0  |  1  |  Komunikasi  |  Kemampuan Menyampaikan Ide  |  banyak menyampaikan ide banyak menyampaikan ide dan membanntu menyepakatinya
0  |  1  |  Penginputan Data ke Excel  |  Keakuratan Data yang Diinput  |  menginputkan data dengan teliti
0  |  1  |  Inisiatif dan Pemecahan Masalah  |  Kemampuan Menyelesaikan Masalah  |  menanggapi masalah dengan baik
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Rekan saya mengusulkan beberapa struktur untuk data yang akan digunakan. Struktur tersebut sangat berguna untuk pengolahan data
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Struktur data yang dia sampaikan sesuai dengan tujuan dari pengumpulan data

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
0  |  1  |  Penginputan  |  Keakuratan Data yang  |  sepertinya tidak ada
Data ke Excel  |  Diinput  |  ketidaktelitian dalam penginputan datanya
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Struktur data yang diusulkan oleh rekan saya sangat baik. Struktur tersebut sangat memadai dan sesuai dengan data yang dikumpulkan.
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  struktur yang dikumpulkan sudah sesuai & memadai dengan data No. dikumpulan.
0  |  1  |  Manajemen Waktu  |  Kemampuan Mengelola Waktu  |  Tepat waktu dan tidak mepet

Kondisi tersebut memvalidasi urgensi penggunaan indikator kedalaman elaborasi (`) sebagai lapisan validasi tambahan. Indikator ` memastikan sebuah kriteria dijelaskan menggunakan jumlah kata yang memadai. Sebagian false positive pada @ dapat direduksi secara hierarkis melalui pemenuhan `.

Varians false negative terpusat pada kriteria yang berorientasi pada objek fisik atau kuantitas, seperti "Jumlah Iklan yang Dikumpulkan", "Tingkat Pemahaman Konten Iklan", dan "Keragaman Platform", sebagaimana disajikan pada [Tabel V.14.](#page-13-0)

Tabel V.14. Sampel Data False Negative

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
1  |  0  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Cukup baik, teman saya membantu dalam memberi saran dan masukan
1  |  0  |  Pengumpulan Iklan Lowongan Kerja  |  Kemudahan dalam Pengumpulan Data  |  Karena Faridha bagian platform TikTok juga (sama dengan Emir) mereka jadi lebih cepat dan mudah dalam mencari loker
1  |  0  |  Pemahaman terhadap Isi Iklan  |  Tingkat Pemahaman Konten Iklan  |  Yups, I'd say she did
1  |  0  |  Pemahaman terhadap Isi Iklan  |  Tingkat Pemahaman Konten Iklan  |  Saya mengumpulkan dulu informasi apa yang terdapat dalam data tersebut dan apa yang bisa saya olah dari data tersebut serta saya masukkan ke dalam sturkut kolom yang kelompok saya punya

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Sampel pada [Tabel V.14](#page-13-0) memperlihatkan kesulitan model dalam menangani narasi implisit. Mahasiswa sering mendeskripsikan aktivitas konkret tanpa menggunakan terminologi rubrik. Sebagai contoh, narasi "memilih platform Linked-In yan berupa teks dll, hal ini menjadi kemudahan bagi saya" gagal melewati threshold 0,84 untuk kriteria "Kemudahan dalam Pengumpulan Data". Penilaian manusia dapat memahami hubungan tersebut melalui proses inferensi. Model embedding mengandalkan semantic similarity tekstual dan gagal melakukan inferensi terhadap gabungan implisit tersebut.

Dalam konteks penerapan digital scaffolding pada zone of proximal development (ZPD), sebagaimana didefinisikan pada subbab II.1.10, kasus FN menyebabkan mahasiswa yang memerlukan bantuan gagal menerima intervensi. Kasus FP memicu pemberian scaffolding tambahan yang bersifat redundan. Mahasiswa dapat mengabaikan scaffolding redundan tersebut tanpa merusak pemahaman mereka.

**V.3.1.2 Pembahasan Indikator Koherensi Skor dan Narasi (**Øø**)**

Hasil evaluasi komputasional pada indikator koherensi skor dan narasi memperlihatkan overlap yang tinggi antar prediksi benar dan salah, sebagaimana dijabarkan pada subbab V.2.1.2. Rata-rata skor similarity untuk kelas TP (0,9100) dan FP (0,9052) memiliki selisih yang sangat tipis. Kondisi ini memperlihatkan bahwa pipeline digital scaffolding cenderung memberikan skor similarity yang tinggi pada sebagian besar narasi, sehingga membatasi ruang pemisah antara klasifikasi TRUE dan FALSE.

Karakteristik ini muncul karena model embedding mampu menangkap topik dari deskriptor skor pada rubrik secara umum, tetapi mengalami kesulitan mendiskriminasi tingkat kualitas jawaban yang bersifat ordinal. Model mengenali bahwa mahasiswa sedang membahas suatu kriteria, tetapi gagal mendeteksi apakah narasi tersebu merepresentasikan tingkat pencapaian "tidak memahami", "cukup memahami", atau "sangat memahami". Akibatnya, narasi yang seharusnya terklasifikasi pada kategori skor yang berbeda tetap menghasilkan skor similarity yang setara.

Pola sebaran kesalahan klasifikasi ini tidak terdistribusi secara merata pada keseluruhan data, sebagaimana divisualisasikan pada [Gambar V.16.](#page-1-0)

Gambar V.16. Sebaran FP dan FN berdasarkan Label Anotasi

Gambar tersebut menunjukkan bahwa kasus false positive (FP) terkonsentrasi pada kriteria yang merepresentasikan tingkatan kualitas dalam skala ordinal, seperti komunikasi, pemahaman, dan kualitas struktur data. Hal ini dikonfirmasi melalui sampel data kesalahan yang disajikan pada [Tabel V.15](#page-1-1).

Tabel V.15. Sampel Data FP pada Koherensi Skor dan Narasi

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
0  |  1  |  Pemahaman terhadap Isi Iklan  |  Sangat memahami informasi penting dari iklan  |  Dia memahami beberapa info penting dalam iklan
0  |  1  |  Pemahaman terhadap Isi Iklan  |  Cukup memahami isi iklan  |  Memahami, karena sudah dapat memilih iklan iklan yang sesuai
0  |  1  |  Pemahaman terhadap Isi Iklan  |  Cukup memahami isi iklan  |  Ya tsinan memahami informasi penting didalam iklan
0  |  1  |  Komunikasi  |  Cukup efektif dalam komunikasi  |  beliau sangat efektif dalam berkomunikasi karna informasi yang di sampaikan jelas dan tegas
0  |  1  |  Komunikasi  |  Ide sangat tersampaikan dengan jelas  |  Dia menyampaikan ide dengan cukup baik
0  |  1  |  Inisiatif dan Pemecahan Masalah  |  Memberikan solusi untuk menyelesaikan masalah  |  mencari jalan keluar dari masalah itu
0  |  1  |  Komunikasi  |  Cukup efektif dalam komunikasi  |  Komunikasinya sudah efektif, dapat

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
menyampaikan ide dan saran dengan baik juga.
0  |  1  |  Penggabungan Data dengan Kelompok Lain  |  Sangat terlibat dan membantu menyelesaikan penggabungan  |  rekan saya cukup berkontribusi dalam penggabungan
0  |  1  |  Komunikasi  |  Ide sangat tersampaikan dengan jelas  |  banyak menyampaikan ide banyak menyampaikan ide dan membanntu menyepakatinya
0  |  1  |  Penginputan Data ke Excel  |  Sangat teliti dalam penginputan  |  ia cukup teliti dalam meningput data.

Sebagian besar FP terjadi akibat kegagalan model membedakan intensitas tingkat pencapaian. Sebagai contoh, narasi "Dia memahami beberapa info penting dalam iklan" diprediksi selaras dengan kriteria "Sangat Memahami Informasi penting dalam iklan", meskipun terdapat gradasi kualitas yang jelas antara capaian "memahami" dan "sangat memahami". Temuan ini mengindikasikan bahwa model mampu mengidentifikasi 'apa' yang sedang dievaluasi, tetapi belum mampu menentukan 'seberapa baik' kualitas performa tersebut berdasarkan teks narasi.

Di sisi lain, kasus false negative (FN) terpusat pada kriteria yang menuntut interpretasi terhadap informasi implisit. Sampel untuk kasus ini dirangkum pada [Tabel V.16](#page-2-0).

Tabel V.16. Sampel Data FN pada Koherensi Skor dan Narasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Kasus FN umumnya muncul ketika mahasiswa menyampaikan bukti evaluasi secara tersirat melalui deskripsi aktivitas konkret atau penyebutan entitas spesifik. Narasi yang menyebutkan penggunaan "media sosial Facebook" atau "Linkedin" merupakan bukti praktis dari kriteria "Platform Bervariasi". Penilai manusia dapat mengubungkan tindakan tersebut dengan kriteria rubrik melalui proses interpretasi. Namun, karena hubungan tersebut dinyatakan menggunakan pengalaman nyata dan bukan terminologi rubrik, model embedding gagal mendeteksinya.

Secara keseluruhan, indikator koherensi skor menyingkap tantangan utama pipeline komputasional berbasis embedding. Sistem mampu mendeteksi deskriptor skor yang sedang dibahas, tetapi menghadapi keterbatasan ketika harus mendiskriminasi tingkat pencapaian ordinal serta menginterpretasikan informasi implisit di dalam narasi mahasiswa.

**V.3.1.3 Pembahasan Indikator Elaborasi (**Øƒ**)**

Berbeda dengan ketiga indikator lainnya yang mengandalkan model embedding untuk mengevaluasi semantik teks, indikator kedalaman elaborasi berbasiskan pada konten leksikal secara struktural, sebagaimana dipaparkan pada subbab V.2.1.3. Pendekatan ini dilandasi oleh asumsi bahwa narasi yang melewati threshold 25 kata menyediakan ruang yang lebih luas bagi mahasiswa untuk menguraikan alasan, menyertakan contoh, atau menjelaskan proses evaluasi yang mendasari penilaian mereka.

Perbedaan proporsi pemenuhan cakupan rubrik antara narasi panjang (23,2%) dan narasi pendek (13,1%) mengindikasikan kesesuaian penetapan threshold tersebut terhadap karakteristik data penilaian. Temuan ini mengonfirmasi bahwa narasi yang lebih panjang cenderung memuat lebih banyak bukti evaluatif yang selaras dengan aspek rubrik penilaian. Oleh karena itu, indikator ini berfungsi untuk mengidentifikasi narasi yang berpotensi belum membangun elaborasi yang memadai sehingga memerlukan dorongan tambahan melalui mekanisme scaffolding.

Meskipun demikian, panjang kalimat tidak dapat diinterpretasikan sebagai representasi mutlak dari kualitas elaborasi. Terdapat kemungkinan mahasiswa menghasilkan narasi yang panjang namun berputar-putar tanpa makna, atau sebaliknya, menyusun narasi singkat yang sangat padat dan substantif. Oleh karena itu, threshold 25 kata diposisikan secara fungsional sebagai indikator untuk mengidentifikasi kemungkinan kurangnya elaborasi, bukan sebagai pengukur kualitas yang holistik. Di dalam digital scaffolding, informasi kedalaman elaborasi tidak beroperasi secara terisolasi, melainkan dipertimbangkan bersama keseluruhan indikator tekstual lainnya dalam pengambilan keputusan.

**V.3.1.4 Pembahasan Indikator Relevansi Topik (**Ø«**)**

Meskipun subbab V.2.1.4 menyatakan bahwa terdapat overlap antar distribusi skor pada Tabel V.4, data menunjukkan bahwa rata-rata skor TAPI tetap berada di atas FP, sementara FN dan TN terkonsentrasi pada rentang skor yang lebih rendah. Pola ini mengonfirmasi bahwa pipeline digital scaffolding mampu menghasilkan prediksi yang cukup relevan. Pipeline digital scaffolding dapat membedakan keberadaan topik evaluatif pada tingkat tertentu dan mengenali apakah narasi mahasiswa sedang membahas aspek yang sesuai dengan pertanyaan rubrik, meskipun belum mencapai pemisahan class yang tegas.

Pola perubahan precission dan recall pada Gambar V.3 yang berlangsung relatif bertahap memperkuat temuan tersebut. Distribusi nilai similarity antara prediksi benar dan salah masih memiliki ruang pemisah untuk menentukan relevansi topik. Namun, pola ini juga mengungkap batas kemampuan model embedding dalam membedakan topik yang dinyatakan secara eksplisit dengan topik tersirat.

Tabel V.17. Sampel Data FP pada Relevansi Topik

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Unit Dekomposisi Rubrik  |  Narasi
0  |  1  |  Inisiatif dan Pemecahan Masalah  |  Dukungan terhadap Anggota Tim  |  membantu menyelesaikan maslah pada anggota tim
0  |  1  |  Penginputan Data ke Excel  |  Keakuratan Data yang Diinput  |  menginputkan data dengan teliti
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Menyarankan struktur data yang memadai dengan data yang ada
0  |  1  |  Komunikasi  |  Partisipasi dalam Diskusi Kelompok  |  ikut berkontribusi saat ada diskusi di kelas
0  |  1  |  Komunikasi  |  Kemampuan Menyampaikan Ide  |  banyak menyampaikan ide banyak menyampaikan ide dan membanntu menyepakatinya
0  |  1  |  Inisiatif dan Pemecahan Masalah  |  Kemampuan Menyelesaikan Masalah  |  menanggapi masalah dengan baik
0  |  1  |  Penginputan Data ke Excel  |  Keakuratan Data yang Diinput  |  sepertinya tidak ada ketidaktelitian dalam penginputan datanya
0  |  1  |  Kolaborasi dan Kerjasama Tim  |  Kemampuan Menyampaikan Ide  |  Dengan mengemukakan pendapatnya

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Unit Dekomposisi Rubrik  |  Narasi
0  |  1  |  Pembuatan  |  Kelengkapan  |  Struktur  |  Struktur data yang dia
Struktur Data  |  Data  |  sampaikan sesuai dengan tujuan dari pengumpulan data
0  |  1  |  Manajemen  |  Kemampuan  |  Mengelola  |  Tepat waktu dan tidak
Waktu  |  Waktu  |  mepet

Berdasarkan [Tabel V.17,](#page-5-0) sebagian besar kasus false positive (FP) muncul ketika mahasiswa menggunakan terminologi yang menceritakan aktivitas umum terkait suatu aspek rubrik, tetapi substansinya belum cukup kuat untuk memenuhi kriteria topik yang dimaksud. Sebagai contoh, pernyataan "menginputkan data dengan teliti" terdeteksi sebagai indikator keakuratan penginputan data, sementara "dengan mengemukakan pendapatnya" diprediksi berkaitan dengan kemampuan menyampaikan ide. Kesalahan ini menunjukkan bahwa model embedding cukup sensitif menangkap sinyal topik, namun masih kesulitan membedakan antara penyebutan aktivitas general dan pembahasan eksplisit terhadap aspek rubrik.

Sebaliknya, sampel false negative (FN) memperlihatkan kesulitan sistem ketika narasi memuat bukti perilaku konkret yang memerlukan inferensi tambahan, dengan sampel yang disajikan pada [Tabel V.18.](#page-6-0) Penyebutan penggunaan platform seperti "LinkedIn" untuk mempermudah proses, atau "Facebook" dan "Tiktok", gagal dipetakan oleh model ke dalam dimensi "Kemudahan Pengumpulan Data" atau "Keragaman Sumber Platform".

Tabel V.18. Sampel Data FN pada Relevansi Topik

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
1  |  0  |  Pembuatan  |  Kelengkapan Struktur  |  Cukup baik, teman saya
Struktur Data  |  Data  |  membantu dalam memberi saran dan masukan
1  |  0  |  Pemahaman  |  Tingkat Pemahaman  |  Yups, I'd say she did
terhadap Isi: Konten Iklan
Iklan
1  |  0  |  Pengumpulan  |  Kemudahan dalam  |  Karena Faridha bagian
Iklan  |  Pengumpulan Data  |  platform TikTok juga (sama
Lowongan: dengan Emir) mereka jadi
Kerja: lebih cepat dan mudah
dalam mencari loker

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Secara keseluruhan, pemrosesan whole-text embedding terbukti cukup efektif untuk mendukung digital scaffolding, khususnya dalam mendeteksi keselarasan fokus narasi mahasiswa terhadap aspek evaluasi. Model embedding berkinerja baik dalam mengenali topik evaluatif eksplisit, namun performanya menurun ketika dihadapkan pada bukti perilaku yang membutuhkan interpretasi implisit. Dalam konteks penelitian ini, kapabilitas tersebut sudah memadai untuk memicu intervensi scaffolding agar mahasiswa tetap mempertahankan relevansi feedback dengan aspek yang ditetapkan dengan rubrik.

**V.3.1.5 Sintesis Jawaban RQ 1**

Berdasarkan evaluasi terhadap keempat indikator tekstual, yaitu cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, serta relevansi topik, pipeline digital scaffolding menunjukkan kemampuan deteksi yang berbeda-beda sesuai dengan karakteristik indikator yang diukur. Hasil evaluasi menunjukkan bahwa indikator yang memerlukan interpretasi semantik yang lebih sederhana cenderung menghasilkan performa yang lebih baik dibandingkan indikator yang menuntut inferensi evaluatif yang lebih kompleks. Temuan ini mengindikasikan bahwa kemampuan pipeline tidak bersifat seragam, melainkan dipengaruhi oleh sifat konstruk yang hendak dideteksi.

Pada indikator berbasis model embedding, cakupan rubrik mencapai performa dengan F1-score 0,61, koherensi skor-narasi menjadi F1-score 0,53, sedangkan relevansi topik mencapai F1-Score 0,43. Kinerja ada indikator relevansi topik merupakan yang terendah, hal tersebut disebabkan oleh: (1) distribusi kelas pada dataset yang tidak seimbang, (2) kebutuhan akan pemahaman konteks yang lebih kompleks, serta (3) adanya narasi yang secara umum terlihat relevan terhadap proyek tetapi tidak spesifik terhadap aspek rubrik yang dinilai. Meskipun demikian, Pipeline digital scaffolding masih mampu mengenali kesesuaian topik pembahasan meskipun mahasiswa menggunakan variasi ekspresi yang berbeda dengan terminologi yang digunakan dalam rubrik. Sebagai contoh, narasi "ia memahami apa yang perlu dicari dalam iklan, walaupun pada awalnya dia tidak paham tetapi selalu menanyakan ketidakpahamannya itu" berhasil dideteksi pada aspek rubrik "Pemahaman terhadap Isi Iklan" pada dekomposisi "Tingkat Pemahaman Konten Iklan." Meskipun tidak menggunakan frasa yang identik dengan dekomposisi rubrik. Temuan ini menunjukkan bahwa model embedding mampu menangkap kesamaan makna pada tingkat frasa semantik yang tidak dapat dijangkau melalui pendekatan berbasis pencocokan kata kunci semata.

Sebaliknya, koherensi skor dan narasi merupakan indikator yang paling menantang. Rendahnya performa pada indikator ini menunjukkan bahwa model embedding mengalami kesulitan ketika harus membedakan tingkatan kualitas jawaban yang bersifat ordinal, seperti membedakan narasi yang merepresentasikan tingkat pemahaman "kurang", "cukup", atau "sangat". Pada kasus ini, narasi mahasiswa sering kali telah membahas aspek deskriptor skor pada rubrik. Namun, deskriptor skor dalam rubrik tidak dibedakan berdasarkan topik yang dibahas melainkan berdasarkan tingkat pencapaian terhadap deskriptor skor yang sama. Akibatnya, narasi yang seharusnya dipetakan ke kategori skor yang berbeda dapat menghasilkan representasi semantik yang berdekatan karena secara bersamaan membahas aspek deskriptor skor yang serupa. Temuan ini menunjukkan bahwa tantangan utama pada indikator koherensi skor dan narasi yang menilai kesesuaian narasi dengan skor yang dituju terletak pada kemampuan pipeline digital scaffolding untuk membedakan tingkatan kualitas yang bersifat ordinal berdasarkan narasi mahasiswa.

Berbeda dengan ketiga indikator tersebut, kedalaman elaborasi diimplementasi melalui aturan heuristik berbasis threshold 25 kata leksikal . Oleh karena itu, indikator ini tidak dievaluasi menggunakan precision, recall, dan F1-score sebagaimana indikator berbasis model embedding. Hasil analisis menunjukkan bahwa narasi yang lebih panjang cenderung memiliki peluang lebih besar untuk memenuhi indikator lain, khususnya cakupan rubrik. Temuan ini mendukung penggunaan kedalaman elaborasi sebagai indikator struktural untuk mengidentifikasi kebutuhan mahasiswa dalam mengembangkan penjelasan yang lebih rinci.

Sintesis terhadap hasil analisis error memperlihatkan adanya pola yang konsisten pada indikator berbasis model embedding. Sebagian besar kesalahan muncul karena kebutuhan untuk melakukan inferensi evaluatif terhadap informasi yang disampaikan secara implisit. Mahasiswa sering kali menyampaikan penilaian melalui pengalaman, observasi, atau deskripsi aktivitas konkret yang tidak menggunakan terminologi yang identik dengan rubrik. Sebagai contoh, narasi seperti "dia dapat memahami informasi dengan sangat baik" dapat merepresentasikan unit dekomposisi "Tingkat Pemahaman Konten Iklan" pada aspek rubrik "Pemahaman terhadap Isi Iklan". Meskipun kata "pemahaman" tidak pernah disebutkan secara langsung. Temuan ini menunjukkan bahwa model embedding tetap diperlukan untuk menangkap variasi ekspresi yang memiliki makna serupa. Namun demikian, hasil penelitian juga menunjukkan bahwa model embedding belum sepenuhnya memadai ketika sistem harus melakukan inferensi evaluatif yang lebih mendalam atau membedakan tingkatan kualitas jawaban yang bersifat ordinal.

Temuan tersebut memberikan implikasi terhadap desain pipeline yang diusulkan. Indikator yang bersifat struktural, seperti kedalaman elaborasi, dapat dideteksi secara efektif melalui pendekatan deterministik yang sederhana dan transparan. Sebaliknya, indikator yang berkaitan dengan kesamaan makna memerlukan representasi semantik melalui embedding. Meskipun demikian, hasil penelitian menunjukkan bahwa representasi semantik saja belum cukup untuk menangani seluruh kompleksitas evaluasi naratif. Oleh karena itu, integrasi pendekatan deterministik dalam pipeline digital scaffolding berperan sebagai mekanisme pelengkap untuk meningkatkan konsistensi pengambilan keputusan.

Dalam konteks digital scaffolding yang beroperasi pada Zone of Proximal Development (ZPD), karakteristik performa pipeline digital scaffolding yang telah diimplementasikan perlu diinterpetasikan berdasaran konsekuensi pedagogis dari setiap jenis kesalahan deteksi diluar besaran metrik komputasional yang dihasilkan. Hasil evaluasi menunjukkan kegagalan mahasiswa yang membutuhkan bantuan yaitu False Negative berpotensi menghilangnya kesempatan untuk memberikan scaffolding untuk memberikan bantuan yang diperlukan agar mahasiswa dapat melanjutkan proses refleksi atau evaluasinya. Sebaliknya, kasus False Positive akan memicu pemberian scaffolding yang berlebihan, namun mahasiswa dapat mengabaikan intervensi tersebut tanpa merusak pemahaman mereka.

Berdasarkan keseluruhan temuan tersebut, RQ1 dapat dijawab bahwa pipeline digital scaffolding yang diusulkan mampu melakukan komputasi dan mendeteksi keempat indikator tekstual narasi feedback, melalui kombinasi model semantik dan aturan heuristik, dengan performa yang berbeda-beda sesuai dengan karakteristik indikator yang diukur. Indikator cakupan rubrik dan koherensi skor-narasi menunjukkan performa deteksi tingkat menengah, kedalaman elaborasi dikur melalui aturan heuristik, sementara relevansi topik menunjukkan performa deteksi terendah. Pipeline digital scaffolding menunjukkan performa yang relatif lebih tinggi pada indikator yang bergantung pada pencocokan makna semantik dan karakteristik tekstual yang dapat diamati secara langsung, namun mengalami penurunan performa ketika diperlukan inferensi evaluatif, seperti membedakan tingkatan kualitas yang bersifat ordinal atau memetakan hubungan implisit antara narasi mahasiswa dan konstruk evaluatif dalam rubrik. Temuan ini menunjukkan bahwa pipeline digital scaffolding memiliki kemampuan untuk mendukung mendeteksi keempat indikator tekstual narasi feedback pada narasi yang telah ditulis mahasiswa, meskipun belum sepenuhnya mampu menangani seluruh kebutuhan interpretasi evaluatif yang terkandung dalam narasi reflektif.

**V.3.2 Dampak Intervensi terhadap Pemenuhan Indikator Tekstual Narasi Feedback (Menjawab RQ 2)**

Research question yang kedua mengevaluasi sejauh mana digital scaffolding membantu pemenuhan keempat indikator tekstual narasi feedback antara kelompok kontrol dan treatment, serta bagaimana mahasiswa berinteraksi dengan sistem tersebut di lingkungan eksperimen. Jawaban pertanyaan ini diinterpretasikan melalui dua sumber yang saling melengkapi, yaitu outcome dan evaluasi proses sebagaimana divisualisasikan pada [Gambar V.17.](#page-12-0)

Gambar V.17. Kerangka untuk Menjawab RQ 2

Evaluasi outcome difokuskan pada pengujian statistik terhadap tingkat pemenuhan keempat indikator tekstual narasi feedback pada kondisi jawaban akhir dalam feedback mahasiswa. Analisis pada tahap ini mengidentifikasi keterkaitan antara keberadaan scaffolding dengan tingkat pemenuhan keempat indikator tekstual narasi feedback. Analisis tingkat proses ini memanfaatkan rekaman proses revisi narasi, transisi status indikator, serta pola respons mahasiswa terhadap teks scaffolding. Integrasi dari kedua perspektif ini memberikan penjelasan yang komprehensif mengenai dampak intervensi dan mekanisme kerjanya.

**V.3.2.1 Perbedaan Hasil Akhir Kelompok Kontrol dan Treatment (RQ 2)**

Analisis terhadap dampak digital scaffolding difokuskan pada interpretasi hasil pengujian statistik inferensial yang telah dilaporkan pada subbab V.2.3. Mengingat penelitian ini merupakan pilot study dengan ukuran sampel yang relatif kecil serta beberapa indikator sepenuhnya memenuhi asumsi parametrik, hasil MANOVA diposisikan sebagai analisis multivariat yang bersifat eksploratori untuk mengidentifikasi pola perbedaan secara keseluruhan antara kelompok kontrol dan treatment. Untuk mengurangi ketergantungan terhadap asumsi paramterik pada tingkat indikator individual, analisis lanjutan dilakukan dengan menggunakan Mann-Whitney U. Oleh karena itu, interpretasi hasil penelitian mempertimbangkan arah perbedaan dan besaran effect size sebagai estimasi awal bagi penelitian selanjutnya yang bersifat konfirmatori.

Pada level multivariat menggunakan MANOVA pada peer assessment menghasilkan Pillai Trace = 0,3047 dan nilai signifikansi } = 0,0441 dan Self Assessment Pillai Trace = 0,2677 dan nilai signifikansi } = 0,0688. Perbedaan ini mengindikasikan bahwa keberadaan digital scaffolding lebih konsisten berkaitan dengan perbedaan profil keempat indikator secara simultan ketika mahasiswa menilai pekerjaan peer mereka dalam peer assessment dibandingkan menilai pekerjaan diri sendiri pada self assessment.

Penelusuran lebih spesifik pada tingkat univariat menyingkap bahwa indikator kedalaman elaborasi (`) menjadi satu-satunya dimensi yang merespons intervensi secara konsisten. Data pada Tabel V.10 dan Tabel V.11 memperlihatkan bahwa indikator ini mencatat nilai } < 0,01 pada kedua jenis assessment dengan effect size rank-biserial 0,49 pada self assessment dan 0,487 pada peer assessment. Konsistensi temuan pada kedua jenis assessment menjadi indikasi kuat bahwa bantuan digital scaffolding berkaitan dengan peningkatan mahasiswa menghasilkan narasi feedback yang lebih elaboratif.

Di sisi lain, indikator cakupan rubrik (@), koherensi skor dan narasi (A), serta relevansi topik (J) tidak mencatat perbedaan yang signifikan antar kelompok Meskipun indikator cakupan rubrik pada self assessment mencatat effect size sebesar 0,329 yang mengarah pada peningkatan kelompok treatment. Namun, bukti empiris dari ukuran sampel ini tidak memiliki kekuatan statistik yang memadai untuk mengesahkannya secara formal.

Mengingat eksperimen ini dikondisikan sebagai pilot study, yang bertujuan mengevaluasi kelayakan implementasi bantuan intervensi digital scaffolding, mengidentifikasi pola awal serta menyediakan estimasi effect size sebagai dasar perencanaan lebih lanjut. Indikator lainnya yang belum menunjukkan signifikansi secara statistik pada penelitian ini dianggap sebagai temuan awal yang membuka peluang dan verifikasi lebih lanjut melalui penelitian dengan sampel yang lebih besar dan statistical power yang lebih memadai.

**V.3.2.2 Dinamika Interaksi dan Resolusi Scaffolding (Menjawab RQ 2)**

Keempat sumber data yang telah disajikan pada subbab V.2.4 mengenai distribusi bantuan, tingkat respons, pola revisi serta dinamika pemenuhan indikator pada dasarnya merekam satu mekanisme yang sama dari berbagai sudut pandang: dimana kesulitan muncul, bagaimana mahasiswa merespons, dengan rasa apa mereka merespons, dan apakah setiap respons berhasil memenuhi indikator tekstual narasi feedback.

Titik awal mekanisme kebutuhan bantuan digital scaffolding yang paling sering muncul. Sebagaimana ditunjukkan pada subbab V.2.4.1, indikator cakupan rubrik @ dan koherensi skor dan narasi A adalah dua indikator yang paling sering memicu bantuan digital scaffolding pada self dan peer assessment. Temuan ini menunjukkan bahwa kebutuhan bantuan yang berkaitan dengan kelengkapan aspek evaluasi serta

keselarasan antara skor dan justifikasi naratif relatif lebih sering muncul selama proses penulisan narasi feedback dibandingkan indikator lainnya.

Ketika kebutuhan terdeteksi dan bantuan digital scaffolding diberikan, mahasiswa pada umumnya menindaklanjuti dengan melakukan perbaikan atau merevisi narasi feedback mereka. Tipe perubahan No Change sangat rendah pada self dan peer assessment menunjukkan bahwa hampir seluruh kesempatan revisi benar-benar diikuti oleh perubahan narasi feedback. Namun demikian, menindaklanjuti bantuan yang diberikan tidak secara otomatis masalah pada indikator tersebut terselesaikan. Tingkat resolusi atau tindaklanjut yang menghasilkan pemenuhan terhadap indikator yang tidak terpenuhi dalam satu kali perbaikan tetap rendah untuk sebagian indikator, dengan indikator relevansi topik memiliki tingkat pemenuhan dalam satu kali perbaikan paling tinggi jika dibandingkan dengan indikator lainnya.

Bentuk tindak lanjut tersebut juga dapat dikatakan homogen atau serupa. Operasi penambahan mendominasi pola revisi pada kedua konteks self dan peer assessment  jauh melampaui substitution, deletion, atau revisi struktural lainnya. Artinya, strategi yang dipilih sebagian besar mahasiswa adalah menambahkan penjelasan, alasan, atau elaborasi ke dalam narasi yang sudah ada, bukan menulis ulang atau menghapus jawaban dari awal. Mahasiswa mempertahankan struktur dasar jawaban dan memperkaya isinya.

Strategi penambahan konten pada narasi feedback yang dominan ini menjelaskan mengapa perubahan status indikator tidak berlangsung seragam. Pada indikator kedalaman elaborasi, strategi menambah penjelasan secara langsung selaras dengan kebutuhan indikator tersebut, sehingga perubahan status menuju kondisi terpenuhi relatif lebih sering ditemukan V.2.4.4 Sebaliknya, pada cakupan rubrik dan koherensi skor-narasi, kebutuhan perbaikan bersifat berbeda: cakupan rubrik menuntut penambahan aspek evaluasi yang benar-benar belum tercakup, bukan sekadar kalimat tambahan apa pun, sedangkan koherensi skor dan narasi menuntut penyelarasan ulang antara skor dan narasi, sebuah proses reflektif, bukan ekspansi konten biasa.

Akan tetapi, ketidakberhasilan pada satu siklus revisi bukan berarti kebutuhan bantuan tersebut sama sekali tidak terselesaikan. Perbandingan antara tingkat penyelesaian pada akhir sesi eksperimen. Subbab V.2.4.4 menunjukkan bahwa sebagian indikator, khususnya kedalaman elaborasi dan relevansi topik, mencapai penyelesaian akhir yang lebih tinggi dibandingkan resolusi pada revisi tunggal. Pola ini mengindikasikan bahwa perbaikan berlangsung secara bertahap, di mana mahasiswa tidak selalu menyelesaikan kebutuhan bantuan pada upaya pertama, tetapi melalui beberapa siklus revisi berikutnya dalam sesi yang sama, sebagian kebutuhan tersebut akhirnya tertangani.

Merangkai temuan-temuan tersebut menunjukkan kemungkinan adanya satu pola yang konsisten, mahasiswa cenderung lebih sering mengalami kesulitan pada indikator cakupan rubrik dan koherensi skor-narasi yang menuntut keterkaitan yang lebih eksplisit antara narasi feedback dengan struktur penilaian yang digunakan. Ketika bantuan diberikan, mahasiswa umumnya merespons dengan menambahkan penjelasan ke dalam narasi yang sudah ada, bukan menulis ulang. Respons tersebut tidak selalu langsung menyelesaikan kebutuhan bantuan yang mendasarinya, terutama pada indikator yang menuntut perubahan struktur evaluatif. Namun melalui beberapa siklus revisi, sebagian kebutuhan tersebut akhirnya terselesaikan pada akhir sesi. Dengan demikian, bantuan digital scaffolding pada penelitian ini berfungsi lebih sebagai pemicu proses revisi bertahap dibandingkan sebagai instruksi yang menghasilkan perbaikan instan, dan dampaknya cenderung lebih terlihat pada indikator yang tampak selaras dengan strategi revisi yang umum dilakukan mahasiswa, yaitu perluasan elaborasi narasi.

**V.3.2.3 Pembahasan Beban Kognitif dan Penerimaan Sistem**

Data eksperimen mengindikasikan bahwa sistem memberikan dukungan yang dipersepsikan membantu proses penyusunan narasi feedback, namun pada saat yang sama memunculkan beban kognitif ekstra akibat rancangan antarmuka yang kurang optimal.

**A. Indikasi Paradoks Utilitas Substantif dan Gangguan Visual**

Salah satu temuan utama dari hasil kuesioner adalah perbedaan persepsi pengguna terhadap utilitas digital scaffolding. Komponen "Arahan mengenai apa yang harus ditulis dalam narasi" dipilih sebagai fitur yang paling membantu penyusunan narasi oleh 7 responden, namun secara bersamaan menduduki peringkat tertinggi sebagai fitur yang paling mengganggu, oleh 6 responden.

Fenomena ini mengindikasikan adanya pemisahan antara kualitas substansi dan mekanisme delivery. Secara substansi, teks digital scaffolding dipersepsikan relevan dengan kebutuhan pengguna dalam menyusun elemen rubrik, yang sejalan dengan target Zone of Proximal Developement (ZPD). Arahan tersebut tepat sasaran dalam memandu kelengkapan elemen rubrik. Namun, mekanisme penyajian teks yang berubah secara real-time berkolerasi dengan laporan peningkatan beban kognitif ekstra pada sebagian pengguna.

Laporan beban kognitif ekstra tercermin dari rata-rata 3,45 pada komponen pertanyaan "merasa pusing/terlalu banyak informasi" dan "mengganggu konsentrasi tulisan". Berdasarkan hasil evaluasi kualitatif terbuka, keluhan pengguna merujuk pada dua isu, yaitu split-attention effect dan auto-scroll issue.

Isu pertama berkaitan berkaitan dengan fenomena split-attention effect, yaitu terbaginya perhatian pengguna. Karena sistem merespons narasi feedback secara real-time, teks scaffolding berubah-ubah secara dinamis saat mahasiswa sedang memformulasikan kalimat. Kondisi ini mengharuskan mahasiswa membagi fokus visual dan kognitif mereka kepada narasi yang sedang diketik dan area scaffolding.

Isu kedua berkaitan dengan perilaku antarmuka saat instruksi diperbaharui. Sejumlah responden melaporkan bahwa perubahan teks scaffolding yang memicu pergeseran viewport ke arah bawah secara otomatis saat mahasiswa sedang mengetik. Pergeseran visual ini berpotensi mendistrupsi konsentrasi mahasiswa karena mereka perlu menyesuaikan kembali posisi layar secara berulang.

**B. Implikasi terhadap Desain Sistem**

Sintesis dari kedua fenomena di atas menyimpulkan bahwa digital scaffolding berbasis model embedding SBERT yang dikembangkan sudah mencapai tingkat utilitas fungsional yang valid untuk mendampingi metode Project-Based Learning (PjBL). Sistem mampu menghasilkan teks digital scaffolding sebagai instruksi perbaikan yang dipersepsikan relevan oleh sebagian besar responden.

Akan tetapi, efektivitas pedagogis ini tereduksi oleh mekanisme feedback yang terlalu agresif. Intervensi sistem yang dilakukan secara instan pada setiap ketikan diduga berkontribusi terhadap meningkatkanya persepsi cognitive load pengguna. Untuk implementasi pada skala yang lebih luas, mekanisme real-time perlu dimodifikasi menggunakan suatu mekanisme adaptif untuk menentukan waktu terbaik memberikan intervensi, atau merelokasi penempatan teks scaffolding secara berdampingan dengan formulir input narasi feedback.

**V.3.2.4 Sintesis Jawaban RQ 2**

Berdasarkan temuan yang telah dipaparkan pada V.3.2.2, V.3.2.1, dan [V.3.2.3](#page-1-0) dapat disusun rangkaian argumen berikut untuk menjawab RQ2 secara utuh.

Pertama, digital scaffolding berhasil mengidentifikasi kebutuhan bantuan untuk mengartikulasikan evaluative expression yaitu kemampuan mengartikulasikan penilaian ke dalam bentuk narasi yang ditulis oleh mahasiswa sesuai dengan frekuensi deteksi tertinggi pada indikator cakupan rubrik dan koherensi skor-narasi, dua indikator yang juga paling sulit dipenuhi mahasiswa secara independen. Kedua, mahasiswa umumnya merespons bantuan digital scaffolding yang diberikan, ditunjukkan oleh proporsi No Change yang sangat rendah pada kedua konteks penilaian. Ketiga, respons tersebut diwujudkan hampir seluruhnya melalui revisi narasi berupa penambahan informasi (insertion), bukan substitusi atau penghapusan. Keempat, karena bentuk revisi yang dominan ini secara struktural lebih cocok untuk memperkaya isi narasi dibandingkan memperbaiki struktur evaluatif, perubahan status pemenuhan indikator yang paling efektif justru terjadi pada indikator kedalaman elaborasi. Kelima, indikator yang menuntut penalaran evaluatif lebih kompleks, yaitu cakupan rubrik dan koherensi skor-narasi, tetap sulit diperbaiki meskipun mahasiswa aktif merevisi. Keenam, kegagalan dalam memperbaiki indikator kompleks tersebut tidak hanya disebabkan oleh kecenderungan tipe revisi, tetapi juga diperparah oleh tingginya beban cognitive load. Akan tetapi hasil kuesioner menunjukkan adanya persepsi gangguan pada sebagian pengguna selama penggunaan digital scaffolding. Hasil kuesioner menunjukkan bahwa sebagian mahasiswa menganggap mekanisme teks digital scaffolding yang muncul secara instan selama proses penulisan sebagai gangguan terhadap konsentrasi mereka

Rangkaian argumen tersebut secara langsung menjelaskan mengapa hasil pengujian statistik pada subbab V.2.3 menunjukkan kedalaman elaborasi sebagai satu-satunya indikator yang signifikan secara konsisten pada Self maupun Peer Assessment, sementara cakupan rubrik, koherensi skor, dan relevansi topik tidak menunjukkan perbedaan signifikan antara kelompok treatment dan kontrol. Dengan demikian, dampak digital scaffolding terhadap pemenuhan indikator tekstual narasi feedback  yang merupakan manifestasi terbatas dari kemampuan evaluative expression dalam kerangka feedback literacy pada mahasiswa tidak bersifat seragam di seluruh indikator, melainkan paling kuat termanifestasi pada indikator yang selaras dengan bentuk revisi yang secara alami dilakukan mahasiswa, yaitu perluasan elaborasi narasi. Pada indikator yang menuntut perubahan struktur evaluatif yang lebih mendalam, dampak bantuan digital scaffolding pada penelitian ini masih terbatas dan memerlukan bentuk digital scaffolding yang lebih eksplisit, lebih bertahap, atau disertai contoh konkret, serta membutuhkan perancangan mekanisme interaksi yang meminimalkan disrupsi kognitif visual agar mahasiswa dapat menjaga konsentrasi saat mengartikulasikan evaluasi mereka.

**V.4 Hasil Perbaikan Aplikasi Pendukung Eksperimen**

Subbab ini merupakan implementasi dari tahap yang didefinisikan dalam subbab III.6.5.4 berdasarkan pembahasan hasil eksperimen yang dipetakan pada subbab V.3.

Subbab [V.3.2.3](#page-1-0) mengidentifikasi adanya keluhan pengguna yang berkaitan dengan distraksi berupa disrupsi fokus (split-attention effect) dan auto-scroll issue selama proses penulisan narasi feedback., sehingga mengganggu proses penulisan narasi feedback mahasiswa. Hal ini didukung oleh saran subjek yang disajikan pada [Tabel](#page-5-0)  [V.19](#page-5-0)

Tabel V.19. Keluhan Subjek yang menyatakan Distraksi

No  |  Bagian Sistem yang Mengganggu  |  Keluhan Subjek Eksperimen
1  |  Contoh kalimat pembuka/sentence starter  |  Sesaat setelah mengetik agak terganggu dengan teks AI yang muncul, yang membuat konsentrasi agak pecah untuk menulis yang ada dipikiran
2  |  Keseluruhan scaffolding utuh  |  Saran posisi rekomendasi fitur AI mungkin bisa di bagian bawah inputan. Karena ketika mengetik, fitur AI yang mulai bekerja otomatis menggulir halaman kebawah.
3  |  Peringatan diagnosis kekurangan narasi yang ditulis  |  karena kadang peringatannya terlalu cepat padahal masih mikir untuk nulis apa

Sebagai respons terhadap temuan tersebut, dilakukan modifikasi pada GUI-43 dan GUI-46 yang telah dimodelkan pada subbab IV.4.2.1G. Modifikasi yang dilakukan berupa transformasi contrainer scaffolding menjadi elemen collapsible yang dapat ditutup dan dibuka sesuai keinginan pengguna. Secara default, scafolding akan tertutup dan hanya menampilkan status dari empat indikator tekstual, sebagaimana disajikan pada [Gambar V.18](#page-7-0). Dalam kondisi ini, tombol panah collapsible akan bercahaya untuk pertama kali sebagai upaya menarik perhatian pengguna untuk membuka gulir scaffolding. Jika mahasiswa menekan tombol collapsible, maka container scaffolding akan tetap terbuka meskipun pertanyaan berganti hingga tombol ditekan kembali, sebagaimana disajikan pada [Gambar V.19](#page-8-0) Pendekatan antarmuka adaptif ini diterapkan untuk mengurangi potensi distraksi visual yang dilaporkan pengguna tanpa menghilangkan visibilitas terhadap status pemenuhan indikator rubrik.

Perlu dicatat bahwa modifikasi dilakukan setelah seluruh data eksperimen selesai dikumpulkan. Oleh karena itu, perubahan tersebut tidak memengaruhi hasil analisis yang digunakan untuk menjawab research question, melainkan berfungsi sebagai tindak lanjut desain berdasarkan masukan subjek eksperimen yang diperoleh selama eksperimen.

Gambar V.18. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

Gambar V.19. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

**V.5 Keterbatasan Penelitian**

Temuan yang diperoleh pada penelitian ini perlu dipahami dalam konteks desain, populasi, dan lingkungan eksperimen yang digunakan. Oleh karena itu interpretasi hasil tidak dimaksudkan untuk menghasilkan kesimpulan yang bersifat universal mengenai potensi kontribusi digital scaffolding dalam mendukung penulisan narasi feedback yang lebih artikulatif pada konteks pembelajaran. Sebaliknya, hasil penelitan memberikan bukti empiris mengenai sejauh mana digital scaffolding  berbasis rubrik bekerja secara komputasional dan kondisi eksperimen yang diuji, sekaligus mengidentifikasi sejumlah keterbatasan yang menjadi peluang pengembangan bagi penelitian selanjutnya.

**V.5.1 Keterbatasan Generalisasi Konteks Penelitian**

Terkait dengan batasan eksternal (external validity)Penelitian yang dilaksanakan pada konteks pembelajaran yang spesifik yaitu mahasiswa Program Sarjana Terapan, Program Studi Teknik Informatika di Politeknik Negeri Bandung yang sedang mengikuti PjBL dalam mata kuliah Manajemen Kualitas Terpadu. Oleh karena itu temuan yang diperoleh perlu dipahami dalam batas konteks tersebut.

Karakteristik tugas, bentuk rubrik, budaya pembelajaran serta tingkat pengalaman mahasiswa yang memberikan narasi feedback merupakan aspek kontekstual yang berbeda dan belum dievaluasi dalam penelitian ini. Oleh karena itu, belum dapat dipastikan bahwa apakah bantuan digital scaffolding akan menunjukkan pola yang sama pada konteks dengan karakteristik yang berbeda. Variasi karakteristik tersebut berpotensi memengaruhi kebutuhan bantuan akan digital scaffolding maupun cara mahasiswa merespons bantuan yang diperoleh. Dengan demikian, temuan yang diperoleh dalam penelitian ini belum dapat diasumsikan berlaku secara langsung pada disiplin ilmu lain, jenjang pendidikan yang berbeda, atau aktivitas reflektif yang menggunakan struktur penilaian yang berbeda.

Perlu diingat bahwa eksperimen yang dilakukan terbatas pada lingkungan institusi dan satu siklus pelaksanaan pembelajaran. Konsekuensinya, penelitian ini belum dapat memastikan apakah pola temuan yang diperoleh akan muncul secara konsisten pada populasi, institusi atau konteks pembelajaran yang berbeda. Penelitian lanjutan pada bidang studi, institusi pendidikan dan skenario jenis pembelajaran selain PjBL diperlukan untuk menguji konsistensi temuan yang diperoleh pada penelitian ini.

**V.5.2 Keterbatasan Desain Eksperimen yang Dipilih**

Penelitian ini menggunakan randomized posttest-only control group design (Desain 6) yang dipilih untuk menghindari potensi bias yang dapat muncul akibat pemberian pre-test sebelum intervensi digital scaffolding diberikan. Meskipun desain ini memiliki kekuatan yang tinggi dalam mengendalikan ancaman validitas internal melalui random assignment, terdapat beberapa keterbatasan yang perlu diperhatikan dalam menginterpretasikan hasil penelitian.

Pertama, penelitian ini tidak dapat mengamati perubahan tingkat pemenuhan pada keempat indikator tekstual narasi feedback pada tingkat individu sebelum dan sesudah menerima perlakuan. Karena pengukuran hanya dilakukan pada tahap posttest, analisis yang dihasilkan berfokus pada perbedaan hasil antara kelompok treatment dan kelompok kontrol, bukan pada besarnya perubahan yang dialami masing-masing mahasiswa selama eksperimen berlangsung. Dengan demikian, penelitian ini tidak dapat menunjukkan secara langsung sejauh mana tingkat pemenuhan keempat indikator tekstual narasi feedback individu meningkat dibandingkan kondisi awalnya sebelum menerima bantuan digital scaffolding.

Kedua, ketiadaan pre-test menyebabkan kemampuan awal mahasiswa terkait penyusunan dan artikulasi narasi feedback tidak dapat diukur secara langsung. Meskipun random assignment digunakan untuk meminimalkan kemungkinan perbedaan karakteristik awal antar kelompok, penelitian ini tidak memiliki data empiris yang dapat digunakan untuk memverifikasi kesetaraan kemampuan awal setiap partisipan sebelum perlakuan diberikan. Oleh karena itu, interpretasi hasil eksperimen didasarkan pada asumsi bahwa proses randomisasi telah menghasilkan distribusi karakteristik awal yang relatif seimbang antara kelompok treatment dan kelompok kontrol.

Ketiga, penelitian ini belum dapat mengevaluasi apakah terdapat perbedaan pola hasil antar mahasiswa dengan tingkat kemampuan awal yang berbeda. Karena tidak tersedia data baseline individual, penelitian ini hanya menghasilkan gambaran kondisi pada tingkat kelompok sehingga variasi yang mungkin muncul berdasarkan kemampuan awal partisipan tidak dapat dianalisis secara langsung.

Meskipun demikian, keterbatasan tersebut merupakan konsekuensi metodologis yang melekat pada penggunaan randomized posttest-only control group design. Dalam konteks penelitian ini, desain tersebut tetap dipilih karena kemampuannya mengurangi potensi testing effect sekaligus memungkinkan evaluasi intervensi dilakukan tanpa memberikan pengukuran awal yang berpotensi memengaruhi respons partisipan terhadap digital scaffolding.

**V.5.3 Keterbatasan Bentuk Digital Scaffolding**

Digital scaffolding pada penelitian ini dirancang dalam bentuk prompt berbasis indikator rubrik yang bertujuan mengarahkan mahasiswa untuk memperbaiki aspek-aspek tertentu pada narasi feedback. Hasil penelitian menunjukkan bahwa bentuk bantuan tersebut lebih sering diikuti oleh perbaikan pada indikator yang berkaitan dengan penambahan informasi, seperti kedalaman elaborasi. Namun demikian, indikator yang memerlukan penalaran evaluatif yang lebih kompleks, seperti koherensi skor dan narasi, masih menunjukkan tingkat penyelesaian kebutuhan bantuan yang relatif lebih rendah dibandingkan indikator lainnya.

Temuan tersebut mengindikasikan bahwa digital scaffolding yang berbasiskan teks prompt mungkin memiliki keterbatasan ketika digunakan untuk mendukung proses evaluasi yang menuntut justifikasi, refleksi, atau penalaran yang lebih mendalam. Dalam konteks tersebut, mahasiswa tidak hanya memerlukan informasi mengenai bagian yang perlu diperbaiki, tetapi juga mungkin memerlukan bantuan yang dapat memandu proses berpikir evaluatif yang mendasari penyusunan narasi feedback.

Penelitian ini hanya mengevaluasi satu bentuk digital scaffolding yang diwujudkan melalui prompt. Oleh karena itu, penelitian ini belum dapat memberikan kesimpulan mengenai bagaimana bentuk scaffolding alternatif, seperti scaffolding reflektif, scaffolding metakognitif, maupun kombinasi beberapa jenis scaffolding, dapat memengaruhi tingkat pemenuhan keempat indikator tekstual narasi feedback mahasiswa. Eksplorasi terhadap bentuk bantuan yang berbeda menjadi peluang penelitian lanjutan untuk memahami jenis scaffolding yang paling sesuai untuk mendukung pemenuhan indikator cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, serta relevansi topik.

**BAB VI**

**ANALISIS DAMPAK HASIL PENELITIAN**

Bab ini menyajikan analisis outcome yang diharapkan dari penerapan hasil penelitian terhadap pemangku kepentingan yang telah diidentifikasi pada subbab I.5, serta evaluasi kinerja dan kegunaan aplikasi pendukung eksperimen (APE) SAPA setelah pipeline digital scaffolding diintegrasikan sebagaimana dipaparkan pada subbab IV.4. Evaluasi disajikan ke dalam tiga bagian, yaitu: (1) outcome yang diharapkan dari mahasiswa dan dosen sebagai pengguna/mitra penelitian, (2) hasil evaluasi kinerja dan kegunaan sistem setelah implementasi yang mencakup pengujian fungsionalitas, pengujian kinerja aplikasi, pengujian usabilitas, pengujian kinerja aplikasi, serta keterbatasan sistem, dan (3) status dokumen keberterimaan dari pengguna/mitra terhadap hasil eksperimen.

**VI.1 Outcome yang Diharapkan dari Pengguna/Mitra**

Sebagaimana telah dipaparkan pada subbab I.5, penelitian ini melibatkan dua kelompok pemangku kepentingan di lingkungan Jurusan Teknik Komputer dan Informatika (JTK) Politeknik Negeri Bandung.

Kelompok pertama adalah mahasiswa yang mengikuti mata kuliah berbasis Project-Based Learning (PjBL) yang memiliki self dan peer assessment sebagai bagian dari proses evaluasi, dalam hal ini mahasiswa peserta mata kuliah Manajemen Kualitas Terpadu yang menjadi subjek pilot study sebagaimana dipetakan pada subbab IV.5.1. Outcome yang diharapkan dari kelompok ini adalah peningkatan kelengkapan, relevansi, dan keselarasan narasi feedback yang mereka tulis selama proses penilaian berlangsung, sehingga proses artikulasi evaluative expression menjadi lebih terarah dibandingkan tanpa bantuan digital scaffolding.

Kelompok kedua adalah dosen pengampu mata kuliah berbasis PjBL yang menggunakan rubrik sebagai komponen evaluasi. Outcome yang diharapkan dari kelompok ini adalah ketersediaan output self dan peer assessment berupa skor numerik dan narasi kualitatif per kriteria yang sudah melalui proses komputasi empat indikator tekstual, sehingga narasi yang diterima dosen memiliki informasi evaluatif yang lebih terstruktur dibandingkan kondisi tanpa digital scaffolding.

Hasil pilot study sebagaimana dipaparkan pada subbab V.2 hingga V.3 menjadi bukti awal sejauh mana kedua outcome tersebut tercapai, khususnya pada indikator kedalaman elaborasi yang menunjukkan indikasi dampak pada kedua jenis assessment.

**VI.2 Hasil Evaluasi Kinerja dan Kegunaan Aplikasi Setelah Implementasi Hasil Penelitian**

Subbab ini mengevaluasi kinerja dan kegunaan APE SAPA secara keseluruhan setelah pipeline digital scaffolding diterapkan, mencakup pengujian fungsionalitas pada subbab [VI.2.1](#page-14-0), serta pengujian usabilitas pada subbab VI.2.2.

**VI.2.1 Pengujian Fungsionalitas**

Pengujian fungsionalitas terhadap APE SAPA telah dilaksanakan sebagaimana dipaparkan pada subbab IV.4.3. Pengujian dilakukan terhadap 42 test case yang mencakup pemeriksaan antarmuka, dekomposisi rubrik, dan seluruh indikator tekstual narasi yang didefinisikan pada Tabel III.3. Hasil pengujian yang didokumentasikan pada Lampiran 3 menunjukkan 41 dari 42 test case dinyatakan lolos, termasuk pengujian fungsionalitas part-of-speech tagging yang terbukti berhasil menyaring input teks acak atau tidak bermakna sebelum diproses oleh model.

Satu test case yang dinyatakan gagal terjadi pada pengujian indikator koherensi skor-narasi dengan skenario narasi yang kontradiktif, yaitu kondisi saat pengguna memasukkan skor tinggi namun menuliskan narasi yang merepresentasikan performa rendah. Sistem secara fungsional berhasil mendeteksi adanya inkonsistensi antara skor dan narasi, namun arsitektur model belum mampu mengekstraksi dan memprediksi angka skor aktual yang tersirat di dalam narasi

secara presisi. Secara keseluruhan, hasil pengujian menunjukkan bahwa fitur-fitur utama APE SAPA hasil integrasi digital scaffolding bekerja sesuai spesifikasi yang dirancang pada subbab IV.4.2, dengan satu limitasi spesifik pada kasus narasi yang bersentimen negatif.

**VI.2.2 Pengujian Usabilitas**

Pengujian usabilitas dilakukan melalui kuesioner evaluasi pengguna terhadap kelompok treatment sebagaimana dipaparkan pada subbab V.2.5, dengan data yang dihimpun dari 11 mahasiswa yang secara aktif menggunakan sistem digital scaffolding. Berdasarkan skala Likert 1-5, mahasiswa menilai bahwa intervensi digital scaffolding membantu mereka mengingat kriteria rubrik yang terlewat dengan skor rata-rata tertinggi, yaitu 4,00. Aspek kegunaan keseluruhan dan fleksibilitas interaksi mencatat rata-rata 3,91, diikuti oleh kejelasan instruksi dan kemudian memahami struktur penilaian dengan skor 3,82. Temuan ini menujukan perceived usefulness yang secara umum positif terhadap sistem.

Meskipun demikian, hasil kuesioner juga mengindikasikan adanya extraneous cognitive load. Pertanyaan yang mengukur perasaan pusing akibat informasi yang teralu padat dan gangguan konsentrasi saat mengetik masing-masing mencatat skor 3,45. Identifikasi komponen antarmuka menunjukkan pola yang ironis, yaitu komponen "arahan mengenai apa yang harus ditulis (Sentence Starter)" merupakan komponen yang paling banyak dipilih sebagai paling membantu, namun pada saat yang sama juga menjadi komponen yang paling banyak dikeluhkan sebagai pengganggu. Saran kualitatif dari subjek eksperimen juga menyoroti isu teknis berupa pergeseran layar otomatis yang membingungkan saat teks scaffolding diperbaharui selagi mahasiswa mengetik. Secara keseluruhan, pengujian usabilitas menunjukkan bahwa sistem dinilai bermanfaat secara fungsional oleh penggunanya, tetapi masih memerlukan penyempurnaan pada sisi pengalaman pengguna agar manfaat tersebut tidak disertai gangguan konsentrasi yang berarti.

VI.2.3 Rekognisi Mitra atas Kebermanfaatan Hasil Penelitian

**BAB VII**

**PENUTUP**

Bab ini menjelaskan kesimpulan dari keseluruhan hasil penelitian yang telah dilakukan untuk menjawab research question yang telah dirumuskan pada subbab I.3, sara bagi penelitian selanjutnya, serta rencana keberlanjutan dan komersialisasi dari hasil penelitian yang dihasilkan pada tugas akhir ini.

**VII.1 Kesimpulan**

Penelitian ini bertujuan merancang pipeline digital scaffolding berbasis rubrik yang mengintegrasikan Natual Language Processing (NLP) dengan rule-based untuk mendeteksi empat indikator tekstual narasi feedback secara real-time, serta mengukur dampak intervensi tersebut terhadap pemenuhan indikator melalui pilot study. Berdasarkan hasil dan pembahasan pada BAB V, kedua tujuan tersebut telah dicapai dengan temuan sebagai berikut.

Terkait RQ 1, pipeline digital scaffolding yang dirancang mampu mendeteksi keempat indikator tekstual narasi feedback melalui kombinasi model semantik dan aturan heuristik, dengan performa yang berbeda-beda sesuai karakteristik indikator. Indikator cakupan rubrik dan koherensi skor-narasi menunjukkan performa deteksi tingkat menengah, dengan F1-Score sebesar 0,61 dan 0,53, kedalaman elaborasi diukur melalui aturan heuristik deterministik berbasis panjang narasi, sementara relevansi topik menunjukkan performa terendah, dengan F1-score senilai 0,43. Pipeline menunjukkan performa yang relatif lebih baik pada indikator yang bergantung pada pencocokan makna semantik dan karakteristik tekstual yang dapat diamati secara langsung, namun mengalami penurunan performa ketika diperlakukan inferensi evaluatif yang lebih kompleks, seperti membedakan tingkatan kualitas ordinal pada indikator koherensi skor dan narasi.

Terkait RQ 2, hasil pengujian multivariat menunjukkan indikasi efek signifikan pada peer assessment, dengan nilai Pillai's Trace sebesar 0,3047 dan p sebesar 0,0441, namun tidak signifikan pada self assessment. Pengujian univariat lebih lanjut mengungkap bahwa dari keempat indikator, hanya kedalaman elaborasi yang secara konsisten memiliki indikasi signifikan pada self assessment, dengan nilai p sebesar 0,005 dan effect size sebesar 0,49, maupun peer assessment dengan nilai p sebesar 0,0059 dan effect size sebesar 0,487, sementara cakupan rubrik, koherensi skor-narasi, dan relevansi topik belum menunjukkan perbedaan yang signifikan antara kelompok kontrol dan treatment. Temuan ini selaras dengan data interaksi pada subbab V.2.4 yang menunjukkan bahwa revisi mahasiswa terhadap scaffolding didominasi oleh operasi penambahan informasi, yang secara struktural lebih sesuai untuk memperkaya isi narasi dibanding memperbaiki struktur evaluatifnya. Dengan demikian, dampak digital scaffolding memiliki indikasi paling kuat pada indikator yang selaras dengan bentuk revisi yang secara alami dilakukan mahasiswa.

Dari sisi penerimaan pengguna, hasil kuesioner pada subbab V.2.5 menunjukkan bahwa mahasiswa secara umum memandang digital scaffolding bermanfaat dalam membantu proses penulisan feedback. Namun demikian, sebagian mahasiswa juga melaporkan adanya tambahan beban kognitif akibat kemunculan scaffolding secara real-time, sehingga aspek rancangan interaksi menjadi perhatian penting pada pengembangan sistem selanjutnya.

Secara keseluruhan, Penelitian ini memberikan tiga kontribusi utama. Pertama, mengusulkan pipeline digital scaffolding berbasis rubrik untuk narasi feedback  berbahasa Indonesia yang menggabungkan semantic embedding dan aturan heuristik. Kedua, menunjukkan bahwa empat indikator tekstual dapat digunakan sebagai dasar komputasional untuk mendeteksi kebutuhan scaffolding selama proses penulisan. Ketiga, menyediakan bukti empiris awal mengenai pengaruh digital scaffolding terhadap kualitas narasi feedback melalui pilot study beserta estimasi effect size sebagai dasar perancangan penelitian berskala lebih besar.

**VII.2 Saran**

Berdasarkan kesimpulan dan keterbatasan penelitian yang telah dipaparkan pada subbab V.5 serta BAB VI, berikut adalah saran yang dapat menjadi fokus bagi penelitian selanjutnya.

1. Peningkatan kemampuan deteksi pada indikator yang menuntut inferensi evaluatif kompleks, khususnya koherensi skor-narasi dan relevansi topik, misalnya melalui fine-tuning model embedding berbahasa Indonesia yang lebih sensitif terhadap perbedaan kualitas ordinal, atau pendekatan lain di luar similarity berbasis embedding tunggal.
2. Eksplorasi bentuk digital scaffolding alternatif di luar prompt berbasis indikator, seperti scaffolding refleksif atau metakognitif, maupun kombinasi beberapa jenis scaffolding, untuk menjawab keterbatasan pada subbab V.5.3.
3. Penggunaan desain eksperimen yang memungkinkan pengukuran perubahan pada tingkat individu, misalnya dengan desain pre-test, untuk mengatasi keterbatasan randomized posttest-only control group design yang diidentifikasi pada subbab V.5.2.
4. Evaluasi lanjutan terhadap efektivitas modifikasi antarmuka collapsible yang diterapkan pada subbab V.4 dalam menurunkan beban kognitif pengguna, karena modifikasi tersebut belum diuji ulang pada kelompok eksperimen baru.
5. Replikasi penelitian pada konteks pembelajaran, mata kuliah, atau institusi yang berbeda di luar JTK Polban dan mata kuliah Manajemen Kualitas Terpadu, untuk menguji konsistensi temuan sebagaimana diidentifikasi pada subbab V.5.1, sekaligus memperbesar jumlah sampel agar power statistik penelitian lebih kuat.

**VII.3 Rencana Keberlanjutan dan Komersialisasi Hasil Penelitian**

**DAFTAR PUSTAKA**

- Aimah, F. R., & Suhartoyo, E. (2024). A decade of Indonesian EFL students' voices toward peer feedback practices during synchronous and asynchronous periods: A systematic literature review. Journal on English as a Foreign Language, 14(1), 48–72. https://doi.org/10.23971/jefl.v14i1.7247
- Albattah, W., & Khan, R. U. (2025). Impact of imbalanced features on large datasets. Frontiers in Big Data, 8. https://doi.org/10.3389/fdata.2025.1455442
- Alfaro, R., Allende-Cid, H., & Allende, H. (2023). Multilabel Text Classification with Label-Dependent Representation. Applied Sciences (Switzerland), 13(6). https://doi.org/10.3390/app13063594
- Bell, S. (2010). Project-Based Learning for the 21st Century: Skills for the Future. The Clearing House: A Journal of Educational Strategies, Issues and Ideas, 83(2), 39–43. https://doi.org/10.1080/00098650903505415
- Boud, D., Lawson, R., & Thompson, D. G. (2013). Does student engagement in self-assessment calibrate their judgement over time? Assessment and Evaluation in Higher Education, 38(8), 941–956. https://doi.org/10.1080/02602938.2013.769198
- Brookhart, S. (2013). How to Create and Use Rubrics for Formative Assessment and Grading. ASCD.
- Brown, P., & Levinson, S. C. (1987). Politeness Some universals in language usage Studies in Interactional Sociolinguistics 4 (Vol. 4).
- Camarata, T., & Slieman, T. A. (2020). Improving Student Feedback Quality: A Simple Model Using Peer Review and Feedback Rubrics. Journal of Medical Education and Curricular Development, 7. https://doi.org/10.1177/2382120520936604
- Campbell, D. T., Stanley, J. C., Mifflin, H., Boston, C., Geneva, D., Hopewell, I., Palo, N. J., & London, A. (1963). EXPERIMENTAL AND QUASI-EXPERIMENT Al DESIGNS FOR RESEARCH.

- Carless, D., & Boud, D. (2018). The development of student feedback literacy: enabling uptake of feedback. Assessment and Evaluation in Higher Education, 43(8), 1315–1325. https://doi.org/10.1080/02602938.2018.1463354
- Cheng, R. W. Y., Lam, S. F., & Chan, J. C. Y. (2008). When high achievers and low achievers work in the same group: The roles of group heterogeneity and processes in project-based learning. British Journal of Educational Psychology, 78(2), 205–221. https://doi.org/10.1348/000709907X218160
- Cho, K., & MacArthur, C. (2011). Learning by Reviewing. Journal of Educational Psychology, 103(1), 73–84. https://doi.org/10.1037/a0021950
- COCHRAN, W. G. . (1977). Sampling techniques. Wiley.
- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences Second Edition.
- Crina, G., & Abraham, A. (2011). Intelligent Systems (Vol. 17). Springer. https://doi.org/10.1007/978-3-642-21004-4
- Curtis, R., Moon, C. C., Hanmore, T., Hopman, W. M., & Baxter, S. (2024). Use the right words: evaluating the effect of word choice and word count on quality of narrative feedback in ophthalmology competency-based medical education assessments. Canadian Medical Education Journal. https://doi.org/10.36834/cmej.76671
- Daou, D., Sabra, R., & Zgheib, N. K. (2020). Factors That Determine the Perceived Effectiveness of Peer Feedback in Collaborative Learning: a Mixed Methods Design. Medical Science Educator, 30(3), 1145–1156. https://doi.org/10.1007/s40670-020-00980-7
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly: Management Information Systems, 13(3), 319–339. https://doi.org/10.2307/249008
- Deemter, K., Krahmer, E., & Theune, M. (2005). Squibs and Discussions Real versus Template-Based Natural Language Generation: A False Opposition? Computational Linguistics, 31, 15–24. http://www.cs.utwente.nl/

- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. http://arxiv.org/abs/1810.04805
- Ding, L., Zhang, H., Zhou, J., & Chen, B. (2025). Contextualization, Procedural Logic, and Active Construction: A Cognitive Scaffolding Model for Topic Sentiment Analysis in Game-Based Learning. Behavioral Sciences 2025, Vol. 15, 15(10). https://doi.org/10.3390/bs15101327
- Dornyei, Zoltan., & Murphey, Tim. (2011). Group Dynamics in the Language Classroom. Cambridge University Press.
- Dunning, D., Heath, C., & Suls, J. M. (2004). Flawed Self-Assessment Implications for Health, Education, and the Workplace. 5(3), 69.
- Durg, A., Zhang, A., & Savelka, J. (2025). LLM-powered Framework for Automatic Generation of Metacognitive Scaffolding Cues for Introductory Programming in Higher Education. https://oli.cmu.edu/
- Enevoldsen, K., Chung, I., Kerboua, I., Kardos, M., Mathur, A., Stap, D., Gala, J., Siblini, W., Krzeminski, D., Winata, G. I., Sturua, S., Utpala, S., Ciancone, M., Schaeffer, M., Sequeira, G., Misra, D., Dhakal, S., Rystrøm, J., Solomatin, R., … Muennighoff, N. (2025). MMTEB: Massive Multilingual Text Embedding Benchmark. 13th International Conference on Learning Representations, ICLR 2025, 19, 102004–102060. https://arxiv.org/pdf/2502.13595
- Fateen, M., Wang, B., & Mine, T. (2024). Beyond Scores: A Modular RAG-Based System for Automatic Short Answer Scoring With Feedback. IEEE Access, 12, 185371–185385. https://doi.org/10.1109/ACCESS.2024.3508747
- Fiel Peres, F. (2026). Effect sizes for nonparametric tests. In Biochemia medica (Vol. 36, Number 1, p. 010101). https://doi.org/10.11613/BM.2026.010101
- Fithriani, R. (2018). Cultural Influences on Students' Perceptions of Written Feedback in L2 Writing. JOURNAL OF FOREIGN LANGUAGE TEACHING & LEARNING, 3.
- Fleischer, T., Moser, S., Deibl, I., Strahl, A., Maier, S., & Zumbach, J. (2023). Digital Sequential Scaffolding during Experimentation in Chemistry

- Education—Scrutinizing Influences and Effects on Learning. Education Sciences, 13(8). https://doi.org/10.3390/educsci13080811
- Gao, M., Hu, X., Yin, X., Ruan, J., Pu, X., & Wan, X. (2025). Survey LLM-based NLG Evaluation: Current Status and Challenges. https://doi.org/10.1162/coli
- Gao, T., Yao, X., & Chen, D. (2022). SimCSE: Simple Contrastive Learning of Sentence Embeddings. http://arxiv.org/abs/2104.08821
- Gao, X., Member, S., Xie, D., Zhang, Y., Wang, Z., Chen, C., He, C., Yin, H., Member, S., & Zhang, W. (2025). A Comprehensive Survey on Imbalanced Data Learning. https://doi.org/10.1007/s11704-025-50274-7
- Gaynor, J. W. (2020). Peer review in the classroom: student perceptions, peer feedback quality and the role of assessment. Assessment and Evaluation in Higher Education, 45(5), 758–775. https://doi.org/10.1080/02602938.2019.1697424
- Ghali, M.-K., Farrag, A., Lam, S., & Won, D. (2025). BEYONDWORDS is All You Need: Agentic Generative AI based Social Media Themes Extractor.
- Gu, J., Chen, J., & Yan, Z. (2026). Fostering feedback literacy by scaffolding selfregulated feedback: a comparative study of GenAI and human peers. Frontiers in Education, 10. https://doi.org/10.3389/feduc.2025.1736446
- Guo, P., Saab, N., Post, L. S., & Admiraal, W. (2020). A review of project-based learning in higher education: Student outcomes and measures. International Journal of Educational Research, 102. https://doi.org/10.1016/j.ijer.2020.101586
- Harris, Z. S. (1954). Distributional Structure. WORD, 10(2–3), 146–162. https://doi.org/10.1080/00437956.1954.11659520
- Hattie, J., & Timperley, H. (2007). The power of feedback. In Review of Educational Research (Vol. 77, Number 1, pp. 81–112). SAGE Publications Inc. https://doi.org/10.3102/003465430298487
- Hertzog, M. A. (2008). Considerations in determining sample size for pilot studies. Research in Nursing and Health, 31(2), 180–191. https://doi.org/10.1002/nur.20247

- Holmes, J., & Wilson, N. (2022). An Introduction to Sociolinguistics. Routledge. www.routledge.com/
- Hyland, F., & Hyland, K. (2001). Sugaring the pill Praise and criticism in written feedback. Journal of Second Language Writing, 10(3), 1815–212.
- Jain, U., Mishra, P., Dash, A., & Pandey, A. (2025). Multi-label multi-class text classification-enhanced attention in transformers with knowledge distillation. In Journal of Applied Research and Technology (Vol. 23, Number 1). www.jart.icat.unam.mx
- Jonsson, A., & Svingby, G. (2007). The use of scoring rubrics: Reliability, validity and educational consequences. In Educational Research Review (Vol. 2, Number 2, pp. 130–144). https://doi.org/10.1016/j.edurev.2007.05.002
- Julious, S. A. (2005). Sample size of 12 per group rule of thumb for a pilot study. Pharmaceutical Statistics, 4(4), 287–291. https://doi.org/10.1002/pst.185
- Jurafsky, Dan., & Martin, J. H. . (2009). Speech and language processing : an introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall.
- Kim, B., Iso, H., Bhutani, N., Hruschka, E., Nakashole, N., & Mitchell, T. (2023). Zero-shot Triplet Extraction by Template Infilling. The Association for Computational Linguistics, 1, 272–284. https://github.com/
- Kollar, I., & Fischer, F. (2010). Peer assessment as collaborative learning: A cognitive perspective. In Learning and Instruction (Vol. 20, Number 4, pp. 344–348). Elsevier BV. https://doi.org/10.1016/j.learninstruc.2009.08.005
- Krajcik, Joseph, B., & Phyllis. (2006). 19. project-based learning. The Cambridge Handbook of the Learning Sciences, 317–333. https://doi.org/https://doi.org/10.1017/CBO9781139519526.018
- Leal, R., Kesäniemi, J., Koho, M., & Hyvönen, E. (2021). Relevance feedback search based on automatic annotation and classification of texts. OpenAccess Series in Informatics, 93. https://doi.org/10.4230/OASIcs.LDK.2021.18
- Levenshtein, V. I. (1966). Binary Codes Capable of Correcting Deletions, Insertions and Reversals. 10.

- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2021). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. http://arxiv.org/abs/2005.11401
- Luan NG, M., Al Ghaithi, A., & Behforouz, B. (2026). Digital Scaffolding as Learning Opportunities: Enhancing Vocabulary Knowledge Through Copilot AI. Educational Process International Journal, 20(1). https://doi.org/10.22521/edupij.2026.20.12
- Lücking, A., Driller, C., Stoeckel, M., Abrami, G., Pachzelt, A., & Mehler, A. (2022). Multiple annotation for biodiversity: developing an annotation framework among biology, linguistics and text technology. Language Resources and Evaluation, 56(3), 807–855. https://doi.org/10.1007/s10579- 021-09553-5
- Manning, C. D., Raghavan, P., & Schütze, H. (2009). An Introduction to Information Retrieval. https://nlp.stanford.edu/IRbook/pdf/irbookonlinereading.pdf
- Manning, C., & Hinrich, S. (1999). Foundations of statistical natural language processing (C. Manning & S. Hinrich, Eds.). MIT Press.
- Mazzullo, E., Bulut, O., Walsh, C., Sitarenios, G., & Macintosh, A. (2025). Fine-Tuning GPT-3.5-Turbo for Automatic Feedback Generation. Proceedings of the ACM Symposium on Applied Computing, 40–47. https://doi.org/10.1145/3672608.3707735
- Mestre, J. P. ., & Ross, B. H. . (2011). The psychology of learning and motivation. 55, Cognition in education. Academic Press.
- Moeliono, A. M. . (2017). Tata bahasa baku bahasa Indonesia. Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan dan Kebudayaan.
- Mohammad, T., Mohammad, T., Nazim, M., Alzubi, A. A. F., & Khan, S. I. (2025). Evaluating The Efficacy of A Large Language Model in Scaffolding Research Report Writing for EFL Learners. International Journal of Basic and Applied Sciences, 14(7), 33–45. https://doi.org/10.14419/g2apsg21

- Mu, H., & Schunn, C. D. (2025). The good, bad, and ugly of comment prompts: Effects on length and helpfulness of peer feedback. International Journal of Educational Technology in Higher Education, 22(1). https://doi.org/10.1186/s41239-025-00502-8
- Muennighoff, N., Tazi, N., Magne, L., Reimers, N., & Ai, C. (2014). MTEB: Massive Text Embedding Benchmark Hugging Face. https://huggingface.co/datasets/mteb/
- Negnevitsky, M. N. (2005). Artificial Intelligence A Guide to Intelligent Systems. Addison Wesley. www.pearsoned.co.uk
- Nelson, M. M., & Schunn, C. D. (2008). The nature of feedback: how different types of peer feedback affect writing performance. Instructional Science 2008 37:4, 37(4), 375–401. https://doi.org/10.1007/s11251-008-9053-x
- Nicol, D., Thomson, A., & Breslin, C. (2014). Rethinking feedback practices in higher education: a peer review perspective. Assessment and Evaluation in Higher Education, 39(1), 102–122. https://doi.org/10.1080/02602938.2013.795518
- Ohland, M. W., Loughry, M. L., Woehr, D. J., Bullard, L. G., Felder, R. M., Finelli, C. J., Layton, R. A., Pomeranz, H. R., & Schmucker, D. G. (2012). The comprehensive assessment of team member effectiveness: Development of a behaviorally anchored rating scale for self- and peer evaluation. Academy of Management Learning and Education, 11(4), 609–630. https://doi.org/10.5465/amle.2010.0177
- Omotehinwa, T. O., Ezekiel, R. A., Onoja, M., Omeye, E. C., & Ibrahim, Y. A. (2025). Comparative Evaluation of Transformer-Based Models for Automated Short-Answer Grading. NIPES - Journal of Science and Technology Research, 7(1 Special Issue), 843–849. https://doi.org/10.37933/nipes/7.4.2025.SI97
- Panadero, E., Jonsson, A., & Botella, J. (2017). Effects of self-assessment on selfregulated learning and self-efficacy: Four meta-analyses. In Educational Research Review (Vol. 22, pp. 74–98). Elsevier Ltd. https://doi.org/10.1016/j.edurev.2017.08.004

- Pea, R. D. (2004). The Social and Technological Dimensions of Scaffolding and Related Theoretical Concepts for Learning, Education, and Human Activity. In The Journal of the Learning Sciences (Vol. 13, Number 3). https://telearn.hal.science/hal-00190619v1
- Perikos, I., Grivokostopoulou, F., & Hatzilygeroudis, I. (2017). Assistance and Feedback Mechanism in an Intelligent Tutoring System for Teaching Conversion of Natural Language into Logic. International Journal of Artificial Intelligence in Education, 27(3), 475–514. https://doi.org/10.1007/s40593- 017-0139-y
- Qasim, R., Bangyal, W. H., Alqarni, M. A., & Ali Almazroi, A. (2022a). A Fine-Tuned BERT-Based Transfer Learning Approach for Text Classification. Journal of Healthcare Engineering, 2022. https://doi.org/10.1155/2022/3498123
- Qasim, R., Bangyal, W. H., Alqarni, M. A., & Ali Almazroi, A. (2022b). A Fine-Tuned BERT-Based Transfer Learning Approach for Text Classification. Journal of Healthcare Engineering, 2022. https://doi.org/10.1155/2022/3498123
- Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (n.d.). Sta n z a : A Python Natural Language Processing Toolkit for Many Human Languages. Retrieved https://spacy.io/
- Qin, P., Xu, W., & Guo, J. (2017). Providing Definitive Learning Direction for Relation Classification System. Journal of Control Science and Engineering, 2017. https://doi.org/10.1155/2017/3924641
- Quirk, R., Greenbaum, S., Leech, G., & Svartvik, J. (1985). Comprehensive of the Language. English, 1–1779. https://books.google.com/books/about/A\_Comprehensive\_Grammar\_of\_the\_ English\_L.html?hl=id&id=jyZaAAAAMAAJ
- Rahimi, Z., Litman, D., Correnti, R., Wang, E., & Matsumura, L. C. (2017). Assessing Students' Use of Evidence and Organization in Response-to-Text Writing: Using Natural Language Processing for Rubric-Based Automated

- Scoring. International Journal of Artificial Intelligence in Education, 27(4), 694–728. https://doi.org/10.1007/s40593-017-0143-2
- Reddy, V., & Veeranjaneyulu, N. (2024). Fine-Tuning Pipeline: A Strategic Approach to Multiclass Text Classification (pp. 946–954). https://doi.org/10.2991/978-94-6463-471-6\_90
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. http://arxiv.org/abs/1908.10084
- Riyanto, S., Sitanggang, I. S., Djatna, T., & Atikah, T. D. (2023). Comparative Analysis using Various Performance Metrics in Imbalanced Data for Multiclass Text Classification. In IJACSA) International Journal of Advanced Computer Science and Applications (Vol. 14, Number 6). http://gcancer.org/pdr
- Romero, C., & Ventura, S. (2020). Educational data mining and learning analytics: An updated survey. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 10(3). https://doi.org/10.1002/widm.1355
- Senel, L. K., Utlu, I., Yucesoy, V., Koc, A., & Cukur, T. (2018). Semantic Structure and Interpretability of Word Embeddings. https://doi.org/10.1109/TASLP.2018.2837384
- Setiawan, I. (2026a). Feedback discourse in Indonesian project-based learning: language use in student self- and peer-assessment. Assessment and Evaluation in Higher Education. https://doi.org/10.1080/02602938.2026.2620645
- Setiawan, I. (2026b). Sentiment-aware NLP in reflective writing: toward fair and adaptive dashboards for Indonesian project-based learning. Interactive Learning Environments. https://doi.org/10.1080/10494820.2026.2624678
- Setiawan, I., Kao, H.-Y., & Chuang, K.-T. (2026). Enhancing Feedback Literacy in Project-Based Science Education: Discourse Analytics and Technology Design. Journal of Science Education and Technology (JOST), Accepted.
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). EXPERIMENTAL AND QUASI-EXPERIMENTAL DESIGNS FOR GENERALIZED CAUSAL INFERENCE .jr-"-* fr HOUGHTON MIFFLIN COMPANY Boston New York.

- Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. Information Processing & Management, 45(4), 427–437. https://doi.org/10.1016/J.IPM.2009.03.002
- Stamper, J., Xiao, R., & Hou, X. (2024). Enhancing LLM-Based Feedback: Insights from Intelligent Tutoring Systems and the Learning Sciences. http://arxiv.org/abs/2405.04645
- Sun, Q., Chen, F., & Yin, S. (2023). The role and features of peer assessment feedback in college English writing. Frontiers in Psychology, 13. https://doi.org/10.3389/fpsyg.2022.1070618
- Tai, J., Ajjawi, R., Boud, D., Dawson, P., & Panadero, E. (2018). Developing evaluative judgement: enabling students to make decisions about the quality of work. Higher Education, 76(3), 467–481. https://doi.org/10.1007/s10734- 017-0220-3
- Thüs, D., Malone, S., & Brünken, R. (2024). Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature. Frontiers in Psychology, 15. https://doi.org/10.3389/fpsyg.2024.1474892
- Torfi, A., Shirvani, R. A., Keneshloo, Y., Tavaf, N., & Fox, E. A. (2021). Natural Language Processing Advancements By Deep Learning: A Survey. http://arxiv.org/abs/2003.01200
- Tsoumakas, G., & Katakis, I. (2009a). Multi-Label Classification: An Overview. http://www.dmoz.org/
- Tsoumakas, G., & Katakis, I. (2009b). Multi-Label Classification: An Overview. http://www.dmoz.org/
- van Popta, E., Kral, M., Camp, G., Martens, R. L., & Simons, P. R. J. (2017). Exploring the value of peer feedback in online learning for the provider. In Educational Research Review (Vol. 20, pp. 24–34). Elsevier Ltd. https://doi.org/10.1016/j.edurev.2016.10.003
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2023). Attention Is All You Need. http://arxiv.org/abs/1706.03762

- Vygotsky, L. S., Cole, M., John-Steiner, V., Scribner, S., & Souberman, E. (1978). Mind in Society The Development of Higher Psychological Processes. Harvard University Press.
- Wan, X., Sun, R., Dai, H., Arik, S. O., & Pfister, T. (2023). Better Zero-Shot Reasoning with Self-Adaptive Prompting. http://arxiv.org/abs/2305.14106
- Wang, L., Yang, N., Huang, X., Yang, L., Majumder, R., & Wei, F. (2024). Improving Text Embeddings with Large Language Models.
- Wang, W., Wei, F., Dong, L., Bao, H., Yang, N., & Zhou, M. (2020). MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers. Advances in Neural Information Processing Systems, 2020-December. https://arxiv.org/pdf/2002.10957
- Weinberger, K. Q., & Saul, L. K. (2009). Distance Metric Learning for Large Margin Nearest Neighbor Classification. In Journal of Machine Learning Research (Vol. 10).
- Wilie, B., Vincentio, K., Winata, G. I., Cahyawijaya, S., Li, X., Lim, Z. Y., Soleman, S., Mahendra, R., Fung, P., Bahar, S., & Purwarianti, A. (2020). IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding. Proceedings of the 1st Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing, AACL-IJCNLP 2020, 843–857. https://doi.org/10.18653/V1/2020.AACL-MAIN.85
- Winstone, N., & Carless, D. (2019). Designing Effective Feedback Processes in Higher Education. Routledge. https://www.routledge.com/
- Wood, D., Bruner, J. S., & Ross, G. (1976). THE ROLE OF TUTORING IN PROBLEM SOLVING. In J. Child Psychol. Psychiat* (Vol. 17). Pergamon Press.
- Yan, Z., & Carless, D. (2022). Self-assessment is about more than self: the enabling role of feedback literacy. Assessment and Evaluation in Higher Education, 47(7), 1116–1128. https://doi.org/10.1080/02602938.2021.2001431

- Yelmen, I., Gunes, A., & Zontul, M. (2023). Multi-Class Document Classification Using Lexical Ontology-Based Deep Learning †. Applied Sciences (Switzerland), 13(10). https://doi.org/10.3390/app13106139
- Yew, E. H. J., Goh, K., Yew, E. H. J., & Goh, K. (2016). Problem-Based Learning: An Overview of its Process and Impact on Learning. Health Professions Education, 2(2), 75–79. https://doi.org/10.1016/j.hpe.2016.01.004
- Zhang, Y., & Schunn, C. D. (2023). Self-regulation of peer feedback quality aspects through different dimensions of experience within prior peer feedback assignments. Contemporary Educational Psychology, 74. https://doi.org/10.1016/j.cedpsych.2023.102210
- Zhang, Y., Schunn, C. D., & Wu, Y. (2024). Interconnecting peer feedback literacy: Exploring the relationship between providing and acting on peer feedback. Studies in Educational Evaluation, 83. https://doi.org/10.1016/j.stueduc.2024.101411
- Zul, M. I., Yasin, S. M., Syarif, D., & Sahid, S. (2024). INTERNATIONAL JOURNAL ON INFORMATICS VISUALIZATION journal homepage : www.joiv.org/index.php/joiv INTERNATIONAL JOURNAL ON INFORMATICS VISUALIZATION An Investigation of the Student Learning Satisfaction Model for User Story Learning in Software Engineering Course. www.joiv.org/index.php/joiv

**LAMPIRAN**

Lampiran 1. Guide Book Anotasi Dataset

BUKU PANDUAN ANOTASI DATASET SELF PEER ASSESSMENT

Oleh:

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

PROGRAM SARJANA TERAPAN
PROGRAM STUDI TEKNIK INFORMATIKA
JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA
POLITEKNIK NEGERI BANDUNG

Lampiran 2. Lamporan TA Self Peer Assessment (SAPA)

PENGEMBANGAN APLIKASI SELF DAN PEER ASSESSMENT DALAM PEMBELAJARAN BERBASIS PROYEK: STUDI KASUS JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG

Development Self and Peer Assessment Application in Project-Based Learning:

A Case Study at the Department of Computer and Informatics Engineering

Politeknik Negeri Bandung

LAPORAN TUGAS AKHIR

Laporan ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Diploma 3 Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

Oleh:

Adhiya Rahma Anzani NIM 221511034

Danendra Gafrila NIM 221511046

Linda Santika NIM 221511052

PROGRAM DIPLOMA 3 PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG

Lampiran 3. Test Result Integrasi Digital Scaffolding pada SAPA

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]