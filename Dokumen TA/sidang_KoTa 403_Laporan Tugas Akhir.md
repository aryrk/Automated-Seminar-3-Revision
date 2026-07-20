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

Bandung, .............................

Pembimbing I,

Pembimbing II,

Irwan Setiawan, S.Si., M.T. NIP. 198004192005011002 Jonner Hutahaean, BSET., M.Info.Sys. NIP. 196210211993031002

Ketua Jurusan Teknik Komputer dan Informatika Koordinator Program Sarjana Terapan Program Studi Teknik Informatika,

Yadhi Aditya Permana, S.T., M.Kom. NIP. 197912242008121001 Santi Sundari, S.Si., M.T. NIP. 197109031999032001

**PEMANFAATAN** *DIGITAL SCAFFOLDING* **BERBASIS RUBRIK UNTUK MENDUKUNG INDIKATOR TEKSTUAL** *FEEDBACK LITERACY* **PADA** *PROJECT-BASED LEARNING*

*RUBRIC BASED DIGITAL SCAFFOLDING UTILIZATION FOR SUPPORTING TEXTUAL INDICATOR OF FEEDBACK LITERACY IN PROJECT-BASED LEARNING*

Tipe TA: Riset (Experiment tools)

Oleh:

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

Tugas Akhir ini telah disidangkan pada tanggal ................................. sesuai dengan ketentuan.

Tim Penguji:

Ketua : Dr. Ani Rahmani, S.Si., M.T. NIP. 196810141993032002 ………………..

Anggota : Yudi Widhiyasana, S.Si., M.T. NIP. 197407182001121002 ……………….. PERNYATAAN PENULIS

Dengan ini menyatakan bahwa laporan Tugas Akhir dengan judul

"PEMANFAATAN DIGITAL SCAFFOLDING BERBASIS RUBRIK

UNTUK MENDUKUNG INDIKATOR TEKSTUAL FEEDBACK

LITERACY PADA PROJECT-BASED LEARNING" adalah karya ilmiah yang

bebas dari unsur tindakan plagiarisme, dan sesuai dengan ketentuan tata tulis yang

berlaku.

Apabila dikemudian hari ditemukan adanya unsur plagiarisme, maka hasil penilaian

Tugas Akhir ini akan dicabut dan bersedia menerima sanksi sesuai dengan

ketentuan yang berlaku.

Demikian pernyataan ini dibuat dengan sesungguhnya dalam keadaan sadar

sepenuhnya.

Bandung, ..........................

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

Feedback literacy atau literasi umpan balik merupakan komponen esensial dalam lingkungan Project-Based Learning (PjBL), di mana mahasiswa dituntut untuk mampu mengartikulasikan evaluasi numerik menjadi narasi kualitatif yang representatif. Namun, mahasiswa sering kali menghadapi kesulitan dalam menyusun narasi yang selaras dengan skor dan memenuhi kriteria rubrik. Penelitian ini merumuskan dan mengalibrasi konfigurasi optimal instrumen digital scaffolding berbasis Natural Language Processing (NLP) yang mengintegrasikan model zeroshot classification dan heuristik rule-based untuk mendeteksi empat indikator tekstual narasi feedback, yaitu: (1) cakupan rubrik, (2) koherensi skor-narasi, (3) kedalaman elaborasi, dan (4) relevansi topik secara real-time. Eksperimen lapangan menggunakan desain posttest-only dengan partisipan mahasiswa yang secara acak dibagi menjadi kelompok treatment dan kontrol. Hasil eksperimen komprehensif (MANOVA) menunjukkan bahwa intervensi scaffolding memberikan dampak yang signifikan secara moderat hingga kuat pada peningkatan indikator kedalaman elaborasi (F(1,54) = 4,76, p < 0,05, rank-biserial correlation=0,49). Meskipun indikator lainnya belum menunjukkan perbedaan statistik yang signifikan, observasi kualitatif mengungkap bahwa scaffolding memiliki indikasi dalam mendisrupsi bias leniensi penilaian dan mendorong mahasiswa untuk memperbaiki kualitas narasinya sebelum disubmit. Penelitian ini berkontribusi pada pengembangan instrumen pendidikan yang memadukan kalibrasi komputasional dengan intervensi pedagogis untuk memfasilitasi pengembangan feedback literacy secara formatif, dengan catatan bahwa performa generalisasi komputasional pada instrumen ini masih memerlukan pengujian independen lanjutan.

Kata Kunci: Digital Scaffolding, Feedback Literacy, Natural Language Processing, Project-Based Learning, Validasi Instrumen.

**ABSTRACT**

Feedback literacy is an essential component in a Project-Based Learning (PjBL) environment, where students must be able to articulate numerical evaluations into in-depth qualitative narratives. However, students often struggle to compose narratives that align with scores and meet rubric criteria. This study formulates and calibrates the optimal configuration of an NLP-based digital scaffolding instrument that integrates a zero-shot classification model and rule-based heuristics to detect four textual indicators of feedback narratives: rubric coverage, score-narrative coherence, elaboration depth, and topic relevance in real-time. A field experiment using a posttest-only design with student participants (n=56)divided into treatment and control groups was conducted. The experimental results (MANOVA) showed that the scaffolding intervention had a moderate to strong significant effect on the elaboration depth indicator (F(1,54) = 4,76, p < 0,05,rank-biserial correlation=0.49). Although other indicators have not shown statistically significant differences, qualitative observations revealed that scaffolding effectively disrupts grading leniency bias and prompts students to reconsider incomplete narratives prior to submission. This research contributes to the development of educational instruments that bridge computational calibration with pedagogical intervention to support the formative development of feedback literacy, noting that the computational generalization performance of this instrument requires further independent testing.

Keywords: Digital Scaffolding, Feedback Literacy, Instrument Validation, Natural Language Processing, Project-Based Learning.

**KATA PENGANTAR**

Puji dan syukur penulis panjatkan ke hadirat Allah SWT, karena atas rahmat dan karunia-Nya, penulis dapat menyelesaikan penyusunan Laporan Tugas Akhir yang berjudul "Pemanfaatan Digital Scaffolding Berbasis Rubrik untuk Mendukung Indikator Tekstual Feedback Literacy pada Project-Based Learning". Laporan ini disusun sebagai salah satu syarat kelulusan program Diploma IV (Sarjana Terapan) pada Program Studi Teknik Informatika, Jurusan Teknik Komputer dan Informatika, Politeknik Negeri Bandung.

Penulis menyadari bahwa penyusunan Tugas Akhir ini tidak akan berjalan lancar tanpa bimbingan, arahan, dan dukungan dari berbagai pihak. Oleh karena itu, penulis ingin menyampaikan ucapan terima kasih yang sebesar-besarnya kepada:

1. Bapak Yadhi Aditia Permana, S.ST., M.Kom., selaku Ketua Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung.
2. Ibu Santi Sundari, S.Si., M.T., selaku Koordinator Program Studi Sarjana Terapan Teknik Informatika Politeknik Negeri Bandung.
3. Bapak Irwan Setiawan, S.Si., M.T., selaku Dosen Pembimbing I, yang telah memberikan bimbingan, arahan, kritik, dan masukan selama proses pelaksanaan penelitian dan penyusunan laporan Tugas Akhir.
4. Bapak Jonner Hutahaean, BSET., M.Info.Sys., selaku Dosen Pembimbing II, yang telah memberikan bimbingan, arahan, kritik, dan masukan selama proses pelaksanaan penelitian dan penyusunan laporan Tugas Akhir.
5. Ibu Dr. Ani Rahmani, S.Si., M.T. dan Bapak Yudi Widhiyasana, S.Si., M.T., selaku Dosen Penguji, yang telah memberikan kritik, saran, serta masukan yang membangun untuk penyempurnaan penelitian ini.
6. Koordinator Tugas Akhir beserta seluruh dosen Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung yang telah memberikan ilmu, pengalaman, dan bimbingan selama masa perkuliahan.

7. Seluruh responden yang telah berpartisipasi dalam proses penelitian melalui pengisian kuesioner dan uji coba, sehingga memberikan masukan yang menjadi dasar pelaksanaan penelitian ini.

8. Orang tua dan keluarga yang senantiasa memberikan doa, dukungan, perhatian, serta semangat kepada penulis selama menempuh pendidikan.

9. Rekan satu tim Tugas Akhir serta seluruh teman-teman Program Studi Sarjana Terapan Teknik Informatika yang telah memberikan bantuan, motivasi, dan kerja sama selama proses penyelesaian penelitian.

10. Seluruh pihak yang tidak dapat disebutkan satu per satu yang telah memberikan bantuan secara langsung maupun tidak langsung dalam penyelesaian Tugas Akhir ini.

Penulis menyadari bahwa laporan ini masih memiliki ruang untuk penyempurnaan. Oleh karena itu, penulis sangat terbuka terhadap kritik dan saran yang konstruktif. Semoga penelitian ini dapat memberikan kontribusi yang bermanfaat bagi pengembangan keilmuan, khususnya di bidang pendidikan dan teknologi informasi.

Bandung, Juli 2026

Penulis

**DAFTAR ISI**

ABSTRAK: i
ABSTRACT: ii
KATA PENGANTAR: iii
DAFTAR ISI: V
DAFTAR GAMBAR: ix
DAFTAR TABEL: xii
DAFTAR RUMUS: XV
DAFTAR ISTILAH: xvii
DAFTAR SINGKATAN: xx
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
II.1.2 Self Assessment ... 13
II.1.3 Peer Assessment ... 14

II.1.4 Feedback ... 15
II.1.5 Rubrik ... 16
II.1.6 Natural Language Processing (NLP) dan Arsitektur Transformer ... 17
II.1.7 Rule Based ... 18
II.1.8 Feedback Literacy ... 19
II.1.9 Zone of Proximal Development ... 24
II.1.10 Scaffolding ... 26
II.1.11 Digital Scaffolding ... 28
II.2 Karya Ilmiah Sejenis ... 30
BAB III METODOLOGI PENELITIAN ... 34
III.1 Penjelasan Penelitian ... 34
III.2 Variabel Penelitian ... 38
III.2.1 Variabel pada Tahap Kalibrasi ... 38
III.2.2 Variabel pada Tahap Eksperimen ... 38
III.3 Data Penelitian ... 39
III.3.1 Data Pengembangan dan Kalibrasi Pipeline Scaffolding ... 40
III.3.2 Data Evaluasi Scaffolding ... 42
III.4 Objek Penelitian ... 43
III.4.1 Objek Material ... 44
III.4.2 Objek Fungsional ... 45
III.5 Perangkat Pendukung ... 45
III.6 Tahapan Pelaksanaan Penelitian ... 46
III.6.1 Identifikasi Masalah dan Studi Pendahuluan ... 48
III.6.2 Studi Literatur dan Pendefinisian Objektif Solusi ... 49
III 6.3 Pemodelan Konfigurasi Pineline ... 50

III.6.4 Formulasi Pendekatan Scaffolding 88
III.6.5 Pembuatan APE 103
III.6.6 Perancangan Skenario Eksperimen RQ 2 106
III.6.7 Penarikan Kesimpulan dan Perumusan Saran 125
BAB IV HASIL PENGEMBANGAN APE 126
IV.1 Analisis Problem Domain dan kebutuhan Eksperimen 126
IV.1.1 Karakteristik Data Narasi Feedback 126
IV.1.2 Hasil Kuantifikasi Masalah 134
IV.1.3 Kebutuhan Eksperimen dan Objektif Solusi 140
IV.2 Hasil Anotasi Dataset 141
IV.2.1 Hasil Dekomposisi Rubrik 141
IV.2.2 Sampel Hasil Anotasi 142
IV.2.3 Validasi Hasil Anotasi 150
IV.3 Hasil Pemodelan dan Kalibrasi Pipeline Digital Scaffolding 151
IV.3.1 Spesifikasi Final Pipeline Digital Scaffolding 151
IV.3.2 Hasil Evaluasi dan Kalibrasi Model 153
IV.4 Hasil Validasi Fungsionalitas Instrumen 163
IV.5 Hasil Perancangan Skenario Eksperimen RQ 2 166
IV.5.1 Pemetaan Subjek Eksperimen 166
IV.5.2 Kuesioner yang Digunakan 166
IV.5.3 Rubrik Eksperimen 167
BAB V HASIL DAN PEMBAHASAN EKSPERIMEN 168
V.1 Ringkasan Metodologi Eksperimen 168
V.2 Hasil Eksperimen 169
V.2.1 Hasil Evaluasi Deteksi Pipeline (RQ 1) 170

V.2.2 Statistik Deskriptif dan Verifikasi Asumsi (RQ 2) 173
V.2.3 Hasil Pengujian Multivariat dan Univariat (RQ 2) 176
V.2.4 Hasil Pengolahan Data Interaksi Scaffolding (RQ 2) 177
V.2.5 Hasil Kuesioner Evaluasi Subjek Eksperimen 182
V.3 Pembahasan Hasil Eksperimen 185
V.3.1 Pembahasan Kemampuan Deteksi Pipeline (Menjawab RQ 1) 186
V.3.2 Dampak Intervensi terhadap Pemenuhan Indikator (RQ 2) 204
V.3.3 Interpretasi Berdasarkan Kerangka Digital Scaffolding 215
V.4 Keterbatasan Penelitian 218
V.4.1 Keterbatasan Generalisasi Konteks Penelitian 218
V.4.2 Keterbatasan Desain Eksperimen yang Dipilih 219
V.4.3 Keterbatasan Bentuk Digital Scaffolding 220
V.4.4 Keterbatasan Dataset 221
V.4.5 Keterbatasan Transferabilitas Threshold pada Rubrik Eksperimen 222
BAB VI ANALISIS DAMPAK HASIL PENELITIAN 223
VI.1 Outcome yang Diharapkan dari Pengguna/Mitra 223
VI.2 Dampak Pedagogis Hasil Penelitian bagi Mitra 224
BAB VII PENUTUP 226
VII.1 Kesimpulan 226
VII.2 Saran 228
VII.3 Rencana Keberlanjutan dan Komersialisasi Hasil Penelitian 228
DAFTAR PUSTAKA 230
LAMPIRAN 241

**DAFTAR GAMBAR**

Gambar II.1 Siklus PjBL dalam Konteks Penelitian 13
Gambar II.2 Alur Self-Assessment 14
Gambar II.3. Alur Peer-Assessment 15
Gambar II.4. Contoh Cakupan Rubrik Tidak Terpenuhi 20
Gambar II.5. Contoh Koherensi Evaluatif Tidak Terpenuhi 21
Gambar II.6. Contoh Elaborasi Narasi Feedback 22
Gambar II.7. Contoh Relevansi Tidak Terpenuhi 23
Gambar II.8 Ilustrasi kerangka ZPD 25
Gambar III.1. Korelasi Rubrik, Pertanyaan, dan Feedback 36
Gambar III.2. Pemetaan Scaffolding pada Kelompok Eksperimen 43
Gambar III.3. Pemetaan Unit Analisis, Objek Material, dan Vektor Indikator 44
Gambar III.4. Tahapan Pelaksanaan Penelitian 47
Gambar III.5. Peta Sintesis Studi Literatur 49
Gambar III.6. Pemetaan Feedback kepada Indikator Komputasi 51
Gambar III.7. Alur Komputasi Indikator dan Keputusan Intervensi 52
Gambar III.8. Pemetaan Dataset untuk Evaluasi 54
Gambar III.9. Pemetaan Dekomposisi Rubrik pada Anotasi Dataset 56
Gambar III.10. Alur Dekomposisi Koherensi Feature-set 59
Gambar III.11. Alur Anotasi Dataset Cakupan Rubrik 60
Gambar III.12. Alur Anotasi Dataset Relevansi Topik 61
Gambar III.13. Alur Anotasi Dataset Koherensi Skor dan Narasi 62
Gambar III.14. Alur Anotasi Dataset oleh Annotator 63
Gambar III.15. Alur Validasi Dataset 63
Gambar III.16. Flowchart Komputasi Indikator Cakupan Rubrik 68
Gambar III.17. Contoh Komputasi Indikator Relevansi Topik 72
Gambar III.18. Pemetaan Eksperimen dan Kalibrasi Model 79
Gambar III.19 Mekanisme Semantic Chunking menggunakan Sentencizer 83
Gambar III.20 Alur Pengelompokan Mutual Exclusive 86
Gambar III.21. Contoh Komputasi Indikator Koherensi Skor dan Narasi 88

Gambar III.22. Flowchart Alur Eksekusi Scaffolding 90
Gambar III.23. Matriks Strategi Scaffolding dan Prompt 95
Gambar III.24 Ilustrasi Variabel Missing_Coverage 99
Gambar III.25 Ilustrasi Transformasi Missing Coverage 100
Gambar III.26 Ilustrasi Pengambilan Variabel Kontekstual untuk Skor 100
Gambar III.27 Rancangan Eksperimen 107
Gambar III.28. Flowchart Keputusan Uji Statistik Per Indikator 118
Gambar IV.1 Perbandingan Rata-Rata Jumlah Kata antar Self dan Peer 135
Gambar IV.2 Sebaran Jumlah Kata antar Peer dan Self Assessment 136
Gambar IV.3 Perbandingan Pola Assessment antar Skor dan Panjang Narasi 137
Gambar IV.4 Pola Periode Pengisian antar Skor dan Panjang Narasi 138
Gambar IV.5 Distribusi Skor Antara Self dan Peer Assessment 139
Gambar IV.6. Distribusi label TRUE dan FALSE pada Dataset 143
Gambar IV.7. Distribusi Tiga Indikator Pada Sampel Anotasi 144
Gambar IV.8. Histogram Jumlah Kata Pada Dataset Anotasi 145
Gambar IV.9 Distribusi Empat Indikator Tekstual Narasi Feedback 146
Gambar IV.10 Hubungan Antar Indikator 147
Gambar IV.11 Pola Overlap Indikator Tidak Terpenuhi 148
Gambar IV.12 Pemenuhan Indikator Cakupan Rubrik berdasarkan Panjang 149
Gambar IV.13 Desain Pipeline yang Dibangun 152
Gambar IV.14. Mekanisme Kalibrasi Model 154
Gambar V.1. Grafik Indikator Cakupan Rubrik Semantic Chunking 170
Gambar V.2. Grafik Performa Koherensi Skor dengan Semantic Chunking 171
Gambar V.3. Grafik Performa Relevansi Topik dengan Whole-text-embedding 173
Gambar V.4. Frekuensi Kebutuhan Bantuan yang Terdeteksi 177
Gambar V.5. Tingkat Resolusi Keempat Indikator 178
Gambar V.6. Tingkat Persistensi Antar Indikator 178
Gambar V.7. Pola Revisi Perubahan 179
Gambar V.8 Dinamika Pemenuhan Indikator Saat Sesi Eksperimen 180
Gambar V.9 Perbandingan Pemenuhan Indikator Terpenuhi 181
Gambar V.10. Rata-rata Skor Evaluasi Penerimaan (TAM) 183

Gambar V.11. Rata-rata Skor Evaluasi Beban Kognitif 183
Gambar V.12. Komponen Scaffolding yang Dinilai Paling Membantu 184
Gambar V.13. Komponen Scaffolding yang Dinilai Membutuhkan Perbaikan . 185
Gambar V.14. Kerangka untuk Menjawab RQ 1 186
Gambar V.15. Distribusi FP dan FN pada Rubrik 187
Gambar V.16. Sebaran FP dan FN berdasarkan Label Anotasi 192
Gambar V.17. Kerangka untuk Menjawab RQ 2 205

**DAFTAR TABEL**

Tabel I.1. Batasan Penelitian 8
Tabel III.1. Pemetaan Tahapan Metodologi dengan RQ 35
Tabel III.2. Notasi Matematis yang Digunakan 37
Tabel III.3. Operasionalisasi Kualitas Narasi Feedback 39
Tabel III.4. Perangkat Pendukung 45
Tabel III.5. Simulasi Alur Data dan Keputusan Intervensi Sistem 53
Tabel III.6 Contoh Proses Dekomposisi Cakupan dan Relevansi Topik 58
Tabel III.7. Contoh Proses Dekomposisi untuk Koherensi Skor dan Narasi 59
Tabel III.8. Skenario Evaluasi Part-of-Speech Taging 65
Tabel III.9. Contoh Perhitungan Indikator Cakupan Rubrik 67
Tabel III.10. Contoh Komputasi Indikator Elaborasi 70
Tabel III.11. Kandidat Model Sentence Embedding 73
Tabel III.12. Instruksi Model Untuk Indikator 75
Tabel III.13. Pemilihan Pendekatan Komputasional 76
Tabel III.14. Rancangan Matriks Evaluasi Model 80
Tabel III.15. Format Pelaporan Hasil Evaluasi 80
Tabel III.16. Format Pelaporan Hasil Evaluasi Mutual Exclusivity 81
Tabel III.17. Contoh Himpunan Koherensi Feature Set 85
Tabel III.18 Analisis Pendekatan Generasi Teks Scaffolding 93
Tabel III.19 Elemen Penyusun Template Teks Scaffolding 97
Tabel III.20. Variabel Kontekstual yang digunakan Template 98
Tabel III.21. Sampel Template Prompt Scaffolding 101
Tabel III.22 Ilustrasi Adaptivitas Output pada Kondisi  yang Identik 102
Tabel III.23. Ringkasan Kelompok Skenario Pengujian 105
Tabel III.24. Contoh Implementasi BARS pada Rubrik CATME 111
Tabel III.25 Format Tabel Pelaporan Verifikasi Asumsi 116
Tabel III.26. Format Pelaporan Uji Manova (Pillai's Trace) 117
Tabel III.27 Tabel Interpretasi Keputusan Uji Asumsi 119
Tabel III.28 Interpretasi Uji Follow Up Per Indikator 120

Tabel III.29 Interpretasi Effect Size 120
Tabel III.30. Format Pelaporan Uji Univariat dan Effect Size 120
Tabel III.31 Karakteristik Perubahan pada Narasi Feedback 122
Tabel III.32. Klasifikasi Pola Revisi 122
Tabel IV.1. Kasus narasi bersifat generik 127
Tabel IV.2. Kasus Cakupan Parsial 128
Tabel IV.3. Kasus Skor Tidak Koheren dengan Narasi yang ditulis 129
Tabel IV.4. Kasus Inkoherensi Skor secara Parsial 130
Tabel IV.5. Kasus Feedback dengan Elaborasi Singkat 131
Tabel IV.6. Kasus Narasi Tidak Relevan dengan Aspek Rubrik Pertanyaan 132
Tabel IV.7. Kasus Narasi Feedback Tidak Relevan Sebagian 133
Tabel IV.8. Detail Data Historis Assessment sebelum Dikomputasi 134
Tabel IV.9. Performa Model 1 Semantic Chunking terhadap Baseline 155
Tabel IV.10. Performa Model 2 Semantic Chunking terhadap Baseline 156
Tabel IV.11. Performa Model 4 Semantic Chunking terhadap Baseline 157
Tabel IV.12. Performa Model 2 Mutual Exclusivity terhadap Baseline 158
Tabel IV.13. Performa Akhir Model untuk Setiap Indikator 160
Tabel IV.14 Analisis Implikasi Performa Hasil Evaluasi dan Eksperimen 162
Tabel V.1 Rincian Keseluruhan Kemampuan Pipeline 170
Tabel V.2. Sebaran Performa Indikator Cakupan Rubrik 171
Tabel V.3. Sebaran Performa Indikator Koherensi Skor dan Narasi 172
Tabel V.4. Sebaran Nilai FN, FP, TN, TP untuk Indikator Relevansi Topik 173
Tabel V.5. Deskripsi Data Terkumpul dari Eksperimen yang Dilakukan 174
Tabel V.6. Statistik Deskriptif Self Assessment 174
Tabel V.7. Statistik Deskriptif Peer Assessent 175
Tabel V.8. Hasil Uji Asumsi 175
Tabel V.9. Hasil Pengujian Multivariat 176
Tabel V.10. Hasil Pengujian Univariat untuk Self Assessment 176
Tabel V.11. Hasil Pengujian Univariat untuk Peer Assessment 176
Tabel V.12. Jumlah Responden Kuesioner 182
Tabel V.13. Sampel data False Positive 188

Tabel V.14. Sampel Data False Negative 189
Tabel V.15. Sampel Data FP pada Koherensi Skor dan Narasi 192
Tabel V.16. Sampel Data FN pada Koherensi Skor dan Narasi 193
Tabel V.17. Sampel Data FP pada Relevansi Topik 196
Tabel V.18. Sampel Data FN pada Relevansi Topik 197

**DAFTAR RUMUS**

Cochran Formula 41
Kondisi Penyelarasan Multi-Dimensi 51
Kondisi Deteksi Per Indikator 52
Pemicu Intervensi Rule-Based 52
Aspek Rubrik 56
Representasi Hubungan Aspek dengan Kriteria 56
Representasi Hubungan Kriteria dengan Deskripsi Penilaian Spesifik 57
Pemetaan Feature Set Indikator Komputasi 57
Feature Set Cakupan dan Relevansi 57
Hasil awal Dekomposi 58
Himpunan Unit Dekomposisi Feature Set Koherensi Skor dan Narasi 59
Himpunan Kandidat Predikat 65
Himpunan Kandidat Subjek 65
Valisasi Part-of-Speech Tagging 65
Persamaan Cakupan Rubrik 66
Formula Cakupan Rubrik 67
Contoh Perhitungan Indikator Cakupan rubrik 67
Himpunan Prediksi Skor Global 69
Verifikasi skor aktual 69
Kondisi Intervensi Kedalaman Elaborasi 70
Himpunan Seluruh Kriteria Penilaian dalam Rubrik 71
Himpunan Unit Dekomposisi Kriteria yang Tidak Menjadi Fokus 71
Nilai Relevansi 71
Fungsi Segmentasi 83
Operator maksimum (Split-Max) 83
Himpunan Koherensi Feature Set 84
Notasi Constraint Mutual Exclusive 85
Elemen Himpunan yang Berkorespondensi dengan Tingkat Skor 85
Notasi Constraint Anggota Himpunan 86

Himpunan Kandidat Skor ... 87
Prediksi Skor Tertinggi Dalam Group ... 87
Himpunan Prediksi Skor ... 87
Fungsi Pengukur Koherensi ... 87
Notasi Rule based ... 91
Notasi Scaffolding sebagai Template Instantiation ... 95
Tingkat Signifikansi yang Disesuaikan ... 119
Implementation Rate ... 121
Persistence Rate ... 122

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

Natural Language Understanding (NLU)

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

POS-Tagging : Proses otomatis untuk memberikan label atau

kategori tata bahasa (seperti kata benda, kata kerja, kata sifat, atau kata sambung) pada setiap kata di

dalam sebuah kalimat.

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

bantuan atau peringatan tekstual kepada mahasiswa penilai (assessor) yang terdeteksi menghasilkan feedback berkualitas rendah, bertujuan untuk memandu mahasiswa untuk memperbaiki narasi feedback.

**DAFTAR SINGKATAN**

AI : Artificial Intelligence

BERT : Bidirectional Encoder Representation from

Transformer

E5 : Embeddings from Bidirectional Encoder

Representations.

LLM : Large Language Models

MANOVA : Multivariate Analysis of Variance. NLP : Natural Language Processing

PjBL : Project Based Learning

POS : Part of Speech

SBERT : Sentence-Bidirectional Encoder Representation

from Transformer

ZPD : Zone of Proximal Development

**BAB I**

**PENDAHULUAN**

Bab ini memuat gambaran umum penelitian yang mencakup latar belakang, perumusan masalah, research question, tujuan penelitian, pemangku kepentingan dan manfaat penelitian, dukungan data, ruang lingkup dan batasan, serta sistematika penulisan tugas akhir.

**I.1 Latar Belakang**

Pembelajaran Berbasis Proyek (PjBL) dirancang dengan tujuan yang lebih dalam dari sekadar menghasilkan produk akhir. Pendekatan ini menempatkan proses kolaborasi sebagai inti pembelajaran, di mana mahasiswa membangun tidak hanya kompetensi teknis tetapi juga kapasitas interpersonal seperti kemampuan bekerja dalam tim, mengambil tanggung jawab, dan mengevaluasi kontribusi diri sendiri maupun rekan sejawat (Guo et al., 2020; Krajcik et al., 2006). Namun, proses kolaborasi tersebut tidak selalu dapat diamati secara langsung oleh dosen karena sebagian besar interaksi terjadi di luar sesi pembelajaran formal. Sebaliknya, anggota kelompok yang terlibat dalam proyek memiliki kesempatan yang lebih besar untuk mengamati bagaimana setiap anggota berkontribusi terhadap penyelesaian tugas (Cheng et al., 2008; Dunning et al., 2004).

Salah satu mekanisme yang umum digunakan untuk memperoleh informasi tersebut adalah melalui self assessment dan peer assessment. Dalam konteks PjBL kedua instrumen tersebut berfungsi sebagai penilaian berbasis rubrik yang umumnya terdiri atas dua komponen yaitu komponen skor numerik dan komentar atau narasi kualitatif (Bell, 2010; Winstone & Carless, 2019). Selain menghasilkan nilai, kedua komponen juga memberikan kesempatan bagi pengajar untuk memperoleh gambaran mengenai dinamika kerja kelompok yang tidak selalu tercermin pada produk akhir, seperti bagaimana mahasiswa merefleksikan kinerja diri sendiri, menilai kontribusi rekan, serta menerapkan standar penilaian yang terdapat pada rubrik (Nicol et al., 2014).

Di antara kedua komponen tersebut, komentar atau narasi kualitatif memiliki peran yang sangat krusial, karena narasi inilah yang secara esensial mentransformasikan sebuah skor angka menjadi feedback yang sesungguhnya (Winstone & Carless, 2019). Tanpa adanya narasi yang mendeskripsikan justifikasi penilaian, sebuah skor numerik hanyalah sebuah vonis yang justru menghentikan tindakan belajar mahasiswa karena tidak memberikan informasi apa pun mengenai langkah perbaikan selanjutnya (Hyland & Hyland, 2001; Mu & Schunn, 2025; Zhang et al., 2024). Oleh karena itu, narasi yang telah berfungsi sebagai feedback ini berperan sebagai sarana refleksi, akuntabilitas, dan dialog pembelajaran antar mahasiswa selama pelaksanaan proyek (Gaynor, 2020; Guo et al., 2020; van Popta et al., 2017).

Fungsi tersebut menjadi berkurang ketika narasi feedback yang ditulis mahasiswa bersifat terlalu umum, terlalu singkat, atau tidak menjelaskan alasan di balik skor yang diberikan (Carless & Boud, 2018). Narasi feedback seperti "pekerjaan dilakukan dengan sangat baik" tidak memberikan informasi yang cukup bagi penerima feedback maupun dosen untuk memahami aspek apa yang sebenarnya dinilai (Aimah & Suhartoyo, 2024; Hattie & Timperley, 2007; Setiawan, 2026a). Akibatnya, kualitas narasi feedback tidak lagi ditentukan hanya oleh skor yang diberikan, tetapi juga oleh bagaimana penilaian tersebut diartikulasikan ke dalam bentuk narasi yang informatif, relevan, dan selaras dengan kriteria penilaian (Brookhart, 2013; Nicol et al., 2014; Winstone & Carless, 2019).

Fenomena tersebut bukan merupakan kasus yang bersifat individual. Penelitian Setiawan (2026a) terhadap 93 mahasiswa Program Studi Teknik Informatika Politeknik Negeri Bandung menunjukkan bahwa hanya 18,4% narasi feedback yang selaras dengan evaluasi numerik yang diberikan. Tingkat keselarasan pada peer assessment bahkan hanya mencapai 13,2%, lebih rendah dibandingkan self assessment sebesar 23,7%.

Temuan tersebut konsisten dengan hasil analisis Setiawan et al. (2026) terhadap 9.180 data self dan peer assessment berbahasa Indonesia, yang mengidentifikasi empat pola tekstual yang secara sistematis membatasi kualitas narasi feedback. Pertama, komentar mahasiswa cenderung singkat dan deskriptif, dengan persentil ke-10 panjang komentar hanya berkisar 2-5 kata pada peer assessment, sehingga membatasi ruang elaborasi. Kedua, sebagian besar komentar tidak memuat referensi eksplisit terhadap kriteria rubrik, terutama pada dimensi yang bersifat kolaboratif seperti kerja sama dan komunikasi. Ketiga, ditemukan kesenjangan kalibrasi yang sistematis antara skor yang diberikan mahasiswa dan skor yang idealnya merepresentasikan performa sesungguhnya, mengindikasikan bahwa keselarasan antara penilaian kuantitatif dan kualitatif tidak selalu terjaga. Keempat, keterbatasan tersebut bervariasi antar dimensi rubrik, menunjukkan bahwa kelengkapan pembahasan kriteria tidak seragam di seluruh aspek penilaian. Keempat pola tekstual inilah yang menjadi dasar konseptual bagi empat indikator tekstual yang dioperasionalkan pada penelitian ini, yaitu cakupan rubrik, koherensi skor-narasi, kedalaman elaborasi, dan relevansi topik.

Kesenjangan antara kemampuan melakukan evaluasi dan kemampuan mengartikulasikannya menempatkan penulisan narasi di dalam Zone of Proximal Development (ZPD) yang mendefinisikan rentang tugas yang belum dapat diselesaikan secara mandiri, tetapi dapat dicapai dengan bantuan (Vygotsky et al., 1978). Hal ini didukung oleh Zhang & Schunn (2023) yang mengakui bahwa konstruksi narasi feedback berada di area ini dan perlu diberikan bantuan. Dalam konteks tersebut, bantuan yang paling efektif bersifat contingent, yaitu hanya diberikan ketika dibutuhkan dan dihentikan ketika mahasiswa telah mampu melanjutkan tugasnya secara mandiri (Pea, 2004).

Setiawan (2026a) mengidentifikasi potensi pemanfaatan sistem berbasis Natural Language Processing (NLP) untuk menghasilkan prompt berbasis rubrik sebagai bentuk digital scaffolding. Temuan tersebut membuka peluang pengembangan sistem yang mampu memberikan bantuan secara otomatis berdasarkan hasil analisis terhadap kualitas narasi feedback mahasiswa. Namun, implementasi digital scaffolding yang memanfaatkan potensi tersebut masih menghadapi sejumlah

tantangan. Sebagai contoh, (Ding et al., 2025) menyoroti kemampuan scaffolding  dalam konteks pendidikan. Namun, sistem yang dibangun hanya menganalisis makna teks setelah feedback dituliskan. Selain itu scaffolding berbasis teknologi Generative AI mampu menghasilkan teks bervariasi meski bersifat probabilistik yang tidak memberikan jaminan konsistensi atau transparansi yang diperlukan dalam konteks intervensi pedagogis yang terstruktur (Luan NG et al., 2026). Sementara Mohammad et al. (2025) menerapkan scaffolding dalam bentuk humanin-the-loop berbasis LLM GPT-4 dengan prompt checklist terstruktur dalam konteks penulisan laporan akademik bagi mahasiswa EFL, namun masih menghadapi kelemahan dimana LLM yang berbasis prediksi statistik tersebut berisiko menghasilkan analisis yang bersifat tidak deterministik.

Kondisi tersebut menunjukkan bahwa masih diperlukan pendekatan digital scaffolding yang mampu memanfaatkan hasil analisis terhadap narasi feedback untuk memberikan intervensi berbasis rubrik secara adaptif, konsisten, dan sesuai dengan kebutuhan mahasiswa selama proses penulisan berlangsung.

Berdasarkan kesenjangan tersebut, penelitian ini bertujuan mengembangkan dan mengevaluasi pendekatan digital scaffolding berbasis rubrik untuk mendukung penulisan jawaban narasi feedback pada self assessment dan peer assessment mahasiswa. Pendekatan yang diusulkan dirancang untuk mengidentifikasi kebutuhan bantuan selama proses penulisan berlangsung dan memberikan intervensi yang sesuai berdasarkan kondisi narasi feedback yang dihasilkan mahasiswa. Selanjutnya, penelitian ini mengevaluasi kemampuan pendekatan tersebut dalam mendukung kualitas feedback mahasiswa melalui serangkaian evaluasi eksperimental terhadap digital scaffolding yang dikembangkan.

**I.2 Rumusan Masalah**

Penelitian ini dilatarbelakangi oleh tiga kesenjangan dalam pelaksanaan self dan peer assessment berbasis rubrik pada lingkungan PjBL, yaitu gap pedagogis, komputasional, hingga intervensi.

Pertama, pada gap pedagogis, mahasiswa belum selalu mampu mengartikulasikan evaluasi ke dalam narasi feedback yang informatif. Berdasarkan temuan empiris Setiawan (2026a), hanya 18,4% narasi yang selaras dengan skor kuantitatif. Gejala lain yang sering muncul meliputi narasi yang terlalu singkat, cakupan kriteria rubrik yang rendah, dan penyimpangan topik evaluasi.

Kedua, pada gap komputasional, pendekatan sistem berbasis NLP pada penelitian sebelumnya beroperasi secara sumatif, di mana analisis narasi feedback dilakukan setelah proses penulisan selesai (Omotehinwa et al., 2025; Rahimi et al., 2017). Sistem belum memiliki kapabilitas real-time untuk memproses teks saat diketik.

Ketiga, pada gap intervensi, sistem evaluasi yang ada saat ini umumnya berhenti pada tahap analisis atau klasifikasi tekstual narasi feedback, namun belum selalu diikuti dengan mekanisme scaffolding berbasis rubrik. Akibatnya, mahasiswa tidak memperoleh prompt atau panduan terstruktur untuk memperbaiki narasi mereka pada saat proses penulisan sedang berlangsung.

Berdasarkan ketiga kesenjangan tersebut, masih terdapat ruang penelitian untuk mengembangkan dan mengevaluasi digital scaffolding yang mampu mendeteksi gejala tekstual feedback secara real-time serta memberikan intervensi selama proses penulisan berlangsung.

**I.3 Research Question**

- RQ 1: Sejauh mana pipeline digital scaffolding yang dirancang, melalui proses kalibrasi model embedding dan aturan heuristik berbasis rubrik, dapat mencapai kesesuaian dengan ground truth berdasarkan penilaian manusia dalam mendeteksi keempat indikator tekstual narasi feedback?
- RQ 2: Sejauh mana intervensi digital scaffolding berbasis rubrik memengaruhi pemenuhan keempat indikator tekstual narasi feedback pada mahasiswa dalam lingkungan eksperimen nyata, ditinjau dari perbedaan tingkat pemenuhan empat indikator tekstual antara kelompok treatment dan kontrol serta pola interaksi mahasiswa dengan scaffolding selama proses penyusunan narasi feedback?

**I.4 Tujuan Penelitian**

Sejalan dengan rumusan masalah dan pertanyaan penelitian yang telah ditetapkan, tujuan utama dari penelitian ini dibagi menjadi dua sasaran komputasional dan eksperimental, yaitu:

1. Membangun dan mengalibrasi konfigurasi optimal pipeline digital scaffolding  yang mengintegrasikan Natural Language Processing (NLP) sebagai instrumen riset. Arsitektur ini ditujukan untuk mendeteksi keempat indikator tekstual yaitu cakupan rubrik, koherensi skor-narasi, kedalaman elaborasi, dan relevansi topik secara real-time selama penulisan aktif narasi self dan peer assessment berdasarkan dataset historis yang tersedia.
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

Untuk menjaga fokus dan arah penelitian, [Tabel I.1](#page-4-0) menyajikan kelompok ruang lingkup dan batasan penelitian ke dalam lima kategori utama.

Tabel I.1. Batasan Penelitian

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**I.8 Sistematika Penulisan**

Sistematika dalam penulisan Tugas Akhir ini dibagi menjadi empat bab dengan penjelasan sebagai berikut:

BAB I Bab ini berisi gambaran umum mengenai penelitian yang dilakukan, termasuk latar belakang penelitian yang menjelaskan permasalahan kualitas narasi feedback pada self dan peer assessment dalam lingkungan Project-Based Learning atau PjBL. Bab ini secara terstruktur menguraikan konteks dan rumusan masalah yang dirumuskan berdasarkan kajian awal, merumuskan research question (RQ) serta tujuan dan manfaat penelitian, serta menjelaskan ruang lingkup, batasan, sumber data, dan sistematika penulisan laporan yang mendukung pengembangan dan evaluasi intervensi digital scaffolding yang diusulkan.

[BAB II](#page-8-0) Bab ini membahas secara rinci kajian literatur yang relevan dengan penelitian, menyajikan kerangka teori yang menjadi dasar dan landasan dalam menjawab research question serta mendukung analisis hasil penelitian ini. Bab ini menetapkan dasar-dasar pedagogis, seperti PjBL, feedback literacy, Zone of Proximal Development (ZPD), serta mekanisme digital scaffolding, sekaligus menjelaskan berbagai teori komputasional dalam Natural Language Processing (NLP). Selain itu, bab ini juga melakukan analisis kritis secara perbandingan terhadap penelitian terdahulu yang memiliki keterkaitan dengan topik yang diteliti guna menunjukkan adanya ketidaksesuaian dalam sistem scaffolding secara real-time.

BAB III Bab ini menjelaskan secara sistematis mengenai metodologi penelitian yang digunakan untuk merancang, mengembangkan, dan mengevaluasi sistem digital scaffolding. Pembahasan dalam bab ini mencakup desain penelitian, metode pengumpulan dan analisis data, variabel penelitian, objek penelitian, serta perangkat dan alat bantu yang digunakan. Selain itu, prosedur penelitian yang mencakup tahapan pengembangan pipeline deteksi indikator tekstual, rancangan digital scaffolding, prosedur eksperimen, serta metode analisis yang digunakan untuk menjawab RQ juga dijelaskan secara rinci.

BAB IV Bab ini memaparkan tahapan operasionalisasi variabel eksperimen ke dalam bentuk pipeline komputasional. Struktur pembahasan dimulai dengan spesifikasi arsitektur tingkat makro yang menghubungkan teori pedagogis dengan model NLP. Bagian utama bab ini kemudian mendeskripsikan konfigurasi logika, konstruksi teks, serta kalibrasi model yang digunakan sebagai instrumen utama dalam eksperimen, serta validasi awal instrumen sebelum diujicobakan kepada subjek penelitian.

BAB V Bab ini menyajikan hasil penelitian berdasarkan analisis data eksperimen dan evaluasi terhadap sistem digital scaffolding yang diusulkan. Evaluasi dilakukan pada dimensi komputasional, outcome, dan proses untuk menilai kemampuan deteksi indikator tekstual, pengaruh intervensi terhadap output feedback yang dihasilkan mahasiswa, serta dinamika interaksi mahasiswa dengan digital scaffolding selama proses penulisan berlangsung. Pembahasan difokuskan pada interpretasi hasil dan perbandingan dengan penelitian sebelumnya untuk menjawab research question. Bagian ini juga membahas evaluasi dampak penggunaan serta tingkat keberterimaan pengguna terhadap hasil penelitian berdasarkan umpan balik yang diperoleh.

BAB VI Bab ini menjelaskan outcome yang diharapkan dari pengguna/mitra. Hal ini ditujukan untuk mengevaluasi minimal sejauh mana keberterimaan pengguna terhadap hasil penelitian ini, sesuai manfaat yang ditetapkan.

BAB VII Bab ini menjelaskan kesimpulan dari keseluruhan hasil penelitian yang telah dilakukan serta menjawab research question yang telah dirumuskan. Kesimpulan disusun berdasarkan hasil analisis dan pembahasan, serta dikaitkan dengan tujuan penelitian. Selanjutnya, disampaikan saran-saran untuk penelitian selanjutnya berdasarkan hasil kesimpulan yang bersifat konstruktif untuk pengembangan lebih lanjut, baik dari aspek teknis, perbaikan metodologi, maupun arah penelitian masa depan serta rencana keberlanjutan yang berpotensi memperluas penerapan sistem yang telah dibangun agar dapat dirasakan manfaatnya dalam jangka panjang.

**BAB II**

**TINJAUAN PUSTAKA**

Bab ini membahas pemahaman dasar mengenai konsep dan teori yang berkaitan dengan topik yang dibahas serta mengidentifikasi karya ilmiah yang relevan sebagai referensi dalam proses penelitian.

**II.1 Dasar Teori**

Dasar teori ini melibatkan konsep-konsep yang mendukung pelaksanaan penelitian. Teori yang dibahas menjadi dasar dalam penyelenggaraan dan penilaian Tugas Akhir.

**II.1.1 Project Based Learning (PjBL)**

Pembelajaran Berbasis Proyek (PjBL) merupakan pendekatan pembelajaran yang secara aktif menggunakan masalah dunia nyata untuk memfasilitasi mahasiswa mengaplikasikan teori ke dalam praktik melalui kerja kelompok kolaboratif (Yew et al., 2016). Karakteristik utama PjBL adalah ketergantungan antar anggota dalam mencapai keberhasilan proyek yang dikerjakan (Yew et al., 2016). Ketergantungan ini menciptakan lingkungan kolektivitisme yang mempengaruhi perilaku sosial dan cara mahasiswa berinteraksi satu sama lain selama proses pengerjaan proyek. Sebagai contoh alur kerja PjBL, [Gambar II.1](#page-9-0) menggambar konteks PjBL pada institusi penelitian, menunjukkan dua fase pengerjaan tugas kelompok dan dua timepoint pelaksanaan self dan peer assessment pada pertengahan dan akhir semester.

Gambar II.1 Siklus PjBL dalam Konteks Penelitian

Dosen pada lingkungan PjBL umumnya terbatas pada produk akhir atau output yang dihasilkan. Sebaliknya, rekan sejawat (peer) terlibat langsung dalam proses harian, pengerjaan dan dinamika internal kelompok, mereka memiliki akses mengenai perilaku serta kontribusi yang tidak teramati oleh dosen (Nicol et al., 2014). Hal ini menciptakan kondisi dimana Self dan Peer Assessment berperan sebagai instrumen utama mengevaluasi dimensi kolaborasi, tanggung jawab, proses yang mendasari hasil akhir proyek (Cheng et al., 2008; Dornyei & Murphey, 2011; Panadero et al., 2017).

Konsep PjBL digunakan dalam penelitian ini sebagai konteks ekosistem pembelajaran kolaboratif yang menjustifikasi perlunya instrumen evaluasi berupa narasi feedback antar rekan sejawat. Lingkungan interdependen ini memicu masalah kesenjangan artikulasi yang menjadi fokus utama intervensi sistem.

**II.1.2 Self Assessment**

Self assessment atau penilaian diri sendiri merupakan bentuk feedback ketika siswa menjelaskan dan mengevaluasi kualitas proses belajar dan hasil kerja sendiri untuk meningkatkan perbaikan pembelajaran di masa depan (Yan & Carless, 2022) yang digambarkan pada [Gambar II.2](#page-10-0). Penerapan self assessment menunjukkan peningkatan hasil akademik, kemampuan mengatur diri, hingga mendorong kesadaran untuk terus meningkatkan kualitas pembelajaran (Panadero et al., 2017). Secara operasional, proses ini menuntut mahasiswa untuk menginternalisasi kriteria dalam rubrik dan mengomunikasikan hasil penilaian tersebut secara konsisten melalui skor numerik dan narasi kualitatif (Setiawan, 2026a).

Gambar II.2 Alur Self-Assessment

Teori mengenai self assessment diperlukan dalam penelitian ini untuk menjelaskan asal mula teks narasi yang dievaluasi, sekaligus menjustifikasi pentingnya bantuan scaffolding guna memitigasi bias over estimasi yang menyebabkan ketidakselarasan skor-narasi saat mahasiswa menyusun evaluasi mandiri.

**II.1.3 Peer Assessment**

Peer assessment merupakan proses siswa memberikan feedback terhadap kontribusi teman sejawatnya dalam kelompok PjBL yang divisualisasikan pada [Gambar II.3.](#page-11-0) Jika diterapkan dengan tepat, metode ini mendorong kemandirian belajar dan memfasilitasi evaluasi mandiri (Nicol et al., 2014). Efektivitas peerassessment sangat bergantung pada kemampuan mahasiswa mengartikulasikan penilaian evaluatif ke dalam teks narasi yang bermakna (Nicol et al., 2014).

Gambar II.3. Alur Peer-Assessment

Konsep peer assessment digunakan sebagai kerangka masalah untuk menunjukkan bagaimana tekanan harmoni memicu narasi yang tidak substantif. Hal ini mendukung rancangan komponen rule-based untuk mendeteksi narasi dengan cakupan rubrik rendah dan mengarahkan kembali fokus mahasiswa pada kriteria penilaian.

**II.1.4 Feedback**

Feedback secara konseptual adalah informasi yang diberikan oleh pengajar, teman sejawat, atau pengalaman sebagai hasil dari kinerja seseorang untuk mendukung mendorong motivasi, memperbaiki proses belajar, dan mengubah kinerja (Hattie & Timperley, 2007; Nelson & Schunn, 2008). Agar efektif, feedback harus menjawab tiga pertanyaan utama: feed up yaitu capaian mengenai target individu yang menerima feedback, feed back yaitu bagaimana kemajuan saat ini dan feed forward  langkah apa yang harus diambil selanjutnya (Hattie & Timperley, 2007). Ketiga fungsi ini menuntut adanya kejelasan standar dan spesifitas informasi agar kesenjangan antara performa atau kinerja saat ini dan tujuan pembelajaran yang akan dicapai dapat dipersempit.

Dalam konteks assessment berbasis rubrik, efektivitas feedback sering kali berkurang apabila hanya direpresentasikan dalam bentuk skor numerik. Skor numerik memberikan informasi mengenai tingkat capaian, tetapi tidak menyediakan penjelasan yang diperlukan untuk memahami alasan penilaian maupun arah perbaikan (Winstone & Carless, 2019). Oleh karena itu, narasi kualitatif berperan sebagai komponen yang menjembatani skor numerik dengan tujuan pedagogis. Melalui narasi tersebut, pemberi feedback dapat mengartikulasikan alasan pemberian skor, mengidentifikasi kekuatan maupun kelemahan, serta menyampaikan saran perbaikan yang lebih spesifik sehingga feedback dapat berfungsi sebagai sarana pembelajaran.

**II.1.5 Rubrik**

Dalam konteks evaluasi kompetensi, rubrik didefinisikan sebagai instrumen penilaian terstruktur yang memuat kriteria spesifik guna menilai kualitas performa atau hasil kerja peserta didik berdasarkan rangkaian standar pencapaian yang eksplisit (Brookhart, 2013). Pada lingkungan PjBL, rubrik berfungsi sebagai alat standarisasi nilai oleh pengajar serta pemandu kognitif yang membantu mahasiswa memahami standar kualitas secara mandiri (Jonsson & Svingby, 2007). Berdasarkan format rancangannya, rubrik secara umum diklasifikasikan menjadi dua jenis, yaitu rubrik holistik yang mengevaluasi proses atau output secara menyeluruh dan simultan, serta rubrik analitik yang mengurai kriteria penilaian ke dalam dimensi-dimensi performa yang terpisah dan independen satu sama lain (Brookhart, 2013).

Rubrik analitik memiliki kontribusi pedagogis yang lebih besar dalam mendukung aktivitas self assessment dan peer assessment karena mampu memberikan informasi yang lebih rinci mengenai aspek-aspek performa yang telah maupun belum dicapai (Jonsson & Svingby, 2007). Secara umum, rubrik analitik terdiri atas tiga komponen utama, yaitu kriteria penilaian, skala penilaian, dan deskripsi tingkat capaian yang menjelaskan karakteristik performa pada setiap tingkat skor (Panadero et al., 2017). Komponen dalam rubrik analitik terdiri dari tiga elemen, yaitu kriteria atau dimensi performa yang dinilai, skala penilaian berupa tingkatan skor kuantitatif kontinu, dan deskripsi tingkat capaian tekstual yang merinci karakteristik performa yang spesifik (Jonsson & Svingby, 2007).

Lampiran 10 menyajikan contoh instrumen rubrik analitik yang diterapkan dalam PjBL pada Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung untuk mengevaluasi dimensi kolaborasi teknis dan pengolahan data iklan yang dilakukan mahasiswa.

Dalam penelitian ini, rubrik diposisikan sebagai representasi eksplisit terhadap standar narasi feedback yang menjadi acuan evaluasi. Keberadaan rubrik memberikan dasar konseptual bagi proses identifikasi karakteristik narasi feedback  serta menjadi sumber pengetahuan yang mendefinisikan aspek-aspek kualitas yang perlu didukung melalui mekanisme scaffolding.

**II.1.6 Natural Language Processing (NLP) dan Arsitektur Transformer**

Landasan komputasional NLP yang digunakan dalam penelitian ini mencakup arsitektur Transformer, model sentence embedding SBERT, cosine similarity sebagai ukuran kemiripan semantik, serta metrik F1-Score untuk evaluasi performa. Sebagaimana disajikan pada Lampiran 4, model embedding digunakan sebagai black box tool dalam penelitian ini, kajian hanya memanfaatkan representasi vektor yang dihasilkannya.

Dalam penelitian ini, pendekatan semantic embedding digunakan untuk menghasilkan representasi vektor dari narasi feedback mahasiswa dan kriteria rubrik, kemudian kesamaan semantiknya diukur menggunakan cosine similarity sebagai komponen utama pipeline deteksi indikator. Model intfloat/multilinguale5-large-instruct dipilih karena menunjukkan performa terbaik pada evaluasi komparatif yang dilakukan pada subbab IV.3.1. Evaluasi performa pipeline menggunakan F1-Score dengan pendekatan micro-averaging.

**II.1.7 Rule Based**

Rule-based merupakan pendekatan dalam expert system yang menggunakan sekumpulan aturan eksplisit (if–then rules) untuk memetakan kondisi tertentu menjadi aksi yang telah ditentukan sebelumnya. Pada sistem berbasis rule-based,  logika pengambilan keputusan didefinisikan secara eksplisit sehingga setiap keputusan dapat ditelusuri kembali berdasarkan aturan yang digunakan (Negnevitsky, 2005).

Salah satu bentuk representasi aturan yang banyak digunakan dalam sistem rulebased adalah decision table. Decision table merupakan representasi tabular dari logika kondisional yang memetakan setiap kombinasi kondisi masukan (input conditions) ke aksi keluaran (output actions) secara eksplisit. Dibandingkan representasi berupa rangkaian if–else, decision table memberikan struktur yang lebih sistematis karena seluruh kemungkinan kombinasi kondisi dapat didokumentasikan dalam satu tabel (Crina & Abraham, 2011)

Secara umum, sebuah decision table terdiri atas tiga komponen utama, yaitu: (1) condition stubs yang mendefinisikan variabel atau kondisi yang dievaluasi, (2) condition entries yang merepresentasikan kombinasi nilai dari setiap kondisi, dan (3) action entries yang mendefinisikan aksi yang dijalankan untuk setiap kombinasi kondisi tersebut.

Karakteristik utama decision table adalah completeness, yaitu setiap kombinasi kondisi memiliki aksi yang terdefinisi, serta determinism, yaitu kombinasi kondisi yang sama selalu menghasilkan aksi yang sama. Kedua karakteristik tersebut menjadikan decision table sesuai digunakan pada domain keputusan yang memiliki ruang kondisi terbatas dan memerlukan proses pengambilan keputusan yang konsisten serta dapat diaudit.

**II.1.8 Feedback Literacy**

Carless & Boud (2018) mendefinisikan feedback literacy sebagai pemahaman, kapasitas, dan disposisi yang diperlukan untuk memahami informasi evaluatif dan menggunakannya untuk meningkatkan pembelajaran. Konsep ini mencakup empat aspek, yaitu mengenali bentuk feedback, evaluative judgement, mengelola respons emosional, dan menerjemahkan feedback menjadi perbaikan. Salah satu aspeknya, evaluative judgement, merupakan kemampuan untuk menilai kualitas pekerjaan berdasarkan standar yang ditetapkan (Tai et al., 2018).

Carless & Boud (2018) tidak secara eksplisit memisahkan kapasitas menilai (evaluative judgement) dari kemampuan mengartikulasikan penilaian tersebut ke dalam bentuk tertulis. Penelitian lanjutan oleh Setiawan (2026a), yang meneliti lebih lanjut mengenai evaluative expression, yaitu keberhasilan mengartikulasikan penilaian tersebut ke dalam narasi tertulis yang selaras dengan rubrik dan dapat dipahami oleh penerima feedback (assessee). Penelitian ini mengadopsi pemisahan (Setiawan, 2026a) sebagai dasar konseptual, dengan Carless & Boud (2018) berfungsi sebagai kerangka payung yang melegitimasi feedback literacy sebagai konstruk yang relevan, bukan sebagai sumber langsung dari pemisahan judgementexpression itu sendiri.

Evaluative expression merupakan konstruk laten sehingga tidak dapat diamati secara langsung, melainkan diinferensi melalui karakteristik tekstual pada narasi yang dihasilkan. Penelitian yang dilakukan oleh Setiawan et al. (2026) mengidentifikasi indikator atau sinyal yang bertindak sebagai manifestasi terbatas dari evaluative expression yang dapat diobservasi melalui teks. Penelitian ini mengadopsinya dalam bentuk sebagai berikut.

Pertama, cakupan rubrik. Cakupan rubrik mengukur sejauh mana narasi feedback secara eksplisit membahas kriteria yang tercantum dalam rubrik penilaian. Dalam literatur Setiawan et al. (2026) mendefinisikannya relevansi terhadap rubrik diidentifikasi melalui kemunculan referensi atau istilah yang berasosiasi dengan standar penilaian. Secara konseptual, kualitas evaluasi tidak hanya ditentukan oleh keberadaan istilah tersebut, tetapi juga oleh sejauh mana mahasiswa mampu menghubungkan evaluasi mereka dengan berbagai aspek kriteria yang relevan. Oleh karena itu, cakupan rubrik berfungsi sebagai sinyal yang merepresentasikan kemampuan mahasiswa dalam menerapkan evaluative judgment. Narasi feedback  dengan cakupan rubrik yang rendah mengindikasikan bahwa proses evaluasi belum sepenuhnya berlandaskan pada kriteria tugas sehingga berpotensi menghasilkan komentar yang bersifat umum dan kurang dapat ditindaklanjuti. Contoh dari indikator ini disajikan pada [Gambar II.4](#page-1-0) menggunakan rubrik pada Lampiran 10.

Gambar II.4. Contoh Cakupan Rubrik Tidak Terpenuhi

Kedua, koherensi evaluatif berkaitan dengan konsistensi antara keputusan evaluasi dan ekspresi evaluasi yang diberikan. Penelitian Setiawan et al. (2026) membahas konsistensi penilaian melalui konsep kalibrasi antar pemberi narasi feedback, yaitu kesesuaian antara hasil self assessment dan penilaian peer assessment. Penelitian ini mengadaptasi konsep tersebut ke dalam konteks yang berbeda dengan mengevaluasi konsistensi secara internal, yaitu kesesuaian antara skor numerik dan narasi feedback yang diberikan oleh mahasiswa. Dengan demikian, indikator koherensi evaluatif merepresentasikan kemampuan mahasiswa untuk menerjemahkan hasil evaluative judgment ke dalam evaluative expression yang selaras dengan keputusan penilaiannya. Contoh dari indikator ini diilustraikan pada [Gambar II.5.](#page-2-0)

Gambar II.5. Contoh Koherensi Evaluatif Tidak Terpenuhi

Ketiga, kedalaman elaborasi diukur berdasarkan jumlah kata pada narasi feedback. Penelitian yang dilakukan Setiawan et al. (2026) menunjukkan bahwa panjang narasi dapat dimanfaatkan sebagai sinyal awal (lightweight analytic signal) untuk mengidentifikasi kemungkinan kurangnya elaborasi. Berangkat dari temuan tersebut, penelitian ini menggunakan panjang narasi sebagai indikator struktural untuk mendeteksi apakah feedback memiliki ruang yang cukup untuk memuat penjelasan, justifikasi, atau rekomendasi yang bermakna. Meskipun jumlah kata tidak secara langsung mencerminkan kualitas isi, narasi yang sangat singkat memiliki keterbatasan struktural dalam menyampaikan evaluasi secara komprehensif. Contoh kasus dari indikator ini diilustrasikan pada [Gambar II.6](#page-3-0)

Gambar II.6. Contoh Elaborasi Narasi Feedback

Keempat, relevansi topik memastikan bahwa konten narasi tidak menyimpang dari aspek rubrik yang menjadi fokus pertanyaan assessment. Penelitian Setiawan et al. (2026) menekankan pentingnya keterkaitan antara narasi feedback dan kriteria penilaian sebagai dasar pemberian bantuan secara otomatis. Penelitian ini mengembangkan konsep tersebut dengan mengevaluasi apakah narasi mahasiswa tetap membahas aspek evaluasi yang sesuai dengan unit penilaian yang sedang dianalisis. Indikator ini merepresentasikan ketepatan arah evaluative judgment sekaligus kemampuan mahasiswa mempertahankan fokus pembahasan selama menyampaikan evaluative expression. Narasi yang menyimpang dari aspek yang sedang dinilai berpotensi mengurangi nilai pedagogis feedback karena informasi yang diberikan menjadi kurang relevan bagi penerima. Contoh dari indikator ini diilustrasikan pada [Gambar II.7](#page-4-0).

Gambar II.7. Contoh Relevansi Tidak Terpenuhi

Keempat karakteristik tekstual tersebut memberikan dasar konseptual untuk memahami bagaimana kualitas evaluasi dapat tercermin pada narasi feedback  mahasiswa. Masing-masing karakteristik merepresentasikan dimensi yang berbeda dari proses artikulasi evaluasi ke dalam bentuk tulisan, sehingga secara bersamasama membentuk landasan teoritis dalam analisis kualitas feedback tertulis.

**II.1.8.1 Dekomposisi Rubrik**

Feedback literacy yang dijelaskan pada [II.1.8](#page-0-0) bersifat konseptual, keempatnya mendeskripsikan kapasitas kognitif yang seharusnya tercermin dalam narasi feedback. Untuk memungkinkan deteksi komputasional terhadap manifestasi tekstual evaluative expression pada narasi feedback, deskripsi rubrik perlu diterjemahkan menjadi unit-unit evaluatif yang dapat dibandingkan secara sistematis oleh pipeline NLP. Proses penerjemahan ini disebut sebagai dekomposisi rubrik.

Dekomposisi rubrik merupakan proses memecah suatu deskripsi penilaian atau kompetensi yang kompleks menjadi sejumlah kriteria atau dimensi yang lebih spesifik dan saling independen. Dalam literatur pendidikan, proses ini sejalan dengan prinsip pengembangan analytic rubric. Berbeda dengan rubrik holistik yang menilai performa secara keseluruhan dalam satu keputusan evaluatif, rubrik analitik memisahkan setiap dimensi penilaian sehingga masing-masing dapat dievaluasi secara independen (Brookhart, 2013). Pendekatan tersebut memungkinkan penyediaan informasi evaluatif yang lebih rinci mengenai capaian peserta didik pada setiap aspek kompetensi, sehingga mendukung identifikasi kekuatan maupun kelemahan secara lebih sistematis (Jonsson & Svingby, 2007).

Dalam bidang Artificial Intelligence, proses mengubah representasi pengetahuan yang masih berbentuk naratif menjadi struktur yang lebih terorganisasi merupakan bagian dari knowledge acquisition dalam kerangka knowledge engineering. Tahapan ini mencakup ekstraksi, strukturisasi, dan formalisasi pengetahuan dari pakar maupun dokumen sehingga dapat direpresentasikan dalam bentuk yang lebih terstruktur dan siap digunakan oleh sistem komputasional (Negnevitsky, 2005). Dari sudut pandang tersebut, dekomposisi rubrik dapat dipandang sebagai proses transformasi pengetahuan evaluatif dari bentuk naratif menjadi representasi yang lebih eksplisit tanpa mengubah makna yang dikandung oleh rubrik itu sendiri.

Dengan demikian, dekomposisi rubrik memberikan landasan konseptual untuk mengubah deskripsi penilaian yang kompleks menjadi unit-unit yang lebih sederhana, eksplisit, dan terstruktur. Representasi yang lebih terstruktur tersebut mempermudah proses analisis terhadap setiap aspek penilaian secara independen sekaligus mempertahankan hubungan hierarkis antara tujuan pembelajaran, dimensi penilaian, dan karakteristik performa yang direpresentasikan dalam rubrik.

**II.1.9 Zone of Proximal Development**

Teori sosiokultural Vygotsky mendefinisikan Zone of Proximal Development (ZPD) sebagai jarak antara kemampuan pemecahan masalah secara mandiri dengan kemampuan yang dapat dicapai melalui bimbingan dari pihak yang lebih kompeten. Pembelajaran optimal terjadi ketika peserta didik mengerjakan tugas yang berada pada area tersebut melalui proses mediasi yang bersifat sementara dan kondisional.

Dalam konteks pemberian feedback, proses menyusun penilaian tertulis merupakan aktivitas kognitif tingkat tinggi yang melibatkan interpretasi terhadap kriteria penilaian, diagnosis kualitas pekerjaan, serta penyusunan justifikasi yang dapat dipahami oleh penerima feedback (Carless & Boud, 2018; Gu et al., 2026). Kompleksitas tersebut menyebabkan penyusunan feedback sering kali berada pada area Zone of Proximal Development, sehingga memerlukan dukungan sementara agar peserta didik mampu menghasilkan feedback yang lebih berkualitas (Kollar & Fischer, 2010).

Dukungan tersebut diberikan secara bertahap sesuai kebutuhan peserta didik dan secara bertahap dikurangi ketika kemampuan mandiri mulai berkembang. Ilustrasi mengenai kerangka kerja ZPD disajikan pada [Gambar II.8](#page-6-0).

Gambar II.8 Ilustrasi kerangka ZPD

Dalam perspektif ZPD, bantuan yang diberikan tidak dimaksudkan untuk menggantikan proses berpikir peserta didik, melainkan sebagai bentuk mediasi sementara agar peserta didik mampu menyelesaikan tugas yang belum dapat diselesaikan secara mandiri. Oleh karena itu, karakteristik utama scaffolding adalah bersifat contingent (Pea, 2004) yaitu hanya diberikan ketika diperlukan, serta fading, yaitu secara bertahap dihentikan ketika peserta didik telah mampu menyelesaikan tugas tersebut secara mandiri.

**II.1.10 Scaffolding**

Konsep scaffolding sebagai strategi instruksional diperkenalkan oleh Wood et al. (1976) sebagai mekanisme yang menjembatani teori Zone of Proximal Development (ZPD) yang dikemukakan oleh Vygotsky. Scaffolding merujuk pada dukungan terstruktur yang diberikan kepada peserta didik selama proses penyelesaian tugas agar mereka mampu mencapai tingkat kemampuan yang belum dapat dicapai secara mandiri. Dukungan tersebut bersifat sementara dan secara bertahap dikurangi seiring meningkatnya kompetensi peserta didik (Pea, 2004).

Literatur menjelaskan bahwa scaffolding memiliki dua karakteristik utama, yaitu contingent dan fading. Prinsip contingent menyatakan bahwa bantuan hanya diberikan ketika peserta didik mengalami kesulitan dalam menyelesaikan tugas, sedangkan prinsip fading menyatakan bahwa bantuan tersebut secara bertahap dikurangi ketika peserta didik telah mampu melanjutkan tugas secara mandiri (Pea, 2004).

Scaffolding sendiri menurut (Cagiltay, 2006) membaginya menjadi empat jenis, yaitu conceptual di mana scaffolding diposisikan untuk membantu pembelajar memahami apa yang perlu dipertimbangkan dan bagaimana dalam melakukan suatu tugas pada level konseptual atau ide, metacognitive memosisikan scaffolding sebagai sarana refleksi yang disampaikan dalam bentuk instruksi untuk mendorong proses artikulasi, sementara procedural memberikan bantuan tentang mengenai pemanfaatan suatu tools atau alat dalam suatu tugas, dan strategic memberikan bantuan dalam posisi memilih terkait strategi menghadapi suatu tugas.

Dalam konteks penulisan feedback, kedua prinsip tersebut memiliki implikasi penting. Bantuan yang diberikan secara terus-menerus tanpa mempertimbangkan kondisi aktual peserta didik berpotensi menimbulkan ketergantungan sehingga kemampuan evaluatif tidak berkembang secara mandiri (Ding et al., 2025; Pea, 2004). Teori scaffolding diperlukan untuk memberikan kerangka instruksional bagaimana intervensi diberikan secara adaptif (contigent) tanpa menimbulkan ketergantungan. Konsep ini mendukung desain komponen rule-based yang menampilkan dan menarik prompt berdasarkan hasil deteksi keempat indikator tekstual.

**II.1.10.1 Karakteristik Scaffolding**

Menurut Belland (2017), untuk memfasilitasi peningkatan keterampilan secara efektif, scaffolding harus memenuhi sejumlah elemen yang dipenuhi.

Pertama, Dynamic Assessment. Menjelaskan bahwa bantuan scaffolding diberikan setelah dilakukan penilaian terhadap performa pembelajar untuk mengidentifikasi kebutuhan belajarnya pada saat yang sama. Berdasarkan hasil penilaian tersebut, scaffolding disesuaikan dengan tingkat kesulitan yang dialami pembelajar sehingga bantuan yang diberikan tepat sasaran.

Kedua, yaitu Providing Just The Right Amount of Support. Scaffolding harus merespons dengan melakukan adaptasi terhadap tingkat dukungannya. Adaptabilitas ini dioperasionalkan melalui mekanisme penyesuaian yang mengatur intensitas bantuan yang diberikan yang diklasifikasikan sebagai adding dan fading. Adding. Dalam kondisi ini, sistem memberikan panduan yang lebih kuat, memberikan petunjuk tambahan, atau meningkatkan frekuensi peringatan untuk menjaga mahasiswa tetap berada di jalur pemecahan masalah. Sementara fading mengacu pada proses pengurangan atau penarikan intensitas dan frekuensi bantuan secara bertahap saat pembelajar mulai menunjukkan peningkatan kompetensi. Literatur menempatkan fading sebagai salah satu karakteristik penting untuk mendorong transisi menuju kemandirian belajar dan pengalihan tanggung jawab.

Ketiga, yaitu intersubejctivity. Elemen ini menjelaskan keadaan ketika target scaffolding dan pemberi scaffolding memiliki pemahaman yang cukup sama mengenai tugas, tujuan, dan penyelesaian yang benar. Sementara itu Saye & Brush (2002) menjelaskan bahwa scaffolding terbagi menjadi dua kategori utama.

Pertama, hard scaffolding. Merupakan bentuk dukungan statis yang dirancang, diantisipasi, dan ditanamkan ke dalam sistem atau materi pembelajaran sebelum siswa mulai mengerjakan tugas. Hard scaffolding umumnya diimplementasikan berbasis komputer karena dirancang untuk mengatasi kesulitan-kesulitan yang sudah terdokumentasikan baik menurut literatur maupun observasi.

Kedua yaitu soft scaffolding. Merupakan bentuk dukungan dinamis dan sangat interaktif yang diberikan secara langsung seketika sesuai dengan kebutuhan pembelajar yang terus berubah-ubah. Dukungan ini umumnya diberikan oleh manusia, seperti dosen atau rekan sejawat, yang mampu menegosiasikan makna secara kontekstual melalui interaksi sosial.

Elemen dan klasifikasi tersebut menjadi landasan dalam merancang sistem digital scaffolding, karena menentukan bagaimana bantuan dipicu, disampaikan, dan disesuaikan terhadap kebutuhan pembelajar selama proses pembelajaran.

**II.1.11 Digital Scaffolding**

Digital scaffolding merupakan implementasi prinsip scaffolding melalui mekanisme komputasional yang mampu mendeteksi kondisi belajar peserta didik secara otomatis dan memberikan bantuan yang sesuai tanpa keterlibatan langsung guru atau tutor (Ding et al., 2025). Berbeda dengan scaffolding konvensional yang bergantung pada observasi manusia, digital scaffolding memanfaatkan informasi yang tersedia selama proses pembelajaran untuk menentukan kapan bantuan perlu diberikan.

Meskipun media implementasinya berbeda, digital scaffolding tetap mempertahankan karakteristik utama scaffolding, yaitu bersifat contingent dan fading. Bantuan diberikan ketika sistem mengidentifikasi bahwa peserta didik mengalami kesulitan pada tugas yang sedang dikerjakan, kemudian dihentikan setelah peserta didik menunjukkan bahwa bantuan tersebut tidak lagi diperlukan (Ding et al., 2025; Pea, 2004).

Dalam penerapannya, intervensi yang diberikan oleh digital scaffolding tidak bersifat non-coercive. Konsep scaffolding non-coercive menjelaskan bahwa intervensi ringan pada individu dapat menginterupsi independensi sesaat, namun pada akhirnya bertujuan untuk memperkuat kemandirian jangka panjang penggunanya agar dapat mengambil keputusan yang selaras dengan nilai-nilai evaluatif mereka. Oleh karena itu, kehadiran digital scaffolding dalam riset ini memosisikan intervensi hanya sebagai opsi panduan kognitif sementara tanpa adanya paksaan.

**II.1.11.1 Pendekatan Generasi Teks untuk Scaffolding**

Digital scaffolding yang memberikan bantuan dalam bentuk teks memerlukan mekanisme Natural Language Generation (NLG), yaitu proses menghasilkan representasi bahasa alami berdasarkan suatu representasi nonlinguistik seperti data, aturan, maupun representasi semantik (Deemter et al., 2005). Dalam konteks sistem instruksional, mekanisme ini berfungsi mengubah hasil analisis kondisi pengguna menjadi teks yang dapat dipahami sebagai arahan atau umpan balik. Literatur NLG mengenal berbagai pendekatan yang berbeda dalam cara menghasilkan teks, mulai dari pendekatan generatif berbasis model bahasa hingga pendekatan berbasis template yang menggunakan struktur kalimat yang telah ditentukan sebelumnya.

Pendekatan yang digunakan dalam penelitian ini adalah template yang menghasilkan teks melalui pemetaan representasi nonlinguistik, seperti data, variabel, atau konstanta, ke dalam struktur kalimat yang telah ditentukan sebelumnya. Template terdiri atas bagian teks tetap dan sejumlah placeholder yang diisi menggunakan nilai masukan pada saat proses generasi berlangsung (Deemter et al., 2005).

Karena struktur kalimat telah ditentukan sebelum proses generasi berlangsung, ruang keluaran pada pendekatan berbasis template bersifat terbatas dan dapat didefinisikan secara eksplisit. Setiap kombinasi nilai masukan akan dipetakan ke struktur kalimat yang sama, sehingga keluaran yang dihasilkan bersifat deterministik dan reproducible, yaitu masukan yang identik akan selalu menghasilkan keluaran yang identik (Deemter et al., 2005). Karakteristik tersebut membedakan pendekatan berbasis template dari pendekatan generatif probabilistik yang membentuk teks melalui proses prediksi satuan kata.

Perbedaan karakteristik tersebut menjadi landasan konseptual dalam memahami alternatif mekanisme generasi teks yang dapat digunakan pada sistem digital scaffolding. Pembahasan mengenai pendekatan yang digunakan dalam penelitian ini beserta alasan pemilihannya dijelaskan pada BAB III.

**II.2 Karya Ilmiah Sejenis**

Tabel II.1 Literatur sejenis dan penulisnya

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Penelitian mengenai feedback literacy menunjukkan bahwa kualitas feedback tidak hanya ditentukan oleh kemampuan mahasiswa memberikan penilaian, tetapi juga oleh kemampuan mengomunikasikan penilaian tersebut dalam bentuk narasi yang dapat dipahami dan ditindaklanjuti. Dalam konteks PjBL, aktivitas self dan peer assessment menempatkan mahasiswa sebagai pemberi sekaligus penerima feedback sehingga kemampuan menyusun narasi evaluatif menjadi bagian penting dari proses pembelajaran. Kajian Setiawan (2026a) yang mengungkapkan bahwa dalam ekosistem PjBL di Indonesia, sebagian besar mahasiswa mampu memberikan skor numerik tinggi tetapi kesulitan menyusun narasi feedback yang selaras dengan rubrik. Temuan tersebut menunjukkan masalah mendasar dalam kemampuan mahasiswa mengekspresikan evaluasi secara eksplisit dalam bentuk feedback bermakna, sehingga intervensi diperlukan saat proses penulisan berlangsung, bukan sekadar deteksi pasca-penulisan.

Berbagai penelitian telah mengidentifikasi sejumlah karakteristik tekstual yang digunakan untuk menganalisis narasi feedback. Penelitian menekankan pentingnya cakupan terhadap aspek-aspek dalam rubrik penilaian (Camarata & Slieman, 2020), Zhang & Schunn (2023) menunjukkan pentingnya koherensi antara skor numerik dan narasi pendukung, Curtis et al. (2024) menggunakan panjang narasi sebagai pendekatan operasional untuk merepresentasikan tingkat elaborasi, sedangkan Sun et al. (2023) membahas relevansi topik sebagai indikator kesesuaian isi feedback  terhadap aspek yang sedang dievaluasi. Keempat karakteristik tersebut memiliki kesamaan, yaitu dapat diidentifikasi melalui informasi tekstual yang tersedia pada narasi feedback sehingga berpotensi dioperasionalkan menjadi indikator komputasional.

Pada sisi intervensi, sejumlah penelitian menunjukkan bahwa Aritificial Intelligence (AI) dapat membantu dalam pemberian intervensi memberikan bantuan berupa digital scaffolding. Ding et al. (2025) mengajukan model scaffolding yang mengintegrasikan kontekstualisasi dan logika prosedural, di mana scaffolding memberikan dukungan dinamis yang selaras dengan tahapan kognitif pembelajaran. Gu et al. (2026) menemukan bahwa AI Generatif (GenAI) mampu memberikan umpan balik instan dan adaptif yang secara efektif menopang proses regulasi diri (Self-Regulated Learning) mahasiswa. Namun, penggunaan AI juga memunculkan tantangan kontrol pedagogis yang serius. Seperti yang diperingatkan oleh Gu et al. (2026) dan didukung oleh temuan Mohammad et al. (2025) ketergantungan mahasiswa pada saran instan dari Large Language Models (LLM) dapat memicu cognitive scaffloding atau kemalasan metakognitif, di mana mahasiswa melemahkan pemikiran kritisnya sendiri dan menerima rekomendasi AI secara otomatis. Selain itu sebagian besar pendekatan masih beroperasi secara sumatif, algoritma hanya memproses data setelah mahasiswa mengirimkan feedback (Omotehinwa et al., 2025; Rahimi et al., 2017).

Perkembangan NLP dalam analisis feedback menunjukkan pergeseran dari pendekatan yang berfokus pada evaluasi hasil akhir menuju ekstraksi berbagai karakteristik tekstual yang semakin beragam. Pada konteks PjBL, Setiawan et al. (2026) meneliti pendekatan seperti dictionary-based matching, ekstraksi fitur wacana, analisis sentimen, maupun klasifikasi speech acts menunjukkan bahwa informasi yang terkandung dalam narasi self assessment dan peer assessment. Setiawan (2026b) juga memvalidasi penggunaan model berbasis bahasa Indonesia untuk mengekstraksi polaritas sentimen dan mengklasifikasikan speech acts dari ribuan teks self assessment dan peer assessment mahasiswa. Pendekatan ini memungkinkan sistem untuk mendeteksi persistensi dan perjuangan kognitif mahasiswa di balik ekspresi yang secara kultural cenderung netral atau menahan diri. Meskipun demikian, sebagian besar penelitian masih memanfaatkan hasil analisis tersebut sebagai sarana evaluasi atau visualisasi setelah mahasiswa menyelesaikan proses penulisan (post-hoc analysis). Dengan kata lain, keluaran NLP belum secara langsung digunakan sebagai dasar pengambilan keputusan pedagogis selama proses penulisan berlangsung. Kesenjangan inilah yang menjadi landasan penelitian ini, yaitu mengintegrasikan hasil deteksi NLP dengan mekanisme rule-based untuk menentukan kebutuhan bantuan dan memicu digital scaffolding secara real-time ketika mahasiswa sedang menyusun narasi self assessment dan peer assessment.

Berdasarkan sintesis tersebut, dapat diidentifikasi bahwa, meskipun berbagai penelitian telah mengidentifikasi karakteristik feedback yang berkaitan dengan kualitas narasi, belum banyak penelitian yang mengoperasionalkan karakteristik tersebut menjadi indikator tekstual yang dapat dideteksi secara otomatis selama proses penulisan berlangsung. Selain itu, meskipun AI telah dimanfaatkan sebagai digital scaffolding, sebagian besar pendekatan masih memberikan bantuan setelah proses penulisan selesai atau belum mengintegrasikan mekanisme untuk menentukan kebutuhan bantuan secara konsisten. Kesenjangan inilah yang menjadi dasar pengembangan arsitektur digital scaffolding berbasis rubrik pada penelitian ini, yang mengintegrasikan pemrosesan NLP dengan mekanisme rule-based untuk memberikan conditional prompt secara real-time selama mahasiswa menyusun feedback pada aktivitas self assessment dan peer assessment di lingkungan PjBL.

**BAB III**

**METODOLOGI PENELITIAN**

Bab ini menjelaskan metodologi penelitian termasuk, objek, variabel, data yang ada dalam penelitian serta metodologi yang dilakukan.

Pada penelitian ini, hubungan antar istilah teknis yang digunakan dalam metodologi dipetakan sebagai berikut: (1) SAPA adalah aplikasi self dan peer assessment berbasis web yang sudah ada dan dikembangkan secara terpisah dari penelitian ini. Aplikasi ini berfungsi sebagai platform pengisian feedback mahasiswa. (2) Aplikasi pendukung eksperimen adalah modifikasi dari SAPA yang mengintegrasikan fitur digital scaffolding sebagai ekstensi, dikembangkan khusus untuk keperluan eksperimen penelitian ini. (3) Pipeline digital scaffolding adalah komponen analitik yang memproses narasi feedback secara real-time untuk mendeteksi pemenuhan keempat indikator tekstual menggunakan pendekatan sentence embedding dan cosine similarity. (4) Rule-based system adalah mekanisme pengambilan keputusan berbasis tabel kondisional yang memetakan vektor hasil deteksi indikator ke dalam keputusan intervensi secara deterministik. (5) Template scaffolding adalah output batuan berupa teks prompt yang ditampilkan kepada mahasiswa ketika sistem mendeteksi satu atau lebih indikator yang belum terpenuhi.

**III.1 Penjelasan Penelitian**

Penelitian yang dilaksanakan menggunakan metode kuantitatif dengan desain posttest-only control group dan alokasi treatment-kontrol secara acak, sebagaimana didefinisikan pada subbab III.6.6.2A. Penelitian ini dilakukan selama periode Januari 2026 hingga Juni 2026. Waktu yang dialokasikan mencakup tahap perbandingan arsitektur NLP, pembuatan pipeline, integrasi sistem scaffolding ke dalam sistem existing, hingga pelaksanaan eksperimen pengujian langsung terhadap subjek penelitian, serta proses analisis hasil data statistik.

Sebagai panduan struktural, [Tabel III.1](#page-1-0) menyajikan pemetaan alur antara tahapan metodologi dengan RQ yang dijawab.

Tabel III.1. Pemetaan Tahapan Metodologi dengan RQ

Tahapan Metodologi  |  Tujuan  |  Menjawab
Pemodelan pipeline pada subbab III.6.3  |  Membangun mekanis deteksi 4  |  RQ 1
indikator tekstual.
Kalibrasi model pada subbab III.6.3  |  Menentukan threshold optimal deteksi  |  RQ 1
untuk eksperimen.
Perancangan eksperimen pada subbab  |  Mempersiapkan kondisi pengujian  |  RQ 2
III.6.6: kelompok treatment dan kontrol
Pengolahan data statistik pada subbab  |  Mengukur perbedaan signifikan  |  RQ 2
III.6.7: antarkelompok eksperimen.

Pendekatan kuantitatif eksperimental dengan desain post-test-only beserta kelompok kontrol dan treatment dipilih. Untuk merepresentasikan esensi penelitian secara matematis dan mendefinisikan batasan dari artefak yang diusulkan, sistem digital scaffolding dirancang secara hybrid, komponen NLP yang telah dijelaskan pada Lampiran 4 bertugas mengukur kualitas semantik teks narasi secara komputasional, sedangkan komponen rule-based yang telah didefinisikan pada subbab II.1.7 menentukan apakah kualitas tersebut melewati threshold atau memerlukan intervensi. Tiga komponen utama dalam arsitektur ini adalah sebagai berikut:

1. Rubrik (ℛ): Kumpulan kriteria evaluasi yang tidak dapat diubah dan telah ditetapkan sebelumnya oleh institusi, didefinisikan sebagai ℛ = , , … , .
2. Pertanyaan kuantitatif dan kualitatif feedback (): Instruksi yang dihasilkan dari rubrik, didefinisikan sebagai fungsi dari rubrik: = -ℛ.
3. Respons siswa (): Feedback, atau variabel yang dapat berubah, didefinisikan sebagai tuple yang terdiri dari skor numerik kuantitatif dan narasi teks kualitatif -, yang ditandai sebagai = -, . Di mana ∈ !, dengan ! merepresentasikan himpunan skala yang digunakan, yaitu 1,2,3,4,5, sementara adalah teks narasi berbahasa Indonesia. Feedback literacy  diimplementasikan melalui fungsi penilaian # yang memetakan satu instance feedback ke vektor empat indikator.

Korelasi dari ketiga komponen tersebut disajikan pada [Gambar III.1](#page-2-0) menggunakan rubrik pada Lampiran 10.

Gambar III.1. Korelasi Rubrik, Pertanyaan, dan Feedback

Untuk merepresentasikan sistem secara formal, penelitian ini menggunakan notasi matematis berikut. Rubrik direpresentasikan sebagai himpunan kriteria statis (ℛ). Pertanyaan assessment diturunkan dari rubrik (). Respons mahasiswa direpresentasikan sebagai pasangan skor numerik dan teks narasi (). Setiap respons dievaluasi oleh empat fungsi pengukur ( − &), masing-masing menghasilkan nilai dalam rentang [0,1] yang dibandingkan terhadap threshold similarity ('(),)) untuk memutuskan apakah intervensi diperlukan.

Seluruh simbol dan definisi operasional yang digunakan dalam sistem dan analisis statistik dirangkum dalam [Tabel III.2](#page-3-0).

Tabel III.2. Notasi Matematis yang Digunakan

Simbol  |  Domain  |  Deskripsi
$\mathcal R$  |  Himpunan  |  Kumpulan kriteria rubrik statis yang ditetapkan
institusi.
Q  |  Fungsi dari R  |  Pertanyaan assessment yang diturunkan dari rubrik.
F  |  Tuple $(s_{num}, s_{txt})$  |  Respons mahasiswa berupa skor dan narasi
feedback.
S  |  Himpunan  |  Skala rubrik yang digunakan, yaitu {1,2,3,4,5}.
Ф  |  Fungsi  |  Fungsi penilaian sistematis yang memetakan F ke
vektor indikator.
$f_i$  |  $F \rightarrow [0,1]$  |  Fungsi pengukur indikator kualitas ke-i
$\theta_{sim,i}$  |  Skalar [0,1]  |  Threshold similarity komputasional untuk indikator
ke i, dikalibrasi dari data historis.
$\theta_i$  |  Skalar [0,1]  |  Threshold keputusan intervensi untuk indikator ke-i,
dalam penelitian ini bernilai mutlak 1 untuk
memastikan pemenuhan indikator secara total.
$d_i$  |  {0,1}  |  Keputusan biner intervensi per indikator, dengan:
1. 0: Tidak membutuhkan intervensi.
62.124: 2. 1: Membutuhkan intervensi.
D  |  ${\{0,1\}^4}$  |  Ruang keputusan biner berdimensi empat, dengan
total 16 kombinasi. Merepresentasikan kombinasi
1(E)  |  D  |  hasil identifikasi indikator komputasi.
d(F)  |  D  |  Vektor keputusan aktual hasil evaluasi empat
11,: indikator pada <i>renspons</i> mahasiswa <i>F</i> .
$\mathcal{P}$  |  Himpunan  |  Kumpulan template conditional-prompt.
М  |  $D \longrightarrow \mathcal{P} \cup \{\emptyset\}$  |  Fungsi <i>rule-based</i> yang memetakan vektor
17  |  Tarala (ee  |  keputusan ke <i>template prompt</i> .
V  |  Tuple $(v_{komponen}, s_{num})$  |  Variabel kontekstual dinamis untuk pengisian
FE  |  E  |  template.
Fungsi: Hasil operasi untuk dekomposisi rubrik.
$T_{pillai}$  |  Skalar  |  Nilai statistik Pillai's Trace dari uji MANOVA.
$\delta_i$  |  Skalar  |  Nilai effect size Cohen's d untuk indikator ke-i.
$\alpha_{adj}$  |  Skalar (0,0125)  |  Signifikansi statistik dengan Bonferroni correction.

Alur arsitektur data bersifat searah, yaitu  $\mathcal{R} \to Q \to F$ , sejalan dengan ilustrasi yang telah disajikan pada Gambar III.1. Artefak digital scaffolding yang diusulkan beroperasi sepenuhnya dalam batas variabel F, sistem tidak mengubah, menghasilkan, atau memodifikasi parameter  $\mathcal{R}$  maupun Q untuk menjaga instrumen evaluasi feedback yang telah ditetapkan. Setiap  $instance\ feedback$  direpresentasikan sebagai pasangan dua modalitas.

**III.2 Variabel Penelitian**

Mengingat penelitian ini terdiri dari dua tahapan untuk menjawab dua RQ, variabel penelitian diklasifikasikan ke dalam dua kelompok, yaitu variabel untuk tahap kalibrasi komputasional dan variabel untuk tahap eksperimen lapangan.

**III.2.1 Variabel pada Tahap Kalibrasi**

Pada tahap ini, penelitian berfokus pada pencarian konfigurasi operasional yang optimal untuk mendeteksi keempat indikator tekstual pada narasi feedback, yaitu:

1. Variabel bebas (independent variable)

Variabel bebas pada tahap ini adalah konfigurasi pendekatan komputasional yang dimanipulasi dan dievaluasi kinerjanya, meliputi (1) jenis kandidat model sentence embedding, (2) metode pemrosesan yaitu whole-text embedding, ,semantic chunking, dan mutual exclusivity.

2. Variabel terikat (dependent variable)

Variabel terikat dalam tahap ini adalah tingkat kesesuaian prediksi pipeline komputasional terhadap data ground truth hasil anotasi manusia. Kinerja ini diukur menggunakan metrik performa kalibrasi, yaitu F1-Score, Precission, dan Recall.

**III.2.2 Variabel pada Tahap Eksperimen**

Variabel penelitian pada tahap eksperimen disusun berdasarkan konfigurasi pipeline evaluasi yang telah dikembangkan dan dikalibrasi pada RQ1. Dalam konteks eksperimen, pipeline berperan sebagai instrumen pengukuran untuk menghasilkan nilai keempat indikator tekstual yang selanjutnya digunakan sebagai variabel terikat pada analisis statistik:

1. Variabel bebas (independent variable)

Variabel bebas dalam penelitian adalah keberadaan intervensi digital scaffolding yang bersifat biner, yaitu aktif dan tidak aktif dalam skema kelompok treatment dan kontrol yang lebih lanjut dijelaskan pada Subbab III.6.6

2. Variabel terikat (*dependent variable*)

Variabel terikat dalam penelitian ini adalah kualitas narasi feedback yang diadaptasi berdasarkan Setiawan et al. (2026) yang mengoperasionalkannya menjadi indikator tekstual yang dapat diobservasi berdasarkan kerangka feedback literacy.

Tabel III.3. Operasionalisasi Kualitas Narasi Feedback (Setiawan et al., 2026)

Indikator: Definisi
Tingkat Cakupan Rubrik: Cakupan kriteria rubrik yang secara eksplisit tercakup dalam teks narasi feedback. Dalam kata lain, merupakan rasio kriteria yang terpenuhi terhadap total kriteria dalam rubrik.
Tingkat Koherensi Evaluatif: Keselarasan narasi feedback yang memiliki konsistensi dengan skor numerik.
Rasio Kedalaman Elaborasi: Jumlah kata yang terdapat dalam narasi feedback () dengan menghitung kata leksikal pada narasi feedback.
Rasio Relevansi Topik: Keselarasan konten teks yang relevan dengan kriteria rubrik ke konten tidak sesuai.

Setiap indikator diukur tingkat pemenuhannya terhadap narasi feedback yang dijawab oleh mahasiswa yang signifikansi perbedaannya diukur menggunakan prosedur statistik pada Subbab III.6.6.3B.

**III.3 Data Penelitian**

Data yang digunakan dalam penelitian ini dikategorikan ke dalam dua kelompok, yaitu: (1) data historis untuk pengembangan dan validasi pipeline , dan (2) data eksperimental sebagai perbandingan evaluasi perbedaan tingkat pemenuhan keempat indikator tekstual narasi feedback antara kelompok kontrol dan kelompok treatment yang menerima bantuan digital scaffolding. Kedua data penelitian didefinisikan pada subbab [III.3.1](#page-6-0) hingga [III.3.2](#page-8-0).

Penggunaan dataset dari Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung dipilih karena relevansi langsung dengan fenomena rendahnya feedback literacy yang telah diidentifikasi sebelumnya, serta untuk memastikan kontinuitas temuan dengan studi Setiawan (2026a) yang menggunakan konteks institusional serupa.

**III.3.1 Data Pengembangan dan Kalibrasi Pipeline Scaffolding**

Data pengembangan dan validasi pipeline berasal dari data historis yang telah dikumpulkan dalam mata kuliah yang menerapkan PjBL di Jurusan Teknik Komputer dan Informatika Politeknik Negeri Bandung pada tahun akademik 2025/2026. Data ini terdiri dari dua bagian, yaitu (1) data feedback yang didefinisikan pada subbab [III.3.1.1](#page-6-1) dan (2) data rubrik pada subbab [III.3.1.2](#page-8-1). Rubrik yang digunakan pada data ini telah didefinisikan pada Lampiran 10.

Dalam konteks text classification pada machine learning, setiap instance data direpresentasikan sebagai satu objek analisis yang memiliki fitur dan label target (Manning et al., 2009). Dalam penelitian ini, satu objek analisis adalah satu pasangan narasi feedback dengan kriteria rubrik. Fitur dari objek ini adalah representasi semantik teks dalam ruang vektor yang dihasilkan oleh model sentence embedding yang telah dijelaskan pada Lampiran 4. Label yang diprediksikan adalah keputusan biner TRUE/FALSE yang menyatakan apakah narasi tersebut diindikasikan membahas aspek rubrik. Skema ini mengikuti paradigma multi-label binary classification di mana satu objek dapat memiliki lebih dari satu label (Tsoumakas & Katakis, 2009), mengingat satu narasi feedback dapat memenuhi atau tidak memenuhi beberapa kriteria feedback literacy secara simultan dan independen satu sama lain.

**III.3.1.1 Data Narasi Feedback**

Bagian pertama dari data pengembangan adalah data feedback. Data ini merupakan hasil self dan peer assessment dengan populasi data sebanyak 10.098 baris yang dihasilkan oleh mahasiswa jenjang D3 pada pertengahan dan akhir semester pada mata kuliah "Proyek 1: Pemanfaatan Aplikasi Perkantoran", mencakup 8.118 peer assessment dan 1.980 self assessment.

Dari jumlah populasi tersebut, diambil sampel berupa 384 baris data untuk diberi anotasi secara manual. Volume data ini ditentukan menggunakan formula Cochran dengan tingkat confidence 95% (z = 1,96), margin of error sebesar 5% (e = 0,05), serta proporsi populasi () ditetapkan sebesar 0,5 untuk memaksimalkan ukuran sampel dalam kondisi varians yang tidak diketahui. Perhitungan dilakukan menggunakan rumus [III.1.](#page-7-0)

$$n_0 = \frac{z^2 \cdot p \cdot (1-p)}{e^2} \tag{III.1}$$

Parameter yang digunakan dalam formula dipertimbangkan untuk hal berikut confidence 95% dipilih sebagai standar minimum yang diterima. Margin of error tujuan anotasi adalah menghasilkan estimasi distribusi feedback literacy yang representatif.

Perhitungan komputasional menggunakan parameter tersebut menghasilkan nilai estimasi <sup>C</sup> = 384,16. Sesuai dengan konversi standar dalam statistik terapan, jumlah sampel final yang ditarik untuk anotasi ditetapkan sebanyak = 384 narasi. Jumlah ini merupakan batas kecukupan statistik untuk mencapai margin of error 5%, sehingga menjamin reliabilitas estimasi distribusi tanpa bergantung pada asumsi varians awal. Untuk memastikan seluruh karakteristik data terwakili secara proporsional, penarikan sampel dilakukan secara acak dari total populasi historis.

Data ini digunakan mengevaluasi arsitektur pipeline pada tahap pengembangan, dengan memuat komponen penilaian kuantitatif dan kualitatif mahasiswa. Struktur data self dan peer assessment yang digunakan disajikan selengkapnya pada Lampiran 5.

Sebagaimana disajikan pada Lampiran 5, data peer assessment memiliki atribut class\_id, assesor\_id, group\_id, assessee\_id, timepoint, indicator, question, peer\_score, dan peer\_comment. Data self assessment menggunakan struktur serupa dengan atribut self\_score menggantikan peer\_score. Data rubrik memuat aspek penilaian, kriteria, pertanyaan kuantitatif dan kualitatif, serta deskriptor untuk setiap skala penilaian.

**III.3.1.2 Data Rubrik**

Bagian kedua dari data pengembangan adalah data rubrik. Data ini mencakup aspek penilaian, kriteria, serta hubungan dengan skor yang digunakan sebagai dasar pertanyaan kuantitatif dan kualitatif pada instrumen assessment. Detail struktur data rubrik yang digunakan disajikan secara lengkap pada Lampiran 5.

Data dikumpulkan secara resmi oleh pihak pengajar PjBL melalui google form sebagai instrumen self dan peer assessment yang telah digunakan sebagai komponen pembelajaran.

**III.3.2 Data Evaluasi Scaffolding**

Data evaluasi adalah data primer yang dikumpulkan dari subjek penelitian dengan menggunakan sistem digital scaffolding, didefinisikan pada subbab [III.3.2.1](#page-9-0) dan menghasilkan data interaksi sebagai ekstensi, sebagaimana didefinisikan pada subbab [III.3.2.2](#page-9-1).

Data evaluasi dikumpulkan menggunakan metode post-test only, yaitu data dikumpulkan hanya pada satu sesi yang sama. Detail desain eksperimen dijabarkan pada subbab III.6.6.2A. Data tersebut didapatkan dari dua kelompok eksperimen, yaitu (1) kelompok treatment yang mengisi feedback dengan scaffolding aktif, dan (2) kelompok kontrol yang mengisi feedback tanpa scaffolding. Secara operasional, kelompok treatment menerima bantuan scaffolding secara real-time selama proses penulisan narasi feedback berlangsung, sedangkan kelompok kontrol menyelesaikan penulisan tanpa intervensi scaffolding apapun. Setelah seluruh jawaban tersebut dianalisis menggunakan pipeline digital scaffolding yang sama untuk menghasilkan skor pemenuhan keempat indikator tekstual narasi feedback. Hasil analisis inilah yang digunakan sebagai data perbandingan antara kelompok kontrol dan treatment. [Gambar III.2](#page-9-2) menyajikan ilustrasi pemetaan intervensi digital scaffolding pada kedua kelompok subjek eksperimen.

Gambar III.2. Pemetaan Scaffolding pada Kelompok Eksperimen

**III.3.2.1 Data Evaluasi**

Merupakan data yang berfungsi untuk mengukur kemampuan scaffolding yang didasarkan pada besar pengaruh (effect size) dan nilai signifikansi Pillai's Trace dari MANOVA. Data akhir ini lebih lanjut akan digunakan pada tahapan III.6.6.3B.

**III.3.2.2 Data Interaksi**

Merupakan data interaksi mahasiswa kelompok treatment yang menerima scaffolding. Setiap narasi feedback yang ditulis mahasiswa dan respon/output dari pipeline digital scaffolding akan dicatat. Data akhir ini lebih lanjut akan digunakan pada tahapan III.6.6.3C.

**III.3.2.3 Data Kuesioner**

Merupakan data respon kuesioner yang didapatkan dari kelompok treatment yang telah menerima bantuan scaffolding saat sesi perancangan skenario eksperimen. Data ini lebih lanjut didapatkan dan dirancang pada tahapan III.6.6.1C.

**III.4 Objek Penelitian**

Dalam penelitian ini, objek penelitian terbagi menjadi dua kelompok, yaitu objek material dan fungsional yang disajikan pada subbab [III.4.1](#page-10-0) hingga [III.4.2](#page-11-0).

**III.4.1 Objek Material**

Objek material penelitian adalah teks narasi dan skor numerik hasil self dan peer assessment berbahasa Indonesia dalam konteks PjBL. Data ini merepresentasikan output feedback literacy mahasiswa yang dapat diamati sebagai target intervensi pipeline NLP.

Unit analisis ditetapkan pada level mahasiswa sebagai penulis feedback atau assessor. Hasil komputasi empat indikator yang telah didefinisikan pada [Tabel III.3](#page-5-0) diagregasi menjadi vektor indikator individu. Agregasi ini menjaga independensi observasi dalam analisis statistik. [Gambar III.3](#page-10-1) menyajikan visualisasi terhadap pemetaan unit analisis, objek material, dan agregasi vektor indikator individu.

Gambar III.3. Pemetaan Unit Analisis, Objek Material, dan Vektor Indikator

Keputusan untuk mengagregasi komputasi empat indikator ke level individu mahasiswa sebagai unit analisis didasarkan pada dua pertimbangan. Pertama, analisis pada level untuk setiap pertanyaan akan menghasilkan observasi yang tidak independen. Hal tersebut disebabkan karena satu mahasiswa dapat menghasilkan beberapa feedback dalam peer assessment untuk setiap rekan sejawat (assessee). Kedua, unit analisis yang relevan adalah mahasiswa sebagai individu, bukan pertanyaan sebagai unit. Keputusan tersebut didasarkan oleh intervensi scaffolding yang dirancang untuk mempengaruhi perilaku penulisan mahasiswa secara keseluruhan, dengan konsekuensi bahwa variasi antar-pertanyaan dalam satu mahasiswa tidak dianalisis secara terpisah.

**III.4.2 Objek Fungsional**

Objek fungsional dalam penelitian ini adalah arsitektur pipeline digital scaffolding pada pengisian self dan peer assessment. Objek dipilih karena sistem evaluasi otomatis konvensional beroperasi secara sumatif tidak bisa memberikan intervensi real-time ketika penulisan feedback berlangsung, yang telah dijelaskan pada subbab I.2. Arsitektur yang diusulkan memastikan intervensi tidak hanya akurat secara semantik tetapi juga dikontrol melalui rule-based.

**III.5 Perangkat Pendukung**

Penelitian ini memanfaatkan berbagai alat, teknologi, dan library untuk mendukung dua tahapan utama, yaitu eksperimen dalam pemodelan NLP dan pengembangan pipeline digital scaffolding. Dengan rincian pada [Tabel III.4](#page-11-1).

Tabel III.4. Perangkat Pendukung

Teknologi  |  Versi  |  Fungsi
Python  |  3.10  |  Bahasa pemrograman utama yang digunakan untuk memproses data
teks, mengeksekusi model NLP, serta melakukan perhitungan untuk
mengevaluasi model.
FastAPI  |  0.x  |  Framework web Python yang memiliki performa tinggi untuk
membangun endpoint dari sistem digital scaffolding.
Vue.js&  |  3.x  |  Framework frontend yang dikombinasikan dengan Inertia.js untuk
Inertia.js: membangun antarmuka digital scaffolding.
Laravel  |  10.x  |  Framework yang digunakan untuk mengelola antarmuka bisnis self dan
peer assessment.
Tailwind CSS  |  3.x  |  Framework CSS utility-first untuk merancang antarmuka pengguna.
Sentence  |  2.x  |  Library utama yang digunakan untuk mengunduh, memuat, dan
Transformer: mengeksekusi model NLP, serta mengekstraksi representasi numerik
+ PyTorch: (embedding) dari teks mahasiswa berbahasa Indonesia untuk keperluan
pengukuran kesamaan semantik.
ChromaDB  |  -  |  Vector database yang digunakan secara spesifik untuk menyimpan dan
melakukan komputasi pencarian kedekatan vektor antar teks
mahasiswa dengan rubrik evaluasi.
Google  |  -  |  Generative AI Service yang digunakan untuk proses dekomposisi
Gemini API: rubrik sebagai bagian dari APE SAPA.

Teknologi  |  Versi  |  Fungsi
Scikit-learn  |  1.3.x  |  Library yang digunakan untuk menghitung kesamaan kosinus antar
vektor rubrik dan teks mahasiswa, serta untuk menghasilkan metrik
performa model.
Pandas+  |  -  |  Library yang digunakan untuk membersihkan serta memproses data
NumPy: mentah.
Google Colab  |  -  |  Digunakan untuk mempercepat proses benchmarking model melalui
atau Kaggle: cloud dengan memanfaatkan GPU seperti NVIDIA T4 atau P100.
notebook
Microsoft  |  -  |  Alat bantu untuk melakukan anotasi manual terhadap dataset, sesuai
Excel atau: dengan rubrik yang telah ditentukan sebelum proses evaluasi
Google: dilakukan.
Spreadsheet
Aplikasi  |  -  |  Lingkungan eksperimen yang merupakan aplikasi internal yang sudah
SAPA: dikembangkan sebelumnya dan terpisah dari penelitian ini. Integrasi
sistem scaffolding ke dalam aplikasi dilakukan atas persetujuan
pengembang aplikasi sebagai fitur tambahan yang diaktifkan secara
selektif berdasarkan kelompok eksperimen.

**III.6 Tahapan Pelaksanaan Penelitian**

Subbab ini membahas tahapan yang dilakukan selama penelitian untuk menjawab kedua pertanyaan penelitian. Secara keseluruhan tahapan terbagi menjadi tahapan yang berfokus pada RQ 1, yaitu perancangan, implementasi, dan evaluasi pipeline digital scaffolding untuk mendeteksi empat indikator tekstual narasi feedback. Pipeline digital scaffolding yang dihasilkan, kemudian digunakan sebagai mekanisme intervensi sekaligus instrumen pengukuran pada tahap kedua untuk menjawab RQ 2, yaitu mengevaluasi bagaimana tingkat pemenuhan keempat indikator tekstual narasi feedback melalui desain eksperimen yang dirancang. Tahapan pelaksanaan penelitian pada [Gambar III.4](#page-13-0) dirancang secara sistematis agar setiap tahap saling mendukung dan menghasilkan output yang dapat digunakan untuk menjawab permasalahan penelitian.

Gambar III.4. Tahapan Pelaksanaan Penelitian

**III.6.1 Identifikasi Masalah dan Studi Pendahuluan**

Tahap ini bertujuan memperoleh pemahaman awal mengenai karakteristik permasalahan yang menjadi dasar perancangan digital scaffolding. Kegiatan dilakukan melalui dua proses yang saling melengkapi, yaitu analisis konseptual terhadap karakteristik objek penelitian dan analisis empiris terhadap data historis self dan peer assessment. Data historis yang digunakan berasal dari 95 mahasiswa pada mata kuliah Proyek 1: Pemanfaatan Aplikasi Perkantoran yang dilaksanakan pada rentang Agustus-Desember 2024 sebagaimana dijelaskan pada III.3.1.

Hasil dari tahap ini digunakan sebagai dasar dalam merumuskan kebutuhan sistem, menentukan pendekatan komputasional yang sesuai, serta menyusun spesifikasi pipeline yang akan dikembangkan. Seluruh hasil analisis dipaparkan pada Lampiran 6.

**III.6.1.1 Identifikasi Karakteristik Indikator Tekstual Narasi**

Analisis konseptual dilakukan untuk mengidentifikasi karakteristik objek penelitian sebelum sistem dikembangkan. Analisis berfokus pada dua aspek.

Pertama, mengidentifikasi karakteristik narasi feedback sebagai objek pemrosesan bahasa alami berdasarkan teori feedback literacy Carless & Boud (2018), beserta karakteristik data tekstual yang digunakan dalam penelitian.

Kedua, karakteristik tekstual pada data historis yang dimiliki berdasarkan keempat indikator tekstual narasi feedback (Camarata & Slieman, 2020; Curtis et al., 2024; Sun et al., 2023; Zhang & Schunn, 2023). Analisis ini digunakan untuk memahami jenis penalaran yang diperlukan pada masing-masing indikator serta menjadi dasar dalam menentukan pendekatan komputasional yang sesuai.

**III.6.1.2 Kuantifikasi Skala Masalah dam Urgensi Intervensi**

Analisis empiris dilakukan menggunakan korpus historis sebanyak 10.098 narasi feedback yang terdiri atas 8.118 peer assessment dan 1.980 self assessment.

Analisis bertujuan mengidentifikasi pola aktual penulisan feedback mahasiswa sebagai dasar perumusan kebutuhan sistem.

Analisis dilakukan menggunakan pendekatan Exploratory Data Analysis (EDA) dan statistik deskriptif terhadap karakteristik narasi, distribusi skor, panjang teks, hubungan antara skor dan narasi, serta berbagai pola yang berkaitan dengan keempat indikator tekstual yang digunakan dalam penelitian. Selain analisis kuantitatif, dilakukan pula penelaahan terhadap contoh-contoh narasi untuk mengidentifikasi bentuk penyimpangan yang muncul pada masing-masing indikator.

**III.6.2 Studi Literatur dan Pendefinisian Objektif Solusi**

Tahap ini bertujuan untuk menerjemahkan masalah empiris yang telah dipaparkan pada tahap studi pendahuluan menjadi spesifikasi teknis formal yang dapat dioperasionalkan sebagai instrumen komputasi. Kajian literatur difokuskan secara terpadu pada tiga domain teoritis dengan output komponen desain sistem yang spesifik, sebagaimana diilustrasikan pada [Gambar III.5.](#page-0-0)

Gambar III.5. Peta Sintesis Studi Literatur

Pertama, domain teori pedagogi untuk menelaah kerangka kerja feedback literacy  (Tai et al., 2018), aspek evaluative judgement (Tai et al., 2018), serta hambatan sosiopragmatis dalam interaksi sosiokultural kolektivistik (Brown & Levinson, 1987; Setiawan, 2026a). Output dari domain ini adalah batasan konseptual untuk mengisolasi parameter indikator kualitas tertulis dari proses kognitif internal, yang menghasilkan pendefinisian empat kriteria manifestasi tekstual evaluative expression terbatas yang dapat diobservasi tanpa memerlukan interpretasi manusia.

Kedua, domain NLP untuk menelaah arsitektur artificial neural network Transformer, pemodelan sentence embedding berbasis pendekatan bi-encoder (Reimers & Gurevych, 2019) serta metrik eksploitasi ruang vektor melalui cosine similarity. Output dari domain ini adalah kodifikasi dan transformasi empat indikator tekstual narasi feedback menjadi fungsi matematis kontinu yang dapat dihitung secara real-time.

Ketiga, domain rule based untuk menelaah penggunaan kondisional decision table (Negnevitsky, 2005) serta metode template-based natural language generation (Deemter et al., 2005). Keluaran dari domain ini adalah spesifikasi pemetaan biner antar-indikator dan perancangan struktural sentence frames yang berfungsi mereduksi tahapan generatif penulisan sesuai prinsip kontingensi scaffolding.

Sintesis dari ketiga domain literatur tersebut dirumuskan menjadi batasan operasional dan objektif solusi. Dokumentasi menjadi landasan formal bagi pemodelan pipeline NLP, perancangan basis data, dan implementasi komponen digital scaffolding pada aplikasi pendukung eksperimen.

**III.6.3 Pemodelan Konfigurasi Pipeline**

Tahapan ini bertujuan untuk memodelkan konfigurasi model NLP yang digunakan untuk komputasi indikator tekstual narasi pada sistem digital scaffolding, mencakup formulasi pada subbab [III.6.3.1](#page-2-0), proses anotasi dataset yang didefinisikan pada subbab [III.6.3.1](#page-4-0), serta evaluasi dan kalibrasi model pada subbab III.6.3.4.

**III.6.3.1 Formulasi Sistem dan Pengukuran**

Empat indikator yang didefinisikan pada Tabel III.3 dievaluasi melalui fungsi penilaian Φ yang memetakan feedback mahasiswa ke dalam empat komponen komputasi sesuai dengan rumus [III.2](#page-2-1).

$$\Phi(F) = [f_1(F), f_2(F), f_3(F), f_4(F)]$$
 (III.2)

Di mana mengukur cakupan rubrik, mengukur koherensi skor dan naratif, <sup>I</sup> mengukur kedalaman elaborasi, dan & mengukur relevansi topik, dengan ) : → ,0,1- untuk setiap K ∈ 1,2,3,4. Dengan kata lain, sistem menghasilkan empat nilai dalam satu respons mahasiswa untuk setiap indikator dengan masing-masing dalam rentang 0 hingga 1. [Gambar III.6](#page-2-2) menyajikan ilustrasi pemetaan feedback kepada keempat indikator komputasi.

Gambar III.6. Pemetaan Feedback kepada Indikator Komputasi

Sistem menetapkan vektor threshold '() = L'(),, '(),, '(),I, '(),&M di mana setiap '(),) dikalibrasi dari distribusi data historis sebagai threshold komputasi pemenuhan indikator, dan ' = ,', ', 'I'&- yang masing-masing bernilai 1 sebagai threshold keputusan intervensi scaffolding. Keputusan intervensi per indikator didefinisikan pada rumus III.3.

$$d_i(F) = \begin{cases} 1 \ jika \ f_i(F) < \theta_i \\ 0 \ sebaliknya \end{cases}, i \in \{1,2,3,4\}$$
 (III.3)

Dengan kata lain, sistem memberikan nilai 1, merepresentasikan bahwa intervensi diperlukan pada indikator ke-i apabila hasil komputasi pemenuhan indikator ke-i berada di bawah threshold  $\theta$ , dan nilai 0 apabila indikator telah terpenuhi sehingga tidak membutuhkan intervensi. Gambar III.7 menyajikan alur feedback ditransformasi menjadi  $f_i$  sebelum dilakukan komputasi keputusan intervensi pada  $d_i$  dalam rumus III.3.

Gambar III.7. Alur Komputasi Indikator dan Keputusan Intervensi

Tujuan dari penelitian ini adalah merancang intervensi rule-based digital scaffolding yang mengevaluasi feedback (F) secara real-time. Jika fungsi mendeteksi rendahnya feedback literacy yang didefinisikan pada rumus III.4, sistem memicu prompt (P) berbasis rule-based dan adaptif pada antarmuka yang telah dijelaskan pada subbab II.1.7.

$$If \exists i: d_i(F) = 1 \to P \tag{III.4}$$

Fungsi pengambilan keputusan intervensi direpresentasikan melalui fungsi aturan  $M:\{0,1\}^4 \to \mathcal{P} \cup \{\emptyset\}$ , yang memetakan 16 kemungkinan kombinasi vektor keputusan biner ke dalam himpunan template prompt  $\mathcal{P}$  yang selaras. Untuk memberikan gambaran operasional mengenai alur transformasi data dari nilai kontinu hasil pemrosesan NLP hingga menjadi keputusan intervensi, Tabel III.5 menyajikan simulasi data pada beberapa kondisi respons mahasiswa.

Tabel III.5. Simulasi Alur Data dan Keputusan Intervensi Sistem

Tahapan Evaluasi Komputasional  |  Kasus Simulasi A (Kondisi Melanggar)  |  Kasus Simulasi B (Kondisi Ideal)
1. Input Feedback (F)  |  Skor: 3  |  Skor: 5
Narasi: "Bagus": Narasi: "Rekan saya
_: mengumpulkan banyak sekali
iklan dari berbagai platform,
dan semua iklannya sangat
relevan tanpa ada kendala
sama sekali. Dia langsung
mengerjakan dengan sangat
mudah"
2. Vektor Indikator kualitas  |  $[f_1 = 0.20, f_2 = 0, f_3 =$  |  $[f_1 = 1.00, f_2 = 1, f_3 =$
$(\Phi(F) = [f_1, f_2, f_3, f_4])$  |  $1, f_4 = 0$  |  $[0, f_4 = 1]$
3. Vektor <i>Threshold</i>  |  $[\theta_1, \theta_2]$  |  $[\theta_3, \theta_4]$
4. Vektor Keputusan Biner  |  $[d_1 = 1, d_2 = 1, d_3 =$  |  $[d_1 = 0, d_2 = 0, d_3 =$
$d(F) = [d_1, d_2, d_3, d_4]$  |  $[1.d_4 = 1]$  |  $0, d_4 = 0]$
(Terjadi Pelanggaran): (Memenuhi Seluruh
Indikator)
5. Aksi Sistem: Memicu Template Prompt
6. Output Antarmuka  |  Menampilkan teks panduan  |  adaptif ataupun fading sesuai
dengan template prompt.

Melalui mekanisme sekuensial yang digambarkan pada Tabel III.5, tujuan komputasi utama untuk melakukan intervensi kontingensi selama fase penulisan aktif dapat berjalan selama real-time, mengarahkan mahasiswa untuk merevisi narasinya hingga kondisi kriteria  $\forall i: f_i(F) \geq \theta_i$  terpenuhi secara mutlak.

III.6.3.2 Anotasi Dataset

Tahap ini bertujuan untuk menghasilkan ground truth yang menjadi dasar objektif bagi seluruh evaluasi pipeline. Pipeline NLP yang dirancang menggunakan pendekatan komputasional yang telah didefinisikan pada Lampiran 4, bahwa tidak ada model yang dilakukan training. Namun, evaluasi performa pipeline tetap memerlukan ground truth dari dataset yang telah dianotasi untuk mengukur

kesesuaian antara RQ . Anotasi juga diperlukan untuk kalibrasi threshold untuk menentukan nilai cosine similarity yang mengindikasikan bahwa sebuah narasi memenuhi atau tidak memenuhi indikator tersebut ('(),)). Sementara itu, indikator kedalaman elaborasi diimplementasi secara langsung menggunakan threshold heuristik jumlah kata, sehingga tidak membutuhkan anotasi. [Gambar III.8](#page-5-0) menyajikan pemetaan dataset tersebut untuk menghasilkan threshold komputasi indikator ('(),)).

Gambar III.8. Pemetaan Dataset untuk Evaluasi

Dari total populasi 10.098 baris data feedback historis, proses anotasi dilakukan terhadap sampel sebanyak 384 data. Jumlah sampel ini dihitung dan dijelaskan representasinya menggunakan Cochran formula pada rumus III.1 sebagaimana dijelaskan pada subbab III.3.1. Formulasi ini direpresentasikan sebagai standar metodologis yang teruji untuk penelitian cross sectional design populasi berskala besar (COCHRAN, 1977). Pada domain riset software engineering, formula Cochran secara empiris telah diaplikasikan untuk menentukan ukuran sampel minimum yang representatif dari populasi terbatas (Zul et al., 2024), serta digunakan secara aktif untuk mereduksi volume dataset teks berskala besar menjadi sampel representatif sebelum tahapan anotasi atau ekstraksi fitur berbasis Natural Language Processing (Ghali et al., 2025).

Pengambilan sampel dilakukan secara acak berdasarkan semester dilaksanakannya assessment untuk memastikan representasi proporsional dari seluruh subkelompok populasi, sehingga dataset tidak didominasi oleh satu class atau satu periode semester pembelajaran tertentu. Selanjutnya, untuk memastikan ecological validity dari dataset (Lücking et al., 2022), distribusi sampel dievaluasi dengan cara menghitung proporsi narasi yang tidak memenuhi empat indikator tekstual narasi feedback. Evaluasi distribusi ini dilakukan di awal untuk memverifikasi bahwa sampel secara akurat merepresentasikan fenomena tekstual aktual di dunia nyata sebelum proses pelabelan dilanjutkan.

**A. Dekomposisi Rubrik sebagai Pre Processing**

Penelitian ini tidak menerapkan tahapan data cleaning seperti stemming, lowercasing, atau penghapusan tanda baca pada narasi feedback mahasiswa. Pendekatan ini merupakan keputusan untuk menjaga ecological validity. Teks dipertahankan dalam bentuk mentah sebagaimana adanya untuk merepresentasikan kondisi lingkungan dunia nyata, sehingga performa model yang dievaluasi benarbenar merepresentasikan keandalannya saat beroperasi secara real-time.

Oleh karena itu, tahapan pre-processing dalam penelitian ini dekomposisi rubrik sebagai feature extraction dengan memecah unit-unit kriteria atomik rubrik. Pemisahan ini merupakan pre-requirement agar model embedding dapat melakukan komputasi kesamaan semantik antara narasi mahasiswa terhadap satu dimensi evaluasi spesifik tanpa bias dari informasi yang overlapping, hal ini didasari pada subbab II.1.8.1. [Gambar III.9](#page-7-0) menyajikan visualisasi pemetaan dekomposisi rubrik terhadap dataset anotasi.

Gambar III.9. Pemetaan Dekomposisi Rubrik pada Anotasi Dataset

Dekomposisi rubrik mengubah bentuk rubrik holistik menjadi unit-unit atomik diskrit yang dapat diproses secara independen oleh pipeline NLP, sebagaimana dijelaskan oleh subbab II.1.8.1.

Secara formal, rubrik dianotasikan sebagai ℛ yang memiliki satu atau lebih aspek (#) ), sebagaimana dinyatakan pada rumus [III.5.](#page-7-1)

$$\mathcal{R} = \{A_1, A_2, \dots, A_n\}$$
 (III.5)

Di mana K ∈ 1,2, … , . Sebagai contoh, beberapa aspek dalam rubrik yang didefinisikan pada Lampiran 10 adalah "Manajemen Waktu" dan "Kontribusi dalam Kelompok".

Setiap aspek (#) ) memiliki satu atau lebih kriteria penilaian (\),A), sebagaimana direpresentasikan dalam rumus [III.6.](#page-7-2)

$$A_i = \{ K_{i,1}, K_{i,2}, \dots, K_{i,m} \}$$
 (III.6)

Dengan i merupakan aspek ke-i, dan ] ∈ 1,2, . . , . Sebagai contoh, aspek "Pembuatan Struktur Data" dalam rubrik pada Lampiran 10, memiliki kriteria "Banyaknya iklan dan keragaman platform yang digunakan."

Dalam rubrik penilaian, setiap kriteria (\),A) memiliki komponen tingkat skor (<sup>6</sup> ∈ !), dengan P merupakan deret nilai yang memetakan rentang penilaian, contohnya P = 1,2,3,4,5. Komponen skor tersebut dihubungkan dengan deskripsi performa spesifik (\),A,(^ ), sebagaimana direpresentasikan pada rumus [III.7](#page-8-0).

$$K_{i,j} = \{K_{i,j,s_1}, K_{i,j,s_2}, \dots, K_{i,j,s_n}\}$$
 (III.7)

Dari setiap kriteria \),A, dihasilkan dua feature set yang melayani indikator berbeda, ditetapkan dengan notasi pada rumus [III.8.](#page-8-1)

$$FE(K_{i,j}) = (COV(K_{i,j}), COH(K_{i,j}))$$
 ( III.8)

Di mana de4b\),Ac merupakan feature set untuk indikator cakupan () dan relevansi topik (&), didefinisikan pada subbab [III.6.3.2.](#page-4-2)[A.](#page-6-0)[1](#page-8-2). Di sisi lain, def-\),A merupakan feature set untuk indikator koherensi skor narasi () yang didefinisikan pada subbab [III.6.3.2.](#page-4-2)[A.](#page-6-0)[2](#page-9-0).

**1. Cakupan dan Relevansi Feature-Set**

Feature set ini merepresentasikan seluruh dimensi substantif yang seharusnya hadir dalam narasi feedback, didefinisikan pada rumus [III.9](#page-8-3).

$$COV(K_{i,j}) = \{c_{cov,1}, c_{cov,2}, \dots, c_{cov,n}\}$$
 (III.9)

Di mana setiap g7h, merupakan satu unit teks yang merepresentasikan satu dimensi evaluatif dari kriteria ke-O pada aspek ke-K. Unit teks tersebut diturunkan dari tiga sumber, yaitu: (1) deskripsi performa spesifik dari setiap skor (\),A,(^ ), (2) pertanyaan kuantitatif, dan (3) pertanyaan kualitatif. Dengan komponen pertanyaan kuantitatif dan kualitatif hanya digunakan jika terdapat komponen penilaian yang tidak disebutkan dalam deskripsi performa spesifik (\),A,(^ ).

Ketiga sumber tersebut dilebur menjadi satu kumpulan kriteria atomik karena ketiganya merepresentasikan dimensi yang seharusnya terdapat dalam narasi feedback. Contoh proses dekomposisi untuk feature set ini disajikan pada [Tabel](#page-9-1)  [III.6](#page-9-1) dengan menggunakan rubrik pada Lampiran 10 untuk aspek "Pengumpulan iklan lowongan kerja".

Tabel III.6 Contoh Proses Dekomposisi Cakupan dan Relevansi Topik

Sumber  |  Isi Konten Asli  |  Kriteria yang diekstraksi
Deskripsi  |  Mengumpulkan sedikit iklan.  |  "jumlah iklan"
performa skor 1
(\),A,(_ )
Deskripsi  |  Mengumpulkan cukup iklan.  |  "jumlah iklan"
performa skor 3
(\),A,(i )
Deskripsi  |  Mengumpulkan banyak dan relevan dari  |  "jumlah iklan", "keragaman
performa skor 5  |  platform yang bervariasi.  |  platform", "relevansi iklan yang
(\),A,(j ): dikumpulkan"
Pertanyaan  |  Seberapa baik rekan Anda dalam  |  -
Kualitatif: mengumpulkan iklan lowongan kerja
dari platform yang ditugaskan? (Nilai
dari skala 1-5)
Pertanyaan  |  Mengapa?  |  "kesulitan dalam pengumpulan
Kuantitatif  |  (Berikan contoh spesifik kontribusi  |  data", "kemudahan dalam
rekan Anda dalam pengumpulan data.: pengumpulam data"
Apakah rekan Anda menghadapi
kesulitan dalam mengumpulkan iklan)

**2. Koherensi Feature-Set**

Untuk mengukur koherensi antara narasi dengan skor yang diberikan, sistem harus mengekstrak deskripsi performa spesifik (\),A,(^ ) menjadi unit-unit kriteria evaluasi yang lebih atomik. Proses ini dilakukan secara manual untuk setiap tingkat skor (<sup>6</sup> ∈ !), menghasilkan notasi pada rumus [III.10](#page-9-2).

$$COH(K_{i,j,s_k}) = \{ c_{coh,1}, c_{coh,2}, \dots, c_{coh,q} \}$$
 (III.10)

Di mana setiap g7k,m merupakan unit teks yang telah didekomposisi untuk kriteria ke-j, aspek ke-K untuk skor ke-P.

[Tabel III.7](#page-10-0) menyajikan contoh proses dekomposisi dengan menggunakan rubrik pada Lampiran 10, pada aspek "Pengumpulan iklan lowongan kerja" (#), dengan pasangan kriteria rubrik "Banyaknya iklan dan keragaman platform yang digunakan" (\,).

Tabel III.7. Contoh Proses Dekomposisi untuk Koherensi Skor dan Narasi

Skala Skor: Dekomposisi
Skor 1 (Sangat Kurang): defb\,,(_ c =
"]Fop]pSPQ FKPKq KPSQ"
Skor 3 (Cukup): defb\,,(i c =
"]Fop]pSPQ pPp KPSQ"
Skor 5 (Sangat Baik): defb\,,(j c =
"]Fop]pSPQ RQTQP KPSQ",
"KPSQ rFSF5Q",
"SQqsr] RFr5QrKQK"

Seluruh unit dekomposisi kemudian digabungkan menjadi satu himpunan besar, sebagaimana direpresentasikan pada rumus [III.11.](#page-10-1)

$$\mathcal{U}(K_{i,j}) = \bigcup_{s_k \in S} COH(K_{i,j,s_k})$$
 (III.11)

Sehingga t-\),A berisi: "iklan relevan", "platform bervariasi", "mengumpulkan banyak iklan", "mengumpulkan cukup iklan", dan "mengumpulkan sedikit iklan".

[Gambar III.10](#page-10-2) mengilustrasikan alur dekomposisi feature-set ini sesuai dengan rumus yang didefinisikan.

Gambar III.10. Alur Dekomposisi Koherensi Feature-set

**B. Pembuatan Panduan Anotasi**

Setiap baris data yang dianotasi merepresentasikan satu pasangan antara narasi feedback dan satu aspek rubrik tertentu. Skema ini mengadopsi multi-label binary classification yang dijelaskan pada Lampiran 4, di mana anotator memberikan label TRUE atau FALSE untuk setiap kriteria berdasarkan aspek yang sedang dievaluasi. Label TRUE diberikan apabila narasi secara eksplisit membahas atau mengindikasikan pemenuhan kriteria pada aspek target tersebut, sedangkan label FALSE diberikan apabila aspek tersebut tidak dibahas dalam narasi feedback. Dalam kerangka ini, coverage dievaluasi secara lokal pada masing-masing aspek rubrik, sehingga hanya menilai apakah aspek spesifik yang menjadi target muncul dalam narasi. [Gambar III.11](#page-11-0) menyajikan alur anotasi dataset untuk cakupan rubrik.

Gambar III.11. Alur Anotasi Dataset Cakupan Rubrik

Relevansi memiliki fungsi yang berbeda dari cakupan. Jika narasi membahas aspek rubrik lain di luar aspek target, maka aspek target tetap diberi label FALSE untuk cakupan, tetapi kondisi tersebut juga menandakan deviasi relevansi secara global karena perhatian mahasiswa bergeser ke dimensi evaluasi yang tidak sedang dinilai. Alur anotasi disajikan pada [Gambar III.12](#page-12-0). Dengan demikian, cakupan mengukur keberadaan konten yang sesuai pada aspek spesifik, sementara relevansi mengevaluasi kesesuaian fokus narasi terhadap ruang lingkup pertanyaan atau aspek yang seharusnya dibahas. Distingsi ini memungkinkan sistem membedakan antara ketiadaan informasi, kekurangan fokus, dan penyimpangan topik secara lebih presisi.

Gambar III.12. Alur Anotasi Dataset Relevansi Topik

Untuk indikator koherensi skor, di mana hanya satu skala dapat bernilai TRUE dalam satu kelompok rubrik guna mempertahankan sifat ordinal skor, dengan visualisasi alur anotasi dataset yang disajikan pada [Gambar III.13.](#page-13-0) Skema anotasi biner ini dipilih dibandingkan rating skala Likert karena tujuan utama pipeline adalah menghasilkan keputusan deterministik per indikator. Oleh karena itu, format ground truth harus selaras secara struktural dengan output prediksi agar evaluasi metrik tetap langsung, konsisten, dan mudah diinterpretasikan.

Gambar III.13. Alur Anotasi Dataset Koherensi Skor dan Narasi

**C. Proses Anotasi**

Anotasi dilakukan oleh dua anotator yang merupakan peneliti dengan pemahaman komprehensif mengenai struktur rubrik PjBL dan definisi operasional indikator tekstual narasi feedback. Proses anotasi dilakukan secara kolaboratif, kedua anotator bekerja bersama dalam saru sesi untuk mengevaluasi dan mendiskusikan setiap baris data.

Selama proses kolaboratif tersebut, panduan anotasi formal memuat definisi operasional setiap label, aturan penanganan kasus ambigu, daftar kata yang berpotensi menimbulkan ambiguitas penilaian, dan contoh berlabel untuk setiap aspek rubrik digunakan sebagai acuan mutlak.

Mengingat proses pelabelan bersifat kolaboratif dan sling membantu, setiap perbedaan interpretasi diselesaikan secara langsung melalui diskusi. Sebagai contoh disagreement, ketika menghadapi narasi "Rekan saya sangat rajin membantu tugas kelompok", satu anotator mungkin menganggap ini memenuhi kriteria rubrik "Kemampuan bekerja sama dengan anggota kelompok lain.", satu anotator mungkin menganggapnya terlalu umum. Penyelesaian dilakukan dengan merujuk kembali pada aturan di panduan anotasi. Apabila diskusi kolaboratif menemui jalan buntu pada kasus yang sangat ambigu, data tersebut ditandai untuk diputuskan pada tahap validasi. Alur proses anotasi disajikan pada [Gambar III.14.](#page-14-0)

Gambar III.14. Alur Anotasi Dataset oleh Annotator

**D. Validasi Anotasi**

Tahap terakhir dari proses anotasi adalah validasi konfirmatif oleh dosen pengampu PjBL selaku domain expert. Sampel acak dari data yang telah dianotasi diserahkan kepada dosen untuk dievaluasi. Dosen exepertise memberikan penilaian akhir mengenai apakah label hasil konsensus kedua anotator telah merepresentasikan sesuai yang diharapkan. Selain itu, dosen juga memberikan keputusan final terhadap narasi edge-case yang sebelumnya tidak dapat disepakati oleh anotator.

Hasil validasi dari dosen inilah yang kemudian mengunci status dataset dan menetapkannya menjadi ground truth final untuk eksperimen pemodelan. Proses ini memastikan bahwa seluruh label anotasi yang dijadikan ground truth konsisten secara logis dan valid serta dapat dipertanggungjawabkan secara pedagogis menurut standar evaluasi dosen. Alur validasi anotasi dataset disajikan pada [Gambar III.15.](#page-14-1)

Gambar III.15. Alur Validasi Dataset

**III.6.3.3 Komponen NLP Pipeline Digital Scaffolding**

Subbab ini mendukung pengembangan pipeline digital scaffolding dengan menjelaskan perumusan matematis keempat indikator tekstual narasi, sebagaimana didefinisikan pada Tabel III.3. Bagian ini berfungsi untuk memetakan definisi formal dari setiap komputasi yang dilakukan sistem, dimulai dari semantic chunking yang didefinisikan pada subbab III.6.3.5A, sebelum mekanisme analisa narasi feedback yang dijabarkan pada subbab [III.6.3.3B](#page-2-0).

**A. Part-of-Speech Tagging**

Untuk mencegah narasi feedback yang berisi teks acak tanpa makna, sistem menerapkan mekanisme identifikasi struktur gramatikal klausa. Menurut Moeliono (2017), syarat minimal terbentuknya sebuah kalimat independen dalam bahasa Indonesia adalah terpenuhinya fungsi subjek dan predikat.

Dalam mendukung hal tersebut, identifikasi diimplementasikan menggunakan NLP toolkit Stanza (Qi et al., n.d.) melalui teknik Part-of-Speech (POS) tagging. Sistem mengekstraksi representasi leksikal dari setiap narasi feedback dan memvalidasi keberadaan kelas kata pengganti subjek, yang umumnya didominasi oleh nomina (NOUN), pranomina (PRON), atau nomina propria (PROPN). Selanjutnya, sistem memvalidasi eksistensi predikat.

Dalam bahasa Indonesia, terdapat variasi kalimat berpredikat non-verbal Moeliono (2017). Oleh karena itu, aturan filter pada sistem dirancang untuk menerima verba (VERB), auxiliary (AUX), adjektiva (ADJ), dan adverba (ADV) sebagai parameter validasi predikat. Apabila representasi POS tag dari narasi feedback gagal memenuhi struktur hierarkis subjek-predikat ini, sistem menolak teks tersebut sebelum dilanjutkan ke tahap komputasi indikator tekstual narasi. Metode ini sejalan dengan kaidah dasar NLP untuk memfilter struktur noise tanpa makna (Jurafsky & Martin, 2009).

Validasi input dievaluasi pada setiap teks narasi feedback  $(s_{txt})$ . Melalui proses tokenisasi, teks  $s_{txt}$  dipecah menjadi himpunan token T. Setiap token  $t \in T$  memiliki atribut kelas kata  $(t_{pos})$  dan panjang karakter  $(|t_{text}|)$ . Berdasarkan tata bahasa baku, sistem mengekstraksi dua himpunan syarat fungsi dari  $s_{txt}$ , yaitu: (1) himpunan kandidat predikat (P), dan (2) himpunan kandidat subjek (S).

Syarat pertama, yaitu himpunan kandidat predikat (P), diimplementasikan dengan mengisolasi token dari  $s_{txt}$  yang kelas katanya merepresentasikan tindakan, keadaan, atau keterangan, sebagaimana disajikan pada rumus III.12.

$$P = \{t \in T | t_{pos} \in \{VERB, AUX, ADJ, ADV\}\}$$
 (III.12)

Syarat kedua, yaitu himpunan kandidat subjek (S), direalisasikan dengan mengisolasi token pronomina, atau nonima atau nomina propria dengan batasan panjang karakter di atas 1 untuk menggugurkan teks dengan satu huruf, sebagaimana disajikan pada rumus III.13.

$$S = \{t \in T | t_{pos} = PRON \lor (t_{pos} \in (NOUN, PROPN) \land |t_{text}| > 1)\} \quad \text{(III.13)}$$

Teks narasi feedback ( $s_{txt}$ ) ditetapkan valid apabila memenuhi eksistensi minimal satu elemen subjek dan satu elemen predikat, sebagaimana direpresentasikan pada rumus III.14.

$$POS(s_{txt}) = \begin{cases} Valid, jika \ (|S| \ge 1) \land (|P| \ge 1) \\ Invalid, jika \ lainnya \end{cases}$$
 (III.14)

Tabel III.8 menyajikan contoh skenario evaluasi narasi feedback menggunakan mekanisme dan rumus yang telah dipetakan.

Skenario  |  Input Teks  |  Ekstraksi POS Tag  |  Evaluasi Himpunan  |  Status Input  |  Alasan
Klausa Verbal Sempurna  |  "Saya merevisi laporan"  |  Saya (PRON), merevisi (VERB), laporan (NOUN)  |  S = 2 $P = 1$  |  Valid  |  Memiliki subjek dan predikat
Klausa Adjektivial Sempurna  |  "Aplikasi ini lambat"  |  Aplikasi (NOUN), ini (PRON), lambat (ADJ)  |  S = 2 $P = 1$  |  Valid  |  Memiliki subjek dan predikat non- verbal
Input acak  |  "asdf hjkl"  |  -  |  S = 0 $P = 0$  |  Invalid  |  Tidak terdapat kelas kata baku

Tabel III.8. Skenario Evaluasi Part-of-Speech Taging

**B. Representasi Vektor dan Metrik Semantik**

Subbab ini mendefinisikan formulasi fungsi evaluasi operasional dari keempat indikator tekstual narasi feedback pada Tabel III.3. Seluruh fungsi dirumuskan berdasarkan mekanisme embedding dan cosine similiarity yang telah dijelaskan pada Lampiran 4. Fungsi tersebut diimplementasikan sebagai acuan utama dalam evaluasi dan eksperimen model, sebagaimana dijabarkan pada subbab IV.3.2.

Evaluasi dilakukan pada tingkat pasangan narasi feedback () dengan himpunan feature-set def-\),A serta de4-\),A yang telah didefinisikan pada subbab IV.2.1.1 dan IV.2.1.2. Setiap pasangan tersebut diasosiasikan dengan label anotasi TRUE/FALSE yang dihasilkan pada subbab IV.2.2. Evaluasi dilakukan untuk memprediksi nilai label anotasi dalam membangun mekanisme deteksi keempat indikator tekstual pada Tabel III.3.

Formulasi keempat nilai indikator tekstual tersebut didefinisikan pada subbab [III.6.3.3](#page-0-0)[.B](#page-2-0).[1](#page-2-1) hingga [III.6.3.3](#page-0-0)[.B](#page-2-0)[.4](#page-6-0). Hasil komputasi direpresentasikan sebagai - = , -, -, <sup>I</sup> -, & -- yang membentuk vektor pemenuhan indikator sebagai acuan utama dalam rule-based system pada subbab III.6.3.5A.

**1. Cakupan Rubrik (**ÅÇ**)**

Indikator pertama berfokus untuk mengevaluasi sejauh mana narasi feedback membahas kriteria rubrik. Secara komputasional, indikator didefinisikan melalui fungsi similiarity antara narasi feedback () dengan feature-set cakupan dan relevansi topik (de4-\),A) yang didefinisikan pada subbab IV.2.1.1, sebagaimana disajikan pada rumus [III.15](#page-2-2).

$$\tilde{y}(s_{txt}, c_{cov,i}) = \begin{cases} 1, & sim_x(s_{txt}, c_{cov,i}) \ge \theta_{sim,1} \\ 0, & sebaliknya \end{cases}$$
(III.15)

Di mana '(), adalah threshold cosine similarity indikator cakupan rubrik yang didapatkan melalui evaluasi pada subbab IV.3.2. Di sisi lain, g7h,) merupakan unit dekomposisi kriteria rubrik yang didefinisikan pada Lampiran 4. Fungsi  $sim_x(.,.)$  merujuk pada fungsi cosine similarity yang dievaluasi.

Selanjutnya, nilai cakupan  $f_1$  dihitung sebagai proporsi kriteria yang terdeteksi. Sebagaimana disajikan pada rumus III.16.

$$f_1(s_{txt}, COV(K_{i,j})) = \frac{\sum_{c_{cov,i} \in COV(K_{i,j})} \check{y}(s_{txt}, c_{cov,i})}{|COV(K_{i,j})|}$$
(III.16)

Dengan  $COV(K_{i,j})$  merupakan feature-set untuk cakupan dan relevansi topik, didefinisikan pada subbab IV.2.1.1. Fungsi ini menghasilkan nilai bilangan real dengan nilai 0 hingga 1  $(f_1(.,.) = x \in \mathbb{R} | 0 \le x \le 1)$ , dengan 1 merepresentasikan bahwa indikator terpenuhi sempurna. Seluruh alur komputasi indikator ini disajikan pada Gambar III.16.

Sebagai contoh komputasi indikator ini, Tabel III.9 menyajikan perhitungan menggunakan rumus III.15 dan III.16 yang telah didefinisikan.

Tabel III.9. Contoh Perhitungan Indikator Cakupan Rubrik

Narasi: "Saya selalu mengelola waktu dengan baik"
$\theta_{sim,i}$ : 0,7
Unit Dekomposisi  |  Isi Narasi yang Relevan  |  Similarity  |  ĭ
Ketepatan Memenuhi Deadline  |  Tidak disebutkan  |  0,5  |  0
Kemampuan Mengelola Waktu  |  "Mengelola waktu dengan baik"  |  0.0  |  1

Berdasarkan Tabel III.9, narasi "Saya selalu mengelola waktu dengan baik" dengan threshold 0,7 memiliki pemenuhan indikator sebesar 0,5, sebagaimana disajikan pada rumus III.17.

$$f_1 = \frac{0+1}{2} = \frac{1}{2} = 0.5$$
 (III.17)

Gambar III.16. Flowchart Komputasi Indikator Cakupan Rubrik

2. Koherensi Skor dan Narasi $(f_2)$

Indikator ini mengukur keselarasan antara skor numerik  $(s_{num})$  dan makna evaluatif dalam narasi feedback  $(s_{txt})$  menggunakan koherensi skor feature-set yang didefinisikan pada subbab IV.2.1.2.

Evaluasi dilakukan berdasarkan nilai  $cosine\ similarity$  narasi terhadap seluruh unit dekomposisi pada setiap tingkat skor  $(s_k \in S)$ . Himpunan prediksi skor global  $(\hat{S}_{base})$  pada pendekatan ini mengumpulkan seluruh tingkat skor yang memiliki setidaknya satu unit dekomposisi dengan nilai  $cosine\ similarity$  sama dengan atau melampaui  $threshold\ (\theta_{sim,2})$ . Secara matematis, komputasi ini didefinisikan pada rumus III.18.

$$\hat{S}_{base}(s_{txt}) = \{ s_k \in S | \exists c \in COH(K_{i,j,s_k}) : sim_x(s_{txt}, c) \ge \theta_{sim,2} \}$$
 (III.18)

Dengan  $sim_x(.,.)$  merujuk pada fungsi cosine similarity yang dievaluasi. Sebagai tahap akhir, dilakukan verifikasi apakah skor aktual mahasiswa  $(s_{num})$  merupakan anggota dari himpunan prediksi global  $(\hat{S}_{base}(s_{txt}))$ , sebagaimana disajikan pada rumus III.19.

$$f_2(F) = \begin{cases} 1, jika \ s_{num} \in \hat{S}_{base}(s_{txt}) \\ 0, sebaliknya \end{cases}$$
(III.19)

Di mana 1 merepresentasikan bahwa skor dan narasi dalam kondisi selaras, sedangkan nilai 0 merepresentasikan ketidakselarasan.

3. Indikator Kedalaman Elaborasi ( $f_3$ )

Indikator kedalaman elaborasi mengukur panjang teks narasi sebagai prasyarat sehingga feedback bersifat informatif.

Didefinisikan fungsi panjang teks  $L(s_{txt})$  yang mengekstraksi jumlah kata leksikal narasi feedback. Evaluasi kedalaman elaborasi diformulasikan sebagai fungsi biner yang membandingkan panjang narasi dengan threshold kata  $(\theta_{sim.3})$ :

$$f_{3} = \begin{cases} 1, & apabila L(s_{txt}) \ge \theta_{sim,3} \\ 0, & sebaliknya \end{cases}$$
 (III.20)

Di mana  $\theta_{len}$  ditetapkan sebagai 25 kata, sebagaimana didefinisikan pada subbab IV.2.2.1. Nilai 1 mengindikasikan bahwa narasi memiliki panjang yang memadai, sedangkan 0 mengindikasikan narasi terlalu pendek.

Pendekatan ini tidak mengasumsikan bahwa panjang teks secara langsung merepresentasikan yang bersifat informatif, tetapi menetapkan batas minimal sebagai kondisi bagi keberadaan elaborasi. Dengan demikian, indikator ini berfungsi sebagai penyaring awal terhadap skor kualitatif/narasi yang terlalu singkat untuk memberikan nilai instruksional. Tabel III.10 menyajikan contoh komputasi indikator elaborasi dalam berbagai skenario.

Tabel III.10. Contoh Komputasi Indikator Elaborasi

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

4. Indikator Relevansi Topik $(f_4)$

Indikator ini mengevaluasi apakah narasi fokus pada aspek penilaian yang dituju. Feedback terdeteksi tidak relevan apabila narasi memiliki nilai similarity setara atau di atas treshold terhadap kriteria lain yang tidak sedang dinilai dari rubrik. Hal ini mengindikasikan bahwa mahasiswa salah sasaran dalam memberikan justifikasi evaluatif.

Didefinisikan  $\mathcal{K}$  sebagai himpunan seluruh kriteria rubrik, diturunkan dari definisi pada rumus III.5 dan III.6. Sebagaimana disajikan pada rumus III.21, dengan  $A_i$  merepresentasikan aspek ke-i.

$$\mathcal{K} = \bigcup_{i=1}^{n} A_i \tag{III.21}$$

Kriteria rubrik yang menjadi fokus penilaian dinotasikan sebagai  $K_{i,j}$ . Di sisi lain,  $K_{other}$  merepresentasikan himpunan seluruh unit dekomposisi yang tidak termasuk ke dalam kriteria yang sedang dinilai, disajikan pada rumus III.23.

$$K_{other}(K_{i,j}) = \bigcup_{K' \in \mathcal{K} \setminus K_{i,j}} COV(K')$$
(III.22)

Dengan COV(.) didefinisikan pada rumus III.9.

Secara konseptual, fungsi indikator relevansi topik dievaluasi menggunakan rumus III.23.

$$f_4(F) = \begin{cases} 0, & apabila \ \exists c \in K_{other}(K_{i,j}) : sim_x(s_{txt}, c) \ge \theta_{sim,4} \\ 1, & sebaliknya \end{cases}$$
(III.23)

Di mana  $\theta_{sim,4}$  adalah threshold semantic similarity untuk indikator koherensi skor dan narasi. Nilai 0 mengindikasikan bahwa narasi membahas kriteria lain di luar kriteria penilaian. Di sisi lain, nilai 1 mengindikasikan bahwa narasi telah berfokus pada kriteria yang dinilai. Dengan  $sim_x(.,.)$  merepresentasikan fungsi cosine similarity yang dievaluasi. Contoh alur komputasi indikator ini disajikan pada Gambar III.17.

Gambar III.17. Contoh Komputasi Indikator Relevansi Topik

**III.6.3.4 Kandidat Model Embedding**

Untuk mendukung proses eksperimen yang dipetakan pada subbab III.6.3 dan pendekatan komputasional yang didefinisikan pada [Tabel III.13,](#page-12-0) pemilihan model sentence embedding didasarkan pada tiga kriteria, yaitu: (1) dukungan multilingual dengan performa yang terverifikasi pada bahasa Indonesia, (2) ukuran model di bawah satu miliar parameter untuk kompabilitas dengan deployment real-time, dan (3) ketersediaan bukti empiris pada benchmark multilingual MMTEB (Enevoldsen et al., 2025).

Seluruh model kandidat yang dievaluasi dikelompokkan ke dalam tiga kategori berdasarkan arsitektur dan pendekatan training, sebagaimana disajikan pada [Tabel](#page-9-0)  [III.11](#page-9-0).

Tabel III.11. Kandidat Model Sentence Embedding

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dalam mengimplementasi model "intfloat/multilingual-e5-large-instruct" yang didefinisikan pada [Tabel III.11,](#page-9-0) instruksi yang digunakan disajikan pada [Tabel](#page-11-0)  [III.12](#page-11-0).

Tabel III.12. Instruksi Model Untuk Indikator

Indikator: Instruksi
Cakupan Rubrik ( ): Temukan teks feedback yang secara eksplisit membahas kriteria rubrik
berikut
Koherensi Skor dan: Temukan teks feedback yang konsisten dengan tingkat penilaian
Narasi ( ): berikut
Relevansi Topik (& ): Temukan teks feedback yang relevan dengan aspek rubrik ini dan tidak
membahas aspek rubrik lainnya

Pendekatan embedding dipilih karena kesesuaian dengan kebutuhan penelitian dan ketersediaan resource, sebagaimana dipetakan pada [Tabel III.13.](#page-12-0)

Tabel III.13. Pemilihan Pendekatan Komputasional

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Pendekatan  |  Penelitian Terdahulu  |  Karakteristik Metode  |  Justifikasi Pemilihan
LLM  |  Penelitian mengenai LLM untuk  |  Pendekatan ini  |  Meskipun performanya yang tinggi, pendekatan ini tidak
mengklasifikasikan teks tidak jarang  |  menggunakan LLM  |  sesuai dengan karakteristik tugas klasifikasi dan implikasi
dilakukan. Hal ini disebabkan oleh prosedur  |  sepenuhnya melakukan  |  operasional karena membutuhkan sumber saya yang besar.
training dan fine-tuning yang bersidat opsional. Model dapat melakukan klasifikasi  |  proses klasifikasi pada teks.  |  Dengan asumsi terdapat 96 mahasiswa yang mengisi
secara akurat menggunakan metode zero-  |  icks.  |  masing-masing 10 pertanyaan dalam skema self dan peer
shot, few-shot prompting, ataupun dynamic: assessment, total permintaan mencapai sekitar 5.280 API
exemplar selection (Lan et al., 2024; Liu &: call untuk satu kali assessment. Jika diasumsikan rata-rata
Shi, 2020; Tripp, 2025).: konsumsi 1.000 token per permintaan, maka total
penggunaan mencapai sekitar 5,28 juta <i>token</i> .
Mengacu pada skema harga model berbiaya rendah (±
$\$0,15$ per 1 juta token input dan $\pm$ $\$0,60$ per 1 juta token
output), estimasi biaya operasional berada pada kisaran
\$1,5–\$3 atau sekitar Rp25.950–Rp51.900 per satu kali
assessment (asumsi kurs Rp17.300/USD).
Meskipun nilai tersebut relatif kecil pada satu siklus, biaya
meningkat secara linear terhadap jumlah pengguna, jumlah
pertanyaan, serta frekuensi interaksi seperti iterasi revisi
atau multi-step scaffolding. Selain itu, pendekatan berbasis
API memperkenalkan ketergantungan eksternal serta biaya
Semantic Text  |  Dandalastan gamantia taut aimilanitu di mana  |  Pendekatan ini bekerja  |  berulang yang dinamis.  Pendekatan <i>semantic similarity</i> berbasis SBERT dengan
Semantic Text Similiarity in  |  Pendekatan semantic text similarity di ruang embedding telah dikembangkan dan  |  dengan cara mengukur  |  cosine similarity dipilih sebagai metode utama dalam
Embedding Space  |  divalidasi secara luas melaluiReimers &  |  jarak kedekatan dua buah  |  penelitian ini karena memiliki keunggulan performa yang
Zeeuug spuce  |  Gurevych (2019)kut:  |  vektor yang  |  stabil, efisiensi tinggi, dan kesesuaian penuh dengan
merepresentasikan: karakteristik data rubrReimers & Gurevych (2019)iris,
1. Reimers & Gurevych (2019)  |  kalimat.  |  Reimers & Gurevych (2019) menunjukkan bahwa
mengusulkan Sentence-BERT, sebuah: arsitektur siamese network pada SBERT menghasilkan
modifikasi dari model <i>pre-trained</i> BERT: sentence embeddings yang bermakna secara semantik dan
yang menggunakan arsitektur <i>siamese</i> dan <i>triplet</i> untuk menghasilkan <i>sentence</i>: dapat dibandingkan langsung melalui cosine similarity,
dan iripiei untuk menghashkan semence

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**III.6.3.5 Evaluasi dan Kalibrasi Model NLP (RQ 1)**

Tahap ini merancang dan menguji pipeline NLP untuk mendeteksi setiap indikator, dengan alur pemetaan yang disajikan pada [Gambar III.18.](#page-0-0) Pipeline yang dirancang menggunakan representasi vektor dari model pre-trained berbasis arsitektur Transformer yang telah dijelaskan pada Lampiran 4. Representasi ini sepenuhnya bergantung pada model yang dipilih, di mana model yang dilatih pada korpus multilingual akan menghasilkan representasi yang berbeda dibandingkan model multilingual atau bahasa Indonesia. Demikian pula, threshold ('(),)) harus dikalibrasi secara empiris terhadap data ground truth.

Gambar III.18. Pemetaan Eksperimen dan Kalibrasi Model

Setiap kandidat model yang didefinisikan pada subbab III.6.3.4 dievaluasi menggunakan dataset yang telah dianotasi sebagai hasil dari proses pada subbab III.6.3.1 sebagai ground truth. Kemudian kesesuaian antara ground truth dengan output pipeline diukur menggunakan metrik F1-Score pada indikator cakupan rubrik (), koherensi skor (), dan relevansi topik (&).

Proses pencarian konfigurasi ini dieksekusi melalui tiga skenario evaluasi komparatif untuk menjawab RQ 1:

1. Whole-text embedding untuk mengukur performa baseline model dalam memproses narasi secara utuh.
2. Semantic Chunking untuk mengukur dampak segmentasi kalimat dalam memitigasi fenomena embedding dilution, yang dijelaskan pada subbab III.6.3.5A.
3. Mutual Exclusivity untuk mengevaluasi penerapan batasan deterministik khusus pada indikator koherensi skor-narasi ( $f_2$ ), sebagaimana dijelaskan pada subbab III.6.3.5B.

Ketiga skenario evaluasi komparatif tersebut dipetakan ke dalam enam kandidat model sentence embedding, sebagaimana dirangkum dalam Tabel III.14.

Tabel III.14. Rancangan Matriks Evaluasi Model

Kandidat Model  |  Whole-Text Embedding  |  Semantic Chunking  |  Mutual Exclusivity
paraphrase-multilingual-mpnet-base-v2  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$
intfloat/multilingual-e5-base  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$
intfloat/multilingual-e5-base + query/passage prefix  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$
intfloat/multilingual-e5-large-instruct  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$
denaya/indoSBERT-large  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$
paraphrase-multilingual-MiniLM-L12-v2  |  $f_1, f_2, f_4$  |  $f_1, f_2, f_4$  |  $f_2$

Untuk mencatat dan membandingkan performa dari skenario whole text embedding dan semantic chunking secara sistematis, dirancang matriks pelaporan hasil kalibrasi. Matriks ini berfungsi sebagai template untuk menyajikan metrik performa sebelum konfigurasi terbaik dipilih sebagai pipeline final. Desain template pelaporan disajikan disajikan pada Tabel III.15.

Tabel III.15. Format Pelaporan Hasil Evaluasi

Variabel Beb: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold $(\theta_{sim,i})$  |  F1  |  Precision  |  Recall
paraphrase-multilingual-: Whole Tex
mpnet-base-v2: Embeeding

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
Semantic Chunking
intfloat/multilingual-e5-base  |  Whole Embeeding  |  Text
Semantic Chunking
intfloat/multilingual-e5-base + query/passage prefix  |  Whole Embeeding  |  Text
Semantic Chunking
intfloat/multilingual-e5-large instruct  |  Whole Embeeding  |  Text
Semantic Chunking
denaya/indoSBERT-large  |  Whole Embeeding  |  Text
Semantic Chunking
paraphrase-multilingual MiniLM-L12-v2  |  Whole Embeeding  |  Text
Semantic Chunking

[Tabel III.16](#page-2-0) menyajikan desain template untuk menyajikan metrik performa mutual exclusivity untuk menguji indikator koherensi skor dan narasi ().

Tabel III.16. Format Pelaporan Hasil Evaluasi Mutual Exclusivity

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet-base: Whole
v2: Text
Embeeding
Mutual
Exclusivity
intfloat/multilingual-e5-base: Whole
Text
Embeeding
Mutual
Exclusivity
intfloat/multilingual-e5-base +: Whole
query/passage prefix: Text
Embeeding
Mutual
Exclusivity

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
intfloat/multilingual-e5-large-instruct: Whole
Text
Embeeding
Mutual
Exclusivity
denaya/indoSBERT-large: Whole
Text
Embeeding
Mutual
Exclusivity
paraphrase-multilingual-MiniLM: Whole
L12-v2: Text
Embeeding
Mutual
Exclusivity

Berbeda dari ketiga indikator lainnya yang dikalibrasi menggunakan cosine similarity terhadap data anotasi, indikator kedalaman elaborasi (I) dikalibrasi secara langsung dari distribusi statistik data historis. Analisis distribusi jumlah kata leksikal dilakukan untuk mengidentifikasi titik infleksi distribusi, yaitu batas di mana frekuensi narasi bertransisi dari zona kluster padat ke distribusi yang jarang. Titik tersebut ditetapkan sebagai threshold ('(),I).

**A. Semantic Chunking**

Teks narasi feedback mahasiswa, terutama yang memiliki volume teks yang panjang umumnya bersifat multi-aspek, di mana terdapat beberapa dimensi penilaian berbeda yang dibahas dalam satu narasi. Apabila keseluruhan teks narasi dilakukan embedding sebagai satu kesatuan, representasi vektor yang dihasilkan merupakan agregasi dari seluruh kalimat, dilakukan melalui mekanisme mean pooling pada level token. Kondisi ini dapat menyebabkan embedding dilution, yaitu informasi spesifik terhomogenisasi oleh informasi dari kalimat lain, sehingga menurunkan nilai cosine similarity pada kriteria target (L. Wang et al., 2024).

Sebagai solusi terhadap masalah tersebut, diusulkan teknik semantic chunking berbasis kalimat yang menggunakan library SpaCy dari sentencizer sebagai komponen segmentasi. Library ini bekerja dengan cara memecah teks secara deterministik berdasarkan himpunan karakter penanda akhir kalimat (stop words), sebagaimana disajikan Gambar III.19.

Gambar III.19 Mekanisme Semantic Chunking menggunakan Sentencizer

Secara formal, fungsi segmentasi dinyatakan pada rumus III.24.

$$U(s_{txt}) = \{u_1, u_2, \dots, u_k\} = sentencizer(s_{txt})$$
 (III.24)

Di mana  $s_{txt}$  adalah teks narasi utuh dari feedback, dan setiap  $u_i$  adalah kalimat hasil segmentasi. Kemudian, untuk mengagregasikan similarity dari level kalimat ke level narasi, digunakan operator maksimum, yaitu:

$$sim_{splitmax}(x_1, x_2) = \max_{\{u_m \in U(x_1)\}} sim(x_1, x_2)$$
 (III.25)

Di mana sim(.,.) merupakan fungsi cosine similarity yang didefinisikan pada Lampiran 4.  $x_1$  dan  $x_2$  merupakan pasangan teks yang dikomputasi, dalam penelitian ini,  $x_1$  merupakan narasi feedback  $(s_{txt})$ . Hal ini dilakukan untuk

mendukung nilai similarity yang tinggi pada satu kalimat dalam merepresentasikan keseluruhan narasi.

Pemilihan kalimat sebagai unit segmentasi didasarkan pada prinsip otomisitas semantik, yaitu bahwa kalimat merupakan unit terkecil yang memuat proposisi independen secara gramatikal dan semantik (Quirk et al., 1985).

Berbeda dengan pendekatan fixed-size chunking yang memotong teks berdasarkan panjang karakter atau token secara arbiter, segmentasi berbasis kalimat memastikan bahwa setiap unit teks memiliki makna yang utuh. Hal ini selaras dengan argumen Qin et al. (2017) mengenai pentingnya menjaga batas kalimat dalam pemrosesan teks, di mana sistem memastikan bahwa fitur yang diekstraksi berasal dari konteks yang lengkap.

**B. Pendekatan Mutual Exclusivity**

Dalam mengevaluasi indikator koherensi skor dan narasi (), model NLP menghadapi tantangan ambiguitas klasifikasi saat membedakan gradasi makna pada tingkat penilaian rubrik yang berdekatan, misalnya untuk membedakan kriteria skor 3 dan 4. Jika hanya mengandalkan cosine similarity murni melalui whole-text embedding, sebuah narasi dapat diprediksi memiliki relevansi yang tinggi terhadap lebih dari satu kriteria skor yang saling bertentangan secara bersamaan.

Untuk mengatasi hal tersebut, diusulkan penerapan aturan mutual exclusivity secara deterministik pada arsitektur evaluasi. Himpunan baris koherensi p-\),A yang telah diekstrak sesuai subbab III.6.3.2.A.2 diklasifikasikan lebih lanjut ke dalam himpunan partisi (°) yang bersifat eksklusif, direpresentasikan pada rumus [III.26](#page-5-1).

$$COH(K_{i,j}) = \{G_1, G_2, ..., G_m\}$$
 (III.26)

Di mana ° merupakan himpunan untuk memartisi unit kriteria yang lebih atomik yang bersaing dalam satu dimensi yang sama. Anggota di dalam himpunan bersifat mutually exclusive, sehingga tidak mungkin sebuah narasi secara logis memenuhi lebih dari satu unit dalam himpunan yang sama secara bersamaan. Sebaliknya, unit dari himpunan yang berbeda bersifat independen. Contoh himpunan disajikan pada [Tabel III.17.](#page-6-0)

Himpuna  |  Unit  |  Irisa  |  Unit Irisan Skor
n: n
Skor
G  |  "]Fop]pSPQ FKPKq KPSQ",  |  Skala  |  "]Fop]pSPQ FKPKq KPSQ"
"]Fop]pSPQ pPp KPSQ", ... 1
"]Fop]pSPQ RQTQP KPSQ"  |  Skala  |  "]Fop]pSPQ pPp KPSQ"
3
Skala: "]Fop]pSPQ RQTQP KPSQ"
5
°  |  "KPSQ rFSF5Q"  |  Skala  |  "KPSQ xFSF5Q"
5
°I  |  "SQqsr] RFr5QrKQK"  |  Skala  |  SQqsr] RFr5QrKQK
5

Tabel III.17. Contoh Himpunan Koherensi Feature Set

Berdasarkan [Tabel III.17](#page-6-0), ° merupakan grup yang mengevaluasi dimensi kriteria jumlah iklan, ° mengevaluasi dimensi relevansi iklan, sementara °I mengevaluasi keberagaman platform. Sifat mutual exclusive berlaku untuk setiap himpunan, narasi yang mendeskripsikan "mengumpulkan sedikit iklan" sekaligus "iklan yang dikumpulkan relevan" secara adalah kondisi yang valid, sehingga kedua unit tersebut dapat bernilai "TRUE" dalam hasil anotasi. Constraint tersebut dinotasikan dalam rumus [III.27](#page-6-1).

$$\left|COH(K_{i,j,s_k}) \cap G_v\right| = 1, \forall G_v \in COH(K_{i,j}) \, \forall s_k \in S$$
 (III.27)

Di mana constraint ini menjaga bahwa setiap himpunan °h hanya dapat memberikan tepat satu anggota kepada himpunan defb\),A,(^ c. Elemen dalam °<sup>h</sup> yang berkorespondensi dengan tingkat skor P dinotasikan sebagai oh,6, sebagaimana disajikan pada rumus [III.28.](#page-6-2)

$$g_{v,k} = G_v \cap COH(K_{i,j,s_k}), g_{v,k} \in G_v$$
 (III.28)

Berdasarkan constraint pada rumus [III.27,](#page-6-1) irisan ini menghasilkan tepat satu elemen, sehingga oh,6 terdefinisi dengan baik.

Selain sifat mutual exclusive, setiap unit hanya dapat berada dalam satu anggota himpunan °, sehingga setiap himpunan merepresentasikan dimensi evaluatif yang independen, sebagaimana direpresentasikan pada rumus [III.29](#page-7-0).

$$G_m \cap G_{m'} = \emptyset \ \forall G_m, G_{m'} \in COH(K_{i,j}), m \neq m'$$
 (III.29)

Di mana ° dan °• adalah dua himpunan yang berbeda dalam def-\),A.

Untuk mengilustrasikan proses dekomposisi feature set ini, [Gambar III.20](#page-7-1) menyajikan alur dekomposisi untuk koherensi skor berdasarkan rubrik historis yang telah didefinisikan pada Lampiran 10.

Gambar III.20 Alur Pengelompokan Mutual Exclusive

Untuk mendukung hal tersebut ke dalam indikator koherensi skor dan narasi  $(f_2)$ , proses prediksi skor dilakukan melalui modifikasi tahapan heuristik komputasi baseline.

Tahap pertama adalah mengumpulkan kandidat skor pada setiap grup partisi  $G_v$  yang memiliki nilai cosine similarity melampaui threshold ( $\theta_{sim,2}$ ), sebagaimana disajikan pada rumus III.30.

$$C_{v}(s_{txt}) = \{k \in S | sim_{x}(s_{txt}, g_{v,k}) \ge \theta_{sim,2}\}$$
 (III.30)

Dengan  $sim_x(.,.)$  merujuk pada salah satu fungsi  $cosine\ similarity$ . Mengingat unit di dalam satu grup bersifat  $mutual\ exclusive$ , fungsi argmax diaplikasikan secara lokal pada himpunan kandidat  $C_v$  untuk mengekstrak prediksi skor tertinggi pada dimensi tersebut, sebagaimana sifat pada subbab III.6.3.2.A.2. Fungsi ini disajikan pada rumus III.31.

$$\hat{s}_{v}(s_{txt}) = arg \max_{k \in C_{v}(s_{txt})} sim_{x}(s_{txt}, g_{v,k})$$
 (III.31)

Pada tahap kedua, sistem mengakumulasikan seluruh prediksi skor lokal dari masing-masing grup dimensi menjadi satu himpunan prediksi global  $(\hat{S})$  melalui operasi union, sebagaimana disajikan pada rumus III.32. Hal ini memungkinkan sistem untuk mengakomodasi narasi mahasiswa yang memuat kondisi silang antar dimensi:

$$\hat{S}(s_{txt}) = \bigcup_{v=1}^{m} {\{\hat{s}_v(s_{txt})\}}$$
 (III.32)

Sebagai tahap akhir, dilakukan verifikasi apakah skor aktual mahasiswa  $(s_{num})$  merupakan anggota dari himpunan prediksi global  $(\hat{S}(s_{txt}))$ , sebagaimana disajikan pada rumus III.33.

$$f_2(F) = \begin{cases} 1, jika \ s_{num} \in \hat{S}(s_{txt}) \\ 0, sebaliknya \end{cases}$$
 (III.33)

Di mana 1 merepresentasikan bahwa skor dan narasi dalam kondisi selaras, sedangkan nilai 0 merepresentasikan ketidakselarasan.

[Gambar III.21](#page-9-0) menyajikan contoh komputasi indikator koherensi skor dan narasi menggunakan narasi "Iklan yang saya kumpulkan jumlahnya sedikit tetapi relevan" dengan '(),I = 0,8. Komputasi pada contoh tersebut mencangkup rumus [III.30](#page-8-0) hingga [III.32.](#page-8-2)

Gambar III.21. Contoh Komputasi Indikator Koherensi Skor dan Narasi

Berdasarkan hasil yang didapatkan pada [Gambar III.21,](#page-9-0) bernilai 1 jika mahasiswa memberikan skor 1 ataupun 5. Sebaliknya, jika skor yang diberikan adalah 2,3, ataupun 4, maka akan bernilai 0.

**III.6.4 Formulasi Pendekatan Scaffolding**

Tahapan ini berfokus pada transformasi konstruk pedagogis abstrak menjadi sistem komputasional yang terukur, operasional, dan dapat dievaluasi secara empiris. Langkah dari tahapan ini adalah perumusan logika inferensi pada subbab [III.6.4.1](#page-12-0), dan perancangan teks dan template scaffolding pada subbab [III.6.4.2](#page-13-0).

Berdasarkan klasifikasi Saye & Brush (2002) yang dijelaskan pada subbab II.1.10.1, digital scaffolding yang dibangun sebagai hard scaffolding, yaitu bantuan yang dirancang sebelumnya berdasarkan suatu tingkat kesulitan yang teridentifikasi di mana dalam konteks penelitian mengacu pada indikator tekstual yang dikemukakan oleh Setiawan et al. (2026) yaitu cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, dan relevansi topik.

Mekanisme bantuan yang diberikan menerapkan prinsip contingency seperti yang telah dijelaskan pada subbab II.1.10.1 sehingga meskipun bersifat hard scaffolding,  Bantuan ditampilkan menyesuaikan dengan keputusan yang dihasilkan berdasarkan deteksi komponen NLP yang telah dijelaskan pada III.6.3.3. Dengan demikian, adaptivity diwujudkan melalui proses evaluasi ulang terhadap indikator tekstual narasi feedback setiap kali mahasiswa melakukan perubahan pada narasi. Dengan demikian, keberadaan maupun isi bantuan selalu mengikuti kondisi teks terkini selama sesi penulisan narasi feedback berlangsung.

Dalam satu sesi penulisan, mekanisme adaptasi direalisasikan melalui proses adding dan fading. Ketika indikator belum terpenuhi sistem menampilkan template bantuan yang sesuai. Setelah indikator terpenuhi pada evaluasi berikutnya, bantuan tersebut tidak lagi ditampilkan. Mekanisme ini merepresentasikan bentuk fading yang bersifat session-bounded, yaitu terbatas pada proses revisi dalam satu sesi penulisan dan tidak mempertahankan riwayat adaptasi antar sesi.

**III.6.4.1 Rule Scaffolding**

Subbab ini menyajikan spesifikasi komputasional rule-based yang memetakan kondisi intervensi terdeteksi ke output scaffolding. Logika pengambilan keputusan pada sistem ini dirancang secara sekuensial untuk memastikan pemrosesan NLP, sebagaimana dipetakan dalam [Gambar III.22.](#page-11-0)

Berdasarkan [Gambar III.22](#page-11-0), sistem menerapkan validasi Part-Of-Speech (POS) tagging yang didefinisikan pada subbab III.6.3.3A sebagai validasi tambahan sebelum embedding dilakukan. Jika teks narasi mahasiswa berupa karakter acak atau tidak memiliki struktur kalimat yang utuh, sistem akan memotong alur eksekusi dan memberikan peringatan tanpa memerlukan proses embedding. Apabila validasi tersebut berhasil dilewati, sistem mengevaluasi keempat indikator yang beroperasi secara paralel dan tidak memiliki dependensi hierarkis satu sama lain.

Gambar III.22. Flowchart Alur Eksekusi Scaffolding

Komponen pengambilan keputusan intervensi dirancang menggunakan pendekatan decision table. Karakteristik domain keputusan ini bersifat terbatas, di mana empat indikator biner menghasilkan tepat 2 & = 16 kombinasi kondisi ditambah satu kondisi invalid. Pemetaan matematis dari kondisi biner tersebut didefinisikan pada rumus [III.34](#page-12-1).

$$P = P_{s} \cup \{P_{0}\}$$

$$M: \{0,1\}^{4} \rightarrow P$$

$$M(d) = \begin{cases} P_{invalid}, jika \ POS(s_{txt}) = Invalid \\ P_{0}, jika \ d = [0,0,0,0] \\ P_{k}, jika \ d = d_{k}, (d_{k}, P_{k}) \in R \end{cases}$$
(III.34)

di mana U( merupakan himpunan 15 template scaffolding intervensi, UC merupakan template konfirmasi non-intervensi yang ditampilkan ketika seluruh indikator terpenuhi, dan U)h=<)@ merupakan template untuk merespons kondisi invalid dari tahap part-of-speech tagging. Varian ℛ adalah himpunan pasangan antara kondisi dengan template yang membentuk decision table.

Ruang keputusan tersebut dikelompokkan ke dalam tiga kategori utama berdasarkan karakteristik pelanggaran indikator tekstual, yaitu:

1. Kondisi Tidak Valid, yaitu representasi POS dari teks narasi gagal memenuhi struktur hierarkis minimal subjek-predikat. Pada kondisi ini, sistem menolak input sebelum mengevaluasi keempat indikator lainnya.
2. Kondisi Ideal, yaitu seluruh indikator terpenuhi (, , I, & = 0). Dalam kondisi ini, sistem menerapkan prinsip fading dengan tidak menampilkan prompt intervensi, namun menampilkan teks konfirmatori.
3. Pelanggaran Tunggal, yaitu hanya satu indikator yang tidak terpenuhi. Scaffolding difokuskan secara eksklusif untuk memperbaiki satu dimensi spesifik.
4. Pelanggaran Komposit, yaitu terjadi kombinasi dari dua atau lebih pelanggaran indikator tekstual narasi feedback secara simultan.

**III.6.4.2 Teks dan Template Scaffolding**

Berdasarkan rule-set yang telah disusun, tahap ini merancang instrumen intervensi pedagogis berupa teks prompt scaffolding.

**A. Pemilihan Pendekatan Generasi Teks Scaffolding**

Berdasarkan kerangka teori yang telah dijabarkan pada subbab II.1.11.1, dilakukan analisis komparatif terhadap keempat pendekatan sebagai mekanisme untuk mendapatkan teks scaffolding secara real-time. Analisis tersebut disajikan pada [Tabel III.18.](#page-14-0)

Tabel III.18 Analisis Pendekatan Generasi Teks Scaffolding

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

**B. Kebutuhan Teks Scaffolding**

Mengacu pada framework desain yang diusulkan Setiawan et al. (2026), sistem ini memanfaatkan sinyal tekstual secara real-time untuk mendeteksi kelemahan spesifik pada narasi mahasiswa, lalu menampilkan panduan yang sesuai dalam bentuk prompt atau teks bantuan untuk indikator cakupan rubrik, koherensi skor dan narasi, elaborasi, maupun relevansi topik yang diilustrasikan pada [Gambar](#page-1-0)  [III.23](#page-1-0).

Gambar III.23. Matriks Strategi Scaffolding dan Prompt (Setiawan et al., 2026)

**C. Spesifikasi Komponen dan Konstruksi Template**

Sebagaimana pendekatan yang dijabarkan dalam subbab III.6.4.2A, teks scaffolding dihasilkan melalui mekanisme template filling, di mana setiap template mendefinisikan teks yang dilengkapi dengan variabel. Untuk mendukung proses tersebut, didefinisikan fungsi 4-#) , yang memetakan pasangan aspek dan narasi feedback ke dalam himpunan variabel kontekstual yang didefinisikan [Tabel III.20](#page-4-0). Secara formal, proses tersebut didefinisikan pada rumus [III.35](#page-1-1).

$$P_k^* = Fill(M(d(F)), V(A_i, F))$$
 (III.35)

Di mana,

1. 0- adalah template yang dipilih berdasarkan hasil komputasi yang didefinisikan pada subbab III.6.3.3B.
2. KSS-. , . adalah operasi substitusi slot yang mengganti variabel dalam template dengan nilai aktual dari 4.

Berdasarkan karakteristik digital scaffolding yang telah dibahas pada subbab II.1.10.1 penelitian ini merancang struktur template scaffolding yang digunakan selama eksperimen. Untuk mempermudah penyusunan pesan bantuan, setiap template disusun menggunakan tiga elemen teks, yaitu pernyataan diagnostik, arahan direktif, dan sentence starter. Ketiga elemen tersebut merupakan keputusan desain (design choice) yang disusun agar selaras dengan tujuan scaffolding pada penelitian ini yang dipaparkan pada [Tabel III.19.](#page-3-0)

Tabel III.19 Elemen Penyusun Template Teks Scaffolding

Komponen  |  Penjelasan  |  Dasar Perancangan  |  Realisasi Pada Template
Diagnostik  |  Kompone merupakan pernyataan deklaratif yang berfungsi untuk menyoroti kelemahan, kekurangan, atau area yang belum tercakup pada narasi feedback yang sedang ditulis.  |  Komponen ini dirancang berdasarkan temuan Nelson & Schunn (2008) yang mengungkapkan bahwa mengidentifikasi masalah secara eksplisit adalah hal esensial yang meningkatkan probabilitas <i>feedback</i> tersebut diimplementasikan oleh <i>assesse</i> .  Selain itu, Cho & MacArthur (2011) menetapkan  |  Komponen ini direalisasikan dengan format "Narasi belum berfokus pada aspek"
problem diagnosis sebagai salah satu fondasi utama dalam skema peer review yang efektif.
Direktif  |  Komponen berfokus pada "apa yang harus dilakukan", dengan cara menuntun dan mewajibkan assessor untuk menulis narasi feedback yang konstruktif atau memberikan solusi perbaikan, sehingga dapat ditindaklanjuti oleh assesse.  |  Konsep ini dirancang berdasarkan temuan Mu & Schunn (2025) sebagai bentuk strategic scaffolding yang memberikan panduan strategis kepada mahasiswa tentang cara memberikan feedback yang baik, termasuk saran untuk menyertakan saran/solusi ke dalam narasi feedback.  |  Komponen ini diimplementasi dengan instruksi "Fokuskan narasimu pada lengkapi dengan" untuk memberikan informasi target komponen penilaian yang harus dipenuhi.
Sentence Starter  |  Pendekatan menyediakan potongan kalimat pembuka untuk menurunkan beban kognitif mahasiswa dan membatasi derajat kebebasan saat menulis.  Alih-alih bingung memikirkan kalimat formalitas yang tidak bermakna (basabasi) atau struktur kalimat yang sopan, mahasiswa diarahkan untuk fokus memikirkan substansi dari evaluasi feedback.  |  Peyediaan sentence starter mengadaptasi gagasan Pea (2004) yang menggunakan procedural facilitators berbentuk lead-in components to sentences sebagai alat untuk membantu penulis pemula.  |  Sentence starter atau kalimat awal ini bersifat opsional, sehingga penggunaannya sepenuhnya bergantung pada preferensi individu. Contoh dari sentence starter adalah "Dalam kegiatan terkait, saya melihat bahwa"

Untuk mengakomodasi seluruh kondisi yang mungkin terjadi, sistem mendefinisikan himpunan template prompt, sebagaimana didefinisikan pada [Tabel](#page-7-0)  [III.21](#page-7-0). Untuk menyesuaikan template prompt dengan kondisi aktual narasi setiap siswa, didefinisikan variabel kontekstual pada [Tabel III.20](#page-4-0), dilengkapi contoh berdasarkan rubrik yang didefinisikan pada Lampiran 10.

Tabel III.20. Variabel Kontekstual yang digunakan Template

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Sebagai visualisasi dari variabel kontekstual pada [Tabel III.20](#page-4-0), [Gambar III.24](#page-5-0) menyajikan contoh variabel missing\_coverage pada aspek penilaian "Pengumpulan Iklan Lowongan Kerja". Disajikan tiga komponen penilaian rubrik, namun narasi tidak membahas komponen "variasi platform", sehingga komponen terebut ditransformasi menjadi input untuk template scaffolding.

Gambar III.24 Ilustrasi Variabel Missing\_Coverage

Sebagaimana didefinisikan [Gambar III.24,](#page-5-0) variabel missing\_coverage diproses lebih jauh menjadi coverage\_expanded. Transformasi ini dilalukan melalui tiga langkah, yaitu:

1. Kumpulkan nilai variabel missing\_coverage sebagai list.
2. Ekspansi setiap item dalam list menggunakan pola "pada aspek {item}, yang teramati adalah [perilaku spesifik terkait {item}]";
3. Jika variabel missing\_coverage mengandung lebih sari saru item, gabungkan seluruh item menggunakan konjungsi ", sementara".

[Gambar III.25](#page-6-0) menyajikan contoh transformasi variabel missing\_coverage ke dalam coverage\_expanded sesuai dengan langkah yang didefinisikan.

Gambar III.25 Ilustrasi Transformasi Missing Coverage

[Gambar III.26](#page-6-1) menyajikan contoh bagaimana variabel predicted\_score dan input\_score didapatkan. Berdasarkan gambar tersebut, input\_score merupakan direct reference terhadap skor yang diberikan mahasiswa dalam feedback. Di sisi lain, pedicted\_score merupakan hasil komputasi dari indikator koherensi skor dan narasi () yang didefinisikan pada subbab III.6.3.3.B.2.

Gambar III.26 Ilustrasi Pengambilan Variabel Kontekstual untuk Skor

Sampel template dilengkapi variabel kontekstual yang dibutuhkannya dapat dilihat pada [Tabel III.21](#page-7-0) dengan keseluruhan teks scaffolding dapat dilihat pada Lampiran 19

Tabel III.21. Sampel Template Prompt Scaffolding

Kode  |  Variables  |  Kompone n  |  Konten
invalid  |  -  |  diagnostik  |  Lengkapi narasi anda dengan membahas komponen penilaian pada rubrik.
0000  |  -  |  diagnostik  |  Feedback sudah sesuai dengan rubrik penilaian, lanjutkan menulis jika diperlukan.
0001  |  target_aspect  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect} yang diminta rubrik.
directive: Fokuskan narasi pada {target_aspect} dan uraikan perilaku yang relevan dengan aspek tersebut.
sentence starter: Terkait {target_aspect}, yang teramati adalah [perilaku spesifik terkait {target_aspect}]
0010  |  -  |  diagnostik  |  Narasi masih bersifat umum, narasi yang ada belum cukup untuk mendukung penilaian. Tambahkan satu contoh kejadian nyata sehingga pembaca dapat memahami dasar penilaian. Sebagai contoh, yang teramati adalah [kejadian konkret terkait]
directive
sentence starter
0011  |  target_aspect  |  diagnostik  |  Narasi masih kurang berfokus pada {target_aspect} dan narasi yang ada belum cukup untuk mendukung penilaian.
directive: Fokuskan pada {target_aspect} dan perkuat dengan satu contoh nyata yang teramati.
sentence starter: Terkait {target_aspect}, yang teramati adalah [kejadian konkret terkait {target_aspect}]. Sebagai contoh, [contoh kejadian konkret lainnya terkait {target_aspect}]

Implikasi dari arsitektur ini adalah sistem bersifat adaptif pada level konten pada template teks scaffolding. Untuk mengilustrasikan mekanisme ini secara konkret. [Tabel III.22](#page-8-0) menyajikan contoh dua mahasiswa dengan kondisi yang identik namun menghasilkan output yang berbeda.

Tabel III.22 Ilustrasi Adaptivitas Output pada Kondisi d(F) yang Identik

Komponen  |  Mahasiswa A  |  Mahasiswa B
Skor  |  5  |  3
Narasi  |  "Semua iklan yang dikumpulkan rekan saya sudah relevan sekali  |  "Rekan saya sudah mengumpulkan iklan sesuai target, da
dengan kebutuhan kelompok, mulai dari role, lokasi, range gaji,: bahkan jumlahnya melampaui ekspektasi, meskipun har
hingga kriteria penerimaan sudah sesuai dengan yang diminta.: beberapa iklan yang relevan dengan kebutuhan kelompok, tapi
1400  |  Platform yang digunakan juga beragam."  |  itu sudah membantu."
d(F)  |  [1, 0, 0, 0]  |  [1, 0, 0, 0]
Templat dipilih s  |  $T_{1000}$  |  $T_{1000}$
{target_  |  aspect}  |  "Pengumpulan Iklan Lowongan Kerja"  |  "Pengumpulan Iklan Lowongan Kerja"
{missing_coverage}  |  "jumlah iklan yang Dikumpulkan", "Kesulitan dalam Pengumpulan Data", "Kemudahan dalam Pengumpulan Data"  |  "keberagaman platform", "Kesulitan dalam Pengumpula Data", "Kemudahan dalam Pengumpulan Data"
{predict  |  ed score}  |  5  |  3
{input s  |  5  |  3
Output  |  Diagnostik  |  Narasi masih kurang menyinggung Jumlah Iklan yang Dikumpulkan,  |  Narasi masih kurang menyinggung Keragaman Platform
$P_k^*$  |  Kesulitan dalam Pengumpulan Data, Kemudahan dalam  |  Pengumpulan, Kesulitan dalam Pengumpulan Data,
Pengumpulan Data yang termasuk dalam rubrik penilaian.: Kemudahan dalam Pengumpulan Data yang termasuk dalam rubrik penilaian.
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

**III.6.5 Pembuatan APE**

Pengembangan Aplikasi Pendukung Eksperimen (APE) SAPA dilakukan menggunakan pendekatan Software Development Life Cycle (SDLC) model Prototyping. Model ini dipilih karena memungkinkan iterasi cepat dalam menguji arsitektur NLP dan penyesuaian antarmuka berdasarkan saran pengguna. Tahapan ini dimulai dari analisis kebutuhan sistem, perancangan diagram, hingga implementasi disajikan pada Lampiran 6 dan Lampiran 7 untuk menjaga fokus pembahasan ini pada substansi penelitian metodologis.

Tahap ini menguraikan bagaimana sistem digital scaffolding dikembangkan dan diintegrasikan ke dalam lingkungan aplikasi existing, yaitu SAPA (Self & Peer Assessment) sebagai instrumen penelitian.

**III.6.5.1 Analisis Lingkungan Eksperimen**

Langkah awal dilakukan dengan menganalisis arsitektur, database, dan antarmuka dari platform SAPA yang digunakan sebagai lingkungan eksperimen. Analisis ini difokuskan pada identifikasi titik integrasi di mana modul NLP dan rule-based engine tanpa mengubah atau menimbulkan gangguan pada fungsi utama assessment. Metode yang digunakan difokuskan pada penentuan titik injeksi logika rule-based dan inferensi model NLP ke dalam alur proses assessment mahasiswa.

**III.6.5.2 Integrasi Pipeline ke dalam Lingkungan Eksperimen**

Setelah titik integrasi terpetakan, proses dilanjutkan dengan merancang mekanisme injeksi pipeline NLP ke dalam alur komputasional sistem yang telah berjalan, yaitu aplikasi SAPA.

**III.6.5.3 Prosedur Validasi Instrumen**

Sebelum digunakan dalam eksperimen, instrumen dievaluasi secara komputasional untuk memastikan fungsionalitas logika ekstraksi NLP berjalan sesuai parameter yang didefinisikan. Evaluasi difokuskan pada pengujian rule-based untuk memastikan intervensi scaffolding terpicu sesuai dengan struktur yang telah didefinisikan pada subbab III.6.4.

Verifikasi instrumen pada tahap ini dirancang secara sistematis dengan mengadopsi prinsip behavioral testing, yaitu pendekatan pengujian yang menilai perilaku output sistem terhadap variasi kondisi input tertentu pada pengujian perangkat lunak, khususnya kerangka CheckList (Ribeiro et al., 2020), yang mengorganisir pengujian ke dalam matrix kapabilitas dan tipe uji, yaitu:

1. Minimum Functionality Test (MFT) untuk menguji apakah suatu kapabilitas dasar berfungsi sesuai spesifikasi pada kasus sederhana dan tidak ambigu. Contohnya apakah pipeline dapat menolak input feedback teks acak.
2. Invariance Test (INV) untuk menguji apakah penyimpangan yang secara semantik tidak relevan tidak mengubah keputusan sistem.
3. Directional Expectation Test (DIR) untuk menguji apakah penyimpangan tertentu mengubah keputusan sistem ke arah yang dapat diprediksi. Contohnya mempersingkat narasi di bawah threshold kata yang seharusnya memicu intervensi elaborasi (I).

Penentuan batas nilai pengujian merujuk pada teknik boundary value analysis dan equivalence partitioning dalam pengujian black-box (Myers et al., 2011).

**A. Variabel Pengujian Instrumen**

Variabel pengujian pada tahap ini dimanipulasi pada tingkat narasi individu melalui data sintetis, dengan:

1. Variabel yang dimanipulasi adalah properti input, meliputi (1) panjang narasi terhadap threshold indikator elaborasi, (2) kombinasi skor numerik dan polaritas sentimen narasi, (3) kesesuaian konten dengan kriteria rubrik, (4) variasi leksikal dan morfologis teks, dan (5) validitas struktural input.
2. Variabel yang diamati adalah keluaran sistem berupa status validasi nilai deteksi indikator dan keputusan intervensi yang dihasilkan.

B. Konstruksi Skenario Validasi Instrumen

Skenario disusun secara purposive, yaitu penentuan sampel secara sengaja diarahkan pada titik-titik kondisi tertentu berdasarkan pertimbangan teoritis untuk memastikan cakupan pada titik-titik yang secara teoritis berisiko menghasilkan kegagalan sistem. Total disusun sebanyak 107 skenario yang terbagi ke dalam tujuh kelompok berdasarkan dimensi yang diuji, sebagaimana dirangkum pada Tabel III.23. Detail lengkap seluruh 107 skenario disajikan pada Lampiran 8.

Tabel III.23. Ringkasan Kelompok Skenario Pengujian

Dimensi yang Diuji  |  Contoh Kasus  |  Jumlah Skenario  |  TipeUji  |  Indikator Target
Boundary threshold panjang narasi  |  Narasi tepat 24 kata, 25 kata, dan narasi yang sangat panjang (100+ kata).  |  23  |  DIR  |  $f_3$
Kombinasi matrix koherensi skor  |  Skor 5 dengan narasi sangat negatif, skor 1 dengan narasi sangat positif.  |  28  |  DIR  |  $f_2$
Relevansi dan cakupan konten rubrik  |  Pujian generik tanpa menyebutkan kriteria rubrik, narasi tidak relevan.  |  21  |  MFT&DIR  |  $f_1, f_4$
Variasi leksikal & morfologis  |  Substitusi sinonim, campuran bahasa Indonesia-inggris, tanda baca tanpa spasi.  |  15  |  INV  |  $f_1$
Redundansi dan manipulasi konten  |  Pengulangan kalimat atau kata untuk menaikkan jumlah kata tanpa menambah substansi.  |  2  |  DIR  |  $f_3$
Validitas dan batas struktural <i>input</i>  |  Teks acak, input kosong, skor di luar rentang 1-5  |  16  |  MFT  |  Filter Validitas
Kontrol positif  |  Narasi yang memenuhi keempat indikator secara eksplisit  |  2  |  MFT  |  $f_1 - f_4$
107

C. Prosedur Eksekusi Pengujian Instrumen

Setiap skenario dieksekusi terhadap pipeline dalam format precondition-procedure-expected result, mengikuti struktur Given-When-Then yang umum digunakan dalam behavior-driven testing. Suatu skenario dinyatakan lulus (PASS) apabila keluaran aktual sistem sesuai dengan hasil yang diharapkan pada dimensi indikator yang menjadi target pengujian; sebaliknya dinyatakan gagal (FAIL) apabila terdapat penyimpangan.

**III.6.6 Perancangan Skenario Eksperimen RQ 2**

Tahap ini bertujuan untuk menetapkan seluruh parameter eksperimen sebelum data eksperimental dikumpulkan, mencakup penentuan subjek, alur interaksi, prosedur statistik dan kriteria interpretasi hasil untuk menjawab RQ 2. Secara umum rancangan skenario eksperimen dapat dilihat pada [Gambar III.27](#page-13-0).

Penjelasan detail mengenai masing-masing komponen skenario eksperimen tersebut dijabarkan secara terstruktur pada subbab [III.6.6.1](#page-14-0) hingga subbab III.6.6.3.

Gambar III.27 Rancangan Eksperimen

**III.6.6.1 Pre-Eksperimen**

Subbab ini membahas aktivitas persiapan lingkungan eksperimen, termasuk subjek eksperimen, rubrik yang digunakan, serta pembuatan kuesioner. Sesuai dengan karakteristik randomized posttest-only control group design, penelitian ini tidak menggunakan pre-test pada kelompok treatment maupun kontrol.

**A. Penentuan Subjek Eksperimen**

Subjek eksperimen adalah mahasiswa JTK POLBAN yang sedang menjalani mata kuliah PjBL pada semester pelaksanaan penelitian, dengan rincian:

1. Kriteria Inklusi, yaitu mahasiswa aktif yang terdaftar dalam satu mata kuliah yang menerapkan PjBL dan bersedia berpartisipasi secara sukarela tanpa konsekuensi nilai akademik.
2. Random Assignment. Mahasiswa yang memenuhi kriteria didaftarkan ke dalam kelompok treatment dan kontrol, sebagaimana didefinisikan pada subbab III.6.6.2A. Penentuan kelompok dilakukan secara acak menggunakan random assignment pada level individu untuk menghindari clustering effect. Proses random assignment dilakukan dengan menghasilkan nilai acak untuk setiap partisipan menggunakan fungsi randomisasi pada aplikasi Spreadsheet, sehingga setiap subjek memiliki probabilitas yang asma untuk masuk ke dalam kelompok treatment atau kontrol. Partisipan dialokasikan secara proporsional ke dalam kelompok treatment dan kontrol sehingga jumlah partisipan pada kedua kelompok tetap seimbang.
3. Ukuran Sampel. Eksperimen ini diposisikan sebagai pilot study dengan target minimal n ≈ 10 per kelompok. Ukuran ini belum memenuhi syarat untuk analisis konfirmatif, namun cukup untuk menghasilkan estimasi effect size awal yang dapat digunakan sebagai masukan dalam perencanaan penelitian. Hal ini didukung oleh Hertzog (2008) yang menyatakan bahwa sampel 10 hingga 20 partisipan per kelompok sudah memadai untuk mengevaluasi parameter feasibility dan mengestimasi varian awal. Selain itu, Julious (2005) merekomendasikan 12 subjek per kelompok sebagai rule of thumb untuk pilot study. Menyadari keterbatasan populasi dan risiko statictical power yang

rendah, hasil eksperimen diposisikan sebagai bukti awal yang berfokus pada effect size serta pola temuan yang muncul dibandingkan dipandang sebagai pengujian konfirmatif.

Eksperimen dilaksanakan pada mata kuliah Manajemen Kualitas Terpadu yang merupakan mata kuliah pada semester delapan di program Sarjana Terapan Teknik Informatika, Politeknik Negeri Bandung yang sedang diikuti oleh mahasiswa angkatan 2022. Berbeda dengan data historis yang digunakan pada tahap pengembangan pipeline dan berasal dari mata kuliah Proyek 1: Pemanfaatan Aplikasi Perkantoran, konteks eksperimen pada penelitian ini menggunakan aktivitas Project Based Learning (PjBL) dalam bentuk proyek penerapan kerangka kerja manajemen kualitas, seperti ISO 9001, ITIL v4, dan COBIT. Mahasiswa bekerja dalam kelompok yang terdiri atas 5-6 orang untuk menyelesaikan studi kasus berbasis role-play serta menyusun laporan proyek sebagai luaran pembelajaran.

Pemilihan konteks ini didasarkan pada kesamaan karakteristik pedagogis dengan lingkungan PjBL yang digunakan pada tahap pengembangan, yaitu adanya kolaborasi tim, pembagian peran, serta penerapan mekanisme self assessment dan peer assessment sebagai sarana evaluasi kontribusi anggota kelompok. Sehingga meskipun domain proyek yang digunakan berbeda, aktivitas evaluatif yang menjadi target bantuan digital scaffolding tetap dipertahankan.

**B. Pembuatan Kuesioner**

Kuesioner dirancang sebagai instrumen evaluasi eksplanatori dengan pendekatan metode campuran untuk melengkapi data kuantitatif dari hasil pengujian statistik. Data kuesioner berfungsi untuk memvalidasi penerimaan intervensi secara psikologis dan operasional oleh pengguna. Skala pengukuran kuantitatif diseragamkan menggunakan skala Likert 5 poin, dengan nilai 1 merepresentasikan "Tidak Setuju", sedangkan nilai 5 merepresentasikan "Setuju" untuk menjaga konsistensi komputasi data. Instrumen dirancang eksklusif untuk kelompok treatment.

Kuesioner difokuskan pada evaluasi pengalaman interaksi mahasiswa terhadap fitur prompt scaffolding. Penyusunan instrumen ini diadaptasi dari dua kerangka teoritism, yaitu:

1. Evaluasi technology acceptance model (Davis, 1989) untuk mengukur secara spesifik perceived ease of use dari prompt yang muncul guna mengetahui sejauh mana panduan tersebut membantu mahasiswa dalam memperbaiki narasi feedback.
2. Evaluasi cognitive load theory (Mestre & Ross, 2011) untuk mengukur apakah kemunculan teks prompt scaffolding berhasil memandu pemikiran mahasiswa (Intrinsic Load) atau menambah beban visual yang tidak perlu (Extraneous Load).

Pemilihan ketiga kerangka evaluasi tersebut didasarkan pada karakteristik pilot study yang berfokus pada persepsi specific task utilization, serta memiliki relevansi langsung dengan kerangka pedagogis ZPD yang dijelaskan pada subbab II.1.9. Kuesioner ini juga memuat open-ended questions untuk menggali opini mahasiswa mengenai akurasi deteksi sistem.

**C. Penyiapan Rubrik Evaluasi**

Instrumen rubrik yang diterapkan dalam tahap eksperimen tidak menggunakan rubrik spesifik proyek pada Lampiran 10. Hal ini dilakukan untuk mengeliminasi bias kompleksitas tugas teknik antar kelompok mahasiswa.

Untuk menjamin validitas instrumen pengujian secara akademis, penelitian ini mengadopsi dan mengadaptasi rubrik standar internasional CATME (Comprehensive Assessment of Team Member Effectiveness) yang dikembangkan khusus untuk peer assessment mahasiswa pada pendidikan tinggi (Ohland et al., 2012). Kerangka instrumen ini dipilih karena secara empiris dirancang berdasarkan taksonomi efektivitas tim yang valid untuk lingkungan kolaboratif mahasiswa.

Berdasarkan struktur aslinya, CATME memuat lima dimensi evaluasi. Namun, untuk mempertahankan netralisasi instrumen terhadap domain teknis proyek, penelitian ini secara terukur mengeliminasi dimensi keterampilan teknis, yaitu knowledge, skill, serta abilities sehingga kriteria rubrik meliputi:

1. Kontribusi terhadap pekerjaan tim untuk menilai dedikasi, alokasi waktu, dan penyelesaian bagian tugas secara mandiri.
2. Interaksi dengan rekan tim untuk menilai kemampuan komunikasi, penyampaian ide, dan penerimaan feedback secara konstruktif.
3. Menjaga fokus dan dinamika tim untuk menilai kesadaran terhadap kemajuan tim dan kemampuan memberikan feedback perbaikan kepada sesama rekan.
4. Komitmen terhadap kualitas untuk menilai tingkat motivasi, ketelitian, dan usaha mahasiswa dalam menghasilkan yang terbaik.

Merujuk pada prinsip perancangan rubrik formatif dari Brookhart (2013), keempat kriteria CATME tersebut diimplementasi menggunakan model Behavioral Anchored Rating Scale (BARS). Dalam implementasinya, model BARS pada CATME menetapkan deskriptor perilaku tekstual yang eksplisit pada anchor skala 1, skala 3, dan skala 5, sedangkan skala 2 dan 4 tidak memiliki behavioral anchors, tetapi digunakan sebagai pilihan bagi siswa untuk memberikan skor di antara skala yang diberikan, sebagaimana diilustrasikan pada [Tabel III.24](#page-2-0).

Tabel III.24. Contoh Implementasi BARS pada Rubrik CATME

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

**A. Desain Eksperimen**

Penelitian ini menerapkan metode kuantitatif berskala pilot study dengan desain randomized posttest-only control group dan alokasi acak terhadap kelompok treatment dan kontrol (Campbell et al., 1963; Shadish et al., 2002). Desain ini dipilih untuk mengevaluasi penggunaan digital scaffolding dalam kondisi pembelajaran yang mendekati praktik nyata, di mana mahasiswa tidak menjalani pre-test sebelum menggunakan sistem. Oleh karena itu, penggunaan desain posttest-only memungkinkan proses penulisan narasi feedback berlangsung secara alami sekaligus meminimalkan testing effect akibat pengukuran awal (Campbell et al., 1963).

Secara metodologis, Shadish et al. (2002) menegaskan bahwa random assigment merupakan instrumen paling kuat untuk menjamin kesetaraan karakteristik antar kelompok sebelum manipulasi dilakukan. Oleh karena itu, setiap perbedaan signifikan yang ditemukan pada post-test lebih mungkin dapat diatribusikan sebagai efek dari intervensi karena pengaruh perbedaan karakteristik awal antar kelompok telah diminimalkan antar kelompok melalui random assignment. Selain itu kontrol terhadap confounding variables juga diperkuat dengan memastikan kedua kelompok berada pada mata kuliah, periode pengerjaan tugas, dan instrumen rubrik yang sama.

**B. Pemberian Instruksi**

Tahapan ini bertujuan memberikan instruksi yang seragam kepada kedua kelompok, meliputi konteks penelitian, prosedur pengerjaan assessment, dan protokol keamanan data. Seluruh subjek diminta menyusun narasi feedback

berdasarkan pengalaman mereka dalam proyek mata kuliah berbasis PjBL. Instruksi disampaikan tanpa mengungkapkan keberadaan modul digital scaffolding untuk meminimalkan potensi bias.

Kedua kelompok mengerjakan assessment secara serentak pada waktu dan lingkungan kelas yang sama. Pengaturan ini memastikan kondisi eksternal yang setara sehingga pengaruh faktor di luar eksperimen terhadap hasil pengukuran dapat diminimalkan.

Untuk memperjelas perbedaan perlakuan antar kelompok, berikut adalah alur yang diterapkan dalam eksperimen ini:

1. Kelompok treatment menerima bantuan scaffolding secara real-time selama proses penulisan narasi feedback berlangsung, setiap kali terjadi pelanggaran indikator, sistem menampilkan prompt panduan berbasis template.
2. Kelompok kontrol tidak menerima scaffolding apapun selama proses penulisan, subjek menyelesaikan seluruh assessment tanpa intervensi sistem.
3. Setelah seluruh jawaban dari kedua kelompok dikirimkan, jawaban tersebut dianalisis menggunakan pipeline digital scaffolding yang sama untuk menghasilkan skor pemenuhan keempat indikator tekstual narasi feedback pada setiap baris pertanyaan assessment.
4. Hasil analisis inilah yang digunakan sebagai data perbandingan antar kelompok treatment dan kontrol.

**C. Operasionalisasi untuk Kelompok Kontrol**

Subjek eksperimen kelompok kontrol dihadapkan antarmuka asessment SAPA tanpa scaffolding. Subjek mengisi assessment dengan modalitas skor kuantitatif dan narasi kualitatif. Subjek eksperimen menyelesaikan seluruh assessment tanpa intervensi scaffolding, sehingga merepresentasikan kondisi penulisan feedback tanpa intervensi scaffolding.

Meskipun kelompok kontrol tidak menerima scaffolding, setiap jawaban dari pertanyaan assessment yang dikirimkan tetap dianalisis menggunakan pipeline digital scaffolding yang sama dengan yang digunakan oleh kelompok treatment. Analisis ini dilakukan untuk memperoleh tingkat pemenuhan keempat indikator tekstual narasi feedback. Hasil analisis tersebut berupa data tingkat pemenuhan pada keempat indikator tekstual narasi feedback dan digunakan sebagai data pengukuran pada kelompok kontrol untuk keperluan perbandingan dengan kelompok treatment yang mendapatkan bantuan digital scaffolding pada proses penulisan.

**D. Operasionalisasi untuk Kelompok Treatement**

Subjek eksperimen kelompok treatment dihadapkan antarmuka assessment SAPA dengan intervensi scaffolding. Kelompok treatment mendapatkan antarmuka SAPA yang identik, di mana perbedaan terletak pada scaffolding yang muncul ketika terjadi pelanggaran terhadap keempat indikator tekstual narasi feedback. Selama proses penyusunan narasi feedback, sistem secara otomatis melakukan evaluasi terhadap keempat indikator tekstual pada setiap perubahan jawaban. Ketika terdeteksi indikator yang belum terpenuhi, sistem menghasilkan scaffolding berbasis template untuk membantu mahasiswa melakukan revisi narasi.

Pada kelompok treatment, sesuai yang dijelaskan pada subbab III.3.2, selain menyimpan hasil akhir dari setiap jawaban assessment, sistem menyimpan data setiap perubahan yang dilakukan oleh mahasiswa. Perubahan dalam konteks ini yaitu, setiap jawaban yang diproses oleh digital scaffolding direkam, sehingga memungkinkannya menangkap proses interaksi mahasiswa dengan teks scaffolding  yang diberikan.

**E. Terminasi Eksperimen**

Setelah waktu yang diberikan selesai, subjek eksperimen diberikan kuesioner yang telah dirancang pada tahapan [III.6.6.1B](#page-0-0) melalui platform Google Form kepada kelompok treatment untuk merekam pengalaman menggunakan aplikasi SAPA.

**III.6.6.3 Pasca Eksperimen**

Setelah eksperimen selesai, dilakukan ekstraksi data hasil eksperimen yang selanjutnya dilanjutkan dengan pengolahan data untuk penarikan kesimpulan.

**A. Ekstraksi Data Hasil Eksperimen**

Tahap ini bertujuan untuk mengumpulkan dan mengagregasi seluruh data yang dihasilkan selama pelaksanaan eksperimen dari kelompok treatment maupun kelompok kontrol. Proses ekstraksi dilakukan langsung dari basis data SAPA dan log yang merekam seluruh interaksi pengguna selama sesi pengerjaan self assessment dan peer assessment.

Data yang diekstraksi terdiri atas dua kategori utama. Kategori pertama adalah data evaluasi hasil assessment yang tersedia untuk kedua kelompok eksperimen. Khusus untuk data kelompok kontrol di mana dalam kondisi tidak menerima scaffolding,  dilakukan langkah tambahan untuk mendapatkan tingkat pemenuhan keempat indikator tekstual narasi feedback yang dilakukan oleh peneliti untuk setiap baris pertanyaan assessment pada kelompok kontrol. Sehingga, baik kelompok treatment  maupun kontrol memiliki data pemenuhan keempat indikator tekstual narasi feedback.

Kategori kedua adalah data interaksi pengguna yang hanya tersedia pada kelompok treatment. Data ini berasal dari log aktivitas sistem yang merekam proses penggunaan digital scaffolding selama penulisan narasi feedback. Informasi yang diekstraksi meliputi waktu pengiriman narasi, status indikator sebelum dan sesudah revisi, jumlah revisi yang dilakukan, riwayat bantuan yang diberikan sistem, serta respons mahasiswa terhadap scaffolding yang muncul selama sesi penulisan.

**B. Pengolahan Data Evaluasi Hasil Eksperimen**

Sebagaimana didefinisikan pada subbab III.3.2.1, pengolahan data evaluasi bertujuan untuk mengetahui ukuran dan signifikansi perbedaan antara kelompok treatment dan kelompok kontrol terhadap tingkat pemenuhan keempat indikator tekstual narasi feedback. Pengolahan ini terdiri dari tiga tahapan, yaitu: (1) verifikasi asumsi, (2) pengujian multivariat, dan (3) pengujian univariat pada setiap indikator yang diikuti dengan perhitungan effect size untuk mengukur besaran perbedaan.

Khusus untuk data hasil eksperimen kelompok kontrol dilakukan terlebih dahulu pengukuran untuk setiap indikator tekstual narasi feedback. Pengukuran ini dilakukan untuk mendapatkan status pemenuhan terhadap setiap indikator berdasarkan skor dan narasi yang telah disubmit oleh mahasiswa dari kelompok kontrol.

Sebelum analisis utama dilaksanakan, verifikasi asumsi dilakukan untuk setiap indikator. Uji Shapiro-Wilk digunakan untuk memverifikasi normalitas distribusi setiap indikator pada kedua kelompok. Pemilihan uji ini didasarkan pada tingkat sensitivitasnya yang lebih tinggi terhadap ukuran sampel kecil dalam konteks pilot study. Selanjutnya, uji Levene digunakan untuk mengevaluasi homogenitas varians antar kelompok treatment dan kontrol. Hasil verifikasi asumsi dilaporkan sesuai dengan format pada [Tabel III.25.](#page-7-0)

Tabel III.25 Format Tabel Pelaporan Verifikasi Asumsi

Jenis Asssessment  |  Indikator  |  Normalitas Kelompok Treatement  |  Normalitas Kelompok Kontrol  |  Homogenitas
Self Assessment: (Cakupan)
(Koherensi)
(Elaborasi) I
(Relevansi) &
Peer Assessment: (Cakupan)
(Koherensi)
(Elaborasi) I
(Relevansi) &

Jika hasil uji mengonfirmasi normalitas per indikator pada setiap kelompok, yang ditunjukkan dengan nilai > 0,05, analisis statistik dilanjutkan pada dua tingkat. Tingkat pertama adalah pengujian multivariat untuk mengevaluasi empat indikator yang didefinisikan pada Tabel III.3 sebagai satu konstruk komprehensif. Tingkat kedua adalah analisis follow-up univariat untuk melihat fenomena pada masingmasing indikator.

Tingkat pertama menggunakan Multivariate Analysis of Variance (MANOVA) untuk menguji signifikansi variabel terikat yaitu pemenuhan keempat indikator tekstual narasi feedback dengan format pelaporan pada [Tabel III.26](#page-8-0). Penggunaan MANOVA diterapkan karena keempat indikator berkorelasi dalam konteks assessment yang sama. Analisis univariat terpisah tanpa koreksi akan mengabaikan interdependensi ini. Pillai's Trace digunakan sebagai effect size multivariat karena bersifat robust terhadap pelanggaran asumsi normalitas multivariat.

Tabel III.26. Format Pelaporan Uji Manova (Pillai's Trace)

Jenis  |  P-value  |  Pillai  |  Signifikan
Assessment  |  Value  |  (Ya/Tidak)

Jika MANOVA menghasilkan < 0.05, terdapat efek multivariat yang signifikan dari intervensi terhadap keempat indikator secara keseluruhan. Analisa kemudian dilanjutkan ke tingkat indikator individu untuk mengidentifikasi indikator spesifik yang berkontribusi.

Sebaliknya, jika MANOVA menghasilkan ≥ 0,05, tidak terdapat efek multivariat yang signifikan pada tingkat signifikansi yang ditetapkan. Karena penelitian ini diklasifikasikan sebagai pilot study dengan ukuran sampel ≈ 10 partisipan untuk setiap kelompok, hasil tidak signifikan ini tidak dapat langsung disimpulkan sebagai bukti ketiadaan efek, melainkan indikasi tidak cukupnya statistical power untuk mendeteksi efek yang ada. Atas dasar ini, analisis follow-up pada tingkat indikator tetap dilaksanakan dengan tujuan utama untuk mengestimasi effect size.

Secara keseluruhan, analisis statistik pada penelitian ini difokuskan pada outcome, yaitu tingkat pemenuhan indikator tekstual pada mahasiswa. Data interaksi yang terekam selama proses penyusunan narasi feedback tidak digunakan sebagai dasar pengujian hipotesis utama. Data tersebut difungsikan secara eksklusif sebagai sumber interpretasi tambahan untuk mendeskripsikan mekanisme kerja digital scaffolding.

Tingkat kedua adalah analisis follow-up yang dilaksanakan secara terpisah per indikator. Karena setiap indikator dapat memiliki status asumsi yang berbeda berdasarkan hasil tahap pertama dalam verifikasi asumsi, prosedur statistik yang digunakan per indikator ditentukan oleh kombinasi status normalitas dan homogenitas varians indikator tersebut. Alur pengambilan keputusan uji statistik ini divisualisasikan pada [Gambar III.28.](#page-9-0)

Gambar III.28. Flowchart Keputusan Uji Statistik Per Indikator

Rincian lebih lanjut mengenai kriteria pengambilan keputusan, penentuan metrik effect size yang bersesuaian dengan setiap uji, serta justifikasi penggunaannya dirangkum pada [Tabel III.27](#page-10-0).

Tabel III.27 Tabel Interpretasi Keputusan Uji Asumsi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dengan demikian, dalam satu analisis follow-up, dimungkinkan bahwa sebagian indikator diuji menggunakan t-test atau Welch's t-test sementara indikator lain diuji menggunakan Mann-Whitney U.

Untuk mengontrol family-wise error rate akibat pengujian empat indikator secara paralel, digunakan prosedur Bonferroni correction. Dengan empat indikator, tingkat signifikansi yang disesuaikan adalah:

$$a_{adjusted} = \frac{0.05}{4} = 0.0125$$
 (III.36)

Interpretasi uji follow up per indikator dapat dilihat pada [Tabel III.28.](#page-11-0)

Effect size per indikator untuk membedakan signifikansi statistik dari tingkat pemenuhan keempat indikator tekstual narasi feedback. Interpretasi nilai effect size merujuk pada Cohen (1988) dan Fiel Peres (2026), yang disajikan pada [Tabel III.29](#page-11-1).

Setiap uji dan effect size yang digunakan dilaporkan pada tabel dalam format yang disajikan pada [Tabel III.30](#page-11-2).

Tabel III.28 Interpretasi Uji Follow Up Per Indikator

Jenis  |  Uji  |  Kriteria  |  Interpretasi
Domono atrili  |  Independent t test/  |  $p < \alpha_{adjusted}$  |  Signifikan
Parametrik  |  Welch's t test  |  $p \geq \alpha_{adjusted}$  |  Tidak Signifikan
Nam Danamatuila  |  M Wil-it II Tt  |  $p < \alpha_{adjusted}$  |  Distribusi indikator berbeda signifikan
Non Parametrik  |  Mann-Whitney U Test  |  $p \geq \alpha_{adjusted}$  |  Tidak signifikan

Tabel III.29 Interpretasi Effect Size

Effect Size  |  Kriteria  |  Interpretasi
0.00 - 0.19: Trivial
Cohomica d (Domometrials)  |  d = 0.20  |  Small Effect
Cohen's d (Parametrik)_  |  d = 0.50  |  Medium
d = 0.80 or higher: Large
r ≥ 0.11: Small
Rank Biserial Corelation (Non Parametrik)  |  r ≥ 0.28  |  Medium
$r \ge 0.43$: Large

Tabel III.30. Format Pelaporan Uji Univariat dan Effect Size

Indikator  |  Uji yang digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect size (Cohen's d atau rank bisserinal correlation)

**C. Pengolahan Data Interaksi Kelompok Treatment**

Pengolahan data pada tahap ini memanfaatkan rekaman data interaksi yang dijelaskan pada subbab III.3.2.2. Data tersebut mencakup kondisi indikator, intervensi yang diberikan, serta perbaikan narasi pada setiap siklus penulisan feedback. Tujuan proses ini adalah mengevaluasi dinamika interaksi mahasiswa dengan instrumen scaffolding. Untuk mencapai tujuan tersebut, pengolahan data dibagi ke dalam lima tahapan analisis, yaitu: (1) Analisis distribusi kebutuhan, (2) evaluasi respons mahasiswa, (3) klasifikasi karakteristik revisi teks, (4) pemetaan pola revisi, dan (5) evaluasi resolusi akhir.

Tahap pertama mengukur distribusi pemenuhan dan persistensi indikator untuk memetakan frekuensi kemunculan scaffolding. Kebutuhan bantuan didefinisikan sebagai kondisi saat indikator tekstual berada pada status "membutuhkan intervensi" sebelum mahasiswa melakukan perbaikan/revisi terhadap narasi. Setiap kondisi ini dihitung sebagai satu kesempatan bagi sistem untuk memberikan scaffolding. Distribusi dihitung berdasarkan frekuensi kemunculan setiap indikator pada konteks self dan peer assessment untuk mengidentifikasi indikator yang paling sering memicu intervensi.

Tahap kedua mengevaluasi respons mahasiswa terhadap kebutuhan scaffolding yang muncul. Analisis ini menggunakan metrik implementation rate dan persitence rate yang merujuk pada konsep Nelson & Schunn (2008) serta Zhang et al. (2024). Implementation rate menghitung proporsi perbaikan yang berhasil memenuhi indikator dibandingkan dengan total kesempatan scaffolding yang dipicu. Perhitungan metrik ini dirumuskan dalam rumus [III.37](#page-12-0).

$$Implementation Rate = \frac{Implemented Opportunities}{Scaffolding Opportunities}$$
 (III.37)

Pada rumus tersebut, implemented opportunities adalah jumlah revisi mahasiswa yang berhasil mengubah status indikator menjadi terpenuhi. Scaffolding opportunities adalah total kejadian indikator berada pada status "membutuhkan intervensi". Metrik pendampingnya adalah persisetence rate yang menghitung proporsi kebutuhan scaffolding yang tetap tidak terpenuhi meskipun intervensi telah diberikan. Perhitungan ini dirumuskan pada rumus [III.38](#page-13-0).

$$Persistence Rate = \frac{Persistence Opportunities}{Scaffolding Opportunities}$$
 (III.38)

Tahap ketiga menganalisis karakteristik perbaikan teks pada setiap revisi. Perubahan narasi dievaluasi dengan membandingkan teks sebelum dan setelah intervensi menggunakan metode Levenshtein Distance (Levenshtein, 1966). Metode ini mengklasifikasikan modifikasi teks ke dalam tiga jenis operasi yang disajikan pada [Tabel III.31](#page-13-1).

Tabel III.31 Karakteristik Perubahan pada Narasi Feedback

Jenis  |  Definisi  |  Contoh
Perubahan
Tanpa  |  Tidak mengubah narasi feedback setelah  |  -
Perubahan (No: menerima bantua scaffolding
Change
Penambahan  |  Menambahkan satu karakter baru ke dalam  |  "bap" menjadi "bapak"
(Insertion)  |  teks yang salah agar menjadi kata yang  |  (menambahkan huruf 'k')
benar.
Penghapusan  |  Menghapus atau membuang satu karakter  |  "bapakk" menjadi "bapak"
(Deletion)  |  yang berlebih atau salah dari sebuah teks.  |  (menghapus satu huruf 'k')
Penggantian  |  Mengganti satu karakter yang salah pada  |  "bapok" menjadi "bapak"
(Substitution /  |  teks dengan satu karakter yang benar.  |  (mengganti huruf 'o' menjadi
Replacement): 'a')

Tahap keempat memetakan dampak setiap revisi terhadap tingkat pemenuhan indikator tekstual. Berdasarkan transisi status dari narasi pada kondisi awal hingga kondisi akhir, lintasan revisi mahasiswa diklasifikasikan ke dalam empat pola deskriptif. Rincian keempat pola revisi tersebut disajikan pada

Tabel III.32. Klasifikasi Pola Revisi

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

Pola  |  Definisi  |  Interpretasi
Tidak  |  Status pemenuhan indikator  |  "Merefleksikan dinamika revisi narasi yang
Konsisten  |  berubah secara fluktuatif antara  |  belum menghasilkan kondisi pemenuhan
Pola  |  "terpenuhi" dan "tidak terpenuhi".  |  indikator secara stabil.
Lainnya

Tahap kelima mengevaluasi hasil kumulatif dari seluruh proses revisi untuk melihat apakah kebutuhan bantuan berhasil diselesaikan pada versi final narasi feedback. Pendekatan ini sejalan dengan konsep closing the feedback loop. Efektivitas intervensi dinilai dari kondisi akhir dokumen, tidak hanya mengukur ada atau tidaknya respons mahasiswa pada satu siklus tertentu. Suatu indikator dinyatakan berhasil diselesaikan apabila indikator tersebut pernah aktif memicu scaffolding pada salah satu tahap revisi, tetapi tidak lagi aktif pada versi final narasi feedback mahasiswa. Sebaliknya, indikator yang tetap aktif hingga versi final dikategorikan sebagai kebutuhan bantuan yang belum terselesaikan.

**D. Pengolahan Data Kuesioner Evaluasi Pengguna**

Pengolahan data pada tahap ini memanfaatkan respons dari kuesioner pascaeksperimen yang diisi oleh subjek pada kelompok treatmet. Sesuai dengan pendekatan metode campuran eksplanatori yang ditetapkan pada subbab [III.6.6.1B](#page-0-0), pengolahan data kuesioner bertujuan untuk memvalidasi penerimaan intervensi secara operasional dan mengukur beban kognitif pengguna. Proses pengolahan data dibagi ke dalam tiga tahapan analisis berdasarkan jenis instrumen pertanyaan, yaitu: (1) analisis metrik penerimaan dan beban kognitif, (2) distribusi preferensi komponen, dan (3) analisis saran kualitatif.

Tahap pertama adalah mengolah data kuantitatif yang mengukur preceived usefullness dan tingkat extraneous cognitive load. Data bersumber dari instrumen skala Likert 5 poin, di mana skor 1 merepresentasikan "Sangat tidak setuju" dan skor 5 merepresentasikan "Sangat Setuju". Pengolahan dilakukan menggunakan statistik deskriptif dengan menghitung nilai rata-rata pada setiap metrik pertanyaan untuk menentukan tendensi sentral dari persepsi pengguna terhadap intervensi scaffolding.

Tahap kedua memetakan evaluasi pengguna teradap komponen antarmuka spesifik. Data bersumber dari instrumen checkboxes yang mengidentifikasi elemen sistem yang dirasa paling membantu dan elemen yang paling membutuhkan perbaikan. Data diolah dengan menghitung frekuensi pemilihan setiap komponen oleh responden, yang kemudian dikonversi menjadi persentase proporsi. Metrik ini digunakan untuk memetakan area antarmuka yang memiliki utilitas tertinggi serta mengisolasi fitur yang menjadi sumber gangguan visual.

Tahap ketiga menganalisis data kualitatif yang diperoleh dari open-ended responses. Teks evaluasi pengguna dioleh menggunakan analisis tematik untuk mengidentifikasi pola keluhan teknis atau kendala operasional selama penulisan narasi. Hasil ekstraksi tema kualitatif ini diposisikan sebagai fungsi eksplanatori untuk menjelaskan penyebab anomali atau tren dominan yang ditemukan pada data kuantitatif.

**E. Interpretasi Data Hasil Eksperimen**

Untuk menjawab RQ2, hasil eksperimen diinterpretasikan melalui tiga sumber analisis yang saling melengkapi, yaitu analisis statistik, kuesioner evaluasi pengguna, dan evaluasi terhadap kerangka konseptual digital scaffolding. Analisis statistik meliputi MANOVA untuk menguji perbedaan simultan keempat indikator tekstual antara kelompok treatment dan kontrol, diikuti analisis univariat untuk mengidentifikasi indikator yang berkontribusi terhadap perbedaan tersebut. Interpretasi juga mempertimbangkan ukuran efek mengingat penelitian ini merupakan pilot study dengan ukuran sampel terbatas.

Analisis kuesioner digunakan untuk mengevaluasi penerimaan pengguna, mekanisme operasional sistem, dan beban kognitif. Selanjutnya, data interaksi kelompok treatment pada eksperimen meliputi persistence rate, resolution rate, frekuensi trigger, dan pola revisi dievaluasi terhadap kerangka konseptual digital scaffolding untuk menilai kesesuaian mekanisme sistem dengan karakteristik scaffolding berdasarkan kerangka teori pada II.1.10.1. Ketiga sumber analisis tersebut saling melengkapi dalam menjawab RQ2 tanpa saling menggantikan.

**III.6.7 Penarikan Kesimpulan dan Perumusan Saran**

Tahap terakhir dalam penelitian ini adalah menarik kesimpulan dan merumuskan saran untuk penelitian lanjut, sebagai manifestasi dari proses "Analisis Hasil Eksperimen". Proses penarikan kesimpulan dilakukan secara deduktif dengan melakukan sintesis hasil analisis statistik hasil eksperimen untuk secara langsung menjawab RQ yang telah ditetapkan pada subbab I.3. Kesimpulan akan difokuskan pada interpretasi awal mengenai hubungan antara penggunaan digital scaffolding dan tingkat pemenuhan indikator tekstual feedback pada kelompok treatment dibandingkan kelompok kontrol.

Sementara itu, perumusan saran pengembangan lanjutan diformulasikan melalui identifikasi limitasi atau anomali komputasional yang ditemukan pada performa model NLP selama pengujian berlangsung. Saran dirumuskan untuk merekomendasikan perbaikan arsitektur atau parameter pada studi mendatang, sehingga murni berbasis pada batasan observasi sistem.

**BAB IV**

**HASIL PENGEMBANGAN APE**

Bab ini menjelaskan tahapan operasionalisasi variabel eksperimen ke dalam bentuk pipeline komputasional. Struktur pembahasan dimulai dengan spesifikasi arsitektur tingkat makro yang menghubungkan teori pedagogis dengan model NLP. Bagian utama bab ini kemudian mendeskripsikan konfigurasi logika, konstruksi teks, serta kalibrasi model yang digunakan sebagai instrumen utama dalam eksperimen.

**IV.1 Analisis Problem Domain dan kebutuhan Eksperimen**

Berdasarkan langkah identifikasi dan studi pendahuluan yang telah diuraikan pada subbab III.6.1, subbab ini menyajikan analisis terhadap karakteristik permasalahan yang ditemukan pada data historis Self Assessment dan Peer Assessment sebagai dasar perancangan pipeline digital scaffolding. Analisis dilakukan untuk mengidentifikasi bagaimana mahasiswa mengartikulasikan penilaian ke dalam bentuk narasi feedback serta bentuk penyimpangan yang muncul terhadap indikator tekstual narasi feedback yang telah didefinisikan pada subbab III.2.2. Selain karakteristik kualitatif, subbab ini juga menyajikan kuantifikasi kondisi aktual berdasarkan data historis sehingga urgensi intervensi scaffolding dapat dijustifikasi secara empiris sebelum proses perumusan pipeline instrumen dilakukan.

**IV.1.1 Karakteristik Data Narasi** *Feedback*

Analisis dilakukan secara manual terhadap sampel acak dari data historis untuk mengisolasi karakteristik kemunculan pola dari penyimpangan terhadap keempat indikator tekstual narasi feedback, sebagaimana didefinisikan pada Tabel III.3. Narasi feedback yang dianalisis memiliki karakteristik sebagai teks bahasa alami yang ditulis secara bebas oleh mahasiswa. Berbeda dengan data terstruktur, narasi dapat menggunakan berbagai variasi ekspresi untuk menyampaikan penilaian yang sama sehingga evaluasi kualitas feedback tidak dapat dilakukan hanya berdasarkan keberadaan kata tertentu. Oleh karena itu, analisis pada subbab ini difokuskan pada pola penyimpangan terhadap empat indikator tekstual yang telah didefinisikan sebelumnya.

**IV.1.1.1 Karakteristik Indikator Cakupan Rubrik.**

Pelanggaran pada indikator cakupan rubrik () ditunjukkan oleh pola dimana mahasiswa kerap dapat menuliskan narasi kualitatif, namun gagal menyebutkan kriteria spesifik yang tertera pada instrumen rubrik. Sebagaimana ditunjukkan pada [Tabel IV.1](#page-3-0) berdasarkan data historis yang dimiliki, dengan rubrik yang telah didefinisikan pada Lampiran 10 untuk aspek manajemen waktu.

Tabel IV.1. Kasus narasi bersifat generik

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel IV.1](#page-3-0) menunjukkan fenomena pada data historis aktual dengan narasi "Sangat baik". Narasi tersebut tidak menjawab komponen penilaian rubrik, yaitu (1) apakah tugas diselesaikan tepat waktu ataupun (2) eksistensi tugas yang terlambat yang dapat dikejar. Alih-alih, narasi hanya berupa pernyataan afektif generik dan tidak memuat referensi terhadap rubrik. Karakteristik teks ini sejalan dengan temuan (Setiawan, 2026a) yang menekankan bahwa teks generik dan afektif mereduksi fungsi evaluasi menjadi sekadar gestur sosial. Kondisi ini pada akhirnya menghilangkan seluruh informasi yang berguna bagi penerima feedback (assessee) untuk mengidentifikasi kualitas kerja mereka (Nicol et al., 2014).

Kasus lainnya yaitu mahasiswa berhasil mengidentifikasi satu kriteria rubrik, tetapi gagal menuliskan kriteria substantif lainnya dalam aspek rubrik yang sama, fenomena ini merupakan contoh cakupan parsial, sebagaimana disajikan pada [Tabel](#page-4-0)  [IV.2.](#page-4-0)

Tabel IV.2. Kasus Cakupan Parsial

, ,  |  nengumpulkan form Facebool  |  iklan sebanyak <mark>yang</mark> k  |  Legend:  |  Tidak dibahas Dibahas
Aspek  |  Kriteria  |  Pertanyaan Kuantitatif  |  Pertanyaan Kualitatif  |  Skala 1 (Sangat Kurang)  |  Skala 3 (Cukup)  |  Skala 5 (Sangat Baik
Pengumpulan iklan Lowongan Kerja  |  Banyaknya iklan dan keragaman platform yang digunakan.  |  Seberapa baik rekan Anda dalam mengumpulka n iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)  |  Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  Mengumpulka n sedikit iklan.  |  Mengumpulkan cukup iklan.  |  Mengumpulka n banyak dan relevan dari platform yang bervariasi.

Narasi pada [Tabel IV.2](#page-4-0) yaitu "Rekan saya mampu mengumpulkan iklan sebanyak yang dibutuhkan khususnya di platform facebook.", secara eksplisit menyinggung dimensi rubrik (1) banyaknya iklan yang dikumpulkan dan (2) platform sumber yang digunakan, namun gagal membahas dimensi (1) relevansi iklan yang diberikan dan (2) kesulitan yang dihadapi ketika mengumpulkan iklan. Kemunculan pola cakupan parsial ini menegaskan bahwa identifikasi cakupan rubrik memerlukan mekanisme yang mampu mengenali hubungan antara narasi mahasiswa dan deskriptor rubrik meskipun keduanya menggunakan formulasi bahasa yang berbeda dengan menetapkan threshold deteksi indikator cakupan rubrik ('(),).

**IV.1.1.2 Karakteristik Indikator Koherensi**

Pelanggaran pada indikator koherensi skor narasi () ditunjukkan oleh pola kontradiksi semantik antara skor kuantitatif (dalam skala 1 sampai 5) dengan narasi kualitatif yang diberikan. Sebagaimana disajikan pada [Tabel IV.3,](#page-5-0) mahasiswa memberikan skor kuantitatif rendah namun dengan narasi cenderung tinggi positif.

Tabel IV.3. Kasus Skor Tidak Koheren dengan Narasi yang ditulis

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel IV.3](#page-5-0) menunjukkan mahasiswa yang memberikan skor 1 untuk aspek rubrik "Pengumpulan Iklan Lowongan Pekerjaan.", dengan narasi "dia sangat rajin melebihi seluruh rekan tim.". Terjadi ketidakselarasan antara skor 1 yang pada idealnya menunjukkan kinerja yang rendah, namun disini narasi cenderung menggambarkan kinerja yang baik.

Ketidakselarasan tersebut membuktikan terjadinya pemisahan terhadap mekanisme pemberian skor dengan narasi yang menjustifikasi nilai yang diberikan, menimbulkan diskrepansi antara skor kuantitatif dan narasi feedback. Mahasiswa umumnya mampu menghasilkan skor kuantitatif, namun mengalami kesulitan dalam menulis narasi kualitatif, ataupun kondisi sebaliknya, sebagaimana disajikan pada [Tabel IV.4.](#page-6-0)

Tabel IV.4. Kasus Inkoherensi Skor secara Parsial

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel IV.4](#page-6-0) menyajikan contoh inkoherensi di mana mahasiswa memilih skor kuantitatif 5, tetapi dengan narasi yang sebatas menyatakan "Baik dalam kontribusinya.". Jika mengacu pada rubrik, skor 5 berpasangan dengan standar deskriptif "Sangat baik.", tidak munculnya kata penguat "Sangat." dalam narasi menunjukkan artikulasi skor 5 yang belum memenuhi standar rubrik. Kondisi tersebut dapat dikategorikan sebagai kasus dimana teks mengalami penurunan akurasi penilaian sebesar satu hingga dua tingkat di bawah standar rubrik. Temuan ini menunjukkan bahwa proses identifikasi koherensi tidak hanya memerlukan pengenalan topik yang sama, tetapi juga kemampuan membedakan tingkat kualitas yang direpresentasikan dalam narasi

**IV.1.1.3 Karakteristik Indikator Kedalaman Elaborasi**

Pelanggaran pada indikator elaborasi (I) ditunjukkan oleh narasi feedback yang sangat pendek, sehingga tidak memungkinkan untuk memuat informasi bermakna, dengan contoh yang disajikan pada [Tabel IV.5.](#page-7-0) Kasus ini mengonfirmasi bahwa adanya hambatan mahasiswa dalam mengartikulasikan penilaian mereka ke dalam bentuk narasi yang sesuai dengan rubrik.

Tabel IV.5. Kasus Feedback dengan Elaborasi Singkat

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Selain kasus yang disajikan pada [Tabel IV.5,](#page-7-0) tercatat adanya fenomena inflasi tekstual tanpa makna. Sebagai contoh, kasus yang muncul dengan narasi "Rekan saya sangat baik dalam pengumpulan dan pengekstrakan data karena ia sangat cepat bahkan nomor 1 tercepat dalam kelompok kami dalam pengumpulan dan pengekstrakan data, saking cepatnya dia juga membantu saya dalam mengumpulkan data di Facebook karena tugas yang dia kerjakan sudah selesai.". Dalam contoh tersebut, narasi memiliki panjang 36 kata yang bersifat repetitif dan berputar-putar menggunakan struktur kalimat pengisi tanpa menambah substansi baru.

Fenomena tersebut menjadi kelemahan jika sistem hanya melakukan perhitungan kuantitas jumlah kata secara murni, karena teks dapat dianggap memenuhi indikator elaborasi (I) meskipun tidak memiliki bobot substansi. Hal ini membuktikan bahwa indikator kedalaman elaborasi (I) tidak dapat digunakan sebagai tolak ukur tunggal, melainkan harus dipadukan dengan indikator lainnya untuk mendeteksi kesesuaian antara volume teks dan substansi yang dapat diobservasi tanpa memerlukan interpretasi manusia.

**IV.1.1.4 Karakteristik Indikator Relevansi Topik**

Pelanggaran pada indikator relevansi topik (&) ditunjukkan oleh munculnya penyimpangan isi narasi feedback dengan aspek rubrik yang sedang dinilai. Pada contoh yang disajikan dalam [Tabel IV.6](#page-8-0) untuk aspek rubrik penilaian "Penggabungan Data dengan Kelompok Lain.", mahasiswa menuliskan narasi: "Saya memang kurang berkomunikasi namun saya mencoba menjadi pendengar yang baik.". Teks tersebut tidak membahas sama sekali terkait penggabungan data yang telah dilakukan, alih-alih membahas mengenai aspek "Komunikasi", yaitu kriteria rubrik lain yang tidak relevan dengan pertanyaan.

Tabel IV.6. Kasus Narasi Tidak Relevan dengan Aspek Rubrik Pertanyaan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Kasus lain yang disajikan pada [Tabel IV.7](#page-9-0) merupakan fenomena dimana relevansi terjadi secara parsial ketika terdapat overlap terminologi dalam rubrik yang digunakan pada Lampiran 10.

Tabel IV.7. Kasus Narasi Feedback Tidak Relevan Sebagian

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Dalam [Tabel IV.7,](#page-9-0) aspek rubrik yang sedang dinilai adalah "Penggabungan Data dengan Kelompok Lain.", namun mahasiswa menuliskan narasi "Dia sudah mengumpulkan sebagian iklan lowongan kerja.". Narasi tersebut secara substansi berisikan mengenai aspek lain, yaitu "Pengumpulan iklan lowongan pekerjaan". Ketidaksesuaian ini disebabkan oleh pertanyaan yang berfokus pada penggabungan data, yang secara tidak langsung berhubungan dengan proses pengumpulan data.

Kondisi tersebut menegaskan bahwa deteksi relevansi (&) tidak dapat dilakukan melalui pencocokan kata kunci sederhana, melainkan memerlukan mekanisme yang mampu membedakan kesamaan terminologi dasar dari kesesuaian semantik terhadap aspek rubrik yang sedang dinilai.

Secara keseluruhan, analisis terhadap data historis menunjukkan bahwa permasalahan kualitas feedback mahasiswa tidak hanya ditandai oleh rendahnya volume narasi, tetapi juga oleh ketidaklengkapan informasi, ketidaksesuaian antara skor dan justifikasi, serta penyimpangan topik terhadap aspek rubrik yang dinilai. Temuan tersebut menunjukkan bahwa setiap indikator merepresentasikan karakteristik permasalahan yang berbeda sehingga kebutuhan deteksinya tidak dapat diasumsikan bersifat seragam. Karakteristik tersebut selanjutnya menjadi dasar untuk menganalisis konsekuensi komputasional dari setiap indikator dan menentukan pendekatan yang sesuai pada perancangan pipeline digital scaffolding sebagaimana dibahas pada subbab berikutnya.

**IV.1.2 Hasil Kuantifikasi Masalah**

Analisis kuantifikasi dilakukan dengan mengamati 10.098 data feedback historis dengan detail yang disajikan pada [Tabel IV.8.](#page-10-0) Setiap data digunakan untuk mengidentifikasi kesenjangan yang terjadi pada pengisian assessment di tengah semester dan akhir semester pembelajaran, distribusi panjang teks narasi, perbandingan self dengan peer assessment, serta selisih skor pada self dan peer assessment.

Tabel IV.8. Detail Data Historis Assessment sebelum Dikomputasi

Jenis Assesment  |  Fase  |  Jumlah Mahasiswa yang Merespons (Assessor)  |  Rata-Rata Skor yang diberikan (Skala 1-5)  |  Standar Deviasi
Self  |  Tengah Semester  |  94  |  1.034  |  4,156  |  0,531
Akhir Semester  |  86  |  946  |  4,012  |  0,485
Peer  |  Tengah Semester  |  95  |  4.455  |  4,292  |  0,427
Akhir Semester  |  95  |  3.663  |  4,119  |  0,565

Berdasarkan detail yang disajikan pada [Tabel IV.8,](#page-10-0) rata-rata skor peer assessent  memiliki nilai yang jauh lebih tinggi dibandingkan dengan self assessment. Meskipun demikian, skor peer assessment memiliki variasi yang lebih tinggi pada akhir semester, ditunjukan dengan standar deviasi yang menyentuh nilai 0,565. Selain itu, terjadi fenomena reduksi jumlah assessor seiring waktu yang menjadi sinyal penurunan keterlibatan mahasiswa, mengakibatkan penyusutan 792 data pada peer assessment, dan 88 data pada self assessment.

[Gambar IV.1](#page-11-0) menyajikan perbandingan rata-rata jumlah kata dalam narasi feedback self dan peer assessment pada periode pengisian tengah semester dan akhir semester.

Gambar IV.1 Perbandingan Rata-Rata Jumlah Kata antar Self dan Peer

Berdasarkan [Gambar IV.1](#page-11-0), tercatat bahwa self assessment pada periode tengah semester memiliki volume narasi tertinggi dengan rata-rata 31 kata, yang kemudian menurun menjadi 24 kata pada akhir semester. Pada sisi lain, peer assessment secara konstan menunjukkan volume yang lebih rendah, yakni dengan rata-rata 14 kata pada tengah semester, sebelum terjadi penurunan hingga 11 kata pada akhir semester.

Kesenjangan yang persisten antara self dan peer assessment di kedua periode pengisian mengindikasikan adanya asimetri sistemik, di mana mahasiswa cenderung menginvestasikan elaborasi yang lebih dalam ketika mengevaluasi diri sendiri dibandingkan teman sejawat. Lebih lanjut, penurunan volume pada kedua instrumen mengisyaratkan adanya efek kelelahan seiring akumulasi beban akademik.

[Gambar IV.2](#page-12-0) menyajikan karakteristik sebaran jumlah kata di balik nilai rata-rata pada [Gambar IV.1](#page-11-0) sebelumnya untuk self dan peer assessment pada setiap periode pengisian.

Gambar IV.2 Sebaran Jumlah Kata antar Peer dan Self Assessment

Berdasarkan [Gambar IV.2](#page-12-0), seluruh kluster data menunjukkan pola distribusi miring ke kanan (positive skewness), dengan konsentrasi frekuensi tertinggi pada rentang 0 hingga 20 kata. Pada fase tengah semester, self assessment mencatat mean 30,6 kata dan median 24 kata, yang menurun menjadi mean 23,7 kata dan median 19 kata pada fase akhir semester. Di sisi lain, peer assessment menunjukkan sebaran yang lebih rendah secara konsisten, dengan mean 13,3 kata dan median 12 kata pada fase tengah semester, sebelum terjadi degradasi dengan mean 11,3 kata dan median 10 kata pada fase akhir semester.

Kondisi median yang secara konsisten berada di bawah mean pada seluruh kluster mengonfirmasi bahwa distribusi didominasi oleh narasi pendek, dengan nilai ratarata yang tinggi dipengaruhi oleh sebagian kecil narasi panjang. Pola ini memiliki implikasi terhadap indikator kedalaman elaborasi, yaitu jika mayoritas respons berada di bawah 20 kata, terdapat risiko bahwa feedback yang diberikan bersifat superfisial dan kurang memuat elaborasi diagnostik yang bermakna bagi penerima feedback (assessee). Kondisi ini menjadi landasan empiris untuk penentuan threshold indikator kedalaman elaborasi ('(),I) pada tahapan eksperimen selanjutnya.

[Gambar IV.3](#page-13-0) menunjukkan bahwa panjang narasi tidak mengikuti pola peningkatan maupun penurunan yang konsisten terhadap skor kuantitatif. Distribusi panjang narasi pada skor 1 hingga skor 5 saling bertumpang tindih pada hampir seluruh kategori skor. Mahasiswa yang memberikan skor rendah (1–2) tidak selalu menulis narasi yang lebih singkat dibandingkan mahasiswa yang memberikan skor tinggi (4–5), demikian pula mahasiswa yang memberikan skor tinggi tidak secara konsisten menghasilkan narasi yang lebih panjang. Temuan ini menunjukkan bahwa besarnya skor numerik tidak dapat digunakan sebagai indikator tingkat elaborasi narasi feedback sendirian.

Gambar IV.3 Perbandingan Pola Assessment antar Skor dan Panjang Narasi

[Gambar IV.3](#page-13-0) mengindikasikan bahwa kemampuan mahasiswa dalam memberikan skor, tidak selalu diikuti dengan kemampuan mengartikulasikannya ke dalam narasi yang bermakna dan sesuai dengan skor yang diberikan.

Lebih lanjut, [Gambar IV.3](#page-13-0) memperjelas bahwa narasi self assessment secara konsisten lebih panjang dibanding peer assessment, dengan selisih 10-30 kata. Didukung oleh konteks budaya kolektivits di Indonesia, pola ini mengindikasikan bahwa mahasiswa cenderung berhati-hati untuk memberikan penilaian rekan sejawat, sehingga feedback cenderung berisikan deskripsi umum dan menghindari evaluasi yang mengancam harmoni kelompok.

Lebih jauh, [Gambar IV.4](#page-14-0) menyajikan perbandingan skor dan panjang narasi berdasarkan periode pengisian assessment. Ditemukan bahwa degradasi panjang narasi terjadi secara relatif merata pada seluruh rentang skor, baik pada self maupun peer assessment.

Gambar IV.4 Pola Periode Pengisian antar Skor dan Panjang Narasi

Pola pada [Gambar IV.4](#page-14-0) mengindikasikan bahwa penurunan panjang narasi bersifat struktural, konsisten dan tidak terbatas pada rentang skor tertentu. Penurunan volume narasi tersebut dapat diinterpretasikan sebagai indikasi adanya perubahan dalam keterlibatan mahasiswa terhadap proses assessment, meskipun penelitian ini tidak secara langsung mengukur aspek keterlibatan kognitif tersebut.

Gambar IV.5 menyajikan distribusi frekuensi rata-rata skor penilaian untuk setiap mahasiswa dalam self dan peer assessment untuk seluruh periode pengisian.

Gambar IV.5 Distribusi Skor Antara Self dan Peer Assessment

Berdasarkan [Gambar IV.5,](#page-0-0) ditemukan distribusi peer assessment dominan pada skor 4 dan 5, sementara self assessment memiliki sebaran pada skor yang lebih rendah. Hal tersebut menunjukkan bahwa mahasiswa cenderung memberikan skor yang lebih tinggi pada rekan sejawat dibandingkan dengan diri sendiri. Berdasarkan framework feedback litracy yang telah dijelaskan pada subbab II.1.8, pola ini dipahami sebagai leniency bias yang didorong oleh dinamika interpersonal, khususnya bias pertemanan pada kelompok (Panadero et al., 2017). Kondisi ini sejalan dengan temuan sebelumnya bahwa narasi pada peer assessment cenderung lebih singkat dan kurang mendalam.

Temuan tersebut menjadi semakin krusial jika dihubungkan dengan data penurunan volume narasi di akhir semester. Mahasiswa tampak terbiasa mengeksekusi penilaian kuantitatif secara instan dengan memberikan skor tinggi, meskipun terdapat subjektivitas dan ketidakselarasan. Namun, tidak terdapat peningkatan dalam menguraikan narasi yang menjadi dasar pertimbangan angka tersebut. Hal tersebut menegaskan bahwa kemudahan mahasiswa dalam mendistribusikan angka tidak diiringi oleh kemampuan mengartikulasikan alasan evaluatif secara naratif.

Kondisi tersebut menunjukkan adanya ruang urgensi untuk intervensi yang dapat membantu mahasiswa secara kognitif sehingga dapat menghubungkan penilaian kuantitatif dengan justifikasi naratif yang lebih representatif.

Seluruh temuan yang telah dipaparkan mengonfirmasi tiga hasil utama, yaitu (1) adanya asimetri alokasi effort atau usaha antara self assessment dan peer assessment, (2) ditemukannya penurunan kuantitas narasi lintas waktu antara tengah semester dan akhir semester, serta (3) ditemukannya fenomena yang terisolasi antara nilai numerik dengan kedalaman eksplorasi teks. Ketiga hal tersebut memperkuat motivasi penelitian, di mana kemampuan mahasiswa dalam mengartikulasi skor ke dalam bentuk narasi feedback tidak berkembang secara alami tanpa adanya intervensi, dan hanya melalui pengulangan proses pengisian instrumen.

**IV.1.3 Kebutuhan Eksperimen dan Objektif Solusi**

Subbab ini adalah manifestasi dari tahapan perumusan kebutuhan eksperimen yang didefinisikan pada subbab III.6.2. Objektif dari solusi didasarkan pada temuan empiris subbab IV.1.1 hingga IV.1.2, yang menegaskan bahwa skor kuantitatif dan narasi pendukung tidak selalu berkembang secara selaras selama proses assessment. Adanya penurunan kualitas narasi mengindikasikan perlunya sebuah instrumen eksperimen komputasional yang mampu mengevaluasi teks dan memandu mahasiswa secara proaktif selama proses penulisan berlangsung.

Untuk memenuhi kebutuhan tersebut, instrumen eksperimen dirancang dengan karakteristik sebagai berikut:

1. Instrumen beroperasi secara deterministik untuk mengevaluasi pemenuhan keempat indikator tekstual, yaitu cakupan rubrik, koherensi skor, kedalaman elaborasi, dan relevansi topik.
2. Instrumen dirancang untuk memberikan intervensi scaffolding berupa panduan tekstual secara proaktif apabila narasi feedback mahasiswa belum memenuhi standar indikator tekstual berdasarkan threshold yang telah dikalibrasi.
3. Pemberian intervensi scaffolding bersifat non-koersif dan akan berhenti secara otomatis saat narasi telah memenuhi seluruh kriteria operasional.

Batasan eksperimen pada instrumen ini difokuskan murni pada evaluasi keempat indikator tekstual berdasarkan empat indikator yang dapat diukur secara komputasional. Evaluasi ini tidak mencakup aspek interpretatif atau linguistik tingkat lanjut yang membutuhkan justifikasi manusia secara manual, sebagaimana telah dibatasi pada subbab I.7.

Keberhasilan solusi dievaluasi melalui dua tahapan yang selaras dengan pertanyaan penelitian. Tahap pertama menjawab RQ1, yaitu mengevaluasi kemampuan pipeline mendeteksi keempat indikator tekstual menggunakan metrik precision, recall, dan F1-score. Tahap kedua menjawab RQ2 melalui pilot study untuk mengukur perbedaan tingkat pemenuhan indikator tekstual antara kelompok treatment dan kelompok kontrol menggunakan analisis multivariat, analisis univariat, dan estimasi effect size.

**IV.2 Hasil Anotasi Dataset**

Subbab ini merupakan manifestasi dari metodologi anotasi dataset yang telah didefinisikan pada subbab III.6.3.1. Sebagaimana dijelaskan, proses anotasi terdiri dari beberapa tahapan, yaitu: (1) pre-processing untuk melakukan dekomposisi terhadap rubrik, hasil tahapan ini disajikan pada subbab [IV.2.1.](#page-2-0) Kemudian, untuk menjaga konsistensi, (2) implementasi panduan anotasi disajikan pada Lampiran 1 sebelum dilakukan proses anotasi. Setelah itu, (3) sampel hasil anotasi disajikan pada subbab [IV.2.2](#page-3-0), sebelum dilakukan (4) validasi pada subbab [IV.2.2.1.](#page-5-0)

**IV.2.1 Hasil Dekomposisi Rubrik**

Sebagai implementasi hasil dari pre-processing, sebagaimana didefinisikan pada subbab III.6.3.2A, tahapan ini menghasilkan dua feature set, yaitu: (1) cakupan dan relevansi topik (def-\),A) yang disajikan pada subbab [IV.2.1.1,](#page-3-1) serta feature set  koherensi skor narasi (de4-\),A) yang disajikan pada subbab [IV.2.1.2.](#page-3-2)

**IV.2.1.1 Hasil Feature Set Cakupan dan Relevansi Topik**

Berdasarkan proses yang didefinisikan pada subbab III.6.3.2.A.2, dekomposisi akhir yang diperoleh disajikan pada Lampiran 13. Feature set ini memiliki total 26 unit yang digunakan sebagai komponen utama indikator cakupan rubrik () dan relevansi topik (&) dalam melakukan vector embedding dan cosine similarity, sebagaimana dijelaskan dalam Lampiran 4.

**IV.2.1.2 Hasil Feature Set Koherensi Skor**

Dengan menggunakan proses yang telah didefinisikan pada subbab III.6.3.2.A.2, hasil dekomposisi disajikan pada Lampiran 14 dengan total 46 unit. Setiap unit digunakan sebagai komponen utama dalam melakukan komputasi indikator koherensi skor dan narasi (), dengan himpunan didapatkan dari aturan mutual exclusivity yang didefinisikan pada subbab III.6.3.5B.

**IV.2.2 Sampel Hasil Anotasi**

Berdasarkan metodologi dan skema multi-label binary classification yang telah diuraikan pada subbab III.6.3.2B, proses anotasi dilaksanakan terhadap sampel acak sebanyak 384 narasi feedback menggunakan hasil dekomposisi rubrik pada subbab [IV.2,](#page-2-1) serta panduan yang telah didefinisikan pada Lampiran 1. Untuk menjaga kerahasiaan data feedback, subbab ini hanya menyajikan sampel dari hasil anotasi dataset.

Anotasi menghasilkan dua dataset berbeda berdasarkan feature set yang didefinisikan pada subbab [IV.2.1](#page-2-0). Dataset yang pertama merupakan manifestasi dari cakupan dan relevansi feature set (def-\),A), dengan sampel anotasi disajikan pada Lampiran 11. Dataset kedua merupakan manifestasi feature set koherensi skor dan narasi (de4-\),A), dengan sampel anotasi yang disajikan pada Lampiran 12.

**IV.2.2.1 Statistik Dataset**

Sebagai hasil akhir dari prosedur anotasi bersumber dari 384 baris data feedback yang dijelaskan pada subbab III.6.3.2C, setiap baris narasi dipasangkan dengan beberapa unit kriteria rubrik untuk dievaluasi secara independen. Proses kombinasi ini mentransformasi 384 narasi menjadi volume data komputasional dengan distribusi sebagai berikut:

1. 1.100 pasangan data untuk indikator cakupan rubrik (). Narasi dipasangkan secara eksklusif dengan unit kriteria dari aspek yang sedang menjadi fokus penilaian untuk mendeteksi kehadiran elemen penilaian spesifik dalam narasi.
2. 1.990 pasangan data untuk indikator koherensi skor dan narasi (). Volume ini didapatkan oleh hubungan narasi feedback dengan deskripsi capaian spesifik (\),A,(^ ) pada skala skor 1, 3, dan 5 secara terpisah.
3. 9.984 pasangan data untuk indikator relevansi topik (&). Jilah ini mencapai titik tertinggi karena metode deteksi yang bersifat global. Setiap narasi dilakukan komputasi silang terhadap total 26 unit dekomposisi kriteria untuk mengidentifikasi apakah narasi menyimpang ke aspek lain di luar pertanyaan.

Distribusi label "TRUE" dan "FALSE" dari hasil anotasi kombinasi pasangan tersebut disajikan pada [Gambar IV.6.](#page-4-0)

Gambar IV.6. Distribusi label TRUE dan FALSE pada Dataset

Dataset ini mencakup sembilan aspek rubrik evaluasi dari mata kuliah yang menerapkan PjBL, yaitu pengumpulan iklan lowongan kerja, pemahaman terhadap isi iklan, pembuatan struktur data, penginputan data ke Excel, penggabungan data dengan kelompok lain, kolaborasi dan kerjasama tim, komunikasi, inisiatif dan pemecahan masalah, serta manajemen waktu. Sebagaimana didefinisikan pada Lampiran 10. Seluruh dataset ini dianalisis lebih lanjut pada subbab [IV.2.2.1A](#page-5-1) dan [IV.2.2.1B.](#page-6-0)

**A. Representasi Dataset**

Sebagai hasil dari prosedur penarikan sampel yang telah ditetapkan pada subbab III.6.3.1, distribusi data pada sampel anotasi dievaluasi untuk memastikan ecological validity dari dataset tersebut. [Gambar IV.7](#page-5-2) mengilustrasikan hasil distribusi narasi yang tidak memenuhi indikator cakupan rubrik (), koherensi skor dan narasi (), serta relevansi topik pada sampel yang telah dianotasi (&).

Gambar IV.7. Distribusi Tiga Indikator Pada Sampel Anotasi

Berdasarkan [Gambar IV.7,](#page-5-2) terindikasi bahwa terdapat 328 feedback yang tidak memenuhi cakupan rubrik (), 266 narasi feedback yang tidak selaras dengan skor kuantitatif (), serta 90 feedback memiliki narasi yang tidak relevan (&). Hal ini secara langsung mengonfirmasi temuan Setiawan (2026a) mengenai tingginya angka ketidakselarasan antara skor narasi dalam kondisi aktual di lapangan.

Di sisi lain, [Gambar IV.8](#page-6-1) menyajikan distribusi jumlah kata pada keseluruhan dataset. Sumbu X merepresentasikan jumlah kata untuk setiap narasi, dan sumbu Y merepresentasikan frekuensi kemunculan narasi dengan panjang kata spesifik.

Gambar IV.8. Histogram Jumlah Kata Pada Dataset Anotasi

[Gambar IV.8](#page-6-1) menyajikan distribusi jumlah kata pada seluruh narasi feedback. Distribusi menunjukkan pola right-skewed dengan konsentrasi terbesar pada narasi yang relatif pendek. Secara visual, terlihat adanya titik perubahan distribusi pada kisaran 25 kata, yaitu batas ketika frekuensi narasi mulai bergeser dari kluster padat menuju distribusi yang lebih jarang. Berdasarkan karakteristik distribusi tersebut, threshold indikator kedalaman elaborasi I ditetapkan sebesar 25 kata. Nilai ini merepresentasikan karakteristik aktual data yang digunakan dalam penelitian dan menjadi dasar operasional untuk membedakan narasi pendek dan narasi panjang pada analisis selanjutnya.

**B. Analisis Komplementaritas Antar Indikator**

Analisis ini bertujuan untuk memverifikasi tiga hal secara empiris, yaitu: (1) apakah skala masalah pada data aktual sesuai dengan yang diidentifikasi pada studi pendahuluan, (2) apakah keempat indikator komputasi yang didefinisikan pada Tabel III.3 bersifat komplementer dan tidak redundan, serta apakah threshold elaborasi ('(),I) bernilai 25 kata memiliki justifikasi empiris terhadap kualitas cakupan rubrik.

[Gambar IV.9](#page-7-0) menyajikan distribusi indikator komputasi tekstual narasi feedback. Dengan sumbu X merepresentasikan indikator cakupan rubrik (), koherensi skor

dan narasi (), serta relevansi topik (&), sebagaimana didefinisikan pada Tabel III.3.

Gambar IV.9 Distribusi Empat Indikator Tekstual Narasi Feedback

Berdasarkan [Gambar IV.9,](#page-7-0) menunjukkan distribusi pemenuhan indikator tekstual pada seluruh narasi feedback. Berdasarkan visualisasi tersebut, indikator cakupan rubrik memiliki tingkat ketidakterpenuhan tertinggi, yaitu 328 dari 384 narasi (85,4%). Indikator koherensi skor dan narasi menunjukkan tingkat ketidakterpenuhan sebesar 69,3%, sedangkan indikator relevansi topik & memiliki tingkat pemenuhan tertinggi dengan proporsi narasi yang masih berada pada topik yang sesuai mencapai 76,6%. Distribusi ini menunjukkan bahwa permasalahan utama pada feedback mahasiswa lebih banyak berkaitan dengan kualitas justifikasi dan kelengkapan evaluasi dibandingkan dengan penyimpangan topik pembahasan.

[Gambar IV.10](#page-8-0) menyajikan kontigensi berpasangan pada distribusi pemenuhan indikator. Dengan pemetaan cakupan rubrik () & relevansi topik (&), cakupan rubrik () & koherensi skor dan narasi (), serta relevansi topik (&) & koherensi skor dan narasi (). Pemetaan tersebut mengungkap pola hubungan yang memvalidasi desain keempat indikator sebagai konstruk yang komplementer.

Gambar IV.10 Hubungan Antar Indikator

Berdasarkan [Gambar IV.10](#page-8-0) pada pasangan indikator cakupan rubrik dan relevansi topik, ditemukan bahwa 246 dari 384 narasi yang tidak memenuhi cakupan rubrik tetap memenuhi indikator relevansi topik. Temuan ini menunjukkan bahwa mahasiswa umumnya masih membahas aspek yang sedang dinilai, namun belum mengembangkan seluruh dimensi evaluasi yang tercantum dalam rubrik. Dengan demikian, indikator cakupan rubrik dan relevansi topik merepresentasikan dua konstruk yang berbeda dan saling melengkapi. Relevansi topik mengukur kesesuaian fokus pembahasan terhadap aspek yang ditanyakan, sedangkan cakupan rubrik mengukur kelengkapan dimensi evaluatif yang muncul dalam narasi.

Pada pasangan cakupan rubrik dan koherensi skor-narasi, tercatat bahwa 237 dari 384 narasi yang tidak memenuhi cakupan rubrik juga tidak memenuhi indikator koherensi. Pola ini menunjukkan bahwa keterbatasan cakupan sering disertai dengan lemahnya justifikasi terhadap skor yang diberikan. Ketika narasi hanya memuat sedikit informasi mengenai kriteria rubrik, ruang bagi narasi untuk merepresentasikan tingkat pencapaian yang sesuai dengan skor juga menjadi terbatas. Temuan ini menjelaskan tingginya co-occurency kegagalan kedua indikator sekaligus mengindikasikan adanya hubungan substantif antara kelengkapan evaluasi dan kemampuan narasi dalam mendukung skor yang diberikan.

Pada pasangan relevansi topik dan koherensi skor-narasi, tidak ditemukan hubungan yang signifikan. Sebagian besar narasi yang relevan terhadap aspek yang ditanyakan tetap dapat gagal memenuhi koherensi skor-narasi. Temuan ini menunjukkan bahwa membahas topik yang benar tidak secara otomatis menghasilkan justifikasi yang sesuai terhadap tingkat skor yang diberikan. Dengan demikian, relevansi topik dan koherensi skor-narasi merepresentasikan dua dimensi indikator tekstual narasi feedback yang relatif independen.

Pola co-occurency ini menjelaskan mengapa kombinasi kegagalan cakupan dan koherensi mendominasi distribusi, dengan analisis yang disajikan pada [Gambar](#page-9-0)  [IV.11.](#page-9-0)

Gambar IV.11 Pola Overlap Indikator Tidak Terpenuhi

Berdasarkan [Gambar IV.11,](#page-9-0) overlap antara kegagalan indikator cakupan rubrik dan koherensi skor-narasi merupakan pola yang paling dominan dengan 177 narasi. Pola ini diikuti oleh narasi yang hanya gagal pada indikator cakupan rubrik sebanyak 69 narasi (18,0%), serta narasi yang gagal pada ketiga indikator secara bersamaan sebanyak 60 narasi (15,6%). Sebaliknya, kegagalan yang hanya melibatkan indikator relevansi topik relatif jarang ditemukan, dengan hanya 3 narasi yang gagal pada indikator tersebut secara terisolasi. Distribusi ini menunjukkan bahwa permasalahan pada dataset lebih banyak berkaitan dengan cakupan aspek evaluasi dan keselarasan antara skor dan narasi dibandingkan dengan kesesuaian topik pembahasan.

Temuan ini memberikan bukti empiris bahwa ketiga indikator menangkap pola kegagalan yang berbeda dan tidak bersifat redundan. Sebagian narasi hanya gagal pada satu indikator tertentu, sementara sebagian lainnya menunjukkan kombinasi kegagalan pada dua atau tiga indikator sekaligus. Variasi pola tersebut mengindikasikan bahwa kualitas feedback mahasiswa tidak dapat direpresentasikan secara memadai oleh satu indikator tunggal. Oleh karena itu, penggunaan pendekatan multi-indikator sebagaimana dirancang pada penelitian ini memperoleh justifikasi empiris dari distribusi data aktual yang diamati.

[Gambar IV.12](#page-10-0) menyajikan jumlah narasi feedback yang termasuk ke dalam kategori panjang (≥ 25 kata) dan kategori pendek (< 25 kata). Lebih jauh, gambar tersebut mengaitkan hubungan jumlah kata dengan pemenuhan indikator cakupan rubrik ().

Gambar IV.12 Pemenuhan Indikator Cakupan Rubrik berdasarkan Panjang

Sebagaimana diungkapkan pada [Gambar IV.12](#page-10-0) menunjukkan distribusi panjang narasi berdasarkan threshold 25 kata yang digunakan pada indikator kedalaman elaborasi I. Dari 384 narasi yang dianalisis, sebanyak 328 narasi (85,4%) termasuk dalam kategori pendek (<25 kata), sedangkan hanya 56 narasi (14,6%) yang termasuk kategori panjang (≥25 kata). Distribusi ini menunjukkan bahwa sebagian besar mahasiswa memberikan feedback dalam bentuk narasi yang relatif singkat.

Untuk mengevaluasi apakah panjang narasi berkaitan dengan kualitas isi yang lebih baik, dilakukan perbandingan terhadap pemenuhan indikator cakupan rubrik (). Hasil analisis menunjukkan bahwa narasi pendek memiliki coverage pass rate sebesar 13,1%, sedangkan narasi panjang mencapai 23,2%. Meskipun perbedaannya tidak terlalu besar, pola ini menunjukkan bahwa narasi yang lebih panjang memiliki peluang yang lebih tinggi untuk memuat elemen rubrik yang relevan.

Namun demikian, sebagian besar narasi panjang tetap tidak memenuhi indikator cakupan rubrik. Temuan ini menunjukkan bahwa panjang narasi tidak identik dengan kualitas isi narasi. Mahasiswa dapat menghasilkan narasi yang panjang tanpa membahas dimensi evaluasi yang diminta rubrik. Sebaliknya, narasi yang sangat singkat memiliki keterbatasan ruang untuk menjelaskan alasan penilaian secara rinci. Oleh karena itu, indikator kedalaman elaborasi I merepresentasikan dimensi yang berbeda dari indikator lainnya, yaitu kecukupan ruang informasi dalam narasi, bukan kualitas semantik dari isi narasi tersebut.

**IV.2.3 Validasi Hasil Anotasi**

Sesuai dengan prosedur yang didefinisikan pada subbab III.6.3.2D, validasi ground truth dilakukan melalui random sampling terhadap 384 data anotasi yang kemudian dilakukan review oleh dosen dengan keahlian pada Project-Based Learning.

Hasil validasi menegaskan bahwa proses pelabelan telah dilakukan sesuai dengan definisi dan kriteria rubrik yang ditetapkan. Didukung oleh buku panduan anotasi pada Lampiran 1 yang berperan sebagai acuan, sehingga setiap keputusan label dapat ditelusuri kembali ke aturan yang eksplisit.

**IV.3 Hasil Pemodelan dan Kalibrasi Pipeline Digital Scaffolding**

Subbab ini merupakan manifestasi dari metodologi pemodelan sistem digital scaffolding yang telah didefinisikan pada subbab III.6.3. Pembahasan mencakup spesifikasi dari pipeline digital scaffolding yang disajikan pada subbab [IV.3.1,](#page-12-0) serta hasil evaluasi pendekatan embedding pada subbab [IV.3.2.](#page-14-0)

**IV.3.1 Spesifikasi Final Pipeline Digital Scaffolding**

Dengan menggunakan pendekatan semantic text similarity, sebagaimana dijelaskan pada Tabel III.13, arsitektur digital scaffolding dibangun sepenuhnya menggunakan model SBERT sebagai alat embedding. Mekanisme dari arsitektur ini disajikan pada [Gambar IV.13.](#page-13-0)

Direpresentasikan pada [Gambar IV.13,](#page-13-0) langkah pertama dalam pipeline digital scaffolding adalah melakukan embedding terhadap kriteria rubrik yang telah dilakukan proses dekomposisi, sebagaimana didefinisikan pada subbab III.6.3.2A. Kemudian, selama mahasiswa menulis feedback, narasi diproses secara real-time untuk dilakukan embedding dalam menentukan semantic similarity dengan kriteria rubrik.

Nilai semantic similarity digunakan sebagai landasan komputasi indikator cakupan rubrik (), koherensi skor dan narasi (), elaborasi (I), dan relevansi topik (&). Komputasi tersebut menghasilkan variabel kontekstual yang digunakan untuk memproduksi teks scaffolding akhir yang diberikan kepada mahasiswa.

Gambar IV.13 Desain Pipeline yang Dibangun

**IV.3.2 Hasil Evaluasi dan Kalibrasi Model**

Subbab ini merupakan manifestasi dari tahap kalibrasi instrumen yang didefinisikan pada subbab III.6.3.5. Evaluasi dilakukan dengan membandingkan hasil prediksi model terhadap dataset anotasi menggunakan mekanisme grid-search. Eksperimen ini memposisikan whole-text embedding sebagai konfigurasi baseline. Evaluasi kemudian difokuskan pada pengukuran dampak dari dua modifikasi komputasional, yaitu semantic chunking dan mutual exclusivity, guna menentukan konfigurasi pipeline akhir yang paling optimal beserta nilai threshold. Mekanisme kalibrasi ini disajikan pada Gambar IV.14.

Gambar IV.14. Mekanisme Kalibrasi Model

**IV.3.2.1 Evaluasi Pendekatan Semantic Chunking**

Eksperimen ini mengevaluasi implementasi semantic chunking yang didefinisikan pada subbab III.6.3.5A terhadap indikator cakupan rubrik (), koherensi skor (), dan relevansi topik (&). [Tabel IV.9](#page-1-0) menyajikan perbandingan metrik F1-Score antara baseline whole-text embedding dengan metode semantic chunking terhadap indikator cakupan rubrik ().

Tabel IV.9. Performa Model Semantic Chunking terhadap Baseline

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual mpnet-base-v2  |  Whole Embedding  |  Text  |  0,27  |  0,5822  |  0,4415  |  0,8545
Semantic Chunking  |  0,27  |  0,5820  |  0,4406  |  0,8568
intfloat/multilingual-e5-base  |  Whole Embedding  |  Text  |  0,81  |  0,5926  |  0,4604  |  0,8314
Semantic Chunking  |  0,81  |  0,6002  |  0,4646  |  0,8476
intfloat/multilingual-e5-base + query/passage prefix  |  Whole Embedding  |  Text  |  0,81  |  0,5760  |  0,4315  |  0,8661
Semantic Chunking  |  0,81  |  0,5826  |  0,4327  |  0,8915
intfloat/multilingual-e5- large-instruct  |  Whole Embedding  |  Text  |  0,84  |  0,6131  |  0,5323  |  0,7229
Semantic Chunking  |  0,84  |  0,6140  |  0,5312  |  0,7275
denaya/indoSBERT-large  |  Whole Embedding  |  Text  |  0,36  |  0,6002  |  0,4940  |  0,7644
Semantic Chunking  |  0,37  |  0,6096  |  0,5000  |  0,7806
paraphrase-multilingual MiniLM-L12-v2  |  Whole Embedding  |  Text  |  0,16  |  0,5706  |  0,4166  |  0,9053
Semantic Chunking  |  0,16  |  0,5720  |  0,4167  |  0,9122

Data pada [Tabel IV.9](#page-1-0) menunjukkan bahwa penerapan semantic chunking secara konsisten memberikan peningkatan F1-Score pada mayoritas model. Model intfloat/multilingual-e5-large-instruct mencapai performa komputasional tertinggi dengan nilai F1 0,6140. Model spesifik bahasa Indonesia, denaya/indoSBERTlarge, juga mencatat eskalasi performa dari 0,6002 menjadi 0,6096. Peningkatan ini mengindikasikan bahwa segmentasi kalimat dapat mereduksi embedding dilution dengan mengisolasi unit informasi spesifik dari teks narasi yang panjang, suatu kondisi yang sangat ideal untuk menelusuri eksistensi kriteria pada indikator cakupan rubrik.

Evaluasi selanjutnya diterapkan pada indikator koherensi skor dan narasi (). Hasil komparasi metode pada indikator ini disajikan pada [Tabel IV.10.](#page-2-0) Pada evaluasi ini, dataset yang digunakan adalah feature-set yang didefinisikan pada IV.2.1.2, namun tidak mengaplikasikan aturan mutual exclusivity yang didefinisikan pada subbab III.6.3.5B.

Tabel IV.10. Performa Model Semantic Chunking terhadap Baseline

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual mpnet-base-v2  |  Whole Embedding  |  Text  |  0,44  |  0,4193  |  0,3129  |  0,6353
Semantic Chunking  |  0,45  |  0,4216  |  0,3170  |  0,6292
intfloat/multilingual-e5-base  |  Whole Embedding  |  Text  |  0,84  |  0,3751  |  0,2778  |  0,5775
Semantic Chunking  |  0,85  |  0,3829  |  0,3145  |  0,4894
intfloat/multilingual-e5-base + query/passage prefix  |  Whole Embedding  |  Text  |  0,83  |  0,3958  |  0,3011  |  0,5775
Semantic Chunking  |  0,83  |  0,3922  |  0,2969  |  0,5775
intfloat/multilingual-e5- large-instruct  |  Whole Embedding  |  Text  |  0,89  |  0,5020  |  0,4458  |  0,5745
Semantic Chunking  |  0,89  |  0,4974  |  0,4403  |  0,5714
denaya/indoSBERT-large  |  Whole Embedding  |  Text  |  0,45  |  0,4139  |  0,3226  |  0,5775
Semantic Chunking  |  0,45  |  0,4195  |  0,3186  |  0,6140
paraphrase-multilingual MiniLM-L12-v2  |  Whole Embedding  |  Text  |  0,48  |  0,3722  |  0,3189  |  0,4468
Semantic Chunking  |  0,39  |  0,3837  |  0,2790  |  0,6140

Pola performa pada [Tabel IV.10](#page-2-0) memperlihatkan dinamika yang berbeda dibandingkan indikator pertama. Meskipun beberapa model mengalami sedikit peningkatan, model dengan performa absolut tertinggi, intfloat/multilingual-e5 large-instruct, justru mengalami degradasi F1 dari 0,5020 menjadi 0,4974. Penurunan akurasi ini terjadi karena segmentasi kalimat menghilangkan konteks global dari narasi utuh. Indikator koherensi membutuhkan pemahaman terhadap struktur kohesi antarkalimat untuk mencocokkan sentimen evaluatif gradasi skor yang berdekatan.

Pola degradasi yang serupa terjadi pada indikator relevansi topik (&). [Tabel IV.11](#page-3-0) menyajikan perbandingan metrik evaluasi pada indikator tersebut.

Tabel IV.11. Performa Model & Semantic Chunking terhadap Baseline

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual mpnet-base-v2  |  Whole Embedding  |  Text  |  0,53  |  0,3071  |  0,3209  |  0,2944
Semantic Chunking  |  0,53  |  0,3200  |  0,3241  |  0,3160
intfloat/multilingual-e5-base  |  Whole Embedding  |  Text  |  0,84  |  0,2924  |  0,2418  |  0,3698
Semantic Chunking  |  0,84  |  0,2966  |  0,2408  |  0,3860
intfloat/multilingual-e5-base + query/passage prefix  |  Whole Embedding  |  Text  |  0,83  |  0,3188  |  0,2421  |  0,4668
Semantic Chunking  |  0,83  |  0,3202  |  0,2399  |  0,4811
intfloat/multilingual-e5- large-instruct  |  Whole Embedding  |  Text  |  0,85  |  0,4296  |  0,4265  |  0,4327
Semantic Chunking  |  0,85  |  0,4155  |  0,4076  |  0,4237
denaya/indoSBERT-large  |  Whole Embedding  |  Text  |  0,48  |  0,3605  |  0,2981  |  0.4560
Semantic Chunking  |  0,5  |  0,3705  |  0,3164  |  0,4470
paraphrase-multilingual MiniLM-L12-v2  |  Whole Embedding  |  Text  |  0,40  |  0,2575  |  0,1824  |  0,4381
Semantic Chunking  |  0,40  |  0,2586  |  0,1802  |  0,4578

[Tabel IV.11](#page-3-0) mengonfirmasi bahwa penerapan semantic chunking kembali menurunkan performa intfloat/multilingual-e5-large-instruct, dengan nilai F1 turun dari 0,4296 menjadi 0,4155. Indikator relevansi topik mengukur apakah narasi mahasiswa konsisten membahas kriteria target tanpa melenceng ke dimensi penilaian lain. Penilaian ini menuntut pemahaman alur narasi secara holistik, sehingga pemotongan kalimat justru merugikan kapabilitas inferensi model.

Sintesis dari ketiga tahapan pengujian ini menetapkan bahwa modifikasi semantic chunking hanya diimplementasikan secara operasional pada indikator cakupan rubrik (). Modifikasi ini dihindari pada indikator koherensi skor dan narasi () serta relevansi topik (&).

**IV.3.2.2 Evaluasi Pendekatan Mutual Exclusivity**

Eksperimen ini mengukur efektivitas penerapan aturan mutual exclusivity yang didefinisikan pada subbab III.6.3.5B. Evaluasi ini dilakukan secara eksklusif pada indikator koherensi skor dan rasi () untuk memitigasi tumpang tindih klasifikasi saat model membedakan gradasi makna pada tingkat penilaian rubrik yang berdekatan. [Tabel IV.12](#page-4-0) menyajikan perbandingan metrik komputasional antara baseline whole-text embedding degan sifat mutual exclusivity deterministik tersebut.

Tabel IV.12. Performa Model Mutual Exclusivity terhadap Baseline

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual-mpnet base-v2  |  Whole Text Embeeding  |  0,44  |  0,4193  |  0,3129  |  0,6353
Mutual Exclusivity  |  0,35  |  0,4315  |  0,3422  |  0,5836
intfloat/multilingual-e5-base  |  Whole Text Embeeding  |  0,84  |  0,3751  |  0,2778  |  0,5775
Mutual Exclusivity  |  0,84  |  0,3954  |  0,3717  |  0,4225
intfloat/multilingual-e5-base + query/passage prefix  |  Whole Text Embeeding  |  0,83  |  0,3958  |  0,3011  |  0,5775
Mutual Exclusivity  |  0,83  |  0,3932  |  0,3700  |  0,4195
intfloat/multilingual-e5-large instruct  |  Whole Text Embeeding  |  0,89  |  0,5020  |  0,4458  |  0,5745
Mutual Exclusivity  |  0,87  |  0,5314  |  0,4409  |  0,6687
denaya/indoSBERT-large  |  Whole Text Embeeding  |  0,45  |  0,4139  |  0,3226  |  0,5775
Mutual Exclusivity  |  0,40  |  0,4386  |  0,3879  |  0,5046

Variabel Bebas: Variabel Terikat
Model  |  Modifikasi  |  Optimal Threshold (ìîXï,X )  |  F1  |  Precision  |  Recall
paraphrase-multilingual-MiniLM L12-v2  |  Whole Text Embeeding  |  0,48  |  0,3722  |  0,3189  |  0,4468
Mutual Exclusivity  |  0,23  |  0,4024  |  0,3008  |  0,6079

[Tabel IV.12](#page-4-0) memperlihatkan bahwa penerapan aturan mutual exclusive memberikan eskalasi performa pada hampir seluruh kandidat model. Model paraphrase-multilingual-MiniLM-L12-v2 mencatatkan peningkatan F1 terbesar dari 0,3722 menjadi 0,4024, disusul oleh model spesifik bahasa Indonesia denaya/indoSBERT-large dari 0,4139 menjadi 0,4386. Lonjakan performa ini mengindikasikan bahwa mengindikasikan bahwa pembatasan ruang prediksi secara deterministik dapat membantu model dalam mendeteksi koherensi skor rubrik yang secara semantik berdekatan.

Setelah intervensi aturan ini diaplikasikan, model intfloat/multilingual-e5-largeinstruct makin kokoh mempertahankan posisinya sebagai representasi dengan performa tertinggi, mencapai skor F1 0,5314. Hal ini menegaskan bahwa kombinasi antara arsitektur model instruction-tuning dengan membatasi ambiguitas prediksi dapat meningkatkan kualitas deteksi. Oleh karena itu, pendekatan mutual exclusivity ditetapkan sebagai konfigurasi untuk indikator koherensi skor dan narasi ().

**IV.3.2.3 Konfigurasi Akhir Model & Temuan Eksperimen**

Sintesis hasil pada subbab [IV.3.2.1](#page-1-1) dan [IV.3.2.2](#page-4-1) menunjukkan bahwa model intfloat/multilingual-e5-large-instruct secara konsisten mencapai nilai F1 tertinggi di antara seluruh kandidat. Rangkaian pengujian komparatif ini menghasilkan temuan bahwa spesialisasi korpus pada bahasa Indonesia melalui model indoSBERT-large tidak melampaui performa model multilingual yang dilengkapi dengan instruction-tuning eksplisit. Arsitektur yang dikendalikan oleh instruksi tugas spesifik terbukti memiliki performa yang lebih tinggi dalam menangani kompleksitas dan ambiguitas semantik pada narasi feedback mahasiswa. Oleh karena itu, intfloat/multilingual-e5-large-instruct dipilih sebagai model embedding utama.

Berdasarkan sintesis tersebut, konfigurasi akhir pipeline ditetapkan sebagai kombinasi dari:

1. Model "embedding intfloat/multilingual-e5-large-instruct" untuk komputasi indikator cakupan rubrik  $(f_1)$ , koherensi skor dan narasi  $(f_2)$ , serta relevansi topik  $(f_4)$ .
2. Strategi semantic chunking untuk komputasi indikator cakupan rubrik  $(f_1)$ .
3. Mekanisme mutual exclusivity untuk indikator koherensi skor dan narasi  $(f_2)$ .
4. Pendekatan whole-text embedding murni untuk mengevaluasi indikator relevansi topik  $(f_4)$ .
5. Aturan heurstik komputasi jumlah kata leksikal untuk indikator kedalaman elaborasi  $(f_3)$  dengan nilai minimum 25 kata, sebagaimana didefinisikan pada subbab IV.2.2.1.

Performa akhir pada dataset disajikan pada Tabel IV.13.

Tabel IV.13. Performa Akhir Model untuk Setiap Indikator

intfloat/multilingual-e5-large-instruct
Indikator  |  Optimal Threshold $(\theta_{sim,i})$  |  F1  |  Precision  |  Recall
Cakupan Rubrik $(f_1)$  |  0.84  |  0.6140  |  0.5312  |  0.7275
Koherensi Skor dan Narasi $(f_2)$  |  0.87  |  0.5314  |  0.4409  |  0.6687
Kedalaman Elaborasi $(f_3)$  |  25 kata  |  -  |  -  |  -
Relevansi Topik $(f_4)$  |  0.85  |  0.4296  |  0.4265  |  0.4327

Berdasarkan Tabel IV.13, indikator relevansi topik ( $f_4$ ) memiliki performa yang rendah dibandingkan dengan indikator lainnya. Hal tersebut merupakan dampak langsung dari distribusi kelas pada dataset anotasi dalam feature-set yang disajikan pada Lampiran 13 dan Lampiran 14. Sebagaimana analisis yang dilakukan pada subbab IV.2.2.1B, hanya terdapat 23,4% narasi feedback yang tidak memenuhi indikator relevansi topik, menyebabkan model cenderung underpredict terhadap

kelas minoritas. Hal ini didukung oleh Albattah & Khan (2025) yang mengonfirmasi bahwa dataset yang tidak seimbang akan mempengaruhi model machine learning sehingga terdapat bias terhadap kelas mayoritas.

**IV.3.2.4 Justifikasi Penentuan Threshold**

Setiap threshold yang ditetapkan pada [Tabel IV.13](#page-6-0) merupakan keputusan desain yang mempengaruhi keseimbangan kinerja sistem. Untuk indikator berbasis embedding (,,&), penentuan threshold similarity ('(),)) dilakukan melalui eksperimen metode grid-search pada rentan nilai ,0,1- dengan interval 0,01. Titik threshold optimal dipilih berdasarkan nilai yang menghasilkan F1-Score tertinggi saat divalidasi terhadap dataset ground truth. Pendekatan data-driven ini memastikan bahwa threshold merepresentasikan cut-off matematis paling ideal antara sensitivitas model dan ketepatan prediksi untuk lingkungan Project-Based Learning.

Pemilihan threshold komputasional ini berdampak langsung pada konsekuensi False Positive (FP) dan False Negative (FN) dalam implementasi real-time. Pada sistem yang beroperasi dalam Zone of Proximal Development (ZPD), keseimbangan ini bersifat krusial. Jika threshold diatur teralu tinggi, risiko FN akan meningkat, sehingga mahasiswa kehilangan kesempatan untuk mendapatkan arahan. Sebaliknya, threshold yang terlalu rendah meningkatkan risiko FP, yang dapa menimbulkan kebingungan atau gangguan konsentrasi akibat scaffolding redundan. Nilai threshold optimal pada [Tabel IV.13](#page-6-0) dipilih karena secara statistik menyeimbangkan risiko tersebut, sehingga intensitasscaffolding yang muncul tidak membebani cognitive load mahasiswa secara berlebihan.

Di sisi lain, threshold untuk kedalaman elaborasi (I) diimplementasikan menggunakan aturan heuristik batas leksikal sebesar 25 kata. Penentuan threshold ini diperoleh dari analisis distribusi right-skewed panjang narasi pada 10.098 data historis. Analisis tersebut mengidentifikasi angka 25 kata sebagai titik infleksi di mana peluang pemenuhan cakupan rubrik meningkat. Konsekuensi dari threshold

struktural ini adalah sifatnya yang absolut, yaitu narasi dengan 24 kata memicu False Negative untuk scaffolding elaborasi, meskipun narasi tersebut mungkin sangat padat. Namun, threshold 25 kata ini dipertahankan karena sifat pengukurannya yang deterministik dan komputasinya yang ringan.

**IV.3.2.5 Implikasi Performa terhadap Validitas Intervensi Scaffolding**

Subbab ini menganalisis lebih jauh dampak performa model pada subbab [IV.3.2.3](#page-5-0) untuk setiap indikator, sebagaimana disajikan pada [Tabel IV.14](#page-8-0)

Tabel IV.14 Analisis Implikasi Performa Hasil Evaluasi dan Eksperimen

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Sebagaimana didefinisikan pada subbab [IV.3.2.3,](#page-5-0) indikator relevansi topik (&) memiliki performa yang paling rendah di antara seluruh indikator lainnya. Meskipun demikian, hal tersebut dapat dimitigasi oleh tiga indikator lainnya yang bekerja secara kolaboratif. Narasi yang benar-benar tidak relevan umumnya juga tidak memenuhi indikator cakupan rubrik (, sehingga intervensi tetap dipicu melalui jalur alternatif meskipun indikator relevansi topik (&) menghasilkan false negative. Dalam konteks pilot study, performa pipeline saat ini dianggap memadai sebagai proof-of-concept untuk mengevaluasi feasibility arsitektur.

**IV.4 Hasil Validasi Fungsionalitas Instrumen**

Sebagai implementasi dari tahap akhir perancangan aplikasi pendukung eksperimen, sebagaimana didefinisikan pada subbab III.6.5.3. Validasi dilakukan melalui dua sudut pandang, yaitu pengujian aplikasi pada subbab [IV.4.1.1](#page-9-0), serta validasi komputasional indikator dalam subbab [IV.4.1.2](#page-10-0) yang secara eksklusif menguji keempat indikator tekstual narasi feedback.

**IV.4.1.1 Pengujian Aplikasi**

Hasil pengujian pada Lampiran 3 menunjukkan 41 dari 42 test case yang dinyatakan lolos. Pengujian fungsionalitas part-of-speech tagging yang didefinisikan pada subbab III.6.3.3A dapat menyaring input teks acak atau tidak bermakna sebelum diproses oleh model. Satu test case yang dinyatakan gagal terjadi pada pengujian indikator koherensi evaluatif dengan skenario narasi yang kontradiktif pada TC18. Dalam pengujian tersebut, pengguna memasukkan skor 5, namun menuliskan narasi feedback yang merepresentasikan kualitas pekerjaan rendah. Meskipun sistem secara fungsional berhasil mendeteksi adanya inkonsistensi antara skor dan narasi, arsitektur model gagal mengekstraksi dan memprediksi angka skor aktual yang tersirat di dalam narasi secara presisi, sehingga sistem mengembalikan nilai prediksi skor "yang belum dapat ditentukan". Hal ini menunjukkan adanya limitation pada model komputasi dalam memetakan dan menyelaraskan rentang semantik narasi yang bersentimen sangat negatif ke dalam skala skor rubrik secara spesifik.

Lebih jauh, dilakukan pengujian untuk memvalidasi apakah sistem mampu memicu 17 kombinasi template yang dirancang pada subbab III.6.4. Secara keseluruhan, pengujian mengonfirmasi bahwa 17 dari 17 template dapat dipicu oleh sistem. Namun, penemuan didapatkan pada satu edge case spesifik dalam template 0010: Narasi pendek yang berfokus pada rubrik target, di mana sistem rentan terhadap kebocoran relevansi sekunder. Meskipun pada akhirnya template tersebut berhasil dipicu, hal ini membutuhkan proses pengujian secara iteratif guna merumuskan isolasi semantik yang murni. Fenomena ini menegaskan adanya limitasi struktural pada model embedding saat memproses teks, di mana ketiadaan kata pendukung seringkali memicu indikator secara tidak akurat. Daftar lengkap skenario validasi, strategi penulisan untuk mencapai kondisi tersebut didokumentasikan pada Lampiran 9.

**IV.4.1.2 Validasi Skenario Logika Komputasional**

Untuk memastikan instrumen digital scaffolding beroperasi sesuai spesifikasi desain sebelum digunakan pada eksperimen lapangan. Pengujian ini menggunakan test suite yang terdiri dari 107 skenario data dummy, dirancang secara sistematis untuk memicu edge cases pada empat indikator pengukuran teks., dengan rincian temuan operasional pada subbab [IV.4.1.2A](#page-10-1) hingga [IV.4.1.2E](#page-11-0), dengan detail yang disajikan pada Lampiran 8.

Secara keseluruhan, hasil pengujian menunjukkan bahwa setiap komponen utama pipeline menghasilkan keluaran yang konsisten dengan aturan keputusan yang telah dirancang. Temuan ini memberikan bukti bahwa mekanisme ekstraksi indikator, pemicu scaffolding, serta pemilihan template telah beroperasi sesuai spesifikasi implementasi. Oleh karena itu, instrumen dinilai layak digunakan pada tahap eksperimen lapangan untuk mengevaluasi pengaruh digital scaffolding terhadap pemenuhan keempat indikator tekstual narasi feedback mahasiswa.

**A. Konsistensi Heuristik Elaborasi (**Åú**)**

Pengujian empiris pada threshold mengindikasikan bahwa heuristik beroperasi secara presisi pada titik 25 kata. Skenario input sepanjang 24 kata secara deterministik memicu intervensi, sedangkan skenario 25 kata diloloskan oleh sistem tanpa terpengaruh oleh noise seperti spasi ganda.

**B. Ketahanan Terhadap Variasi Semantik (**ÅÇ**)**

Model embedding (intfloat/multilingual-e5-large-instruct) mengindikasikan robustness terhadap fenomena parafrase. Sistem dapat mengukur cakupan rubrik baik pada penggunaan istilah formal akademis maupun ragam bahasa informal, hal tersebut memberikan indikasi bahwa kemampuan semantik relatif melampaui sekadar pencocokan keywords dasar. Temuan ini menunjukkan bahwa indikator tidak bergantung pada pencocokan kata secara literal.

**C. Bias Polaritas pada Deteksi Koherensi (**Åô**)**

Matriks pengujian yang dilakukan dengan kombinasi 5 skor numerik dengan 3 variasi sentimen teks mendeteksi keberadaan bias polaritas. Model dapat mendeteksi inkoherensi pada skor ekstrem, contohnya skor 5 bersentimen negatif dinilai tidak koheren. Akan tetapi, pada skor 2, 3, ataupun 4, model menunjukkan sensitivitas yang rentan terhadap false-positive.

**D. Keterbatasan Filter Relevansi Topik (**Å°**)**

Uji coba pada narasi off-domain seperti artikel berita menunjukkan bahwa algoritma pada dasarnya menghitung kedekatan kosinus vektor. Jika teks offdomain memuat serangkaian kata yang secara vektor berdekatan dengan jangkar rubrik, teks tersebut berpeluang diinterpretasikan sebagai relevan oleh sistem.

**E. Validasi Filter Input Kebahasaan**

Filter yang didefinisikan pada subbab III.6.3.3A dapat menolak noise seperti deret angka murni, teks acak, dan bahasa asing. Modul ini mensyaratkan keberadaan struktur frasa atau kalimat yang koheren dalam bahasa Indonesia agar komputasi inferensi NLP selanjutnya dapat dieksekusi, menjaga resource dari beban iterasi yang tidak valid.

**IV.5 Hasil Perancangan Skenario Eksperimen RQ 2**

Subbab ini merupakan manifestasi dari tahapan pre-eksperimen yang dipetakan pada subbab III.6.6.1. Bagian ini mendeskripsikan tiga komponen utama dalam eksperimen, yaitu: (1) partisi kelompok subjek eksperimen, (2) instrumen pengukuran melalui kuesioner, dan (3) standar penilaian berbasis rubrik.

**IV.5.1 Pemetaan Subjek Eksperimen**

Distribusi subjek eksperimen dilakukan melalui metode randomisasi menggunakan fungsi pada google spreadsheet. Proses ini menghasilkan pemetaan 56 mahasiswa ke dalam dua kelompok independen, dengan 27 subjek dialokasikan sebagai kelompok treatment dan 29 subjek sebagai kelompok kontrol. Untuk memfasilitasi mekanisme peer assessment, subjek pada masing-masing kelompok didatarkan ke dalam unit kerja beranggotakan dua hingga tiga orang. Unit ini memastikan setiap assessee menerima jumlah evaluasi yang seimbang dari rekan sejawat dalam kelompok yang sama.

**IV.5.2 Kuesioner yang Digunakan**

Evaluasi respons subjek diukur menggunakan instrumen kuesioner kelompok treatment secara eksklusif, sebagaimana didefinisikan pada subbab III.6.6.1B. Pada seluruh instrumen, istilah "sistem digital scaffolding" secara konsisten diganti menggunakan terminologi "Teks AI". Penggunaan istilah umum ini berfungsi sebagai generalisasi konteks bagi subjek eksperimen yang tidak diberikan informasi spesifik mengenai arsitektur penelitian. Pendekatan ini bertujuan meminimalkan potensi bias akibat ekspektasi teknis dari subjek saat memberikan evaluasi.

Kelompok treatment menerima kuesioner yang difokuskan pada pengukuran tingkat utilitas dan potensi gangguan dari intervensi digital scaffolding selama proses penulisan narasi. Untuk menjaga konsistensi dengan landasan metodologi pada BAB III, dua belas butir pertanyaan di dalam instrumen ini dibagi secara terstruktur ke dalam empat kelompok dimensi, yaitu: (1) Technology Acceptancce Model (TAM) untuk mengukur perceived usefulness dan perceived ease of use, (2) Cognitive Load Theory untuk mengidentifikasi tingkat extraneous cognitive load, (3) preferensi komponen antarmuka untuk mengisolasi elemen spesifik sistem, serta (4) Kualitatif Eksplanatori melalui open-ended questions. Pemetaan ini dirancang untuk mempermudah proses analisis deskriptif dan triangulasi pada [BAB V](#page-14-0). Detail butir pertanyaan beserta klasifikasi dimensi dan tipe respons disajikan pada Lampiran 15.

**IV.5.3 Rubrik Eksperimen**

Standar evaluasi dalam eksperimen ini menggunakan kerangka penilaian CATME (Comprehensive Assessment of Team Member Effectiveness), sebagaimana didefinisikan pada subbab III.6.6.1C. Lampiran 16 menjabarkan empat aspek pengukuran perilaku, yaitu: (1) Produktivitas, (2) komunikasi, (3) manajemen tim, dan (4) standar kualitas. Penilaian diukur menggunakan rentan kualitatif 1 hingga 5, dengan skala 2 dan 4 merupakan komponen penilaian yang menghubungkan skala di sekitarnya. Setiap tingkatan skor memiliki deskriptor evaluasi tekstual yang digunakan oleh sistem untuk membandingkan kesesuaian antara angka dan narasi mahasiswa.

Rubrik didefinisikan kemudian melewati tahapan dekomposisi sebagai preprocessing menggunakan metode pada subbab III.6.3.2A. Tahapan tersebut menghasilkan feature-set cakupan dan relevansi topik (de4-\),A) yang disajikan pada Lampiran 17, serta feature-set koherensi skor dan narasi (def-\),A) pada Lampiran 18.

**BAB V**

**HASIL DAN PEMBAHASAN EKSPERIMEN**

Bab ini menyajikan hasil dan pembahasan dari eksperimen yang telah dirancang dan dilaksanakan untuk mengevaluasi kinerja pipeline digital scaffolding berbasis NLP. Pembahasan difokuskan pada dua sasaran, yaitu: (1) memvalidasi akurasi komputasional sistem dalam mendeteksi indikator teks secara real-time, serta (2) menganalisis dampak intervensi scaffolding tersebut terhadap kualitas narasi feedback mahasiswa pada lingkungan PjBL. Seluruh hasil disajikan secara objektif, diikuti dengan interpretasi analitis, serta penjabaran keterbatasan penelitian.

**V.1 Ringkasan Metodologi Eksperimen**

Sebagaimana telah diuraikan secara rinci pada BAB III, penelitian ini menggunakan metode kuantitatif dengan desain randomized post-test-only control group dan alokasi acak. Eksperimen ini dirancang untuk menjawab dua pertanyaan penelitian. Tujuan pertama, yaitu RQ 1, difokuskan pada pengujian validitas komputasional dari pipeline digital scaffolding berbasis NLP dalam mendeteksi keempat indikator tekstual secara otomatis. Tujuan kedua, yaitu RQ 2, adalah mengukur dampak intervensi tersebut terhadap pemenuhan indikator tekstual pada kelompok mahasiswa yang menerima scaffolding (treatment) dibandingkan dengan kelompok kontrol, serta mengevaluasi dinamika interaksi mahasiswa saat menggunakan sistem tersebut.

Untuk mencapai tujuan tersebut, eksperimen dikondisikan sebagai pilot study yang melibatkan mahasiswa program studi Teknik Informatika di Politeknik Negeri Bandung. Partisipan merupakan mahasiswa yang sedang menempuh mata kuliah berbasis PjBL, di mana alokasi ke dalam kelompok treatment dan kontrol dilakukan secara acak dengan rincian distribusi yang telah dipetakan pada subbab [IV.5.1](#page-12-0).

Proses pengujian dilakukan di dalam lingkungan aplikasi pendukung eksperimen SAPA. Intervensi scaffolding diintegrasikan ke dalam aplikasi ini dengan

memanfaatkan pemrosesan teks linguistik yang didukung oleh model sentence embedding berarsitektur transformer. Penggunaan arsitektur ini memungkinkan sistem melakukan evaluasi semantik terhadap teks yang diinputkan mahasiswa selama proses penilaian berlangsung.

Aliran data dalam eksperimen ini dibagi ke dalam dua tahap utama. Tahap pemodelan awal menggunakan 384 data historis assessment yang telah dianotasi secara manual sebagai ground truth untuk keperluan kalibrasi threshold deteksi sistem. Setelah sistem terkalibrasi, tahap eksperimen utama dilaksanakan untuk menghasilkan dua jenis data, yaitu: (1) data outcome berupa skor dan narasi akhir dari mahasiswa, serta (2) data proses yang merekam jejak interaksi aktivitas perbaikan narasi selama mahasiswa menggunakan aplikasi.

Keberhasilan dari seluruh proses tersebut dievaluasi melalui tiga dimensi pengukuran. Dimensi komputasional mengevaluasi akurasi deteksi model menggunakan metrik F1-Score, precssion, dan recall. Dimensi outcome menguji perbedaan performa pada keempat indikator kualitas narasi feedback antar kelompok menggunakan analisis multivariat dan univariat, serta pengukuran besaran dampak melalui rank-biserial correlation. Terakhir, dimensi proses mengukur dinamika response mahasiswa terhadap scaffolding melalui metrik impementation rate dan persistence rate.

**V.2 Hasil Eksperimen**

Bagian ini menyajikan data kuantitatif yang diperoleh dari pelaksanaan eksperimen. Penyajian data dibagi ke dalam empat segmen, meliputi metrik performa komputasional pipeline pada subbab [V.2.1,](#page-1-0) statistik deskriptif dan verifikasi asumsi pada subbab [V.2.2](#page-4-0), pengujian inferensial multivariat dan uniavariat pada subbab [V.2.3](#page-7-0), serta rekam interaksi mahasiswa dengan scaffolding pada subbab [V.2.4](#page-8-0).

**V.2.1 Hasil Evaluasi Deteksi Pipeline (RQ 1)**

Subbab ini menyajikan hasil evaluasi komputasional dari pipeline digital scaffolding dalam mendeteksi empat indikator tekstual narasi feedback. Pengujian dilakukan terhadap 384 data ground truth untuk menentukan threshold optimal dan performa deteksi menggunakan merik F1-Score, precission, dan recall dengan rincian keseluruhan pada [Tabel V.1](#page-1-1) dengan berdasarkan konfigurasi akhir pipeline pada subbab IV.3.2.3.

Indikator  |  Threshold  |  F1  |  Precision  |  Recall  |  TP  |  FP  |  FN  |  TN
Cakupan Rubrik  |  0.84  |  0.6140  |  0.5312  |  0.7275  |  315  |  278  |  118  |  389
Relevansi Topik  |  0.85  |  0.4296  |  0.4265  |  0.4327  |  241  |  324  |  316  |  9103
Koherensi Skor  |  0.87  |  0.5314  |  0.4409  |  0.6687  |  220  |  279  |  109  |  1381

Tabel V.1 Rincian Keseluruhan Kemampuan Pipeline

**V.2.1.1 Evaluasi Deteksi Indikator Cakupan Rubrik (**ÅÇ**)**

Deteksi pada indikator cakupan rubrik mencapai kesesuaian dengan ground truth nilai F1-Score sebesar 0,6140 pada threshold 0,84 menggunakan pendekatan semantic chunking yang didefinisikan dalam subbab III.6.3.5A. Pada konfigurasi ini, pipeline menghasilkan 315 kasus true positive (TP), 118 false negative (FN), dan 389 true negative (TN). Nilai recall tercatat sebesar 0,7275 dan precission sebesar 0,5312. Pola trade-off antara precission dan recall terhadap penyesuaian threshold divisualisasikan pada [Gambar V.1](#page-1-2).

Gambar V.1. Grafik Indikator Cakupan Rubrik Semantic Chunking

Distribusi skor similarity berdasarkan klasifikasi prediksi disajikan pada [Tabel V.2](#page-2-0). Rata-rata skor untuk kasus TP adalah 0,8677 dan FP adalah 0,857. Selisih rata-rata antara TP dan FP tercatat sebesar 0,0103. Rata-rata skor FN adalah 0,8222 dan TN adalah 0,8197, dengan selisih sebesar 0,0025.

Outcome  |  Count  |  Mean  |  Std  |  Min  |  Max
FN  |  118  |  0.8222  |  0.0120  |  0.7876  |  0.8397
FP  |  278  |  0.8574  |  0.0141  |  0.8401  |  0.9073
TN  |  389  |  0.8197  |  0.0145  |  0.7678  |  0.8399

TP 315 0.8677 0.0181 0.8403 0.9146

Tabel V.2. Sebaran Performa Indikator Cakupan Rubrik

**V.2.1.2 Evaluasi Deteksi Indikator Koherensi Skor dan Narasi (**Åô**)**

Evaluasi pada indikator koherensi skor dan narasi menggunakan pendekatan mutually exclusive yang didefinisikan pada subbab III.6.3.5A, performa pada indikator ini mencapai kesesuaian dengan ground truth dengan nilai F1-Score optimal sebesar 0,53 pada threhold 0,89. Hasil klasifikasi pada titik kompromi ini mencatat 189 kasus True Positive (TP), 236 False Positive (FP), 140 False Negative (FN), dan 1.424 True Negative (TN). Dinamika pertukaran nilai presisi, recall, dan F1-Score terhadap pergeseran threshold divisualisasikan pada [Gambar V.2.](#page-2-1)

Gambar V.2. Grafik Performa Koherensi Skor dengan Semantic Chunking

Distiribusi skor similarity pada klasifikasi output prediksi untuk indikator ini disajikan pada [Tabel V.3.](#page-3-0) Rata-rata skor similarity untuk kasus TP tercatat sebesar 0,9100, sedangkan kasu FP memiliki rata-rata sebesar 0,9052. Pada klasifikasi negatif, rata-rata skor FN adalah 0,8678 dan TN adalah 0,8526.

Tabel V.3. Sebaran Performa Indikator Koherensi Skor dan Narasi

Outcome  |  Count  |  Mean  |  Std  |  Min  |  Max
FN  |  140  |  0.8678  |  0.0157  |  0.8186  |  0.8893
FP  |  236  |  0.9052  |  0.0119  |  0.8900  |  0.9465
TN  |  1424  |  0.8526  |  0.0222  |  0.7781  |  0.8900
TP  |  189  |  0.9100  |  0.0144  |  0.8901  |  0.9550

**V.2.1.3 Evaluasi Deteksi Indikator Elaborasi (**Åú**)**

Indikator kedalaman elaborasi dievaluasi tanpa melibatkan proses klasifikasi berbasis similarity terhadap anotasi acuan. Mekanisme kerja indikator ini menggunakan threshold deterministik dengan batas minimal 25 kata leksikal. Hasil perhitungan pada data historis menunjukkan bahwa narasi yang mencapai atau melebihi threshold 25 kata memiliki proporsi pemenuhan cakupan rubrik sebesar 23,2%. Sementara itu, narasi dengan panjang di bawah threshold tersebut mencatat tingkat pemenuhan cakupan rubrik yang rendah, yaitu sebesar 13,1%.

**V.2.1.4 Evaluasi Deteksi Indikator Relevansi Topik (**Å°**)**

Deteksi relevansi topik dievaluasi menggunakan pendekatan whole-text embedding pada seluruh narasi. Pendekatan ini menghasilkan nilai F1-Score optimal sebesar 0,4296 pada threshold 0,85. Pada titik kalibrasi tersebut, metrik precission tercatat sebesar 0,4265 dan recall sebesar 0,4327. Hasil klasifikasi prediksi memuat 241 kasus true positive (TP), 324 false positive (FP)), 316 false negative (FN), dan 9.103 true negative (TN). Pola perubahan persisi dan recall terhadap penyesuaian threshold disajikan pada [Gambar V.3.](#page-4-1)

Gambar V.3. Grafik Performa Relevansi Topik dengan Whole-text-embedding

Distribusi skor similarity pada klasifikasi prediksi untuk indikator relevansi topik disajikan pada [Tabel V.4.](#page-4-2) Rata-rata skor untuk kasus RP adalah 0,8690, sedangkan FP adalah 0,8608. Untuk kasus klasifikasi negatif, rata-rata skor FN tercatat sebesar 0,8266 dan TN sebesar 0,8075.

Tabel V.4. Sebaran Nilai FN, FP, TN, TP untuk Indikator Relevansi Topik

Outcome  |  Count  |  Mean  |  Std  |  Min  |  Max
FN  |  316  |  0.8266  |  0.0170  |  0.7703  |  0.8500
FP  |  324  |  0.8608  |  0.0094  |  0.8501  |  0.8979
TN  |  9103  |  0.8075  |  0.0196  |  0.7481  |  0.8500
TP  |  241  |  0.8690  |  0.0152  |  0.8501  |  0.9127

**V.2.2 Statistik Deskriptif dan Verifikasi Asumsi (RQ 2)**

Subbab ini menyajikan deskripsi partisipan, statistik deskriptif dari tingkat pemenuhan indikator tekstual narasi feedback, serta hasil verifikasi asumsi parametrik sebelum pengujian inferensial dilakukan.

Penentuan partisipan didasarkan pada kriteria inklusi mahasiswa aktif yang bersedia berpartisipasi secara sukarela tanpa konsekuensi terhadap penilaian akademik. Meskipun subjek eksperimen telah dipetakan pada subbab IV.5.1, tidak seluruh subjek eksperimen menyelesaikan kedua assessment . Beberapa mahasiswa hanya mengirimkan self assessment atau peer assessment, sedangkan sebagian lainnya tidak menyelesaikan salah satu komponen tersebut.

Penelitian ini tidak melakukan imputasi terhadap data yang tidak terkumpul tersebut. Analisis dilakukan menggunakan data yang benar-benar tersedia, sehingga jumlah observasi pada setiap jenis assessment mengikuti jumlah respons yang berhasil dikumpulkan dari masing-masing kelompok.

Distribusi partisipan yang dialokasikan ke dalam kelompok treatment dan kontrol, beserta total dokumen self dan peer assessment yang terkumpul disajikan pada [Tabel V.5.](#page-5-0)

Tabel V.5. Deskripsi Data Terkumpul dari Eksperimen yang Dilakukan

Kelompok  |  Jumlah Mahasiswa  |  Total Mahasiswa mengisi Self Assessment  |  Total Mahasiswa mengisi Peer Assessment  |  Total Jawaban Self  |  Total Jawaban Peer
Treatment  |  15  |  15  |  14  |  57  |  56
Kontrol  |  17  |  17  |  17  |  68  |  75

Berdasarkan [Tabel V.5](#page-5-0) terdapat satu data yang tidak terkumpul untuk peer assessment. Proporsi yang tidak terkumpul hanya satu relatif kecil jika dibandingkan dengan 32 subjek eksperimen. Dengan demikian, hasil eksperimen yang akan dipaparkan diinterpretasikan berdasarkan data yang tersedia.

Unit analisis pada pengujian ini adalah mahasiswa.Nilai evaluasi merupakan hasil agregasi tingkat pemenuhan indikator pada seluruh narasi feedback yang ditulis oleh setiap mahasiswa. Statistik deskriptif yang mencakup nilai mean, standar deviasi, median, nilai minimum, dan maksimum untuk kelompok treatment dan kontrol disajikan pada [Tabel V.6](#page-5-1) untuk self assessment dan [Tabel V.7](#page-6-0) untuk peer assessment.

Tabel V.6. Statistik Deskriptif Self Assessment

Indikator  |  Kelompok  |  Mean  |  Standar Deviasi  |  Median  |  Min  |  Max
Cakupan Rubrik  |  Treatment  |  0.267  |  0.258  |  0.25  |  0.0  |  0.75
Kontrol  |  0.132  |  0.219  |  0.00  |  0.0  |  0.75
Koherensi Skor  |  Treatment  |  0.467  |  0.297  |  0.50  |  0.0  |  0.75

Indikator  |  Kelompok  |  Mean  |  Standar Deviasi  |  Median  |  Min  |  Max
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

Sebelum pengujian multivarfiat dan univariat dilaksanakan, dilakukan verifikasi asumsi normalitas menggunakan uji Shapiro-Wilk dan homogenitas variant menggunakan uji Levene. Hasil uji asumsi untuk seluruh indikator pada kedua jenis assessment dilaporkan pada [Tabel V.8](#page-6-1).

Tabel V.8. Hasil Uji Asumsi

Jenis Asssessment  |  Indikator  |  Normalitas Kelompok Treatement  |  Jenis Asssessment  |  Indikator
Self Assessment  |  (Cakupan)  |  Tidak  |  Tidak  |  Ya
(Koherensi)  |  Tidak  |  Tidak  |  Ya
(Elaborasi) I  |  Tidak  |  Tidak  |  Tidak
(Relevansi) &  |  Ya  |  Tidak  |  Ya
Peer Assessment  |  (Cakupan)  |  Tidak  |  Tidak  |  Ya
(Koherensi)  |  Ya  |  Tidak  |  Ya
(Elaborasi) I  |  Tidak  |  Tidak  |  Tidak
(Relevansi) &  |  Ya  |  Tidak  |  Ya

Berdasarkan hasil pengujian tersebut, sebagian besar indikator pada self maupun peer assessment tidak memenuhi asumsi distribusi normal. Pada uji homogenitas, sebagian besar indikator memiliki varians yang homogen, kecuali indikator kedalaman elaborasi (I) yang menunjukkan pelanggaran homogenitas baik pada self maupun peer assessment.

**V.2.3 Hasil Pengujian Multivariat dan Univariat (RQ 2)**

Pengujian statistik infersial dilakukan secara bertahap, dimulai dari analisis multivariat untuk melihat efek keseluruhan, dilanjutkan dengan analisis univariat untuk setiap indikator. Pengujian multivariat menggunakan Multivariate Anaysis of Variance (MANOVA) dengan metrik Pillai's Trace. Hasil pengujian multivariat disajikan pada [Tabel V.9.](#page-7-1)

Tabel V.9. Hasil Pengujian Multivariat

Jenis Assessment  |  Pillai Value  |  p-value  |  Signifikan
Self  |  0.2677  |  0.0688  |  Tidak
Peer  |  0.3047  |  0.0441  |  Ya

Pada pengujian self assessment, nilai pillai's trace tercatat sebesar 0,2677 dengan nilai signifikansi = 0,0688. Pada peer assessment, nilai Pillai's Trace tercatat sebesar 0,3047 dengan nilai signifikansi = 0,0441.

Pengujian tahap kedua menggunakan analisis univariat Mann-Whitney U yang didampingi dengan pengukuran effect size menggunakan rank-biserial correlation. Keputusan penggunaan uji non parametrik ini didasarkan pada hasil verifikasi asumsi sebelumnya. Hasil pengujian univariat beserta besaran dampaknya disajikan pada [Tabel V.10](#page-7-2) untuk self assessment, dan [Tabel V.11](#page-7-3) untuk peer assessment.

Tabel V.10. Hasil Pengujian Univariat untuk Self Assessment

Indikator  |  Uji yang Digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect Size
(Cakupan)  |  Mann-Whitney  |  0.0880  |  Tidak  |  0.329
(Koherensi)  |  Mann-Whitney  |  0.6823  |  Tidak  |  0.086
(Elaborasi) I  |  Mann-Whitney  |  0.0054  |  Ya  |  0.49
(Relevansi) &  |  Mann-Whitney  |  0.9223  |  Tidak  |  -0.024

Tabel V.11. Hasil Pengujian Univariat untuk Peer Assessment

Indikator  |  Uji yang Digunakan  |  p-value  |  Signifikan (Ya/Tidak)  |  Effect Size
(Cakupan)  |  Mann-Whitney  |  0.3809  |  Tidak  |  0.176
(Koherensi)  |  Mann-Whitney  |  0.2722  |  Tidak  |  -0.231
(Elaborasi) I  |  Mann-Whitney  |  0.0059  |  Ya  |  0.487
(Relevansi) &  |  Mann-Whitney  |  0.9189  |  Tidak  |  -0.025

Pada self assessment, pengujian univariat menunjukkan nilai = 0,0054 pada indikator kedalaman elaborasi (I), dengan effect size sebesar 0,490. Indikator cakupan rubrik (), koherensi skor (), dan relevansi topik (&) mencatat nilai signifikansi di atas threshold ? yang disesuaikan.

Pola seragam ditemukan pada peer assessment, di mana indikator kedalaman elaborasi (I) mencatat nilai signifikansi = 0,0059 dengan effect size sebesar 0,487. Indikator lainnya tidak mencatat perbedaan yang signifikan secara statistik.

**V.2.4 Hasil Pengolahan Data Interaksi Scaffolding (RQ 2)**

Subbab ini menyajikan data proses interaksi mahasiswa dengan digital scaffolding selama penyusunan narasi feedback. Data yang disajikan mencakup frekuensi kebutuhan bantuan yang terdeteksi, tingkat resolusi dan persistensi indikator, serta klasifikasi operasi edit yang dilakukan mahasiswa pada setiap siklus revisi.

**V.2.4.1 Distribusi Kebutuhan Bantuan, Resolusi, dan Persistensi**

Sistem digital scaffolding mendeteksi kebutuhan bantuan setiap kali sebuah indikator teridentifikasi tidak terpenuhi pada awal siklus revisi. Frekuensi kemunculan kebutuhan bantuan pada setiap indikator diukur pada self assessment dan peer assessment. Distribusi frekuensi ini divisualisasikan melalui heatmap pada [Gambar V.4.](#page-8-1)

Gambar V.4. Frekuensi Kebutuhan Bantuan yang Terdeteksi

Respons mahasiswa terhadap scaffolding dievaluasi menggunakan metrik tingkat resolusi, yaitu proporsi kebutuhan bantuan yang berhasil diselesaikan pada revisi berikutnya, dan tingkat persistensi, yaitu proporsi kebutuhan bantuan yang tetap bertahan pasca-intervensi. Data tingkat resolusi divisualisasikan pada [Gambar V.5](#page-9-0) dan tingkat persistensi disajikan pada [Gambar V.6.](#page-9-1)

Gambar V.5. Tingkat Resolusi Keempat Indikator

Gambar V.6. Tingkat Persistensi Antar Indikator

Berdasarkan data tersebut, indikator relevansi topik (&) mencatat tingkat resolusi tertinggi pada kedua assessment, yaitu 29,9% pada self assessment dan 33,3% pada peer assessment. Sebaliknya, indikator cakupan rubrik () mencatat tingkat resolusi terendah pada self assessment (5,1%) dengan tingkat persistensi yang tinggi, yaitu 93,4% pada self assessment dan 95,5% pada peer assessment. Indikator kedalaman elaborasi (I) mencatat resolusi sebesar 21,0% pada self assessment dan 9,7% pada peer assessment.

**V.2.4.2 Karakteristik Perbaikan Narasi**

Perubahan tekstual narasi pasca-intervensi dievaluasi menggunakan operasi Levenshtein pada tingkat token, yang mengklasifikasikan revisi ke dalam empat kategori, yaitu: (1) No Change (NC), (2) Insertion (INS), (3) Deletion (DEL), dan (4) Substitution (SUB). Distribusi klasifikasi operasi ini disajikan pada [Gambar](#page-10-0)  [V.7](#page-10-0).

Gambar V.7. Pola Revisi Perubahan

Operasi Insertion mendominasi pada kedua konteks penilaian, yaitu 61,6% pada self assessment dan 69,5% pada peer assessment. Operasi Substitution menempati urutan kedua dengan proporsi 23,2% pada self assessment dan 17,2% pada peer assessment. Operasi Deletion mencatat proporsi yang relatif kecil, yaitu 12,3% pada self dan 8,6% pada peer assessment. Kategori No Change berada pada proporsi terendah, yaitu 2,9% pada self assessment dan 4,7% pada peer assessment.

**V.2.4.3 Dinamika Pemenuhan Indikator Tekstual Narasi Feedback**

Analisis perubahan status indikator pada [Gambar V.8](#page-11-0) menunjukkan proporsi pemenuhan berbeda antar indikator.

Gambar V.8 Dinamika Pemenuhan Indikator Saat Sesi Eksperimen

Indikator kedalaman elaborasi, menunjukkan kondisi berhasil terpenuhi yang lebih sering ditemukan dibandingkan indikator lainnya. Sebaliknya, pada indikator cakupan rubrik, koherensi skor dan relevansi topik, keberadaan bantuan digital scaffolding tidak selalu diikuti oleh perubahan pemenuhan status indikator yang bertahan hingga akhir sesi eksperimen

**V.2.4.4 Penyelesaian Akhir Kebutuhan Scaffolding**

Pada [Gambar V.9](#page-12-0) disajikan kondisi kebutuhan bantuan digital scaffolding yang berhasil teratasi pada akhir sesi selalu lebih tinggi dibandingkan yang terpenuhi hanya melalui satu kali revisi setelah menerima bantuan digital scaffolding.

Gambar V.9 Perbandingan Pemenuhan Indikator Terpenuhi

[Gambar V.9](#page-12-0) menyajikan perbandingan antara tingkat penyelesaian kebutuhan bantuan setelah revisi pertama dan tingkat penyelesaian kebutuhan bantuan pada akhir sesi revisi. Pada seluruh indikator, tingkat penyelesaian pada akhir sesi lebih tinggi dibandingkan tingkat penyelesaian setelah revisi pertama.

Pada indikator cakupan rubrik, tingkat penyelesaian meningkat dari sekitar 7,6% menjadi 21,2%. Pada indikator koherensi skor dan narasi, tingkat penyelesaian meningkat dari sekitar 5,9% menjadi 15,9%. Sementara itu, indikator kedalaman elaborasi menunjukkan peningkatan dari sekitar 16,4% menjadi 43,9%, dan indikator relevansi topik meningkat dari sekitar 30,9% menjadi 50,0%.

Hasil tersebut menunjukkan adanya perbedaan antara tingkat penyelesaian kebutuhan bantuan yang terjadi segera setelah bantuan digital scaffolding diberikan dan tingkat penyelesaian yang tercapai pada akhir sesi revisi.

**V.2.5 Hasil Kuesioner Evaluasi Subjek Eksperimen**

Data kuesioner evaluasi penerimaan pengguna (TAM) pada bagian ini dikumpulkan sebagai data sekunder/eksplanatori murni. Data ini berfungsi untuk memberikan konteks kualitatif guna mengeksplorasi apakah dinamika interaksi mahasiswa yang dianalisis dalam RQ2, dipengaruhi oleh beban kognitif antarmuka, dan bukan merupakan pengujian dari pertanyaan penelitian utama yang bersifat algoritmik.

Subbab ini memaparkan hasil evaluasi kuesioner yang dirancang sebagai instrumen eksplanatori dengan pendekatan metode campuran, sebagaimana telah ditetapkan pada subbab III.6.6.1B, dengan jumlah responden yang disajikan pada [Tabel V.12](#page-13-0). Pengumpulan data kualitatif dan kuantitatif ini berfungsi untuk memvalidasi penerimaan intervensi secara psikologis dan operasional oleh pengguna. Sesuai dengan pedoman implementasi pada subbab IV.5.2. Pemaparan hasil difokuskan pada evaluasi penerimaan intervensi dalam kelompok treatment melalui subbab [V.2.5.1](#page-13-1).

Tabel V.12. Jumlah Responden Kuesioner

Kelompok: Jumlah Responden
Treatment: 11 Responden
Kontrol: 14 Responden
Total: 25 Responden

**V.2.5.1 Evaluasi Penerimaan dan Beban Kognitif**

Kuesioner pada kelompok treatment difokuskan pada pengukuran preceived usefullness dalam [Gambar V.10](#page-14-0) dan identifikasi cognitive load dari intervensi digital scaffolding selama proses penulisan dalam [Gambar V.11](#page-14-1). Berdasarkan rancangan instrumen pada Lampiran 15, mahasiswa diminta memberikan evaluasi menggunakan skala linier (1-5), di mana skor 1 merepresentasikan "Sangat Tidak Setuju" dan skor 5 merepresentasikan "Sangat Setuju". Data ini dihimpun dari 11 subjek yang secara aktif menggunakan sistem.

Gambar V.10. Rata-rata Skor Evaluasi Penerimaan (TAM)

Gambar V.11. Rata-rata Skor Evaluasi Beban Kognitif

Berdasarkan nilai rata-rata dari skala Likert 5 poin, fitur intervensi menunjukkan penerimaan utilitas yang positif. Responden menilai bahwa intervensi digital scaffolding berhasil membantu mereka mengingat kriteria rubrik yang terlewat dengan skor rata-rata tertinggi yaitu 4,00. Aspek kegunaan keseluruhan dan fleksibilitas interaksi memiliki rata-rata 3,91, diikuti oleh kejelasan instruksi dan kemudahan memahami struktur penilaian dengan skor 3,82. Namun, data juga

menunjukkan kehadiran distorsi kognitif. Pertanyaan yang mengukur extraneous cognitive load, yaitu perasaan pusing akibat informasi yang terlalu padat dan gangguan konsentrasi saat mengetik, masing-masing mencatat skor yang cukup signifikan, yaitu 3,45.

Untuk memetakan secara spesifik elemen antarmuka yang berdampak pada utilitas maupun beban kognitif tersebut, responden ditugaskan untuk mengidentifikasi komponen yang dirasa paling membantu yang disajikan pada [Gambar V.12](#page-0-0), sekaligus paling mengganggu yang disajikan pada [Gambar V.13](#page-1-0). Data dikumpulkan melalui instrumen checkboxes yang mengizinkan pilihan lebih dari satu.

Gambar V.12. Komponen Scaffolding yang Dinilai Paling Membantu

Hasil pemetaan komponen yang paling membantu menunjukkan bahwa "Arahan mengenai apa yang harus ditulis dalam narasi" menjadi preferensi utama yang dipilih oleh 7 responden (38,9%). Komponen "Peringatan kekurangan narasi yang ditulis" berada pada posisi kedua, dipilih oleh 6 responden (33,3%). Indikator status warna dan sentence starter masing-masing dipilih sebayak dua kali (11,1%). Terdapat pula satu responden yang menambahkan opsi khusus berupa pandan rentang angka/skor (5,6%).

Gambar V.13. Komponen Scaffolding yang Dinilai Membutuhkan Perbaikan

Di sisi lain, hasil identifikasi komponen tang membutuhkan perbaikan atau dinilai mengganggu, menunjukkan pola distribusi yang ironis. Komponen "Arahan mengenai apa yang harus ditulis dalam narasi" justru menduduki peringkat teratas sebagai fitur yang paling mengganggu oleh 6 responden (42,3%), diikuti oleh "Peringatan diagnosis kekurangan narasi yang ditulis" oleh 3 responden (21,4%) dan "Contoh kalimat pembuka" oleh 2 responden (14,3%). Selain itu, terdapat masukan kualitatif spesifik dari beberapa responden mengenai mekanisme UI. Tiga entri respons menyoroti isu teknis pergeseran layar otomatis, di mana pembaruan teks scaffolding saat mahasiswa sedang mengetik menyebabkan layar bergulir ke bawah, sehingga membingungkan dan mengganggu fokus visual.

**V.3 Pembahasan Hasil Eksperimen**

Subbab ini menginterpretasikan hasil pengujian komputasional dan statistik inferensial yang telah dipaparkan pada subbab sebelumnya untuk menjawab dua research questions. Pembahasan menstrukturkan temuan empiris ke dalam dua fokus analisis utama. Fokus pertama mengevaluasi kapabilitas teknis pipeline digital scaffolding dalam mendeteksi indikator tekstual narasi feedback di lingkungan PjBL untuk menjawab RQ 1. Fokus kedua menganalisis dampak pedagogis dari intervensi tersebut terhadap pemenuhan indikator tekstual narasi feedback, yang ditinjau melalui sintesis komprehensif antara luaran statistik, dinamika proses revisi mahasiswa, dan implikasi beban kognitif pengguna untuk menjawab RQ 2.

**V.3.1 Pembahasan Kemampuan Deteksi Pipeline (Menjawab RQ 1)**

Research question pertama mengevaluasi sejauh mana pipeline digital scaffolding mampu mendeteksi keempat indikator tekstual narasi feedback melalui kombinasi model semantik terhadap ground truth anotasi dan aturan heuristik. Jawaban atas pertanyaan ini diinterpretasikan melalui tiga kerangka evaluasi, sebagaimana divisualisasikan pada [Gambar V.14.](#page-2-0)

Gambar V.14. Kerangka untuk Menjawab RQ 1

Kerangka evaluasi pertama berfokus pada capaian komputasional menggunakan metrik performa F1-Score yang merepresentasikan konfigurasi optimal hasil kalibrasi terhadap 384 data ground truth. Kerangka kedua meninjau justifikasi fungsional berdasarkan rasio risiko antar False Positive dan False Negative secara spesifik untuk setiap indikator tekstual.

Berdasarkan keseluruhan hasil evaluasi, keempat indikator menunjukkan karakteristik deteksi yang berbeda. Cakupan rubrik menghasilkan performa yang relatif stabil untuk mengidentifikasi keberadaan aspek-aspek rubrik. Koherensi skor dan narasi merupakan indikator yang paling menantang karena memerlukan penalaran terhadap tingkat kualitas jawaban. Kedalaman elaborasi dioperasionalkan menggunakan pendekatan deterministik berbasis jumlah kata sehingga tidak dievaluasi sebagai tugas klasifikasi semantik. Sementara itu, relevansi topik masih mampu mengenali domain pembahasan, namun performanya menurun ketika hubungan antara narasi dan aspek rubrik harus disimpulkan secara implisit.

**V.3.1.1 Pembahasan Indikator Cakupan Rubrik (**ÅÇ**)**

Berdasarkan hasil evaluasi komputasional pada indikator cakupan rubrik dalam subbab IV.3.2.3, nilai recall (0,7275) tampak lebih tinggi dibandingkan precision (0,5312). Hal ini merepresentasikan sensitivitas pipeline yang lebih tinggi terhadap kebenaran unit dekomposisi di dalam narasi mahasiswa. Konsekuensi dari sensitivitas ini adalah meningkatnya jumlah deteksi positif yang kurang tepat (FP).

Ruang pemisahan class menggunakan threshold 0,84 tergolong sangat sempit. Selisih rata-rata skor similarity antara TP dan FP hanya sebesar 0,0103. Distribusi nilai yang sempit ini memperlihatkan bahwa pasangan narasi dan dekomposisi rubrik yang berstatus FALSE pada ground truth masih dapat menghasilkan skor similarity yang tinggi, ditunjukkan pada [Gambar V.15](#page-3-0).

Gambar V.15. Distribusi FP dan FN pada Rubrik

Varians false positive terkonsentrasi pada kriteria yang menuntut abstraksi tinggi, seperti "Kemampuan Mengelola Waktu", "Kemampuan Menyampaikan Ide", dan "Kelengkapan Struktur Data". Kriteria-kriteria ini mencatat 19 hingga 25 kasus FP. Model embedding cenderung mengaitkan kosakata umum mahasiwa dengan kriteria tersebut. Pipeline menganggap suatu kriteria telah dibahas meskipun mahasiswa belum mengevaluasi aspek tersebut secara eksplisit.

[Tabel V.13](#page-4-0) menunjukkan bahwa model sering memberikan skor cosine similarity tinggi (0,89 hingga 0,9) pada narasi yang hanya menyebutkan istilah terkait rubrik tanpa penjelasan memadai. Sebagai contoh, kalimat "menginputkan data dengan teliti" memperoleh skor tinggi terhadap kriteria "Keakuratan Data yang Diinput". Narasi tersebut belum menyertakan alasan atau proses evaluasi yang mendukung pertanyaan terkait. Temuan ini mengindikasikan bahwa model lebihi mudah mengenali kesamaan topik dibandingkan memverifikasi substansi kriteria. Narasi yang sangat singkat dan superfisial masih terdeteksi memenuhi kriteria.

Tabel V.13. Sampel data False Positive

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
tersebut sangat memadai dan sesuai dengan data yang dikumpulkan.
0  |  1  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  struktur yang dikumpulkan sudah sesuai & memadai dengan data No. dikumpulan.
0  |  1  |  Manajemen Waktu  |  Kemampuan Mengelola Waktu  |  Tepat waktu dan tidak mepet

Kondisi tersebut memvalidasi urgensi penggunaan indikator kedalaman elaborasi (I) sebagai lapisan validasi tambahan. Indikator I memastikan sebuah kriteria dijelaskan menggunakan jumlah kata yang memadai. Sebagian false positive pada dapat direduksi secara hierarkis melalui pemenuhan I.

Varians false negative terpusat pada kriteria yang berorientasi pada objek fisik atau kuantitas, seperti "Jumlah Iklan yang Dikumpulkan", "Tingkat Pemahaman Konten Iklan", dan "Keragaman Platform", sebagaimana disajikan pada [Tabel V.14.](#page-5-0)

Tabel V.14. Sampel Data False Negative

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Sampel pada [Tabel V.14](#page-5-0) memperlihatkan kesulitan model dalam menangani narasi implisit. Mahasiswa sering mendeskripsikan aktivitas konkret tanpa menggunakan terminologi rubrik. Sebagai contoh, narasi "memilih platform Linked-In yan berupa teks dll, hal ini menjadi kemudahan bagi saya" gagal melewati threshold 0,84 untuk kriteria "Kemudahan dalam Pengumpulan Data". Penilaian manusia dapat memahami hubungan tersebut melalui proses inferensi. Model embedding mengandalkan semantic similarity tekstual dan gagal melakukan inferensi terhadap gabungan implisit tersebut.

Dalam konteks penerapan digital scaffolding pada zone of proximal development (ZPD), sebagaimana didefinisikan pada subbab II.1.9, kasus FN menyebabkan mahasiswa yang memerlukan bantuan gagal menerima intervensi. Kasus FP memicu pemberian scaffolding tambahan yang bersifat redundan. Mahasiswa dapat mengabaikan scaffolding redundan tersebut tanpa merusak pemahaman mereka.

**V.3.1.2 Pembahasan Indikator Koherensi Skor dan Narasi (**Åô**)**

Hasil evaluasi komputasional pada indikator koherensi skor dan narasi memperlihatkan overlap yang tinggi antar prediksi benar dan salah, sebagaimana dijabarkan pada subbab V.2.1.2. Rata-rata skor similarity untuk kelas TP (0,9100) dan FP (0,9052) memiliki selisih yang sangat tipis. Kondisi ini memperlihatkan bahwa pipeline digital scaffolding cenderung memberikan skor similarity yang tinggi pada sebagian besar narasi, sehingga membatasi ruang pemisah antara klasifikasi TRUE dan FALSE.

Karakteristik ini muncul karena model embedding mampu menangkap topik dari deskriptor skor pada rubrik secara umum, tetapi mengalami kesulitan mendiskriminasi tingkat kualitas jawaban yang bersifat ordinal. Model mengenali bahwa mahasiswa sedang membahas suatu kriteria, tetapi gagal mendeteksi apakah narasi tersebu merepresentasikan tingkat pencapaian "tidak memahami", "cukup memahami", atau "sangat memahami". Akibatnya, narasi yang seharusnya terklasifikasi pada kategori skor yang berbeda tetap menghasilkan skor similarity yang setara.

Pola sebaran kesalahan klasifikasi ini tidak terdistribusi secara merata pada keseluruhan data, sebagaimana divisualisasikan pada [Gambar V.16.](#page-8-0)

Gambar V.16. Sebaran FP dan FN berdasarkan Label Anotasi

Gambar tersebut menunjukkan bahwa kasus false positive (FP) terkonsentrasi pada kriteria yang merepresentasikan tingkatan kualitas dalam skala ordinal, seperti komunikasi, pemahaman, dan kualitas struktur data. Hal ini dikonfirmasi melalui sampel data kesalahan yang disajikan pada [Tabel V.15](#page-8-1).

Tabel V.15. Sampel Data FP pada Koherensi Skor dan Narasi

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik Narasi
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

Di sisi lain, kasus false negative (FN) terpusat pada kriteria yang menuntut interpretasi terhadap informasi implisit. Sampel untuk kasus ini dirangkum pada [Tabel V.16](#page-9-0).

Tabel V.16. Sampel Data FN pada Koherensi Skor dan Narasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Kasus FN umumnya muncul ketika mahasiswa menyampaikan bukti evaluasi secara tersirat melalui deskripsi aktivitas konkret atau penyebutan entitas spesifik. Narasi yang menyebutkan penggunaan "media sosial Facebook" atau "Linkedin" merupakan bukti praktis dari kriteria "Platform Bervariasi". Penilai manusia dapat mengubungkan tindakan tersebut dengan kriteria rubrik melalui proses interpretasi. Namun, karena hubungan tersebut dinyatakan menggunakan pengalaman nyata dan bukan terminologi rubrik, model embedding gagal mendeteksinya.

Secara keseluruhan, indikator koherensi skor menyingkap tantangan utama pipeline komputasional berbasis embedding. Sistem mampu mendeteksi deskriptor skor yang sedang dibahas, tetapi menghadapi keterbatasan ketika harus mendiskriminasi tingkat pencapaian ordinal serta menginterpretasikan informasi implisit di dalam narasi mahasiswa.

**V.3.1.3 Pembahasan Indikator Elaborasi (**Åú**)**

Berbeda dengan ketiga indikator lainnya yang mengandalkan model embedding untuk mengevaluasi semantik teks, indikator kedalaman elaborasi berbasiskan pada konten leksikal secara struktural, sebagaimana dipaparkan pada subbab V.2.1.3. Pendekatan ini dilandasi oleh asumsi bahwa narasi yang melewati threshold 25 kata menyediakan ruang yang lebih luas bagi mahasiswa untuk menguraikan alasan, menyertakan contoh, atau menjelaskan proses evaluasi yang mendasari penilaian mereka.

Perbedaan proporsi pemenuhan cakupan rubrik antara narasi panjang (23,2%) dan narasi pendek (13,1%) mengindikasikan kesesuaian penetapan threshold tersebut terhadap karakteristik data penilaian. Temuan ini mengonfirmasi bahwa narasi yang lebih panjang cenderung memuat lebih banyak bukti evaluatif yang selaras dengan aspek rubrik penilaian. Oleh karena itu, indikator ini berfungsi untuk mengidentifikasi narasi yang berpotensi belum membangun elaborasi yang memadai sehingga memerlukan dorongan tambahan melalui mekanisme scaffolding.

Meskipun demikian, panjang kalimat tidak dapat diinterpretasikan sebagai representasi mutlak dari kualitas elaborasi. Terdapat kemungkinan mahasiswa menghasilkan narasi yang panjang namun berputar-putar tanpa makna, atau sebaliknya, menyusun narasi singkat yang sangat padat dan substantif. Oleh karena itu, threshold 25 kata diposisikan secara fungsional sebagai indikator untuk mengidentifikasi kemungkinan kurangnya elaborasi, bukan sebagai pengukur kualitas yang holistik. Di dalam digital scaffolding, informasi kedalaman elaborasi tidak beroperasi secara terisolasi, melainkan dipertimbangkan bersama keseluruhan indikator tekstual lainnya dalam pengambilan keputusan.

**V.3.1.4 Pembahasan Indikator Relevansi Topik (**Å°**)**

Meskipun subbab V.2.1.4 menyatakan bahwa terdapat overlap antar distribusi skor pada Tabel V.4, data menunjukkan bahwa rata-rata skor TAPI tetap berada di atas FP, sementara FN dan TN terkonsentrasi pada rentang skor yang lebih rendah. Pola ini mengonfirmasi bahwa pipeline digital scaffolding mampu menghasilkan prediksi yang cukup relevan. Pipeline digital scaffolding dapat membedakan keberadaan topik evaluatif pada tingkat tertentu dan mengenali apakah narasi mahasiswa sedang membahas aspek yang sesuai dengan pertanyaan rubrik, meskipun belum mencapai pemisahan class yang tegas.

Pola perubahan precission dan recall pada Gambar V.3 yang berlangsung relatif bertahap memperkuat temuan tersebut. Distribusi nilai similarity antara prediksi benar dan salah masih memiliki ruang pemisah untuk menentukan relevansi topik. Namun, pola ini juga mengungkap batas kemampuan model embedding dalam membedakan topik yang dinyatakan secara eksplisit dengan topik tersirat.

Tabel V.17. Sampel Data FP pada Relevansi Topik

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Unit Dekomposisi Rubrik  |  Narasi
0  |  1  |  Inisiatif dan  |  Dukungan terhadap  |  membantu menyelesaikan
Pemecahan  |  Anggota Tim  |  maslah pada anggota tim
Masalah
0  |  1  |  Penginputan  |  Keakuratan Data yang  |  menginputkan data dengan
Data ke Excel  |  Diinput  |  teliti
0  |  1  |  Pembuatan  |  Kelengkapan Struktur  |  Menyarankan struktur data
Struktur Data  |  Data  |  yang memadai dengan data
yang ada
0  |  1  |  Komunikasi  |  Partisipasi dalam Diskusi  |  ikut berkontribusi saat ada
Kelompok: diskusi di kelas
0  |  1  |  Komunikasi  |  Kemampuan  |  banyak menyampaikan ide
Menyampaikan Ide: banyak menyampaikan ide
dan membanntu
menyepakatinya
0  |  1  |  Inisiatif dan  |  Kemampuan  |  menanggapi masalah
Pemecahan  |  Menyelesaikan Masalah  |  dengan baik
Masalah
0  |  1  |  Penginputan  |  Keakuratan Data yang  |  sepertinya tidak ada
Data ke Excel  |  Diinput  |  ketidaktelitian dalam
penginputan datanya
0  |  1  |  Kolaborasi dan  |  Kemampuan  |  Dengan mengemukakan
Kerjasama Tim  |  Menyampaikan Ide  |  pendapatnya
0  |  1  |  Pembuatan  |  Kelengkapan Struktur  |  Struktur data yang dia
Struktur Data  |  Data  |  sampaikan sesuai dengan

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Unit Dekomposisi Rubrik  |  Narasi
data: tujuan dari pengumpulan
0  |  1  |  Manajemen  |  Kemampuan  |  Mengelola  |  Tepat  |  waktu  |  dan  |  tidak
Waktu  |  Waktu  |  mepet

Berdasarkan [Tabel V.17,](#page-12-0) sebagian besar kasus false positive (FP) muncul ketika mahasiswa menggunakan terminologi yang menceritakan aktivitas umum terkait suatu aspek rubrik, tetapi substansinya belum cukup kuat untuk memenuhi kriteria topik yang dimaksud. Sebagai contoh, pernyataan "menginputkan data dengan teliti" terdeteksi sebagai indikator keakuratan penginputan data, sementara "dengan mengemukakan pendapatnya" diprediksi berkaitan dengan kemampuan menyampaikan ide. Kesalahan ini menunjukkan bahwa model embedding cukup sensitif menangkap sinyal topik, namun masih kesulitan membedakan antara penyebutan aktivitas general dan pembahasan eksplisit terhadap aspek rubrik.

Sebaliknya, sampel false negative (FN) memperlihatkan kesulitan sistem ketika narasi memuat bukti perilaku konkret yang memerlukan inferensi tambahan, dengan sampel yang disajikan pada [Tabel V.18.](#page-13-0) Penyebutan penggunaan platform seperti "LinkedIn" untuk mempermudah proses, atau "Facebook" dan "Tiktok", gagal dipetakan oleh model ke dalam dimensi "Kemudahan Pengumpulan Data" atau "Keragaman Sumber Platform".

Tabel V.18. Sampel Data FN pada Relevansi Topik

Label  |  Prediksi  |  Aspek Rubrik yang Dijawab  |  Dekomposisi Rubrik  |  Narasi
1  |  0  |  Pembuatan Struktur Data  |  Kelengkapan Struktur Data  |  Cukup baik, teman saya membantu dalam memberi
saran dan masukan
1  |  0  |  Pemahaman terhadap Isi Iklan  |  Tingkat Pemahaman Konten Iklan  |  Yups, I'd say she did
1  |  0  |  Pengumpulan Iklan Lowongan Kerja  |  Kemudahan dalam Pengumpulan Data  |  Karena Faridha bagian platform TikTok juga (sama dengan Emir) mereka jadi lebih cepat dan mudah dalam mencari loker
1  |  0  |  Pengumpulan Iklan  |  Jumlah Iklan yang Dikumpulkan  |  Dzakir aktif mengisi data loker ketika di kampus. Saya tidak pernah melihat

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Secara keseluruhan, pemrosesan whole-text embedding terbukti cukup efektif untuk mendukung digital scaffolding, khususnya dalam mendeteksi keselarasan fokus narasi mahasiswa terhadap aspek evaluasi. Model embedding berkinerja baik dalam mengenali topik evaluatif eksplisit, namun performanya menurun ketika dihadapkan pada bukti perilaku yang membutuhkan interpretasi implisit. Dalam konteks penelitian ini, kapabilitas tersebut sudah memadai untuk memicu intervensi scaffolding agar mahasiswa tetap mempertahankan relevansi feedback dengan aspek yang ditetapkan dengan rubrik.

**V.3.1.5 Sintesis Jawaban RQ 1**

Berdasarkan evaluasi terhadap keempat indikator tekstual, yaitu cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, serta relevansi topik, pipeline digital scaffolding menunjukkan kemampuan deteksi yang berbeda-beda sesuai dengan karakteristik indikator yang diukur. Hasil evaluasi menunjukkan bahwa indikator yang memerlukan interpretasi semantik yang lebih sederhana cenderung menghasilkan performa yang lebih baik dibandingkan indikator yang menuntut inferensi evaluatif yang lebih kompleks. Temuan ini mengindikasikan bahwa kemampuan pipeline tidak bersifat seragam, melainkan dipengaruhi oleh sifat konstruk yang hendak dideteksi.

Pada indikator berbasis model embedding, proses kalibrasi menemukan bahwa konfigurasi optimal pipeline pada dataset yang tersedia menghasilkan tingkat kesesuaian cakupan rubrik mencapai performa dengan F1-score 0,61, koherensi skor-narasi menjadi F1-score 0,53, sedangkan relevansi topik mencapai F1-Score 0,43. Kinerja ada indikator relevansi topik merupakan yang terendah, hal tersebut disebabkan oleh: (1) distribusi kelas pada dataset yang tidak seimbang, (2) kebutuhan akan pemahaman konteks yang lebih kompleks, serta (3) adanya narasi yang secara umum terlihat relevan terhadap proyek tetapi tidak spesifik terhadap aspek rubrik yang dinilai. Meskipun demikian, Pipeline digital scaffolding masih mampu mengenali kesesuaian topik pembahasan meskipun mahasiswa menggunakan variasi ekspresi yang berbeda dengan terminologi yang digunakan dalam rubrik. Sebagai contoh, narasi "ia memahami apa yang perlu dicari dalam iklan, walaupun pada awalnya dia tidak paham tetapi selalu menanyakan ketidakpahamannya itu" berhasil dideteksi pada aspek rubrik "Pemahaman terhadap Isi Iklan" pada dekomposisi "Tingkat Pemahaman Konten Iklan." Meskipun tidak menggunakan frasa yang identik dengan dekomposisi rubrik. Temuan ini menunjukkan bahwa model embedding mampu menangkap kesamaan makna pada tingkat frasa semantik yang tidak dapat dijangkau melalui pendekatan berbasis pencocokan kata kunci semata.

Sebaliknya, koherensi skor dan narasi merupakan indikator yang paling menantang. Rendahnya performa pada indikator ini menunjukkan bahwa model embedding mengalami kesulitan ketika harus membedakan tingkatan kualitas jawaban yang bersifat ordinal, seperti membedakan narasi yang merepresentasikan tingkat pemahaman "kurang", "cukup", atau "sangat". Pada kasus ini, narasi mahasiswa sering kali telah membahas aspek deskriptor skor pada rubrik. Namun, deskriptor skor dalam rubrik tidak dibedakan berdasarkan topik yang dibahas melainkan berdasarkan tingkat pencapaian terhadap deskriptor skor yang sama. Akibatnya, narasi yang seharusnya dipetakan ke kategori skor yang berbeda dapat menghasilkan representasi semantik yang berdekatan karena secara bersamaan membahas aspek deskriptor skor yang serupa. Temuan ini menunjukkan bahwa tantangan utama pada indikator koherensi skor dan narasi yang menilai kesesuaian narasi dengan skor yang dituju terletak pada kemampuan pipeline digital scaffolding untuk membedakan tingkatan kualitas yang bersifat ordinal berdasarkan narasi mahasiswa.

Berbeda dengan ketiga indikator tersebut, kedalaman elaborasi diimplementasi melalui aturan heuristik berbasis threshold 25 kata leksikal . Oleh karena itu, indikator ini tidak dievaluasi menggunakan precision, recall, dan F1-score sebagaimana indikator berbasis model embedding. Hasil analisis menunjukkan bahwa narasi yang lebih panjang cenderung memiliki peluang lebih besar untuk memenuhi indikator lain, khususnya cakupan rubrik. Temuan ini mendukung penggunaan kedalaman elaborasi sebagai indikator struktural untuk mengidentifikasi kebutuhan mahasiswa dalam mengembangkan penjelasan yang lebih rinci.

Sintesis terhadap hasil analisis error memperlihatkan adanya pola yang konsisten pada indikator berbasis model embedding. Sebagian besar kesalahan muncul karena kebutuhan untuk melakukan inferensi evaluatif terhadap informasi yang disampaikan secara implisit. Mahasiswa sering kali menyampaikan penilaian melalui pengalaman, observasi, atau deskripsi aktivitas konkret yang tidak menggunakan terminologi yang identik dengan rubrik. Sebagai contoh, narasi seperti "dia dapat memahami informasi dengan sangat baik" dapat merepresentasikan unit dekomposisi "Tingkat Pemahaman Konten Iklan" pada aspek rubrik "Pemahaman terhadap Isi Iklan". Meskipun kata "pemahaman" tidak pernah disebutkan secara langsung. Temuan ini menunjukkan bahwa model embedding tetap diperlukan untuk menangkap variasi ekspresi yang memiliki makna serupa. Namun demikian, hasil penelitian juga menunjukkan bahwa model embedding belum sepenuhnya memadai ketika sistem harus melakukan inferensi evaluatif yang lebih mendalam atau membedakan tingkatan kualitas jawaban yang bersifat ordinal.

Temuan tersebut memberikan implikasi terhadap desain pipeline yang diusulkan. Indikator yang bersifat struktural, seperti kedalaman elaborasi, dapat dideteksi secara efektif melalui pendekatan deterministik yang sederhana dan transparan. Sebaliknya, indikator yang berkaitan dengan kesamaan makna memerlukan representasi semantik melalui embedding. Meskipun demikian, hasil penelitian menunjukkan bahwa representasi semantik saja belum cukup untuk menangani seluruh kompleksitas evaluasi naratif. Oleh karena itu, integrasi pendekatan deterministik dalam pipeline digital scaffolding berperan sebagai mekanisme pelengkap untuk meningkatkan konsistensi pengambilan keputusan.

Di luar besaran metrik komputasional yang telah dipaparkan, karakteristik performa pipeline tersebut juga perlu diinterpretasikan dari sisi konsekuensi pedagogisnya, mengingat sistem beroperasi sebagai mekanisme scaffolding pada Zone of Proximal Development (ZPD) yang telah dijelaskan pada subbab II.1.9 Dalam konteks ini, kesalahan deteksi pada tingkat indikator baik berupa false negative maupun false positive perlu ditinjau sebagai potensi gangguan terhadap prinsip scaffolding itu sendiri.

Prinsip contingency (Pea, 2004) yang diadopsi pada subbab III.1 mensyaratkan bahwa bantuan selaras dengan kebutuhan aktual mahasiswa. Baik false negative maupun false positive pada dasarnya merupakan pelanggaran terhadap prinsip tunggal ini, FN berarti bantuan tidak diberikan padahal kondisi aktual membutuhkannya, sedangkan FP berarti bantuan diberikan padahal kondisi aktual tidak membutuhkannya. Kedua jenis kesalahan ini perlu dipahami sebagai konsekuensi klasifikasi biner pada tingkat indikator tekstual yang dijelaskan pada rumus III.3, yang dalam penelitian ini diperlakukan sebagai proksi operasional atas kebutuhan intervensi, dengan kesadaran bahwa proksi tersebut terbatas pada manifestasi tekstual yang dapat diobservasi pada subbab I.7 poin 8, bukan pengukuran langsung terhadap kapasitas evaluative judgement mahasiswa secara utuh.

Pembahasan berikut secara spesifik merujuk pada konsekuensi FN/FP dalam konteks kelompok treatment, yaitu ketika deteksi indikator digunakan untuk memicu intervensi real-time bukan pada kelompok kontrol, yang narasinya juga dianalisis melalui pipeline yang sama namun semata untuk keperluan pengukuran outcome pasca-eksperimen yang dijelaskan pada III.6.6.3A tanpa memicu scaffolding apa pun.

Karena sistem beroperasi secara real-time dan mengevaluasi ulang indikator pada setiap perubahan teks sesuai dengan requirement yang dijelaskan pada Lampiran 6, sebuah kejadian false negative pada satu siklus evaluasi tidak serta-merta berarti kesempatan intervensi hilang secara permanen dalam sesi tersebut, indikator yang sama tetap dievaluasi ulang seiring mahasiswa melanjutkan revisi. Risiko yang sesungguhnya bersifat kumulatif yaitu apabila false negative terjadi berulang pada beberapa siklus revisi, atau terjadi tepat pada versi narasi yang akhirnya dikirimkan tanpa revisi lanjutan, barulah kesempatan intervensi pada kondisi tersebut benarbenar tidak tertangani hingga akhir sesi penulisan tersebut.

Sebaliknya, false positive tidak dapat diperlakukan sebagai kesalahan tanpa biaya. Temuan pada subbab V.2.5 mengenai split-attention effect dan gangguan autoscroll menunjukkan bahwa kemunculan scaffolding terlepas dari ketepatan triggernya diindikasikan berkorelasi dengan peningkatan beban kognitif. Dengan demikian, FN dan FP sama-sama membawa konsekuensi nyata, namun berbeda jenis: FN berisiko pada gap pedagogis yang tidak tertangani, sedangkan FP berisiko pada beban kognitif dan disrupsi visual akibat intervensi yang tidak relevan.

Berdasarkan keseluruhan temuan tersebut, RQ1 dapat dijawab bahwa proses kalibrasi pipeline digital scaffolding yang diusulkan memiliki indikasi konfigurasi yang memaksimalkan kesesuaian dengan anotasi manusia pada dataset yang tersedia dalam mendeteksi keempat indikator tekstual narasi feedback, melalui kombinasi model semantik dan aturan heuristik, dengan performa yang berbedabeda sesuai dengan karakteristik indikator yang diukur. Indikator cakupan rubrik dan koherensi skor-narasi menunjukkan performa deteksi tingkat menengah, kedalaman elaborasi dikur melalui aturan heuristik, sementara relevansi topik menunjukkan performa deteksi terendah. Pipeline digital scaffolding menunjukkan performa yang relatif lebih tinggi pada indikator yang bergantung pada pencocokan makna semantik dan karakteristik tekstual yang dapat diamati secara langsung, namun mengalami penurunan performa ketika diperlukan inferensi evaluatif, seperti membedakan tingkatan kualitas yang bersifat ordinal atau memetakan hubungan implisit antara narasi mahasiswa dan konstruk evaluatif dalam rubrik.

Temuan ini menunjukkan bahwa pipeline digital scaffolding memiliki potensi feasibility untuk mengekstraksi keempat indikator tekstual narasi feedback pada narasi yang telah ditulis mahasiswa, meskipun belum sepenuhnya mampu menangani seluruh kebutuhan interpretasi evaluatif yang terkandung dalam narasi reflektif serta memerlukan pengujian terpisah pada held-out test set yang independen untuk memverifikasi performa generalisasi secara mutlak. Di sisi lain, tinjauan terhadap konsekuensi pedagogis dari kesalahan deteksi menunjukkan bahwa false negative dan false positive membawa risiko yang berbeda sifat, masing-masing berpotensi menghambat penyelesaian kesenjangan artikulasi atau menambah beban kognitif sehingga performa pipeline perlu dimaknai tidak hanya dari akurasi komputasionalnya, tetapi juga dari kesesuaiannya dengan prinsip contingency yang mendasari desain scaffolding.

**V.3.2 Dampak Intervensi terhadap Pemenuhan Indikator (RQ 2)**

Research question yang kedua mengevaluasi sejauh mana digital scaffolding membantu pemenuhan keempat indikator tekstual narasi feedback antara kelompok kontrol dan treatment, serta bagaimana mahasiswa berinteraksi dengan sistem tersebut di lingkungan eksperimen. Jawaban pertanyaan ini diinterpretasikan melalui dua sumber yang saling melengkapi, yaitu outcome dan evaluasi proses sebagaimana divisualisasikan pada [Gambar V.17.](#page-6-0)

Sebelum membahas hasil pengujian statistik lebih jauh, terdapat satu batasan yang perlu diperhatikan terkait mekanisme pemicu intervensi pada eksperimen ini. Sistem digital scaffolding mengevaluasi narasi mahasiswa menggunakan threshold yang sebelumnya dikalibrasi pada instrumen data historis. Threshold tersebut diterapkan langsung pada rubrik eksperimen tanpa proses validasi ulang secara empiris. Keputusan desain ini membawa risiko bahwa akurasi deteksi pipeline selama eksperimen berlangsung berpotensi lebih rendah dibandingkan metrik F1- Score yang dilaporkan pada jawaban RQ 1.

Data frekuensi kebutuhan bantuan yang terekam berdasarkan Gambar V.4, frekuensi pemicu scaffolding berada pada rentang distribusi yang operasional. Sistem tidak mengalami malfungsi seperti pemberian intervensi secara terus menerus atau tidak memicu intervensi sama sekali. Hal ini menunjukkan bahwa threshold masih berfungsi, namun hasil pengujian perlu diinterpretasikan dengan kesadaran bahwa efektivitas intervensi memiliki risiko tranferabilitas tersebut.

Gambar V.17. Kerangka untuk Menjawab RQ 2

Evaluasi outcome difokuskan pada pengujian statistik terhadap tingkat pemenuhan keempat indikator tekstual narasi feedback pada kondisi jawaban akhir dalam feedback mahasiswa. Analisis pada tahap ini mengidentifikasi keterkaitan antara keberadaan scaffolding dengan tingkat pemenuhan keempat indikator tekstual narasi feedback. Analisis tingkat proses ini memanfaatkan rekaman proses revisi narasi, transisi status indikator, serta pola respons mahasiswa terhadap teks scaffolding. Integrasi dari kedua perspektif ini memberikan penjelasan yang komprehensif mengenai dampak intervensi dan mekanisme kerjanya.

**V.3.2.1 Perbedaan Hasil Akhir Kelompok Kontrol dan Treatment (RQ 2)**

Analisis terhadap dampak digital scaffolding difokuskan pada interpretasi hasil pengujian statistik inferensial yang telah dilaporkan pada subbab V.2.3. Mengingat penelitian ini merupakan pilot study dengan ukuran sampel yang relatif kecil, serta tidak seluruh indikator memenuhi asumsi parametrik, hasil MANOVA diposisikan sebagai analisis multivariat yang bersifat eksploratori untuk mengidentifikasi pola perbedaan secara keseluruhan antara kelompok kontrol dan treatment. Untuk mengurangi ketergantungan pada asumsi parametrik di tingkat indikator individual, analisis lanjutan dilakukan menggunakan Mann-Whitney U. Atas dasar itu, interpretasi hasil penelitian ini menekankan arah perbedaan dan besaran effect size sebagai estimasi awal bagi penelitian konfirmatori berikutnya, alih-alih klaim signifikansi yang definitif.

Pada level multivariat menggunakan MANOVA pada peer assessment menghasilkan Pillai Trace = 0,3047 dan nilai signifikansi = 0,0441 dan Self Assessment Pillai Trace = 0,2677 dan nilai signifikansi = 0,0688. Perbedaan ini mengindikasikan bahwa keberadaan digital scaffolding lebih konsisten berkaitan dengan perbedaan profil keempat indikator secara simultan ketika mahasiswa menilai pekerjaan peer dibandingkan ketika menilai pekerjaan diri sendiri.

Penelusuran lebih spesifik pada tingkat univariat menyingkap bahwa indikator kedalaman elaborasi (I) menjadi satu-satunya dimensi yang merespons intervensi secara konsisten. Data pada Tabel V.10 dan Tabel V.11 memperlihatkan bahwa indikator ini mencatat nilai < 0,01 pada kedua jenis assessment dengan effect size rank-biserial 0,49 pada self assessment dan 0,487 pada peer assessment. Konsistensi temuan pada kedua jenis assessment menjadi indikasi kuat bahwa bantuan digital scaffolding berkaitan dengan peningkatan mahasiswa menghasilkan narasi feedback yang lebih elaboratif.

Di sisi lain, indikator cakupan rubrik (), koherensi skor dan narasi (), serta relevansi topik (&) tidak mencatat perbedaan yang signifikan antar kelompok Meskipun indikator cakupan rubrik pada self assessment mencatat effect size sebesar 0,329 yang mengarah pada peningkatan kelompok treatment. Namun, bukti empiris dari ukuran sampel ini tidak memiliki kekuatan statistik yang memadai untuk mengesahkannya secara formal.

Perbedaan signifikansi multivariat antara peer assessment dan self assessment dapat ditelusuri sebagian melalui karakteristik kondisi awal narasi pada kedua konteks penilaian tersebut. Data deskriptif pada Tabel V.6 dan Tabel V.7 menunjukkan bahwa pada kelompok kontrol, rerata pemenuhan indikator kedalaman elaborasi tercatat lebih rendah pada peer assessment (0,044) dibandingkan self assessment (0,074). Kondisi awal yang lebih rendah ini memberikan ruang perbaikan yang secara proporsional lebih besar bagi digital scaffolding untuk menghasilkan perubahan yang dapat diamati pada indikator tersebut, sebagaimana tercermin dari effect size kedalaman elaborasi yang sedikit lebih tinggi pada peer assessment (0,487) dibandingkan self assessment (0,49)

Namun demikian, pola tersebut tidak berlaku secara seragam pada ketiga indikator lainnya. Pada kelompok kontrol, rerata pemenuhan cakupan rubrik justru lebih tinggi pada peer assessment (0,191) dibandingkan self assessment (0,132), demikian pula pada koherensi skor dan narasi (0,603 berbanding 0,426). Pola ini bertentangan dengan asumsi bahwa peer assessment secara konsisten memiliki kondisi awal yang lebih rendah pada seluruh indikator.

Dengan demikian, penjelasan mengenai ruang perbaikan yang lebih besar hanya dapat diposisikan secara spesifik pada indikator kedalaman elaborasi, dan tidak dapat digeneralisasi sebagai penjelasan tunggal atas signifikansi multivariat pada peer assessment secara keseluruhan. Kontribusi cakupan rubrik, koherensi skornarasi, dan relevansi topik terhadap perbedaan multivariat tersebut tidak dapat dijelaskan melalui mekanisme yang sama, dan penelitian ini tidak memiliki data yang cukup untuk mengisolasi penyebab spesifik dari asimetri tersebut pada ketiga indikator lainnya.

Perlu ditegaskan bahwa keterbatasan statistical power bukan satu-satunya penjelasan yang mungkin bagi hasil non-signifikan pada indikator cakupan rubrik, koherensi skor-narasi, dan relevansi topik. Sebagaimana telah dibahas pada subbab V.4, threshold similarity yang memicu intervensi dikalibrasi menggunakan data historis dan diterapkan langsung pada rubrik CATME tanpa validasi ulang secara empiris. Kondisi ini membuka kemungkinan penjelasan alternatif, yaitu bahwa mekanisme pemicu scaffolding tidak sepenuhnya akurat dalam mendeteksi kebutuhan bantuan pada rubrik eksperimen, sehingga hasil non-signifikan tersebut berpotensi mencerminkan ketidaktepatan triggering, bukan semata-mata ketiadaan efek scaffolding itu sendiri.

Untuk menilai plausibilitas penjelasan alternatif ini, data frekuensi kebutuhan bantuan pada subbab V.2.4.1 dapat ditinjau sebagai bukti tidak langsung. Distribusi trigger pada penelitian ini tidak menunjukkan pola ekstrem, seperti satu indikator yang hampir selalu maupun hampir tidak pernah memicu bantuan pada seluruh partisipan, yang mengindikasikan bahwa sistem tidak mengalami kegagalan kalibrasi yang bersifat gross. Namun demikian, data ini hanya mengonfirmasi bahwa perilaku sistem berada pada rentang yang wajar, bukan bukti bahwa threshold telah terkalibrasi secara tepat terhadap struktur rubrik CATME, mengingat penelitian ini tidak memiliki ground truth anotasi pada rubrik eksperimen untuk memverifikasi ketepatan triggering secara langsung.

Data kuesioner pada subbab V.2.5.1 turut ditinjau untuk mencari sinyal kualitatif yang mendukung atau menolak hipotesis ketidaktepatan triggering. Keluhan mahasiswa yang terekam didominasi oleh isu penyajian antarmuka, yaitu splitattention effect dan gangguan auto-scroll, bukan oleh keluhan mengenai ketidaksesuaian antara scaffolding yang muncul dan kebutuhan aktual narasi mereka. Ketiadaan pola keluhan seperti "scaffolding muncul padahal tulisan sudah sesuai" atau "scaffolding tidak muncul padahal dibutuhkan" tidak mendukung hipotesis ketidaktepatan triggering secara kuat, meskipun ketiadaan bukti ini juga tidak dapat dijadikan bukti bahwa triggering telah berlangsung optimal.

Dengan demikian, penelitian ini tidak menemukan indikasi bahwa mekanisme triggering scaffolding mengalami kegagalan kalibrasi yang ekstrem selama eksperimen berlangsung. Namun, penelitian ini juga tidak memiliki bukti yang cukup untuk memastikan bahwa threshold hasil kalibrasi pada data historis sepenuhnya valid ketika diterapkan pada rubrik CATME. Oleh karena itu, hasil non-signifikan pada ketiga indikator tersebut perlu dipandang sebagai temuan yang dibatasi oleh dua sumber ketidakpastian yang tidak dapat dipisahkan kontribusinya secara empiris dalam desain penelitian ini, yaitu keterbatasan statistical power sebagai pilot study dan risiko transferabilitas threshold pada rubrik yang berbeda dari data kalibrasi.

**V.3.2.2 Dinamika Interaksi dan Resolusi Scaffolding (Menjawab RQ 2)**

Keempat sumber data yang telah disajikan pada subbab V.2.4 mengenai distribusi bantuan, tingkat respons, pola revisi serta dinamika pemenuhan indikator pada dasarnya merekam satu mekanisme yang sama dari berbagai sudut pandang: dimana kesulitan muncul, bagaimana mahasiswa merespons, dengan rasa apa mereka merespons, dan apakah setiap respons berhasil memenuhi indikator tekstual narasi feedback.

Titik awal mekanisme kebutuhan bantuan digital scaffolding yang paling sering muncul. Sebagaimana ditunjukkan pada subbab V.2.4.1, indikator cakupan rubrik dan koherensi skor dan narasi paling sering memicu bantuan digital scaffolding pada self maupun peer assessment, menunjukkan bahwa kesulitan terkait kelengkapan aspek evaluasi dan keselarasan skor-justifikasi lebih sering muncul dibandingkan indikator lainnya.

Ketika kebutuhan terdeteksi dan bantuan digital scaffolding diberikan, mahasiswa pada umumnya menindaklanjuti dengan melakukan perbaikan atau merevisi narasi feedback mereka. tipe perubahan No Change sangat rendah pada kedua jenis assessment. Namun, menindaklanjuti bantuan tidak berarti masalah otomatis terselesaikan. Tingkat resolusi dalam satu kali perbaikan tetap rendah untuk sebagian indikator, dengan relevansi topik mencatat tingkat pemenuhan tertinggi. Bentuk tindak lanjut ini juga relatif homogen yaitu operasi penambahan mendominasi pola revisi pada kedua konteks, jauh melampaui substitusi, penghapusan, atau revisi struktural mahasiswa cenderung mempertahankan struktur jawaban dan memperkaya isinya, bukan menulis ulang dari awal.

Dominasi strategi penambahan ini menjelaskan mengapa perubahan status indikator tidak berlangsung seragam. Pada kedalaman elaborasi, strategi menambah penjelasan selaras langsung dengan kebutuhan indikator tersebut, sehingga perubahan menuju status terpenuhi relatif lebih sering ditemukan V.2.4.4. Sebaliknya, cakupan rubrik menuntut penambahan aspek evaluasi yang benar-benar belum tercakup, bukan sekadar kalimat tambahan. Sementara koherensi skor-narasi menuntut penyelarasan ulang antara skor dan narasi. Kebutuhan yang lebih spesifik ini membuat strategi "menambah" saja tidak selalu cukup.

Konsekuensinya paling terlihat pada cakupan rubrik, yang mencatat tingkat persistensi tertinggi di antara keempat indikator. Data pada subbab V.2.4.1 menunjukkan bahwa indikator cakupan rubrik mencatat tingkat persistensi tertinggi di antara keempat indikator (93,4% pada self assessment; 95,5% pada peer assessment).

Pertama dari sisi desain sistem. Mekanisme rule-based yang diterapkan III.6.3.5A bersifat deterministik dan statis: kombinasi vektor keputusan yang sama akan selalu menghasilkan template prompt yang sama sesuai dengan rumus III.34 tanpa variasi bentuk maupun eskalasi bantuan berdasarkan riwayat kegagalan mahasiswa pada siklus-siklus sebelumnya.

Kedua, dari sisi konstruk indikator: pemenuhan cakupan rubrik menuntut pengetahuan substantif untuk menghubungkan kriteria rubrik yang abstrak dengan pengalaman konkret mahasiswa selama proyek, tuntutan kognitif yang berpotensi tidak teratasi hanya dengan pengulangan arahan template, terlepas dari apakah arahan tersebut bervariasi atau identik. Kemungkinan ini sejalan dengan pola false negative yang ditemukan pada evaluasi komputasional pipeline V.3.1, di mana narasi yang menyampaikan bukti evaluatif secara implisit gagal dipetakan oleh model ke kriteria rubrik eksplisit. Namun, perlu dicatat bahwa temuan pada V.3.1.1 tersebut merupakan bukti keterbatasan deteksi model, bukan bukti langsung mengenai kesulitan artikulasi mahasiswa, sehingga kedua sumber keterbatasan ini, kegagalan model mengenali narasi yang sebenarnya relevan, dan kegagalan mahasiswa menulis narasi yang relevan sama sekali, tidak dapat dipisahkan kontribusinya terhadap data persistence rate yang tersedia.

Dengan demikian, tingginya persistensi pada cakupan rubrik paling tepat diinterpretasikan sebagai indikasi bahwa mekanisme within-session tanpa eskalasi bentuk bantuan belum teruji ketahanannya terhadap kegagalan berulang pada indikator yang menuntut penyelarasan substantif antara pengalaman konkret dan kriteria abstrak dengan penyebab spesifiknya tidak dapat dipilah lebih lanjut dari data yang tersedia. Gambaran di atas didasarkan pada tingkat resolusi dalam satu kali siklus revisi. Namun, ketidakberhasilan pada satu siklus tidak berarti kebutuhan bantuan sama sekali tidak terselesaikan sepanjang sesi. Data pada subbab V.2.4.4 menunjukkan bahwa sebagian indikator, khususnya kedalaman elaborasi dan relevansi topik, mencapai penyelesaian akhir yang lebih tinggi dibandingkan resolusi pada revisi tunggal. Pola ini mengindikasikan bahwa perbaikan berlangsung secara bertahap, di mana mahasiswa tidak selalu menyelesaikan kebutuhan bantuan pada upaya pertama, tetapi melalui beberapa siklus revisi berikutnya dalam sesi yang sama, sebagian kebutuhan tersebut akhirnya tertangani.

Merangkai temuan-temuan ini, digital scaffolding pada penelitian ini berfungsi lebih sebagai pemicu proses revisi bertahap dibandingkan instruksi yang menghasilkan perbaikan instan. Dampaknya cenderung lebih terlihat pada indikator yang selaras dengan strategi revisi umum mahasiswa, perluasan elaborasi narasi dan kurang terlihat pada indikator yang menuntut penyelarasan substantif antara kriteria abstrak, pengalaman konkret, dan justifikasi skor.

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

V.3.2.4 **Sintesis Jawaban RQ 2**

Berdasarkan hasil analisis statistik (Subbab V.3.2.1), data proses interaksi (SubbabV.3.2.2), dan evaluasi terhadap kerangka digital scaffolding (Subbab V.3.2.3), dapat disusun rangkaian interpretasi untuk menjawab RQ2 secara komprehensif.

Pertama, digital scaffolding secara konsisten mendeteksi kebutuhan bantuan selama proses revisi. Indikator cakupan rubrik dan koherensi skor–narasi merupakan indikator yang paling sering memicu scaffolding sekaligus paling sering gagal dipenuhi mahasiswa secara mandiri. Pola ini konsisten dengan implementasi dynamic assessment yang telah dievaluasi pada Subbab [V.3.3.3.](#page-2-0)

Kedua, mahasiswa secara aktif merespons scaffolding yang diberikan. Hal ini ditunjukkan oleh proporsi No Change yang rendah pada kedua konteks penilaian, dengan revisi yang didominasi oleh strategi penambahan informasi (insertion) dibandingkan substitusi maupun penghapusan.

Ketiga, dominasi revisi berbentuk insertion berimplikasi pada perbedaan tingkat keberhasilan antarindikator. Sebagaimana dibahas pada Subbab V.3.2.2 dan [V.3.3.4](#page-3-0), mekanisme adding–fading biner memadai untuk indikator kedalaman elaborasi yang dapat dipenuhi melalui penambahan informasi, tetapi belum cukup mendukung indikator cakupan rubrik dan koherensi skor–narasi yang memerlukan restrukturisasi isi evaluatif. Kondisi tersebut juga dipengaruhi oleh batasan desain sistem yang tidak menerapkan mekanisme eskalasi bantuan berdasarkan riwayat kegagalan mahasiswa (Subbab I.7 poin 12). Hubungan kausal antara jenis revisi dan keberhasilan pemenuhan indikator tidak dapat dipastikan dari data yang tersedia karena klasifikasi Levenshtein hanya merekam jenis operasi tekstual tanpa mengevaluasi kesesuaiannya dengan isi scaffolding.

Keempat, keterbatasan perbaikan pada indikator yang lebih kompleks turut dipengaruhi oleh mekanisme penyajian scaffolding secara real-time, yang menimbulkan beban kognitif tambahan selama proses revisi, sebagaimana dibahas pada Subbab V.3.2.3.

Kelima, signifikansi multivariat yang lebih konsisten pada peer assessment dibandingkan self assessment sebagian dapat dikaitkan dengan kondisi awal indikator kedalaman elaborasi yang lebih rendah pada peer assessment. Namun, penjelasan tersebut tidak berlaku secara umum karena pola kondisi awal pada indikator cakupan rubrik, koherensi skor–narasi, dan relevansi topik tidak menunjukkan kecenderungan yang sama.

Secara keseluruhan, hasil tersebut menunjukkan bahwa dampak digital scaffolding terhadap kualitas narasi feedback bersifat spesifik terhadap karakteristik indikator yang dituju. Efektivitas intervensi paling jelas terlihat pada indikator kedalaman elaborasi, yang selaras dengan pola revisi dominan mahasiswa serta karakteristik mekanisme adding–fading yang diterapkan. Sebaliknya, indikator yang memerlukan restrukturisasi isi evaluatif belum menunjukkan peningkatan yang sebanding, sehingga pengembangan mekanisme scaffolding yang lebih adaptif, bertahap, dan mampu menyesuaikan intensitas bantuan berdasarkan riwayat revisi menjadi arah pengembangan yang relevan pada penelitian selanjutnya.

**V.3.3 Interpretasi Berdasarkan Kerangka Digital Scaffolding**

Selain interpretasi terhadap hasil pengujian statistik dan data proses yang telah dipaparkan pada subbab sebelumnya, bagian ini menginterpretasikan implementasi sistem berdasarkan kerangka konseptual digital scaffolding yang telah ditetapkan pada Subbab III.6.4. Interpretasi disusun mengikuti struktur konseptual penelitian, yaitu identitas pedagogis sistem, prinsip pemberian bantuan, karakteristik operasional digital scaffolding, dan evaluasi terhadap implementasinya. Dengan demikian, pembahasan menjelaskan kesesuaian digital scaffolding yang dibangun dengan karakteristik digital scaffolding yang menjadi landasan perancangannya.

**V.3.3.1 Identitas sebagai** *Hard Computer-Based Scaffold*

Berdasarkan klasifikasi Saye & Brush (2002), scaffolding yang dikembangkan dalam penelitian ini termasuk hard computer-based scaffold yang ditanamkan pada Aplikasi SAPA. Seluruh mekanisme intervensi dibangun sebelum proses pengisian narasi feedback terlebih dahulu berdasarkan aturan dan kondisi yang telah didefinisikan pada III.6.4.1. Selama proses perbaikan narasi, pemberian intervensi berlangsung tanpa intervensi pihak ketiga diluar dari digital scaffolding itu sendiri. Karakteristik tersebut merefleksikan identitas pedagogis scaffolding sebagaimana telah dirancang pada tahap pengembangan.

**V.3.3.2 Contingency dan Shared External Representation**

Prinsip contingency diwujudkan melalui mekanisme yang hanya mengaktifkan intervensi digital scaffolding ketika hasil evaluasi indikator menunjukkan adanya kebutuhan bantuan. Keputusan tersebut dihasilkan oleh fungsi keputusan 0yang dijelaskan pada Subbab III.6.4.1 sehingga setiap pemberian bantuan didasarkan pada kondisi narasi yang sedang dievaluasi.

Rubrik yang telah didekomposisi sebagai de4 dan def pada Subbab III.6.3.2A berperan sebagai berperan sebagai shared external representation Pea (2004) Digital scaffolding memberikan intervensi dengan acuan unit dekomposisi tersebut. Sebagai contoh, variabel missing\_coverage pada Tabel III.17 secara langsung diturunkan dari hasil dekomposisi rubrik. Dalam konteks penelitian ini, shared external representation merujuk pada penggunaan acuan evaluatif yang sama oleh sistem dan mahasiswa selama proses intervensi digital scaffolding.

**V.3.3.3 Dynamic Assessment**

Karakteristik dynamic assessment Belland (2017) didasarkan pada temuan data implementation rate dan frekuensi trigger serta pola revisi yang disajikan pada Subbab V.2.4. Temuan pada data tersebut digunakan untuk menilai apakah sistem melakukan diagnosis secara berulang berdasarkan kondisi terbaru artefak tulisan mahasiswa. Hasil menunjukkan bahwa sistem mengevaluasi ulang keempat indikator tekstual pada setiap siklus revisi sehingga diagnosis selalu disesuaikan dengan kondisi terbaru dari artefak tulisan mahasiswa. Dengan demikian, proses diagnosis berlangsung secara berulang sepanjang siklus revisi dan konsisten dengan karakteristik dynamic assessment.

**V.3.3.4** *Adding–Fading*

Karakteristik providing just the right amount of support melalui mekanisme adding dan fading (Belland, 2017) didasarkan pada temuan data persistence rate dan resolution rate pada Subbab V.2.4.1. Hasil menunjukkan bahwa tingkat keterwujudan karakteristik ini berbeda pada setiap indikator.

Pada indikator kedalaman elaborasi, persistence rate yang relatif rendah disertai resolution rate yang lebih tinggi menunjukkan bahwa setelah scaffolding diberikan, mahasiswa umumnya mampu merevisi narasi hingga indikator tersebut terpenuhi. Kondisi tersebut memungkinkan mekanisme fading berlangsung sesuai dengan rancangan sistem.

Sebaliknya, indikator cakupan rubrik memperlihatkan persistence rate sebesar 93,4% pada self assessment dan 95,5% pada peer assessment. Nilai tersebut menunjukkan bahwa indikator tetap belum terpenuhi meskipun scaffolding telah diberikan berulang kali. Sesuai dengan batasan penelitian pada Subbab I.7 poin 12, sistem mempertahankan bentuk dan intensitas template prompt yang sama pada setiap siklus revisi tanpa mempertimbangkan riwayat kegagalan mahasiswa.

Perbedaan tersebut menunjukkan bahwa mekanisme adding–fading biner memiliki tingkat kecukupan yang berbeda sesuai karakteristik revisi yang diperlukan. Mekanisme ini mendukung revisi yang berorientasi pada penambahan informasi, sebagaimana ditunjukkan pada indikator kedalaman elaborasi, namun belum memberikan dukungan yang memadai pada revisi yang memerlukan restrukturisasi isi evaluatif, sebagaimana terlihat pada indikator cakupan rubrik. Pola tersebut sejalan dengan hasil eksperimen pada Subbab V.2.3, di mana peningkatan yang signifikan hanya ditemukan pada indikator kedalaman elaborasi, serta menjadi dasar bagi pengembangan mekanisme eskalasi bantuan pada penelitian selanjutnya

**V.4 Keterbatasan Penelitian**

Temuan yang diperoleh pada penelitian ini perlu dipahami dalam konteks desain, populasi, dan lingkungan eksperimen yang digunakan. Oleh karena itu interpretasi hasil tidak dimaksudkan untuk menghasilkan kesimpulan yang bersifat universal mengenai potensi kontribusi digital scaffolding dalam mendukung penulisan narasi feedback yang lebih artikulatif pada konteks pembelajaran. Sebaliknya, hasil penelitian memberikan bukti empiris mengenai sejauh mana digital scaffolding  berbasis rubrik bekerja secara komputasional dan kondisi eksperimen yang diuji, sekaligus mengidentifikasi sejumlah keterbatasan yang menjadi peluang pengembangan bagi penelitian selanjutnya.

**V.4.1 Keterbatasan Generalisasi Konteks Penelitian**

Terkait dengan batasan eksternal (external validity)Penelitian yang dilaksanakan pada konteks pembelajaran yang spesifik yaitu mahasiswa Program Sarjana Terapan, Program Studi Teknik Informatika di Politeknik Negeri Bandung yang sedang mengikuti PjBL dalam mata kuliah Manajemen Kualitas Terpadu. Oleh karena itu temuan yang diperoleh perlu dipahami dalam batas konteks tersebut.

Karakteristik tugas, bentuk rubrik, budaya pembelajaran serta tingkat pengalaman mahasiswa yang memberikan narasi feedback merupakan aspek kontekstual yang berbeda dan belum dievaluasi dalam penelitian ini. Oleh karena itu, belum dapat dipastikan bahwa apakah bantuan digital scaffolding akan menunjukkan pola yang sama pada konteks dengan karakteristik yang berbeda. Variasi karakteristik tersebut berpotensi memengaruhi kebutuhan bantuan akan digital scaffolding maupun cara mahasiswa merespons bantuan yang diperoleh. Dengan demikian, temuan yang diperoleh dalam penelitian ini belum dapat diasumsikan berlaku secara langsung pada disiplin ilmu lain, jenjang pendidikan yang berbeda, atau aktivitas reflektif yang menggunakan struktur penilaian yang berbeda.

Perlu diingat bahwa eksperimen yang dilakukan terbatas pada lingkungan institusi dan satu siklus pelaksanaan pembelajaran. Konsekuensinya, penelitian ini belum dapat memastikan apakah pola temuan yang diperoleh akan muncul secara konsisten pada populasi, institusi atau konteks pembelajaran yang berbeda. Penelitian lanjutan pada bidang studi, institusi pendidikan dan skenario jenis pembelajaran selain PjBL diperlukan untuk menguji konsistensi temuan yang diperoleh pada penelitian ini.

**V.4.2 Keterbatasan Desain Eksperimen yang Dipilih**

Penelitian ini menggunakan randomized posttest-only control group design (Desain 6) yang dipilih untuk menghindari potensi bias yang dapat muncul akibat pemberian pre-test sebelum intervensi digital scaffolding diberikan. Meskipun desain ini memiliki kekuatan yang tinggi dalam mengendalikan ancaman validitas internal melalui random assignment, terdapat beberapa keterbatasan yang perlu diperhatikan dalam menginterpretasikan hasil penelitian.

Pertama, penelitian ini tidak dapat mengamati perubahan tingkat pemenuhan pada keempat indikator tekstual narasi feedback pada tingkat individu sebelum dan sesudah menerima perlakuan. Karena pengukuran hanya dilakukan pada tahap posttest, analisis yang dihasilkan berfokus pada perbedaan hasil antara kelompok treatment dan kelompok kontrol, bukan pada besarnya perubahan yang dialami masing-masing mahasiswa selama eksperimen berlangsung. Dengan demikian, penelitian ini tidak dapat menunjukkan secara langsung sejauh mana tingkat pemenuhan keempat indikator tekstual narasi feedback individu meningkat dibandingkan kondisi awalnya sebelum menerima bantuan digital scaffolding.

Kedua, ketiadaan pre-test menyebabkan kemampuan awal mahasiswa terkait penyusunan dan artikulasi narasi feedback tidak dapat diukur secara langsung. Meskipun random assignment digunakan untuk meminimalkan kemungkinan perbedaan karakteristik awal antar kelompok, penelitian ini tidak memiliki data empiris yang dapat digunakan untuk memverifikasi kesetaraan kemampuan awal setiap partisipan sebelum perlakuan diberikan. Oleh karena itu, interpretasi hasil eksperimen didasarkan pada asumsi bahwa proses randomisasi telah menghasilkan distribusi karakteristik awal yang relatif seimbang antara kelompok treatment dan kelompok kontrol.

Ketiga, penelitian ini belum dapat mengevaluasi apakah terdapat perbedaan pola hasil antar mahasiswa dengan tingkat kemampuan awal yang berbeda. Karena tidak tersedia data baseline individual, penelitian ini hanya menghasilkan gambaran kondisi pada tingkat kelompok sehingga variasi yang mungkin muncul berdasarkan kemampuan awal partisipan tidak dapat dianalisis secara langsung.

Meskipun demikian, keterbatasan tersebut merupakan konsekuensi metodologis yang melekat pada penggunaan randomized posttest-only control group design. Dalam konteks penelitian ini, desain tersebut tetap dipilih karena kemampuannya mengurangi potensi testing effect sekaligus memungkinkan evaluasi intervensi dilakukan tanpa memberikan pengukuran awal yang berpotensi memengaruhi respons partisipan terhadap digital scaffolding.

**V.4.3 Keterbatasan Bentuk Digital Scaffolding**

Digital scaffolding pada penelitian ini dirancang bersifat hard scaffolding dalam bentuk prompt berbasis indikator rubrik yang bertujuan mengarahkan mahasiswa untuk memperbaiki aspek-aspek tertentu pada narasi feedback. Hasil penelitian menunjukkan bahwa bentuk bantuan tersebut lebih sering diikuti oleh perbaikan pada indikator yang berkaitan dengan penambahan informasi, seperti kedalaman elaborasi. Namun demikian, indikator yang memerlukan penalaran evaluatif yang lebih kompleks, seperti koherensi skor dan narasi, masih menunjukkan tingkat penyelesaian kebutuhan bantuan yang relatif lebih rendah dibandingkan indikator lainnya. Respons terhadap keluhan usabilitas ini dari segi antarmuka aplikasi telah didokumentasikan pada Lampiran 7 sebagai bagian dari transparansi pengembangan, namun tidak dievaluasi ulang dalam eksperimen utama ini.

Temuan tersebut mengindikasikan bahwa digital scaffolding yang berbasiskan teks prompt mungkin memiliki keterbatasan ketika digunakan untuk mendukung proses evaluasi yang menuntut justifikasi, refleksi, atau penalaran yang lebih mendalam. Dalam konteks tersebut, mahasiswa tidak hanya memerlukan informasi mengenai bagian yang perlu diperbaiki, tetapi juga mungkin memerlukan bantuan yang dapat memandu proses berpikir evaluatif yang mendasari penyusunan narasi feedback.

Penelitian ini hanya mengevaluasi satu bentuk digital scaffolding yang diwujudkan melalui prompt. Oleh karena itu, penelitian ini belum dapat memberikan kesimpulan mengenai bagaimana bentuk scaffolding alternatif, seperti scaffolding reflektif, scaffolding metakognitif, maupun kombinasi beberapa jenis scaffolding, dapat memengaruhi tingkat pemenuhan keempat indikator tekstual narasi feedback mahasiswa. Eksplorasi terhadap bentuk bantuan yang berbeda menjadi peluang penelitian lanjutan untuk memahami jenis scaffolding yang paling sesuai untuk mendukung pemenuhan indikator cakupan rubrik, koherensi skor dan narasi, kedalaman elaborasi, serta relevansi topik.

**V.4.4 Keterbatasan Dataset**

Evaluasi performa pipeline (RQ 1) memiliki keterbatasan metodologis terkait penggunaan dataset anotasi. Pada penelitian ini, satu-satunya dataset anotasi yang tersedia digunakan secara serentak untuk seleksi model embedding, pemilihan metode ekstraksi, dan penentuan threshold.

Karena keterbatasan ukuran dataset, penelitian ini tidak memisahkan data seleksi dari data evaluasi. Akibatnya, metrik F1-Score yang dilaporkan merepresentasikan performa konfigurasi terbaik yang secara khusus dimaksimalkan terhadap dataset tersebut. Pendekatan ini rentan terhadap leakage antara fase kalibrasi dan evaluasi, sehingga nilai akurasi yang dilaporkan mengalami overestimate dan tidak dapat diklaim sebagai ukuran generalisasi mulai performa pipeline data baru.

**V.4.5 Keterbatasan Transferabilitas Threshold pada Rubrik Eksperimen**

Terdapat risiko pergeseran performa saat pipeline diimplementasikan pada lingkungan eksperimen. Threshold similarity yang menjadi pemicu intervensi scaffolding dikalibrasi menggunakan distribusi skor semantik dari rubrik historis. Namun, pada saat eksperimen, treshold ini digunakan secara langsung pada rubrik yang berbeda tanpa dilakukan validasi ulang secara empiris.

Perlu dicatat bahwa risiko ketidaksesuaian threshold pada konteks rubrik yang berbeda ini sebagian dapat dimitigasi oleh karakteristik arsitektur pipeline. Karena model embedding digunakan dalam kondisi frozen dan tidak mengalami fine-tuning atau pembaruan parameter selama sistem beroperasi, representasi semantik yang dihasilkan bersifat konsisten dan bebas dari risiko overfitting yang umum terjadi pada fase training.

Meskipun demikian, stabilitas representasi semantik model ini tidak serta-merta menjamin stabilitas threshold. Distribusi nilai cosine similarity sangat berpotensi bergeser mengikuti karakteristik linguistik unit dekomposisi pada rubrik eksperimen yang memiliki panjang frasa, tingkat abstraksi kriteria, dan domain kosakata yang berbeda dari rubrik historis. Oleh karena itu, stabilitas mode tidak dapat disamakan dengan ketepatan threshold di konteks yang baru, dan performa deteksi saat eksperimen berlangsung berpotensi tidak seoptimal hasil yang dilaporkan pada tahap kalibrasi.

**BAB VI**

**ANALISIS DAMPAK HASIL PENELITIAN**

Bab ini menyajikan analisis outcome yang diharapkan dari penerapan hasil penelitian terhadap pemangku kepentingan yang telah diidentifikasi pada subbab I.5, serta mengevaluasi sejauh mana instrumen digital scaffolding ini dapat diterima oleh pengguna secara fungsional maupun usabilitas berdasarkan temuan pada babbab sebelumnya.

**VI.1 Outcome yang Diharapkan dari Pengguna/Mitra**

Sebagaimana telah dipaparkan pada subbab I.5, penelitian ini melibatkan dua kelompok pemangku kepentingan di lingkungan Jurusan Teknik Komputer dan Informatika (JTK) Politeknik Negeri Bandung.

Kelompok pertama adalah mahasiswa yang mengikuti mata kuliah berbasis Project-Based Learning (PjBL) yang memiliki self dan peer assessment sebagai bagian dari proses evaluasi, dalam hal ini mahasiswa peserta mata kuliah Manajemen Kualitas Terpadu yang menjadi subjek pilot study sebagaimana dipetakan pada subbab IV.5.1. Outcome yang diharapkan dari kelompok ini adalah peningkatan kelengkapan, relevansi, dan keselarasan narasi feedback yang mereka tulis selama proses penilaian berlangsung, sehingga proses artikulasi evaluative expression menjadi lebih terarah dibandingkan tanpa bantuan digital scaffolding.

Kelompok kedua adalah dosen pengampu mata kuliah berbasis PjBL yang menggunakan rubrik sebagai komponen evaluasi. Outcome yang diharapkan dari kelompok ini adalah ketersediaan output self dan peer assessment berupa skor numerik dan narasi kualitatif per kriteria yang sudah melalui proses komputasi empat indikator tekstual, sehingga narasi yang diterima dosen memiliki informasi evaluatif yang lebih terstruktur dibandingkan kondisi tanpa digital scaffolding.

Hasil pilot study sebagaimana dipaparkan pada subbab V.2 hingga V.3 menjadi bukti awal sejauh mana kedua outcome tersebut tercapai, yaitu internalisasi kriteria evaluasi oleh mahasiswa (evaluative judgement dan evaluative expression) dan ketersediaan narasi terstruktur bagi dosen, khususnya pada indikator kedalaman elaborasi yang menunjukkan indikasi dampak pada kedua jenis assessment.

**VI.2 Dampak Pedagogis Hasil Penelitian bagi Mitra**

Subbab ini mengevaluasi dampak pedagogis dari instrumen digital scaffolding secara keseluruhan, ditinjau dari manfaatnya dalam mendukung proses refleksi mahasiswa dan evaluasi formatif dosen. Evaluasi ini menyintesis temuan utama yang telah diuraikan pada BAB IV dan BAB V untuk menakar dampak nyata riset ini bagi mitra.

Dari sisi proses pembelajaran, intervensi ini membantu dosen sebagai pihak pemangku kepentingan untuk mengidentifikasi gap artikulasi dan meminimalisir narasi feedback dengan kualitas rendah berdasarkan keempat indikator tekstual narasi feedback, yaitu cakupan terhadap rubrik, koherensi, kedalaman elaborasi, serta relevansi topik. Bagi mahasiswa, scaffolding berfungsi sebagai pendamping kognitif yang memberikan arahan adaptif saat mereka merumuskan penilaian di dalam Zone of Proximal Development (ZPD). Secara pedagogis, riset ini menunjukkan potensi penerapan sistem komputasional untuk mendukung pembentukan skill feedback literacy, yakni kapasitas kognitif mahasiswa untuk memahami kriteria rubrik dan mengartikulasikannya menjadi penilai objektif yang lebih konstruktif di lingkungan PjBL JTK.

Dari sisi penerimaan pengguna berdasarkan evaluasi di subbab V.2.5, keberadaan sistem ini mendapatkan respons yang positif dari mahasiswa, khususnya dalam memfasilitasi mahasiswa mengingat kriteria rubrik yang terlewat. Meskipun dinilai sangat bermanfaat, analisis juga mengungkap efek samping berupa peningkatan beban kognitif pada pengguna. Hal ini dipicu oleh perubahan tampilan layar yang terjadi saat mahasiswa masih berada di tengah proses mengetik narasi.

Temuan di atas mengonfirmasi bahwa meskipun integrasi instrumen digital scaffolding secara arsitektural memiliki dampak pada penyusunan narasi evaluatif, adopsi jangka panjang yang optimal oleh mahasiswa masih memerlukan penelitian lanjutan untuk mengeksplorasi bentuk scaffolding lainnya.

**BAB VII**

**PENUTUP**

Bab ini menjelaskan kesimpulan dari keseluruhan hasil penelitian yang telah dilakukan untuk menjawab research question yang telah dirumuskan pada subbab I.3, sara bagi penelitian selanjutnya, serta rencana keberlanjutan dan komersialisasi dari hasil penelitian yang dihasilkan pada tugas akhir ini.

**VII.1 Kesimpulan**

Penelitian ini bertujuan merancang pipeline digital scaffolding berbasis rubrik yang mengintegrasikan Natual Language Processing (NLP) dengan rule-based untuk mendeteksi empat indikator tekstual narasi feedback secara real-time, serta mengukur dampak intervensi tersebut terhadap pemenuhan indikator melalui pilot study. Berdasarkan hasil dan pembahasan pada BAB V, kedua tujuan tersebut telah dicapai dengan temuan sebagai berikut.

Terkait RQ 1, proses kalibrasi pipeline digital scaffolding yang dirancang memiliki indikasi menemukan konfigurasi optimal pada dataset historis yang tersedia untuk mendeteksi keempat indikator tekstual narasi feedback melalui kombinasi model semantik dan aturan heuristik, dengan tingkat kesesuaian yang berbeda-beda sesuai karakteristik indikator. Indikator cakupan rubrik dan koherensi skor-narasi menunjukkan tingkat kesesuaian deteksi tingkat menengah, dengan F1-Score sebesar 0,61 dan 0,53, kedalaman elaborasi diukur melalui aturan heuristik deterministik berbasis panjang narasi, sementara relevansi topik menunjukkan tingkat kesesuaan terendah, dengan F1-score senilai 0,43. Pipeline menunjukkan performa yang relatif lebih baik pada indikator yang bergantung pada pencocokan makna semantik dan karakteristik tekstual yang dapat diamati secara langsung, namun mengalami penurunan performa ketika diperlakukan inferensi evaluatif yang lebih kompleks, seperti membedakan tingkatan kualitas ordinal pada indikator koherensi skor dan narasi. Karena ketiadaan data uji yang independen, performa ini merepresentasikan feasibility sistem pada tahap kalibrasi.

Terkait RQ 2, hasil pengujian multivariat menunjukkan indikasi efek signifikan pada peer assessment, dengan nilai Pillai's Trace sebesar 0,3047 dan p sebesar 0,0441, namun tidak signifikan pada self assessment. Pengujian univariat lebih lanjut mengungkap bahwa dari keempat indikator, hanya kedalaman elaborasi yang secara konsisten memiliki indikasi signifikan pada self assessment, dengan nilai p sebesar 0,005 dan effect size sebesar 0,49, maupun peer assessment dengan nilai p sebesar 0,0059 dan effect size sebesar 0,487, sementara cakupan rubrik, koherensi skor-narasi, dan relevansi topik belum menunjukkan perbedaan yang signifikan antara kelompok kontrol dan treatment. Temuan ini selaras dengan data interaksi pada subbab V.2.4 yang menunjukkan bahwa revisi mahasiswa terhadap scaffolding didominasi oleh operasi penambahan informasi, yang secara struktural lebih sesuai untuk memperkaya isi narasi dibanding memperbaiki struktur evaluatifnya. Dengan demikian, dampak digital scaffolding memiliki indikasi paling kuat pada indikator yang selaras dengan bentuk revisi yang secara alami dilakukan mahasiswa.

Dari sisi penerimaan pengguna, hasil kuesioner pada subbab V.2.5 menunjukkan bahwa mahasiswa secara umum memandang digital scaffolding bermanfaat dalam membantu proses penulisan feedback. Namun demikian, sebagian mahasiswa juga melaporkan adanya tambahan beban kognitif akibat kemunculan scaffolding secara real-time, sehingga aspek rancangan interaksi menjadi perhatian penting pada pengembangan sistem selanjutnya.

Secara keseluruhan, penelitian ini memberikan tiga kontribusi utama. Pertama, mengusulkan pipeline digital scaffolding berbasis rubrik untuk narasi feedback berbahasa Indonesia yang menggabungkan semantic embedding dan aturan heuristik. Kedua, menunjukkan bahwa empat indikator tekstual dapat digunakan sebagai dasar komputasional untuk mendeteksi kebutuhan scaffolding selama proses penulisan. Ketiga, menyediakan bukti empiris awal mengenai pengaruh digital scaffolding terhadap kualitas narasi feedback melalui pilot study beserta estimasi effect size sebagai dasar perancangan penelitian berskala lebih besar, dengan catatan bahwa efektivitas ini diukur dalam kondisi transfer threshold antarrubrik yang masih memerlukan validasi lebih lanjut.

**VII.2 Saran**

Berdasarkan kesimpulan dan keterbatasan penelitian yang telah dipaparkan pada subbab [V.4](#page-4-0) serta [BAB VI,](#page-9-0) berikut adalah saran yang dapat menjadi fokus bagi penelitian selanjutnya.

1. Peningkatan kemampuan deteksi pada indikator yang menuntut inferensi evaluatif kompleks, khususnya koherensi skor-narasi dan relevansi topik, misalnya melalui fine-tuning model embedding berbahasa Indonesia yang lebih sensitif terhadap perbedaan kualitas ordinal, atau pendekatan lain di luar similarity berbasis embedding tunggal.
2. Eksplorasi bentuk digital scaffolding alternatif di luar prompt berbasis indikator, seperti scaffolding refleksif atau metakognitif, maupun kombinasi beberapa jenis scaffolding, untuk menjawab keterbatasan pada subbab [V.4.3.](#page-6-0)
3. Penggunaan desain eksperimen yang memungkinkan pengukuran perubahan pada tingkat individu, misalnya dengan desain pre-test, untuk mengatasi keterbatasan randomized posttest-only control group design yang diidentifikasi pada subbab [V.4.2](#page-5-0).
4. Evaluasi lanjutan terhadap efektivitas modifikasi antarmuka collapsible yang diterapkan pada Lampiran 7 dalam menurunkan beban kognitif pengguna, karena modifikasi tersebut belum diuji ulang pada kelompok eksperimen baru.
5. Replikasi penelitian pada konteks pembelajaran, mata kuliah, atau institusi yang berbeda di luar JTK Polban dan mata kuliah Manajemen Kualitas Terpadu, untuk menguji konsistensi temuan sebagaimana diidentifikasi pada subbab [V.4.1](#page-4-1), sekaligus memperbesar jumlah sampel agar power statistik penelitian lebih kuat.

**VII.3 Rencana Keberlanjutan dan Komersialisasi Hasil Penelitian**

Untuk memaksimalkan dampak dari penelitian ini, dirumuskan beberapa langkah keberlanjutan. Pertama, hasil riset empiris ini akan dipublikasikan ke dalam jurnal

atau prosiding konferensi ilmiah yang berfokus pada inovasi pendidikan dan linguistik komputasional, guna menyumbangkan temuan pada diskursus feedback literacy. Kedua, secara institusional, pipeline scaffolding ini memiliki prospek teknis untuk diintegrasikan secara permanen ke dalam arsitektur aplikasi SAPA yang digunakan secara luas oleh Jurusan Teknik Komputer dan Informatika, sehingga instrumen ini dapat direplikasi pada berbagai mata kuliah PjBL lainnya di semester mendatang. Ketiga, apabila didukung oleh optimasi infrastruktur komputasi di masa depan, fungsionalitas sistem ini dapat diabstraksikan menjadi modul plug-and-play yang independen. Hal ini membuka ruang untuk integrasi lintas platform dengan Learning Management System (LMS) eksternal di luar institusi melalui skema lisensi B2B (Business-to-Business), yang menjadi pijakan awal menuju komersialisasi produk ed-tech spesifik.

**DAFTAR PUSTAKA**

- Aimah, F. R., & Suhartoyo, E. (2024). A decade of Indonesian EFL students' voices toward peer feedback practices during synchronous and asynchronous periods: A systematic literature review. Journal on English as a Foreign Language, 14(1), 48–72. https://doi.org/10.23971/jefl.v14i1.7247
- Albattah, W., & Khan, R. U. (2025). Impact of imbalanced features on large datasets. Frontiers in Big Data, 8. https://doi.org/10.3389/fdata.2025.1455442
- Alfaro, R., Allende-Cid, H., & Allende, H. (2023). Multilabel Text Classification with Label-Dependent Representation. Applied Sciences (Switzerland), 13(6). https://doi.org/10.3390/app13063594
- Bell, S. (2010). Project-Based Learning for the 21st Century: Skills for the Future. The Clearing House: A Journal of Educational Strategies, Issues and Ideas, 83(2), 39–43. https://doi.org/10.1080/00098650903505415
- Belland, B. R. (2017). Instructional Scaffolding in STEM Education Strategies and Efficacy Evidence. https://doi.org/10.1007/978-3-319-02565-0
- Brookhart, S. (2013). How to Create and Use Rubrics for Formative Assessment and Grading. ASCD.
- Brown, P., & Levinson, S. C. (1987). Politeness Some universals in language usage Studies in Interactional Sociolinguistics 4 (Vol. 4).
- Cagiltay, K. (2006). Scaffolding strategies in electronic performance support systems: Types and challenges. Innovations in Education and Teaching International, 43(1), 93–103. https://doi.org/10.1080/14703290500467673
- Camarata, T., & Slieman, T. A. (2020). Improving Student Feedback Quality: A Simple Model Using Peer Review and Feedback Rubrics. Journal of Medical Education and Curricular Development, 7. https://doi.org/10.1177/2382120520936604
- Campbell, D. T., Stanley, J. C., Mifflin, H., Boston, C., Geneva, D., Hopewell, I., Palo, N. J., & London, A. (1963). EXPERIMENTAL AND QUASI-EXPERIMENT Al DESIGNS FOR RESEARCH.

- Carless, D., & Boud, D. (2018). The development of student feedback literacy: enabling uptake of feedback. Assessment and Evaluation in Higher Education, 43(8), 1315–1325. https://doi.org/10.1080/02602938.2018.1463354
- Cheng, R. W. Y., Lam, S. F., & Chan, J. C. Y. (2008). When high achievers and low achievers work in the same group: The roles of group heterogeneity and processes in project-based learning. British Journal of Educational Psychology, 78(2), 205–221. https://doi.org/10.1348/000709907X218160
- Cho, K., & MacArthur, C. (2011). Learning by Reviewing. Journal of Educational Psychology, 103(1), 73–84. https://doi.org/10.1037/a0021950
- COCHRAN, W. G. . (1977). Sampling techniques. Wiley.
- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences Second Edition.
- Crina, G., & Abraham, A. (2011). Intelligent Systems (Vol. 17). Springer. https://doi.org/10.1007/978-3-642-21004-4
- Curtis, R., Moon, C. C., Hanmore, T., Hopman, W. M., & Baxter, S. (2024). Use the right words: evaluating the effect of word choice and word count on quality of narrative feedback in ophthalmology competency-based medical education assessments. Canadian Medical Education Journal. https://doi.org/10.36834/cmej.76671
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly: Management Information Systems, 13(3), 319–339. https://doi.org/10.2307/249008
- Deemter, K., Krahmer, E., & Theune, M. (2005). Squibs and Discussions Real versus Template-Based Natural Language Generation: A False Opposition? Computational Linguistics, 31, 15–24. http://www.cs.utwente.nl/
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. http://arxiv.org/abs/1810.04805
- Ding, L., Zhang, H., Zhou, J., & Chen, B. (2025). Contextualization, Procedural Logic, and Active Construction: A Cognitive Scaffolding Model for Topic

- Sentiment Analysis in Game-Based Learning. Behavioral Sciences 2025, Vol. 15, 15(10). https://doi.org/10.3390/bs15101327
- Dornyei, Zoltan., & Murphey, Tim. (2011). Group Dynamics in the Language Classroom. Cambridge University Press.
- Dunning, D., Heath, C., & Suls, J. M. (2004). Flawed Self-Assessment Implications for Health, Education, and the Workplace. 5(3), 69.
- Durg, A., Zhang, A., & Savelka, J. (2025). LLM-powered Framework for Automatic Generation of Metacognitive Scaffolding Cues for Introductory Programming in Higher Education. https://oli.cmu.edu/
- Enevoldsen, K., Chung, I., Kerboua, I., Kardos, M., Mathur, A., Stap, D., Gala, J., Siblini, W., Krzeminski, D., Winata, G. I., Sturua, S., Utpala, S., Ciancone, M., Schaeffer, M., Sequeira, G., Misra, D., Dhakal, S., Rystrøm, J., Solomatin, R., … Muennighoff, N. (2025). MMTEB: Massive Multilingual Text Embedding Benchmark. 13th International Conference on Learning Representations, ICLR 2025, 19, 102004–102060. https://arxiv.org/pdf/2502.13595
- Fateen, M., Wang, B., & Mine, T. (2024). Beyond Scores: A Modular RAG-Based System for Automatic Short Answer Scoring With Feedback. IEEE Access, 12, 185371–185385. https://doi.org/10.1109/ACCESS.2024.3508747
- Fiel Peres, F. (2026). Effect sizes for nonparametric tests. In Biochemia medica (Vol. 36, Number 1, p. 010101). https://doi.org/10.11613/BM.2026.010101
- Gao, T., Yao, X., & Chen, D. (2022). SimCSE: Simple Contrastive Learning of Sentence Embeddings. http://arxiv.org/abs/2104.08821
- Gaynor, J. W. (2020). Peer review in the classroom: student perceptions, peer feedback quality and the role of assessment. Assessment and Evaluation in Higher Education, 45(5), 758–775. https://doi.org/10.1080/02602938.2019.1697424
- Ghali, M.-K., Farrag, A., Lam, S., & Won, D. (2025). BEYONDWORDS is All You Need: Agentic Generative AI based Social Media Themes Extractor.

- Gu, J., Chen, J., & Yan, Z. (2026). Fostering feedback literacy by scaffolding selfregulated feedback: a comparative study of GenAI and human peers. Frontiers in Education, 10. https://doi.org/10.3389/feduc.2025.1736446
- Guo, P., Saab, N., Post, L. S., & Admiraal, W. (2020). A review of project-based learning in higher education: Student outcomes and measures. International Journal of Educational Research, 102. https://doi.org/10.1016/j.ijer.2020.101586
- Hattie, J., & Timperley, H. (2007). The power of feedback. In Review of Educational Research (Vol. 77, Number 1, pp. 81–112). SAGE Publications Inc. https://doi.org/10.3102/003465430298487
- Hertzog, M. A. (2008). Considerations in determining sample size for pilot studies. Research in Nursing and Health, 31(2), 180–191. https://doi.org/10.1002/nur.20247
- Hyland, F., & Hyland, K. (2001). Sugaring the pill Praise and criticism in written feedback. Journal of Second Language Writing, 10(3), 1815–212.
- Jain, U., Mishra, P., Dash, A., & Pandey, A. (2025). Multi-label multi-class text classification-enhanced attention in transformers with knowledge distillation. In Journal of Applied Research and Technology (Vol. 23, Number 1). www.jart.icat.unam.mx
- Jonsson, A., & Svingby, G. (2007). The use of scoring rubrics: Reliability, validity and educational consequences. In Educational Research Review (Vol. 2, Number 2, pp. 130–144). https://doi.org/10.1016/j.edurev.2007.05.002
- Julious, S. A. (2005). Sample size of 12 per group rule of thumb for a pilot study. Pharmaceutical Statistics, 4(4), 287–291. https://doi.org/10.1002/pst.185
- Jurafsky, Dan., & Martin, J. H. . (2009). Speech and language processing : an introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall.
- Kollar, I., & Fischer, F. (2010). Peer assessment as collaborative learning: A cognitive perspective. In Learning and Instruction (Vol. 20, Number 4, pp. 344–348). Elsevier BV. https://doi.org/10.1016/j.learninstruc.2009.08.005

- Krajcik, Joseph, B., & Phyllis. (2006). 19. project-based learning. The Cambridge Handbook of the Learning Sciences, 317–333. https://doi.org/https://doi.org/10.1017/CBO9781139519526.018
- Leal, R., Kesäniemi, J., Koho, M., & Hyvönen, E. (2021). Relevance feedback search based on automatic annotation and classification of texts. OpenAccess Series in Informatics, 93. https://doi.org/10.4230/OASIcs.LDK.2021.18
- Levenshtein, V. I. (1966). Binary Codes Capable of Correcting Deletions, Insertions and Reversals. 10.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2021). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. http://arxiv.org/abs/2005.11401
- Luan NG, M., Al Ghaithi, A., & Behforouz, B. (2026). Digital Scaffolding as Learning Opportunities: Enhancing Vocabulary Knowledge Through Copilot AI. Educational Process International Journal, 20(1). https://doi.org/10.22521/edupij.2026.20.12
- Lücking, A., Driller, C., Stoeckel, M., Abrami, G., Pachzelt, A., & Mehler, A. (2022). Multiple annotation for biodiversity: developing an annotation framework among biology, linguistics and text technology. Language Resources and Evaluation, 56(3), 807–855. https://doi.org/10.1007/s10579- 021-09553-5
- Manning, C. D., Raghavan, P., & Schütze, H. (2009). An Introduction to Information Retrieval. https://nlp.stanford.edu/IRbook/pdf/irbookonlinereading.pdf
- Mazzullo, E., Bulut, O., Walsh, C., Sitarenios, G., & Macintosh, A. (2025). Fine-Tuning GPT-3.5-Turbo for Automatic Feedback Generation. Proceedings of the ACM Symposium on Applied Computing, 40–47. https://doi.org/10.1145/3672608.3707735
- Mestre, J. P. ., & Ross, B. H. . (2011). The psychology of learning and motivation. 55, Cognition in education. Academic Press.

- Moeliono, A. M. . (2017). Tata bahasa baku bahasa Indonesia. Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan dan Kebudayaan.
- Mohammad, T., Mohammad, T., Nazim, M., Alzubi, A. A. F., & Khan, S. I. (2025). Evaluating The Efficacy of A Large Language Model in Scaffolding Research Report Writing for EFL Learners. International Journal of Basic and Applied Sciences, 14(7), 33–45. https://doi.org/10.14419/g2apsg21
- Mu, H., & Schunn, C. D. (2025). The good, bad, and ugly of comment prompts: Effects on length and helpfulness of peer feedback. International Journal of Educational Technology in Higher Education, 22(1). https://doi.org/10.1186/s41239-025-00502-8
- Muennighoff, N., Tazi, N., Magne, L., Reimers, N., & Ai, C. (2014). MTEB: Massive Text Embedding Benchmark Hugging Face. https://huggingface.co/datasets/mteb/
- Myers, Glenford., Sandler, Corey., & Badgett, Tom. (2011). The Art of Software Testing, 3rd Edition. 240. https://books.google.com/books/about/The\_Art\_of\_Software\_Testing.html?h l=id&id=GjyEFPkMCwcC
- Negnevitsky, M. N. (2005). Artificial Intelligence A Guide to Intelligent Systems. Addison Wesley. www.pearsoned.co.uk
- Nelson, M. M., & Schunn, C. D. (2008). The nature of feedback: how different types of peer feedback affect writing performance. Instructional Science 2008 37:4, 37(4), 375–401. https://doi.org/10.1007/s11251-008-9053-x
- Nicol, D., Thomson, A., & Breslin, C. (2014). Rethinking feedback practices in higher education: a peer review perspective. Assessment and Evaluation in Higher Education, 39(1), 102–122. https://doi.org/10.1080/02602938.2013.795518
- Ohland, M. W., Loughry, M. L., Woehr, D. J., Bullard, L. G., Felder, R. M., Finelli, C. J., Layton, R. A., Pomeranz, H. R., & Schmucker, D. G. (2012). The comprehensive assessment of team member effectiveness: Development of a behaviorally anchored rating scale for self- and peer evaluation. Academy of

- Management Learning and Education, 11(4), 609–630. https://doi.org/10.5465/amle.2010.0177
- Omotehinwa, T. O., Ezekiel, R. A., Onoja, M., Omeye, E. C., & Ibrahim, Y. A. (2025). Comparative Evaluation of Transformer-Based Models for Automated Short-Answer Grading. NIPES - Journal of Science and Technology Research, 7(1 Special Issue), 843–849. https://doi.org/10.37933/nipes/7.4.2025.SI97
- Panadero, E., Jonsson, A., & Botella, J. (2017). Effects of self-assessment on selfregulated learning and self-efficacy: Four meta-analyses. In Educational Research Review (Vol. 22, pp. 74–98). Elsevier Ltd. https://doi.org/10.1016/j.edurev.2017.08.004
- Pea, R. D. (2004). The Social and Technological Dimensions of Scaffolding and Related Theoretical Concepts for Learning, Education, and Human Activity. In The Journal of the Learning Sciences (Vol. 13, Number 3). https://telearn.hal.science/hal-00190619v1
- Perikos, I., Grivokostopoulou, F., & Hatzilygeroudis, I. (2017). Assistance and Feedback Mechanism in an Intelligent Tutoring System for Teaching Conversion of Natural Language into Logic. International Journal of Artificial Intelligence in Education, 27(3), 475–514. https://doi.org/10.1007/s40593- 017-0139-y
- Qasim, R., Bangyal, W. H., Alqarni, M. A., & Ali Almazroi, A. (2022a). A Fine-Tuned BERT-Based Transfer Learning Approach for Text Classification. Journal of Healthcare Engineering, 2022. https://doi.org/10.1155/2022/3498123
- Qasim, R., Bangyal, W. H., Alqarni, M. A., & Ali Almazroi, A. (2022b). A Fine-Tuned BERT-Based Transfer Learning Approach for Text Classification. Journal of Healthcare Engineering, 2022. https://doi.org/10.1155/2022/3498123
- Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (n.d.). Sta n z a : A Python Natural Language Processing Toolkit for Many Human Languages. Retrieved https://spacy.io/

- Qin, P., Xu, W., & Guo, J. (2017). Providing Definitive Learning Direction for Relation Classification System. Journal of Control Science and Engineering, 2017. https://doi.org/10.1155/2017/3924641
- Quirk, R., Greenbaum, S., Leech, G., & Svartvik, J. (1985). Comprehensive of the Language. English, 1–1779. https://books.google.com/books/about/A\_Comprehensive\_Grammar\_of\_the\_ English\_L.html?hl=id&id=jyZaAAAAMAAJ
- Rahimi, Z., Litman, D., Correnti, R., Wang, E., & Matsumura, L. C. (2017). Assessing Students' Use of Evidence and Organization in Response-to-Text Writing: Using Natural Language Processing for Rubric-Based Automated Scoring. International Journal of Artificial Intelligence in Education, 27(4), 694–728. https://doi.org/10.1007/s40593-017-0143-2
- Reddy, V., & Veeranjaneyulu, N. (2024). Fine-Tuning Pipeline: A Strategic Approach to Multiclass Text Classification (pp. 946–954). https://doi.org/10.2991/978-94-6463-471-6\_90
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. http://arxiv.org/abs/1908.10084
- Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond Accuracy: Behavioral Testing of NLP Models with CheckList. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 4902–4912. https://doi.org/10.18653/V1/2020.ACL-MAIN.442
- Saye, J. W., & Brush, T. (2002). Scaffolding Critical Reasoning About History and Social Issues in Multimedia-Supported Learning Environments. Educational Technology Research and Development, 50(2), 77–96. https://doi.org/http://doi.org/10.1007/BF02505026.
- Setiawan, I. (2026a). Feedback discourse in Indonesian project-based learning: language use in student self- and peer-assessment. Assessment and Evaluation in Higher Education. https://doi.org/10.1080/02602938.2026.2620645
- Setiawan, I. (2026b). Sentiment-aware NLP in reflective writing: toward fair and adaptive dashboards for Indonesian project-based learning. Interactive Learning Environments. https://doi.org/10.1080/10494820.2026.2624678

- Setiawan, I., Kao, H.-Y., & Chuang, K.-T. (2026). Enhancing Feedback Literacy in Project-Based Science Education: Discourse Analytics and Technology Design. Journal of Science Education and Technology (JOST), Accepted.
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). EXPERIMENTAL AND QUASI-EXPERIMENTAL DESIGNS FOR GENERALIZED CAUSAL INFERENCE .jr-"-* fr HOUGHTON MIFFLIN COMPANY Boston New York.
- Sun, Q., Chen, F., & Yin, S. (2023). The role and features of peer assessment feedback in college English writing. Frontiers in Psychology, 13. https://doi.org/10.3389/fpsyg.2022.1070618
- Tai, J., Ajjawi, R., Boud, D., Dawson, P., & Panadero, E. (2018). Developing evaluative judgement: enabling students to make decisions about the quality of work. Higher Education, 76(3), 467–481. https://doi.org/10.1007/s10734- 017-0220-3
- Thüs, D., Malone, S., & Brünken, R. (2024). Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature. Frontiers in Psychology, 15. https://doi.org/10.3389/fpsyg.2024.1474892
- Tsoumakas, G., & Katakis, I. (2009). Multi-Label Classification: An Overview. http://www.dmoz.org/
- van Popta, E., Kral, M., Camp, G., Martens, R. L., & Simons, P. R. J. (2017). Exploring the value of peer feedback in online learning for the provider. In Educational Research Review (Vol. 20, pp. 24–34). Elsevier Ltd. https://doi.org/10.1016/j.edurev.2016.10.003
- Vygotsky, L. S., Cole, M., John-Steiner, V., Scribner, S., & Souberman, E. (1978). Mind in Society The Development of Higher Psychological Processes. Harvard University Press.
- Wang, L., Yang, N., Huang, X., Yang, L., Majumder, R., & Wei, F. (2024). Improving Text Embeddings with Large Language Models.
- Wang, W., Wei, F., Dong, L., Bao, H., Yang, N., & Zhou, M. (2020). MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-

- Trained Transformers. Advances in Neural Information Processing Systems, 2020-December. https://arxiv.org/pdf/2002.10957
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

Lampiran 4. Teori NLP Arsitektur Transformer

**TEORI NATURAL LANGUAGE PROCESSING DAN ARSITEKTUR TRANSFORMER**

**LAMPIRAN TUGAS AKHIR**

Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

**Oleh:**

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

**PROGRAM SARJANA TERAPAN PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG**

Lampiran 5. Struktur Data Penelitian

**STRUKTUR DATA PENELITIAN (PEER ASSESSMENT, SELF ASSESSMENT, RUBIK)**

**LAMPIRAN TUGAS AKHIR**

Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

**Oleh:**

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

**PROGRAM SARJANA TERAPAN PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG**

Lampiran 6. Analisis Sistem Perancangan Teknis

**ANALISIS SISTEM BERJALAN DAN PERANCANGAN TEKNIS APE**

**LAMPIRAN TUGAS AKHIR**

Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

**Oleh:**

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

**PROGRAM SARJANA TERAPAN PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG 2026**

**PERBAIKAN ANTARMUKA APLIKASI PENDUKUNG EKSPERIMEN PASCA ESPERIMEN**

**LAMPIRAN TUGAS AKHIR**

Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di Jurusan Teknik Komputer dan Informatika

**Oleh:**

Aryo Rakatama 221524003 Muhammad Rama Nurimani 221524021

**PROGRAM SARJANA TERAPAN PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA POLITEKNIK NEGERI BANDUNG**

Lampiran 8. Detail Validasi Skenario Logika Komputasional

Test Case ID  |  Module* (Feature)  |  Case* (-/+/edge)  |  lest Case Name* (Scenario)  |  Precondition* (GIVEN)  |  Steps to execute* (WHEN)  |  Test Data <sup>≠</sup>  |  Expected Result* (THEN)  |  As Expected  |  Result* (PASS/FAIL)  |  Remark
NLP Logic Validation  |  Baseline — Ideal (semua indikator terpenuhi)  |  yze  |  Kirim POST request dengan skor 5  |  Rekan saya menunjukkan komithmen kerja yang sangat Inggi selama proyek bertangsung. Dia selalu memesukan kualitas hasil akhir memenuhi standar yang disepakati, melakukan evaluasi secara berkala dan sagera memperbalki kekurangan. Kuntifusanya sangal menentukan kebertasilan tim.  |  valid=True, d1=0, d2=0, d3=0, d4=0  |  -
TC-NLP-A02  |  NLP Logic Validation  |  positif  |  Rasoline — Ideal Panjang  |  - API NLP aktif pada http://tocalhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 4  |  Sopanjang proyek, rekan saya memunjukkar dedikasi yang kual terhadap etandar kualifas pekerjaan. Komitmen kerjanya terihat dara setiap terasi revisi yang dilakukan dengan telili. Meskipun belum sempurna, dia selalu mengevaluasi hasil kerjanya dan berupaya memperbaikinya sebelum dikumpulkan.  |  d3=0  |  valid=True, d1=0, d2=1, d3=0, d4=1  |  PASS
TC-NLP-B01  |  NLP Logic Validation  |  negatif  |  Malas — Hanya 1 kata  |  - API NLP aktif pada http://localhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 3  |  Balk.  |  d3=1  |  valid=False, d1=1, d2=1, d3=1, d4=1  |  PASS  |  -
rc-NLP-B02  |  NLP Logic Validation  |  negatif  |  Malas — 5 kata  |  <ul> <li>API NLP aktif pada http://localhost:8080/feedback/anal yze</li> </ul>  |  Kirim POST request dengan skor 3  |  Dia bekerja cukup balk.  |  d3=1  |  valid=True, d1=1, d2=1, d3=1, d4=0  |  PASS  |  -
TC-NLP-B03  |  NLP Logic Validation  |  negatif  |  Malas — 15 kata  |  - API NLP aktif pada http://localhost:8080/feedback/anal yzc  |  Kirim POST request dengan skor 4  |  Rekan saya cukup bertanggung jawab dan selalu menyelesalkan tugas yang diberikan kepadanya tepat waktu.  |  d3=1  |  valid=True, d1=1, d2=1, d3=1, d4=1  |  PASS  |  -
TC-NLP-B04  |  NLP Logic Validation  |  negatif  |  Malas — 20 kata  |  - API NLP aktif peda http://localhost:8080/feedback/anal yze  |  Kirlm POST request dengan skor 4  |  Dia cukup balk dalam mengerjakan proyek ini. Selalu hadir dalam meeting dan mengumpulkan tugas tepat waktu. Kerja sama juga cukup baik.  |  d3=1  |  valld=True, d1=1, d2=1, d3=1, d4=0  |  PASS  |  -
TC-NLP-B05  |  NLP Logic Validation  |  edge  |  Malas Tepat 24 Kata (Edge Case Bawah (3)  |  - API NLP aktif pada http://localhost.8080/feedback/anal yze  |  Kirim POST request dengan skor 4  |  Rekan saya menunjukkan kemilmen kerja yang baik dalam menjaga standar kualitas serta kualitas hasil akhir yang selalu memuaskan seluruh anggota tim kami selama proyek  |  d3=1  |  valid=True, d1=0, d2=1, d3=1, d4=1  |  PASS
TC-NLP-B06  |  NLP Logic Validation  |  edge  |  Malas — Tepat 25 Kata (Edge Case Atas f3)  |  - API NLP aktif pada http://localhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 4  |  Rekan saya menunjukkan komitmen kerja yang baik dalam menjaga standar kualitas serta kualitas hasil akhir yang selalu memuaskan seluruh anggola tim kami selama proyek ini  |  d3=0  |  valid=True, d1=0, d2=1, d3=0, d4=1  |  PASS  |  -
TC-NLP-B07  |  NLP Logic Validation  |  negatif  |  Malas — Input Kosong  |  - API NLP aktif pada http://localhost:8080/feedback/anal yzc  |  Kirim POST request dengen skor 3  |  d3=1  |  valid=False, d1=1, d2=1, d3=1, d4=1  |  PASS  |  -
TC-NLP-B08  |  NLP Logic Validation  |  negatif  |  Malas — Hanya Spasi Panjang  |  API NLP aktif pada http://localhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 3  |  d3=1  |  valid=False, d1=1, d2=1, d3=1, d4=1  |  PASS  |  -
TC-NLP-B09  |  NLP Logic Validation  |  negatif  |  Malas — Mengisi Angka Saja  |  API NLP aktif pada http://localhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 3  |  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25  |  d3=1  |  valid=False, d1=1, d2=1, d3=1, d4=1  |  PASS
TC-NLP-C01  |  NLP Logic Validation  |  positif  |  Copy-Paste — Satu kalimat diulang 5x  |  Kirim POST request dengan skor 4  |  Rekan saya bekerja dengan baik, Rekan saya bekerja dengan baik, Rekan saya bekerja dengan baik, Rekan saya bekerja dengan baik, Rekan saya bekerja dengan baik.  |  d3=0  |  valid=True, d1=1, d2=1, d3=0, d4=0  |  PASS
TC-NLP-C02  |  NLP Logic Validation  |  positif  |  Copy-Paste — Kata 'baik' diulang 30x  |  - API NLP aktif pada http://localhost:8080/feedback/anal yze  |  Kirim POST request dengan skor 4  |  baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik baik  |  Observasional  |  valid=False, d1=1, d2=1, d3=1, d4=1  |  PASS  |  Observasiona
TC-NLP-D01  |  NLP Logic Validation  |  negatif  |  Basa-Basi — Pujian generik tanpa keyword rubrik  |  - API NLP aktif pada http://localhost-8080/feedback/anal yzu  |  Kirim POST request dengan skor 5  |  Rekan saya adalah orang yang sangat baik, ramah, dan solalu mau membantu siapupun yang kesulitan. Dia mudah bergaul dan menyenangkan diajak bekerjasama. Orangnya juga jujur dan tidak pemah berbohong kepada anggota tim.  |  d1=1  |  valid=True, d1=1, d2=0, d3=0, d4=0  |  PASS  |  -

Lampiran 9. Hasil Pengujian Kombinasi Template

Test Case ID  |  Template Target  |  Module  |  Case Type  |  Test Case Name  |  Precondition  |  Steps to Execute  |  Test Data (Narasi)  |  Expected Result (Template Key)  |  Actual Result (Template Key)  |  Result (PASS/FAIL)  |  Remark
TC-TPL-TC01  |  invalid  |  Template Coverage Validation  |  negatif  |  Template[invalid] — Narasi kosong (valid=False)  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=3  |  invalid  |  invalid  |  PASS  |  -
TC-TPL-TC02  |  0  |  Template Coverage Validation  |  positif  |  Template[0000] — Narasi ideal komprehensif skor 5  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Rekan saya menunjukkan komitmen kerja yang sangat tinggi selama proyek berlangsung. Dia selalu memastikan kualitas hasil akhir memenuhi standar yang disepakati, melakukan evaluasi secara berkala dan s  |  0  |  0  |  PASS  |  -
TC-TPL-TC03  |  1  |  Template Coverage Validation  |  negatif  |  Template[0001] — Narasi pasar+keyword rubrik skor koheren  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=3  |  Saya kemarin pergi ke pasar membeli sayur dan menemukan komitmen kerja pedagang yang tinggi. Standar kualitas dagangannya terjaga, evaluasi dan perbaikan kualitas pekerjaan terlihat nyata pada setiap  |  1  |  1  |  PASS  |  -
TC-TPL-TC04  |  10  |  Template Coverage Validation  |  edge  |  Template[0010] — Narasi 9 kata keyword rubrik terisolasi  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Hasil akhir pekerjaannya selalu dievaluasi dan kualitasnya luar biasa.  |  10  |  10  |  PASS  |  -
TC-TPL-TC05  |  11  |  Template Coverage Validation  |  negatif  |  Template[0011] — Narasi pasar pendek+keyword rubrik skor koheren  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=3  |  Di pasar tadi saya melihat komitmen kerja yang bagus. Standar kualitas produk dijaga. Evaluasi rutin dilakukan.  |  11  |  11  |  PASS
TC-TPL-TC06  |  100  |  Template Coverage Validation  |  positif  |  Template[0100] — Semua keyword rubrik disebut + skor=5 + narasi negati  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Komitmen kerja rekan saya sangat buruk dan tidak konsisten. Standar kualitas diabalikan dan kualitas hasil akhir sangat jauh dari ekspektasi. Evaluasi dan perbaikan kualitas pekerjaan tidak pemah dila  |  100  |  100  |  PASS  |  -
TC-TPL-TC07  |  101  |  Template Coverage Validation  |  positif  |  Template[0101] — Narasi A02 skor=4: dedikasi tapi d2+d4 terpicu  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=4  |  Sepanjang proyek, rekan saya menunjukkan dedikasi yang kuat terhadap standar kualitas pekerjaan. Komitmen kerjanya terlihat dari setiap iterasi revisi yang dilakukan dengan teliti. Meskipun belum semp  |  101  |  101  |  PASS  |  -
TC-TPL-TC08  |  110  |  Template Coverage Validation  |  positif  |  Template[0110] — Keyword rubrik pendek + skor=5 + narasi negatif  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Komitmen kerja buruk. Standar kualitas diabaikan. Kualitas hasil akhir mengecewakan. Evaluasi tidak dilakukan.  |  110  |  110  |  PASS  |  -
TC-TPL-TC09  |  111  |  Template Coverage Validation  |  positif  |  Template[0111] — Keyword rubrik eksplisit pendek skor=4 (Round2 U02a a  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=4  |  Komitmen kerja rekan baik. Standar kualitas terpenuhi. Kualitas hasil akhir memuaskan. Evaluasi dilakukan.  |  111  |  1 11  |  PASS  |  -
TC-TPL-TC10  |  1000  |  Template Coverage Validation  |  positif  |  Template[1000] — Pujian generik tanpa keyword rubrik panjang skor=5  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Rekan saya adalah orang yang sangat baik, ramah, dan selalu mau membantu siapapun yang kesulitan. Dia mudah bergaul dan menyenangkan diajak bekerjasama. Orangnya juga jujur dan tidak pernah berbohora  |  1000  |  1000  |  PASS  |  -
TC-TPL-TC11  |  1001  |  Template Coverage Validation  |  positif  |  Template[1001] — Narasi komunikasi panjang di QID standar kualitas sko  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Rekan saya memiliki kemampuan komunikasi yang sangat luar biasa. Dia selalu menyampaikan informasi dengan jelas dan efektif kepada seluruh anggota tim. Kemampuannya dalam berkomunikasi dan berkoordina  |  1001  |  1001  |  PASS  |  -
TC-TPL-TC12  |  1010  |  Template Coverage Validation  |  positif  |  Template[1010] — Pujian generik singkat tanpa keyword rubrik skor=5  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Rekan saya sangat baik dan menyenangkan diajak kerja sama.  |  1010  |  1010  |  PASS  |  -
TC-TPL-TC13  |  1011  |  Template Coverage Validation  |  positif  |  Template[1011] — 'sangat produktif' singkat skor=5 di QID kualitas  |  API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=5  |  Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.  |  1011  |  1011  |  PASS  |  -
TC-TPL-TC14  |  1100  |  Template Coverage Validation  |  negatif  |  Template[1100] — Pujian generik panjang skor=1 (inkoherensi besar)  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=1  |  Rekan saya adalah orang yang sangat baik hati, selalu ramah dan jujur kepada semua anggota tim. Dia menyenangkan untuk diajak bekerja sama dan tidak pemah membuat masalah apapun di dalam kelompok kam  |  1100  |  1100  |  PASS
TC-TPL-TC15  |  1101  |  Template Coverage Validation  |  negatif  |  Template[1101] — Narasi kualitas di QID produktivitas skor=1  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=1  |  Rekan saya menunjukkan standar kualitas yang baik dan selalu mengevaluasi pekerjaan serta memperbaiki kualitas hasil akhirnya. Komitmen kerjanya terhadap mutu produk sangat patut diapresiasi oleh selu  |  1101  |  1101  |  PASS  |  -
TC-TPL-TC16  |  1110  |  Template Coverage Validation  |  negatif  |  Template[1110] — Pujian generik singkat skor=1  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=1  |  Rekan saya sangat baik dan menyenangkan diajak kerja.  |  1110  |  1110  |  PASS  |  -
TC-TPL-TC17  |  1111  |  Template Coverage Validation  |  negatif  |  Template[1111] — Produktivitas singkat di QID kualitas skor=1  |  - API NLP aktif pada endpoint /feedback/analyze  |  POST /feedback/analyze dengan skor=1  |  Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.  |  1111  |  1 111  |  1 PASS  |  -

Lampiran 10 Rubrik historis

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Lampiran 11. Sampel Data Anotasi Dataset Cakupan Rubrik dan Relevansi

Bany: Pemahaman informasi penting dari iklan yang dikumpulkan.
Narasi Feedback (S <sub>txt</sub> )  |  Jumlah Iklan yang Dikumpulkan  |  Keragaman Platform Pengumpulan  |  Kesulitan dalam Pengumpulan Data  |  Kemudahan dalam Pengumpulan Data  |  Relevansi Iklan yang Dikumpulkan  |  Tingkat Pemahaman Konten Iklan  |  Identifikasi Informasi Penting
Saya berperan aktif dalam menyamakan format data, menyesuaikan header kolom yang akan dipakai dalam struktur kelompok apa saja. Masalah yang dihadapi adalah banyaknya struktur data yang berbeda atau salah penginputan sehingga harus mem validasi ulang  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Rekan saya memahami dengan baik isi iklan yang dikumpulkannya. Ia bisa mengenali informasi penting seperti posisi, persyaratan, dan lokasi kerja, sehingga data yang ia kumpulkan mudah diproses lebih lanjut.  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  TRUE  |  TRUE
Dia sangat aktif karena dia ketua juga  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Karena rekan saya bagian platform TikTok juga (sama dengan rekan saya yang satunya) mereka jadi lebih cepat dan mudah dalam mencari loker  |  FALSE  |  TRUE  |  FALSE  |  TRUE  |  FALSE  |  FALSE  |  FALSE
Rekan saya menyelesaikan 50 data facebook dengan baik dan tepat waktu  |  TRUE  |  TRUE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE
Rekan saya teliti dalam penginputan data  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE  |  FALSE

Lampiran 12. Sampel Dataset Koherensi Skor Narasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Banya: aknya iklan dan keragaman platform yang digunakan.
Kriteria  |  Skala 1 (Sangat Kurang)  |  ang)  |  Skala  |  3 (Cukup  |  )  |  Skala 5  |  (Sangat Baik)
Narasi  |  Yang Ditanyakan  |  Mengumpulkan sedikit iklan  |  Iklan tidak relevan  |  Platfor tidak bervaria  |  Mengumpulkan cukun iklan  |  Iklan cukup relevan  |  Platform cukup bervariasi  |  Mengumpulka banyak iklan  |  sangat s  |  atform angat rvariasi
Pemahan: nan informasi pe
yang dikumpu: kan.
Jarasi  |  Vuitouio Vong Dito  |  myakan  |  Skala 1 (Sangat Kurang)  |  Skala 3   Skala 5 (Sanga (Cukun)   Raik)  |  t
I  |  varasi  |  Kriteria Yang Dita  |  шуакап  |  Tidak memaham isi iklan  |  Cukup i memahami isi iklan  |  Sangat memahami informasi penting dari iklan
aik isi iklan yang d: Pemahaman informas
seperti posisi, persy ulkan mudah dipros  |  dari iklan yang dikumpulkan  |  FALSE  |  FALSE  |  TRUE
data yang di kur  |  npulkan rekan say  |  a sudah rapih dan m  |  udah dibad  |  ca  |  Ketelitian dan keal penginputan da
dia dapat mema  |  hami informasi de  |  ngan sangat baik  |  Pemahaman informas dari iklan yang diku  |  FALSE  |  FALSE  |  TRUE
Sudah memabah  |  Pemahaman informas dari iklan yang diku  |  FALSE  |  FALSE  |  TRUE
kemudian nan  |  Saya pertama-tama menganalisa atau mencari posisinya terlebih dahulu kemudian nama perusahaanya, skill/requirement, dan terakhir link/kontak untuk menghubungi HRD.  |  an nama perusahaanya, skill/requirement, dan terakhir dan  |  Pemahaman informas dari iklan yang diku  |  FALSE  |  FALSE  |  FALSE
dia memahami dikumpulkan  |  dia memahami cukup baik tentang data yang cukup penting untuk dikumpulkan  |  Pemahaman informasi penting dari iklan yang dikumpulkan  |  FALSE
karena, ia selali  |  karena, ia selalu tepat waktu  |  Kemampuan menyelesaikan tugas sesuai tenggat waktu
Cukup memaha  |  Cukup memahami namun ia tidak bisa mengungkapkannya  |  si penting mpulkan  |  FALSE  |  TRUE FALSE

Lampiran 13. Hasil Akhir Dekomposisi Rubrik untuk Cakupan dan Relevansi

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
Konsistensi Komunikasi Selama Proyek
Kemampuan mengidentifikasi dan: Tingkat Inisiatif dan Proaktivitas
menyelesaikan masalah.: Kemampuan Menyelesaikan Masalah
Respons terhadap Kendala dan Masalah
Kemampuan menyelesaikan tugas: Ketepatan Memenuhi Deadline
sesuai tenggat waktu.: Kemampuan Mengelola Waktu

Lampiran 14. Hasil Dekomposisi Rubrik Untuk Koherensi Skor dan Narasi

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
Banyaknya iklan dan  |  Skala 1 (Sangat  |  $G_1$  |  Mengumpulkan sedikit iklan
keragaman platform  |  Kurang)  |  $G_2$  |  Iklan tidak relevan
yang digunakan.  |  <i>S</i> <sup>7</sup>  |  $G_3$  |  Platform tidak bervariasi
Skala 3 (Cukup)  |  $G_1$  |  Mengumpulkan cukup iklan
Shara 5 (Canap)  |  $G_2$  |  Iklan cukup relevan
$G_3$: Platform cukup bervariasi
Skala 5 (Sangat Baik)  |  $G_1$  |  Mengumpulkan banyak iklan
Skala 3 (Saligat Daik)  |  $G_2$  |  Iklan sangat relevan
Platform sangat bervariasi
Pemahaman  |  Skala 1 (Sangat  |  $G_3$ $G_1$  |  Tidak memahami isi iklan
informasi penting dari: Kurang)
iklan yang  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup memahami isi iklan
dikumpulkan.  |  Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat memahami informasi penting dari iklan
Kesesuaian dan  |  Skala 1 (Sangat  |  $G_1$  |  Struktur data tidak sesuai
kejelasan struktur  |  Kurang)  |  $G_2$  |  Struktur data tidak lengkap
data untuk memuat  |  Skala 3 (Cukup)  |  $G_1$  |  Struktur data cukup sesuai
informasi.  |  17  |  $G_3$  |  Struktur data memiliki beberapa kekurangan
Skala 5 (Sangat Baik)  |  $G_1$  |  Struktur data sangat baik
$G_2$: Struktur data lengkap
Ketelitian dan keakuratan  |  Skala 1 (Sangat Kurang)  |  $G_1$  |  Banyak kesalahan dalam data yang diinput
penginputan data.  |  Kurang)  |  $G_2$  |  Tidak teliti dalam penginputan
pengmputan data.  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup akurat dengan sedikit kesalahan
Skala 5 (Sangat Baik)  |  $G_1$  |  Data sangat akurat
Skulu 3 (Sungut Bulk)  |  $G_2$  |  Sangat teliti dalam penginputan
Partisipasi dalam menggabungkan data  |  Skala 1 (Sangat Kurang)  |  $G_1$  |  Tidak banyak terlibat dalam penggabungan data
kelompok.  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup terlibat namun tidak signifikan
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat terlibat dan membantu menyelesaikan penggabungan
Kemampuan bekerja sama dengan anggota  |  Skala 1 (Sangat Kurang)  |  $G_1$  |  Tidak banyak bekerja sama
kelompok lain.  |  Skala 3 (Cukup)  |  $G_1$  |  Cukup kooperatif, namun kontribusi terbatas
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat kooperatif dan banyak membantu tim
Efektivitas dalam  |  Skala 1 (Sangat  |  $G_1$  |  Tidak efektif dalam komunikasi
menyampaikan ide dan berdiskusi.  |  Kurang)  |  $G_2$  |  Ide tidak tersampaikan dengan jelas
Skala 3 (Cukup)  |  $G_1$  |  Cukup efektif dalam komunikasi
$G_2$: Ide cukup tersampaikan dengan jelas
$G_3$: Komunikasi tidak konsisten
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat efektif dalam
1: komunikasi

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
$G_2$: Ide sangat tersampaikan dengan
jelas
Kemampuan  |  Skala 1 (Sangat  |  $G_1$  |  Tidak memiliki inisiatif
mengidentifikasi dan  |  Kurang)  |  $G_2$  |  Tidak memberikan solusi untuk
menyelesaikan: menyelesaikan masalah
masalah.  |  Skala 3 (Cukup)  |  $G_2$  |  Cukup memberikan solusi
$G_3$: Memberikan solusi hanya dalam
beberapa situasi
Skala 5 (Sangat Baik)  |  $G_1$  |  Sangat proaktif
$G_2$: Memberikan solusi untuk
menyelesaikan masalah
Kemampuan  |  Skala 1 (Sangat  |  $G_1$  |  Banyak tugas yang terlambat
menyelesaikan tugas  |  Kurang)  |  diselesaikan
sesuai tenggat waktu.  |  Skala 3 (Cukup)  |  $G_1$  |  Beberapa tugas terlambat
$G_2$: Tugas yang terlambat masih
terkejar
Skala 5 (Sangat Baik)  |  $G_1$  |  Semua tugas diselesaikan tepat
waktu

Lampiran 15. Kuesioner Kelompok Treatment

No  |  Dimensi  |  Pertanyaan  |  Tipe
1  |  TAM (Perceived  |  Teks AI yang muncul membantu  |  Skala linier 1 sampai 5
Usefulnss): saya mengingat kriteria rubrik yang
terlewat saat mengisi assessment.
2  |  TAM (Perceived  |  Secara keseluruhan, kehadiran teks  |  Skala linier 1 sampai 5
Usefulnss): AI berguna bagi saya dalam proses
pengisian assessment.
3  |  TAM (Perceived  |  Instruksi yang diberikan oleh AI  |  Skala linier 1 sampai 5
Ease of Use): sangat jelas dan mudah dipahami.
4  |  TAM (Perceived  |  Interaksi dengan fitur teks AI  |  Skala linier 1 sampai 5
Ease of Use): berjalan secara fleksibel dan tidak
mengganggu proses mengetik saya.
5  |  Cognitive Load  |  Munculnya teks AI saat saya  |  Skala linier 1 sampai 5
(Extraneous: sedang mengetik membuat saya
Load): merasa pusing karena terlalu
banyak informasi.
6  |  Cognitive Load  |  Membaca teks AI yang muncul  |  Skala linier 1 sampai 5
(Extraneous: mengganggu konsentrasi saya
Load): terhadap kalimat yang sedang saya
tulis.
7  |  TAM (Perceived  |  Kehadiran teks AI mempermudah  |  Skala linier 1 sampai 5
Usefulness): saya memahami struktur penilaian
pada assessment.
8  |  Kualitatif  |  Apakah Anda merasa teks AI yang  |  Teks jawaban panjang
Eksplanatori: muncul sudah akurat dalam
mendeteksi kekurangan tulisan
Anda?
Jelaskan alasannya.
9  |  Preferensi  |  Bagian mana dari sistem teks AI ini  |  Kotak centang, dengan opsi:
Komponen  |  yang menurut Anda paling  |  1. Peringatan diagnosis
Hambatan  |  mengganggu atau perlu diperbaiki?  |  kekurangan narasi yang ditulis
2. Contoh kalimat
pembuka/sentence starter
3. Arahan mengenai apa yang
harus ditulis dalam narasi
4. Indikator status hijau atau
kuning
5. Semuanya mengganggu
Mahasiswa dapat menambahkan
opsi lain yang tidak disediakan
serta memilih lebih dari satu
opsi.
10  |  Kualitatif  |  Jelaskan alasanmu memilih  |  Teks jawaban panjang
Eksplanatori: jawaban di atas
11  |  Preferensi  |  Bagian panduan mana yang paling  |  Kotak centang, dengan opsi:
Komponen  |  membantu kamu saat menulis  |  1. Peringatan kekurangan
Utilitas  |  narasi feedback?  |  narasi yang ditulis
2. Contoh kalimat
pembuka/sentence starter
3. Arahan mengenai apa yang
harus ditulis dalam narasi

No  |  Dimensi  |  Pertanyaan  |  Tipe
4. Indikator status hijau atau kuning 5. Tidak ada yang membantu Mahasiswa dapat menambahkan opsi lain yang tidak disediakan serta memilih lebih dari satu opsi.
12  |  Kualitatif  |  Jelaskan alasanmu  |  memilih  |  Teks jawaban panjang
Eksplanatori: jawaban di atas

Lampiran 16. Rubrik CATME yang Digunakan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Lampiran 17. Feature-set Eksperimen Cakupan dan Relevansi Topik

Kriteria: Unit hasil dekomposisi
Penyelesaian Tugas
Kualitas Pekerjaan
Ketepatan Waktu
Kontribusi terhadap Pekerjaan Tim: Inisiatif
Kontribusi
Tingkat produktivitas
Responsivitas Komunikasi
Sikap dalam Diskusi
Interaksi dengan Rekan Tim: Mendengarkan Ide atau Pendapat
Kualitas Feedback yang Diberikan
Dampak terhadap Dinamika Komunikasi
Kepedulian terhadap Kemajuan Proyek
Perhatian terhadap Tenggat Waktu
Menjaga Fokus dan Dinamika Tim: Kesediaan Membantu
Kemampuan Menjaga Fokus
Kepedulian terhadap Kualitas Hasil Akhir
Komitmen terhadap Kualitas: Evaluasi dan Perbaikan Kualitas Pekerjaan
Komitmen terhadap Standar yang Ditetapkan

Lampiran 18. Feature-set Eksperimen Koherensi Skor dan Narasi

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
Kontribusi terhadap  |  $G_1$  |  Tidak menyelesaikan tugas
Pekerjaan Tim  |  $G_2$  |  Kualitas sangat buruk
, and the second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second second  |  1  |  $G_3$  |  Sering terlambat
$G_4$: Tidak berkontribusi sama sekali
$G_1$: Menyelesaikan tugas
$G_2$: Kualitas memadai
3  |  $G_3$  |  Tepat waktu
$G_4$: Tanggung jawab
$G_1$: Menyelesaikan semua tugas
$G_1$: Menyelesaikan lebih banyak dari yang
<b>U</b> 1: diberikan
5  |  $G_2$  |  Melebihi ekspektasi
$G_3$: Menyelesaikan sebelum tenggat waktu
$G_4$: Inisiatif
Interaksi dengan  |  $G_1$  |  Mengabaikan komunikasi
Rekan Tim  |  $G_2$  |  Mendominasi pembicaraan
Tteltaii Tiiii  |  1  |  $G_2$  |  Tidak mendengarkan ide
1  |  $G_3$  |  Bersikap defensif
$G_4$: Sering memicu konflik
$G_1$: Berkomunikasi secara wajar
$G_1$: Merespon pesan
3: $G_1$
$G_2$: Merespon pertanyaan Menyampaikan ide
Tidak mendominasi
$G_2$
$G_3$: Terbuka terhadap kritik dan masukan Tidak memicu konflik
$G_4$
$G_1$: Sangat aktif berkomunikasi
5  |  $G_2$  |  Mendengarkan pendapat dengan baik
$G_3$: Memberikan feedback yang konstruktif
$G_4$: Menciptakan suasana positif
M ' E 1 1  |  $G_4$  |  Menghargai semua anggota tim
Menjaga Fokus dan  |  $G_1$  |  Tidak peduli dengan kemajuan
Dinamika Tim  |  1  |  $G_2$  |  Tidak peduli dengan tenggat waktu
$G_3$: Tidak bersedia membantu
$G_4$: Mengalihkan fokus pada hal yang tidak relevan
3  |  $G_1$  |  Mengetahui status kemajuan
$G_2$: Memperhatikan tenggat waktu
$G_3$: Bersedia membantu
$G_4$: Membantu tim tetap fokus
$G_1$: Proaktif memantau kemajuan
_  |  $G_2$  |  Mengingatkan mengenai tenggat waktu
5  |  $G_3$  |  Menawarkan bantuan
$G_4$: Sangat menjaga fokus
$G_4$: Sangat menjaga dinamika
Komitmen terhadap  |  $G_1$  |  Tidak peduli dengan hasil akhir
Kualitas  |  1  |  $G_2$  |  Pekerjaan ceroboh
1  |  $G_2$  |  Tidak ada keinginan untuk memperbaiki
$G_3$: Tidak mengevaluasi kualitas
3  |  $G_1$  |  Menunjukkan kepedulian terhadap kualitas

Kriteria  |  Skala  |  Himpunan  |  Unit Dekomposisi
$G_2$: Memastikan hasil akhir memenuhi standar
$G_3$: Mengevaluasi hasil kerja tim
$G_1$: Memiliki motivasi tinggi
$G_2$: Mendorong rekan untuk melampaui standar
3  |  $G_3$  |  Sangat teliti dalam mengevaluasi hasil kerja
tim

Lampiran 19 Teks Scaffolding

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
1101  |  target_aspect, missing_covera ge, predicted_skor, input_skor  |  diagnostik  |  Narasi belum berfokus pada {target_aspect}, belum mencakup {missing_coverage}, dan narasi yang kamu berikan lebih mencerminkan skor {predicted_skor} daripada skor {input_skor} yang diberikan.
directive: Fokuskan pada {target_aspect}, lengkapi dengan {missing_coverage}, dan uraikan kejadian atau perilaku konkret yang menjadi alasan pemberian skor

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]