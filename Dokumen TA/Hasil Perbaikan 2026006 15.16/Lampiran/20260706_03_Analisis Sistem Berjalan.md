ANALISIS SISTEM BERJALAN
DAN PERANCANGAN TEKNIS APE
LAMPIRAN TUGAS AKHIR
Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan
Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di
Jurusan Teknik Komputer dan Informatika
Oleh:
Aryo Rakatama 221524003
Muhammad Rama Nurimani 221524021
PROGRAM SARJANA TERAPAN
PROGRAM STUDI TEKNIK INFORMATIKA
JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA
POLITEKNIK NEGERI BANDUNG
2026

DAFTAR ISI
DAFTAR ISI ........................................................................................................... i
DAFTAR GAMBAR ............................................................................................. ii
DAFTAR TABEL ................................................................................................ iii
BAB I PERANCANAN TEKNIS APE ................................................................. 4
I.1 Hasil Analisis Sistem Berjalan ...................................................................... 4
I.1.1 Deskripsi Sistem Existing ....................................................................... 4
I.1.2 Identifikasi Titik Integrasi ...................................................................... 6
I.1.3 Komponen yang Dimodifikasi ................................................................ 6
I.1.4 Komponen yang Ditambahkan ............................................................... 7
I.2 Hasil Perancangan dan Integrasi Konponen .................................................. 7
I.2.1 Arsitektur Aplikasi Pendukung Eksperimen .......................................... 8
I.2.2 Hasil Integrasi ....................................................................................... 34
i

DAFTAR GAMBAR
Gambar I.1. Proses Bisnis SAPA 5
Gambar I.2. BPMN to-be Setelah APE diintegrasikan 9
Gambar I.3. Use Case Diagram APE yang Akan Dikembangkan 11
Gambar I.4. Class Diagram Keseluruhan (to-be) 14
Gambar I.5. Class Diagram Bagian Modifikasi 15
Gambar I.6. ERD Keseluruhan SAPA 17
Gambar I.7. ERD Bagian Modifikasi 18
Gambar I.8. Sequence Diagram UC-05 Manage Assessment 20
Gambar I.9. Sequence Diagram UC-10 Answer Peer Assessment 21
Gambar I.10. Sequence Diagram UC-10 Answer Self Assessment 22
Gambar I.11. Arsitektur Aplikasi setelah Integrasi 34
ii

DAFTAR TABEL
Tabel I.1. Titik Integrasi 6
Tabel I.2. Komponen Yang Dimodifikasi 6
Tabel I.3. Komponen Yang Ditambahkan 7
Tabel I.4. Functional Requirements 10
Tabel I.5. Non Functional Requirements 10
Tabel I.6. Use Case Scenario Receive Scaffolding (UC-17) 12
Tabel I.7. GUI-22 24
Tabel I.8. GUI-25 25
Tabel I.9. GUI-21 26
Tabel I.10. GUI-24 28
Tabel I.11. GUI-43 30
Tabel I.12. GUI-46 32
iii

BAB I
PERANCANAN TEKNIS APE
Lampiran ini menyajikan dokumentasi software engineering dari integrasi sistem
scaffolding ke dalam lingkungan Aplikasi Pendukung Eksperimen (APE).
Pembahasan mencakup pemodelan Business Process Model and Notation (BPMN)
sistem berjalan, arsitektur integrasi, Use Case, dan rancangan antarmuka GUI.
I.1 Hasil Analisis Sistem Berjalan
Analisis Sistem Existing bertujuan untuk mengidentifikasi lingkungan tempat
sistem scaffolding diintegrasikan untuk isolasi modifikasi kode. Tahapan ini
dilakukan dengan meninjau dokumen SRS (Software Requirement Specification),
SDD (Software Design Documentation), manual book, dan source code.
I.1.1 Deskripsi Sistem Existing
Aplikasi SAPA merupakan platform berbasis web yang dirancang untuk
mendukung pengisian self dan peer assessment mahasiswa JTK Polban. Aplikasi
ini memungkinkan dosen untuk mengelola proyek (mata kuliah), membuat dan
membagikan formulir assessment, serta memantau dan mengevaluasi hasil
assessment. Keseluruhan proses bisnis SAPA disajikan pada Gambar I.1.
Berdasarkan abstraksi Business Process Model and Notation (BPMN), siklus
operasional SAPA telah dirancang dengan alur yang sistematis untuk memfasilitasi
evaluasi sumatif. Alur bisnis direpresentasikan mulai dari tahap inisiasi di mana
dosen menyusun proyek dan instrumen rubrik penilaian, dilanjutkan oleh fase
pengerjaan evaluasi oleh mahasiswa, dan diakhiri dengan pemrosesan rekomendasi
skor menggunakan SLA Algorithm oleh sistem sebagai material analis bagi dosen.
4

Gambar I.1. Proses Bisnis SAPA
5

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

I.1.2 Identifikasi Titik Integrasi  Commented [AR1]: (Kertas dilipat tanpa catatan)
- Bu Ani
Berdasarkan tinjauan yang dilakukan terhadap dokumen SRS, SDD, serta source
code ditemukan titik integrasi untuk kebutuhan digital scaffolding terhadap enam
halaman, sebagaimana disajikan pada Tabel I.1.
Tabel I.1. Titik Integrasi
| Aspek      |                                                                  | Komponen yang terlibat  |     |     |
| ---------- | ---------------------------------------------------------------- | ----------------------- | --- | --- |
| Interface  | GUI-43 (Form Self Assessment) dan GUI-46 (Form Peer Assessment)  |                         |     |     |

GUI-22 (Detail Question Self Assessment) dan GUI-25 (Detail Question
Peer Assessment)

GUI-21 (List Self Assessment) dan GUI-24 (List Peer Assessment)
| Logika Bisnis  | AssessmentController (menangani UC-10 Answer Assessment) pada SD- |     |     |     |
| -------------- | ----------------------------------------------------------------- | --- | --- | --- |
10 (Self Assessment) dan SD-11(Peer Assessment))
| Basis Data (Data)  | Entitas Tabel ‘Criteria’ , ‘Assessment’ dan ‘Reflective Assessment’  |     |     |     |
| ------------------ | -------------------------------------------------------------------- | --- | --- | --- |

Titik integrasi digital scaffolding berada pada fase pengisian narasi feedback
sebelum mahasiswa melakukan operasi simpan jawaban. Hal ini diimplementasikan
dengan menambahkan event yang menangkap perubahan narasi pada UC-10
(Answer Assessment) pada SD-10 dan SD 11.

I.1.3 Komponen yang Dimodifikasi
Untuk melakukan integrasi sistem digital scaffolding terhadap aplikasi SAPA,
beberapa komponen yang tersedia perlu dimodifikasi sebagaimana disajikan pada
Tabel I.2.
Tabel I.2. Komponen Yang Dimodifikasi
| Aspek  | Komponen        |                                                           | Modifikasi         |                     |
| ------ | --------------- | --------------------------------------------------------- | ------------------ | ------------------- |
|        |                 | Modifikasi                                                | dilakukan  dengan  | menambahkan  kolom  |
|        | Tabel Criteria  | decomposition_status untuk mengetahui status dari proses  |                    |                     |
dekomposisi rubrik.
Dilakukan penambahan kolom baru pada kedua tabel
| Data  |                    | tersebut, yaitu use_scaffolding untuk menentukan aktif  |                        |                       |
| ----- | ------------------ | ------------------------------------------------------- | ---------------------- | --------------------- |
|       | Tabel  Assessment  |                                                         |                        |                       |
|       | dan                | atau  tidaknya                                          | komponen  digital      | scaffolding  pada     |
|       |                    | assessment                                              | spesifik,  dan  kolom  | decomposition_status  |
reflective_assessment
untuk mengetahui status dekomposisi rubrik pada level
pertanyaan assessment.
Modifikasi dilakukan pada GUI-21 dan GUI-24 pada
|     | Halaman  daftar  | self  tombol toggle publish, sehingga hanya dapat melakukan  |     |     |
| --- | ---------------- | ------------------------------------------------------------ | --- | --- |
dan peer assessment.
publikasi assessment setelah proses dekomposisi selesai.
Antarmuka
|     | Halaman  pengisian  | Modifikasi dilakukan pada GUI-43 dan GUI-46 dengan  |                     |                  |
| --- | ------------------- | --------------------------------------------------- | ------------------- | ---------------- |
|     | self  dan  peer     | menyematkan                                         | mekanisme  polling  | atau  debounce.  |
|     | assessment          | Modifikasi ini memungkinkan sistem untuk menangkap  |                     |                  |
6

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Aspek  | Komponen  |     |     | Modifikasi  |     |     |     |
| ------ | --------- | --- | --- | ----------- | --- | --- | --- |
kondisi teks narasi mahasiswa sebagai input sistem digital
scaffolding.
Modifikasi yang diterapkan berupa penambahan relasi
|     | UC-10  pada  | SD-10  <<extends>> pada UC-17. Di sisi lain, UC-10 melakukan  |     |     |     |     |     |
| --- | ------------ | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
Proses
|     | dan SD-11  | proses  | pemanggilan  | terhadap  |     | API  pipeline  | digital  |
| --- | ---------- | ------- | ------------ | --------- | --- | -------------- | -------- |
scaffolding.

I.1.4 Komponen yang Ditambahkan
| Sebagai  | ekstensi  dari  subbab  | I.1.3,  | Tabel  | I.3  menyajikan  |     | komponen  | yang  |
| -------- | ----------------------- | ------- | ------ | ---------------- | --- | --------- | ----- |
ditambahkan terhadap arsitektur SAPA berdasarkan identifikasi titik integrasi pada
Tabel I.1.
Tabel I.3. Komponen Yang Ditambahkan
| Aspek  | Komponen  |                   |     | Penambahan  |              |          |        |
| ------ | --------- | ----------------- | --- | ----------- | ------------ | -------- | ------ |
|        |           | Untuk  mendukung  |     | proses      | dekomposisi  | rubrik,  | perlu  |
penambahan ditambahkan entitas relasional baru yang terdiri
Tabel  Criteria,
dari
|       | Assessment,  | dan  1.               |     |     |     |     |     |
| ----- | ------------ | --------------------- | --- | --- | --- | --- | --- |
| Data  | Reflective   | rubric_decomposition  |     |     |     |     |     |
2.  question_decompositon
Assessment
3.  assessment_decomposition_link
4.
reflective_decomposition_link
|     | Halaman  detail     | Pada  GUI-22                                        | dan   | GUI-25,        | diperlukan  | toggle       | untuk  |
| --- | ------------------- | --------------------------------------------------- | ----- | -------------- | ----------- | ------------ | ------ |
|     | question pada self  | mengaktifkan                                        | atau  | menonaktifkan  |             | scaffolding  | untuk  |
|     | dan  peer           | membantu proses pengujian pada kelompok mahasiswa.  |       |                |             |              |        |
assessment
| Antarmuka  | Halaman  daftar     | Pada GUI-21 dan GUI-24, komponen indikator loading yang      |         |              |          |                      |              |
| ---------- | ------------------- | ------------------------------------------------------------ | ------- | ------------ | -------- | -------------------- | ------------ |
|            | self  dan  peer     | menggambarkan                                                | proses  | dekomposisi  |          | rubrik  ditambahkan  |              |
|            | assessment          | untuk mengetahui status pre-processiong scaffolding.         |         |              |          |                      |              |
|            | Halaman             | Sebagai  halaman                                             |         | utama  yang  | menjadi  | fokus                | penelitian,  |
|            | pengisian self dan  | komponen scaffolding ditambahkan dalam bentuk persegi pada   |         |              |          |                      |              |
|            | peer assessment     | antarmuka ini.                                               |         |              |          |                      |              |
|            | UC-17               | Penambahan proses komunikasi antara aktor yang sedang        |         |              |          |                      |              |
|            | (Mahasiswa          | mengetik narasi kualitatif untuk dikirim ke service digital  |         |              |          |                      |              |
Proses
|     | menerima  digital  | scaffolding.  |     |     |     |     |     |
| --- | ------------------ | ------------- | --- | --- | --- | --- | --- |
scaffolding)

I.2 Hasil Perancangan dan Integrasi Konponen
Subbab ini menjelaskan perancangan sistem yang diusulkan sebagai pengembangan
dari aplikasi SAPA dengan penambahan fitur conditional scaffolding. Perancangan
dilakukan berdasarkan kebutuhan sistem yang telah diidentifikasi sebelumnya.

7

I.2.1 Arsitektur Aplikasi Pendukung Eksperimen
Pada kondisi saat ini (as-is), aplikasi SAPA mendukung proses self dan peer
assessment di mana mahasiswa mengisi jawaban kuantitatif dan narasi feedback
secara langsung tanpa adanya intervensi atau bantuan selama proses penulisan,
sebagaimana direpresentasikan oleh Gambar I.1. Evaluasi terhadap kualitas narasi
hanya terjadi secara implisit dan umumnya baru terlihat pada hasil akhir penilaian
atau umpan balik dari dosen.
Kondisi yang diusulkan (to-be) pada Gambar I.2, dengan simbol berwarna
merepresentasikan komponen yang ditambahkan untuk mendukung mekanisme
digital scaffolding yang terintegrasi dalam proses pengisian narasi. Sistem secara
aktif mengevaluasi input narasi mahasiswa secara real-time menggunakan rubrik
yang telah didekomposisi, kemudian memberikan conditional prompt apabila
ditemukan bahwa feedback belum memenuhi indikator yang diharapkan. Integrasi
dilakukan pada level fitur aplikasi SAPA sebagaimana didefinisikan pada subbab
I.1.3 dan I.1.4.
Lebih jauh, untuk mempertahankan standar dan konsistensi proses integrasi,
analisis pada functional requirements, non-functional requirements, use case
diagram, class diagram, database, sequence diagram, hingga perancangan
antarmuka didefinisikan pada subbab I.2.1.1 hingga I.2.1.7.
Melalui perubahan ini seluruh komponen dan fitur lainnya yang telah tersedia pada
aplikasi SAPA, seperti pengumpulan assessment, perhitungan nilai, dan pemberian
feedback oleh dosen tetap berjalan sebagaimana mestinya tanpa adanya modifikasi.
8

9
Gambar I.2. BPMN to-be Setelah APE diintegrasikan

10
I.2.1.1 Functional Requirements
Tabel I.4 menyajikan functional requirement untuk memfasilitasi sistem digital
scaffolding, hal ini dilakukan untuk memastikan proses eksperimen dapat
dilaksanakan.
Tabel I.4. Functional Requirements
Kode FR Deskripsi
Sistem harus dapat menampilkan teks scaffolding (conditional prompt) dengan
FR-01 kode template 0001 hingga 1111 sesuai hasil analisis indikator saat mahasiswa
mengisi narasi kualitatif assessment.
Sistem harus menyediakan mekanisme bagi dosen untuk mengaktifkan atau
FR-02
menonaktifkan fitur scaffolding untuk setiap assessment.
Sistem harus dapat melakukan komputasi empat indikator tekstual narasi
FR-03 menggunakan konfigurasi pipeline digital scaffolding. Komputasi dilakukan
dengan mekanisme debounce 1,5 detik dan interval maksimum 1,5 detik.
Sistem harus dapat menggunakan template dengan kode 0000 ketika seluruh
FR-04
indikator tekstual narasi terpenuhi.
Sistem dapat melakukan proses dekomposisi rubrik secara otomatis
FR-05
menggunakan API Gemini.
Sistem harus merekam data log interaksi (behavioral log) secara sekuensial
selama sesi penulisan aktif, yang mencakup riwayat perubahan teks narasi,
FR-06
modifikasi skor kuantitatif, riwayat pemicu prompt scaffolding per indikator,
serta timestamp interaksi.
I.2.1.2 Non Functional Requirements
Non-functional requirement yang disajikan pada Tabel I.5 berfungsi untuk
membantu sistem digital scaffolding pada penelitian ini.
Tabel I.5. Non Functional Requirements
Kode NFR Deskripsi
Sistem harus memproses dan mengembalikan hasil evaluasi scaffolding dalam
NFR-01 waktu maksimum 5 detik sejak permintaan diterima oleh pipeline digital Commented [AR2]: (dilingkari)
scaffolding. - Bu Ani
Model embedding yang digunakan pada pipeline digital scaffolding,
sebagaimana didefinisikan konfigurasi akhir pipeline harus dipastikan tersedia
NFR-02
selama siklus hidup layanan tanpa perlu pemuatan ulang pada setiap request
analisa feedback.
Sistem hanya memproses feedback yang unik dalam satu sesi mahasiswa pada
NFR-03
setiap pertanyaan assessment.
Aplikasi menerapkan mekanisme caching menggunakan kombinasi skor dan
NFR-04 teks narasi sebagai key untuk mencegah pemanggilan API yang redundan dan
mengurangi beban komputasi server.

I.2.1.3 Use Case Diagram
Sebagai ekstensi fitur aplikasi SAPA, pipeline digital scafolding digambarkan
sebagai UC-17 (Receive Scaffolding) yang berelasi extend terhadap UC-10 (Answer
Assessment) dalam use case diagram SAPA yang disajikan pada Gambar I.3.
Gambar I.3. Use Case Diagram APE yang Akan Dikembangkan
11

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Untuk mendukung use case diagaram pada Gambar I.3, Tabel I.6 menyajikan use
case scenario untuk UC-17 (Receive Digital Scaffolding Prompt).
Tabel I.6. Use Case Scenario Receive Scaffolding (UC-17)
| Use Case section  | Comment                            |     |     |     |     |     |
| ----------------- | ---------------------------------- | --- | --- | --- | --- | --- |
| Use case Name     | UC-17 Receive Digital Scaffolding  |     |     |     |     |     |
| Scope             | Aplikasi Existing (SAPA)           |     |     |     |     |     |
| Level             | Sub Function                       |     |     |     |     |     |
| Primary Actor     | Mahasiswa                          |     |     |     |     |     |
1.
| Stakeholder and Interest  | Mahasiswa ingin mendapatkan bantuan selama menulis narasi  |     |     |     |     |     |
| ------------------------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
feedback.
| Precondition  | 1.  Mahasiswa berada di tahapan mengisi assessment (UC-10)  |     |     |     |     |     |
| ------------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- |
2.  Target assessment (self/peer) sudah dipilih
| Success Guarantee  | Teks scaffolding berhasil ditampilkan saat skor kualitatif/narasi  |     |     |     |     |     |
| ------------------ | ------------------------------------------------------------------ | --- | --- | --- | --- | --- |
tidak memenuhi minimal satu dari empat indikator tekstual narasi
feedback

|     | Teks  | scaffolding  dengan  | kode  | 0000  | ditampilkan  | saat  skor  |
| --- | ----- | -------------------- | ----- | ----- | ------------ | ----------- |
kuantitaif/narasi memenuhi seluruh empat indikator tekstual narasi
feedback
| Action  |     | Actor  |     |     | System  |     |
| ------- | --- | ------ | --- | --- | ------- | --- |
1.
|     | Mahasiswa mengetik skor  |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- |
kualitatif/narasi
|     |     |     |     | 2.  Sistem memantau input teks  |     |     |
| --- | --- | --- | --- | ------------------------------- | --- | --- |
selama periode debouncing
1,5 detik
3.
|     |     |     |     | Sistem  | memproses  | teks      |
| --- | --- | --- | --- | ------- | ---------- | --------- |
|     |     |     |     | narasi  | setelah    | melebihi  |
waktu debounce
4.
|     |     |     |     | Sistem       | mengirimkan  | teks      |
| --- | --- | --- | --- | ------------ | ------------ | --------- |
|     |     |     |     | scaffolding  |              | (prompt)  |
|     |     |     |     | berdasarkan  | teks         | narasi    |
yang terkomputasi
|     | 5.  Mahasiswa menerima teks  |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- |
scaffolding
| Extension  | 1.  Jika dalam waktu 1,5 detik sistem tidak mendeteksi teks yang  |     |     |     |     |     |
| ---------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
valid untuk dikirim, sistem tetap dalam kondisi menunggu
atau menampilkan pesan pengingat kepada mahasiswa
2.a. Sistem tidak menerima perubahan input teks selama periode
tertentu
| Special Requirements  | 1.  Sistem harus dapat memberikan teks scaffolding dalam batas  |     |     |     |     |     |
| --------------------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
waktu 1,5 detik setelah waktu debounce.
1.
| Technology and Data  | Sistem                                                    | menggunakan  | pipeline    | digital  | scaffolding        | yang  |
| -------------------- | --------------------------------------------------------- | ------------ | ----------- | -------- | ------------------ | ----- |
| Variations           | berisikan model NLP berbasis Transformer untuk memproses  |              |             |          |                    |       |
| List                 | teks narasi.                                              |              |             |          |                    |       |
|                      | 2.  Sistem                                                | menggunakan  | rule-based  |          | untuk  menentukan  |       |
keputusan jenis teks scaffolding yang ditampilkan
| Frequencey of Occurence  | Setiap kali siswa melakukan perubahan skor kualitatif/narasi  |     |     |     |     |     |
| ------------------------ | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
dalam jangka waktu 1,5 detik.
| Miscellanous  | -   |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |

12

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

I.2.1.4 Class Diagram
Class diagram memetakan struktur teknis sistem dengan mendetailkan atribut dan
metode pada setiap kelas serta cara kelas-kelas tersebut berinteraksi. Gambar I.4
| menyajikan  | keseluruhan  | arsitektur  class  | diagram  | SAPA,  | dengan  | komponen  |
| ----------- | ------------ | ------------------ | -------- | ------ | ------- | --------- |
berwarna hitam merepresentasikan bagian existing yang telah tersedia, sementara
komponen berwarna merah merepresentasikan penambahan atau modifikasi untuk
memfasilitasi pipeline digital scaffolding. Untuk meningkatkan visibilitas, Gambar
I.5 menyajikan class diagram yang terisolasi terhadap komponen terdampak.

Berdasarkan gambar tersebut, salah satu komponen yang terdampak adalah type
criteria yang menyimpan komponen penilaian rubrik, modifikasi dilakukan dengan
menambahkan atribut status dekomposisi. Komponen lain yang terdampak yaitu
assessment dan reflective, modifikasi dilakukan dengan menambahkan toggle
| aktivasi    | scaffolding  | dan  status  dekomposisi  |            | pada  level  | pertanyaan.  | Class      |
| ----------- | ------------ | ------------------------- | ---------- | ------------ | ------------ | ---------- |
| assessment  | berfungsi    | untuk  menyimpan          | informasi  | mengenai     | self         | dan  peer  |
assessment, di sisi lain, class reflective adalah ekstensi dari self assessment dengan
komponen yang serupa.

Untuk menyimpan hasil dekomposisi rubrik, class question decomposition dan
rubric decomposition diperlukan untuk menyimpan feature-set cakupan rubrik dan
| relevansi topik ((cid:1)(cid:2)(cid:3)((cid:5) |           | (cid:6),(cid:8) )) serta feature-set koherensi skor dan narasi ((cid:1)(cid:2)(cid:10)((cid:5) |              |            |           | (cid:6),(cid:8) )).  |
| ---------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------- | ------------ | ---------- | --------- | -------------------- |
| Kedua  class                                   | tersebut  | menjadi  salah                                                                                 | satu  input  | komputasi  | pipeline  | digital              |
scaffolding.

13

14
Gambar I.4. Class Diagram Keseluruhan (to-be)

Gambar I.5. Class Diagram Bagian Modifikasi
15

16
I.2.1.5 Entity Relationship Diagram
Basis data keseluruhan aplikasi sapa dengan modifikasi yang telah disesuaikan
disajikan pada Gambar I.6, dengan komponen yang memiliki warna merah
merepresentasikan modifikasi/penambahan yang dilakukan berdasarkan analisis
pada subbab I.1. Untuk meningkatkan visibilitas diagram, Gambar I.7 menyajikan
diagram yang terisolasi pada entitas terdampak.
Sistem menggunakan dua tabel dekomposisi yang memiliki peran yang berbeda.
Rubric_decomposition merupakan tabel yang menyimpan feature-set untuk
indikator cakupan rubrik, relevansi, dan koherensi skor dari aspek rubrik spesifik.
Di sisi lain, question_decomposition menyimpan feature-set untuk indikator
cakupan rubrik yang dimiliki oleh pertanyaan feedback, terlepas dari rubrik maupun
bobot aspek pada rubrik. Pemisahan kedua tabel dekomposisi tersebut bertujuan
untuk mencegah adanya duplikasi ataupun konflik pada pertanyaan yang berbeda
namun menggunakan aspek rubrik yang sama.

17
Gambar I.6. ERD Keseluruhan SAPA

Gambar I.7. ERD Bagian Modifikasi
18

19
I.2.1.6 Sequence Diagram
Sequence Diagaram menunjukkan cara objek berkomunikasi satu sama lain dalam
sistem. Pada penelitian ini, diagram dibuat berdasarkan modifikasi dari sistem
existing, meliputi proses pengisian self dan peer assessment pada Gambar I.9 serta
Gambar I.10, dan juga proses manage assessment pada Gambar I.8.
Dalam aplikasi SAPA yang sudah ada, saat proses manage assessment oleh dosen
berlangsung, assessment ditambahkan dengan cara mengunggah file Excel yang
berisi detail rubrik assessment. Rubrik tersebut mencakup berbagai aspek seperti
pertanyaan, jenis assessment, jenis skill, hingga aspek yang dinilai serta kriteria
yang digunakan untuk setiap pertanyaan. Dalam penelitian ini, proses import
melibatkan tahapan untuk melakukan dekomposisi rubrik. Proses ini berjalan secara
asynchronous di latar belakang, sehingga pengguna tidak perlu menunggu pada
halaman SAPA hingga proses selesai, seperti yang ditunjukkan pada Gambar I.8.
Selanjutnya, ketika mahasiswa mengisi self ataupun self assessment, aplikasi yang
sudah ada memiliki perilaku seperti formulir pada umumnya, yaitu pengguna dapat
mengisi atau mengubah isi formulir hingga proses submit assessment. Dalam
penelitian ini, mahasiswa diberikan prompt scaffolding yang bertujuan untuk
meningkatkan feedback literacy ketika siswa melakukan menulis narasi, yang
ditampilkan pada Gambar I.9 dan Gambar I.10.

20
Gambar I.8. Sequence Diagram UC-05 Manage Assessment

Gambar I.9. Sequence Diagram UC-10 Answer Peer Assessment
21

Gambar I.10. Sequence Diagram UC-10 Answer Self Assessment
22

23
I.2.1.7 Perancangan Antarmuka
Perancangan antarmuka didasari oleh aplikasi SAPA existing berdasarkan pada
subbab I.1.3 dan I.1.4. Setelah dosen mengunggah file excel yang berisikan rubrik
dan pertanyaan assessment, aplikasi akan memulai proses dekomposisi rubrik
menggunakan API Gemini. Kemudian, dosen dapat menuju antarmuka pada GUI-
22 ataupun GUI-24 untuk melihat daftar assessment, mencoba mengisi assessment,
hingga melakukan publikasi assessment. Publikasi tidak dapat dilakukan sebelum
sistem selesai melakukan dekomposisi rubrik, ditandai dengan indikator loading
pada bagian kanan dari toggle publikasi.
Secara default, setiap assessment memiliki scaffolding ketika mahasiswa mengisi
narasi. Namun, dosen dapat menonaktifkan fitur scaffolding pada antarmuka di
Tabel I.7 dan
Tabel I.8. Akibatnya, siswa tidak mendapatkan prompt scaffolding selama mengisi
self/peer assessment. Implementasi hal tersebut digunakan untuk membantu proses
eksperimen terhadap kelompok mahasiswa dalam penelitian ini.
Pada sudut pandang mahasiswa ketika mengisi assessment, dengan antarmuka pada
Tabel I.11. GUI- dan Tabel I.12. Jika scaffolding aktif, maka mahasiswa akan
mendapatkan teks prompt tepat di atas kolom narasi untuk membantu
meningkatkan pemenuhan keempat indikator tekstual narasi feedback.

24

Tabel I.7. GUI-22
| Kode UI    | GUI-22                                                                                                         | Kode FR  | FR-02  | Kode UC  UC-05  |     |
| ---------- | -------------------------------------------------------------------------------------------------------------- | -------- | ------ | --------------- | --- |
| Nama       | Self Assessment – Detail Question                                                                              |          |        |                 |     |
| Deskripsi  | Halaman ini menampilkan detail dari setiap pertanyaan beserta rubrik dalam satu assessment yang telah dibuat.  |          |        |                 |     |
Modifikasi pada penelitian ini adalah penambahan opsi untuk mengatur aktivasi scaffolding dalam mendukung FR-02.
Design

Component
|     | Functional Type  | Purpose (Kegunaan)  |     |     | Keterangan Persyaratan  |
| --- | ---------------- | ------------------- | --- | --- | ----------------------- |
List
| Tittle Section  | Information  | Menampilkan judul utama dari halaman  |     | Harus sesuai dengan konteks halaman.  |     |
| --------------- | ------------ | ------------------------------------- | --- | ------------------------------------- | --- |
Toggle  Toggle Button  Mengaktifkan  atau  menonaktifkan  Jika aktif (biru), scafolding diterima siswa ketika menulis narasi
Scaffolding  scaffolding pada assessment.  feedback. Jika nonaktif (abu-abu), siswa tidak menerima scaffolding.
| Button  Start  | Action Button  | Menampilkan  | form  pertanyaan  |     |     |
| -------------- | -------------- | ------------ | ----------------- | --- | --- |
-
| Assessment  |     | berdasarkan aspek kriteria.  |     |     |     |
| ----------- | --- | ---------------------------- | --- | --- | --- |
Cad Qustion  Information  Menampilkan  daftar  pertanyaan  Data pertanyaan sudah tersedia di database atau sudah import data
|     |     | berdasarkan aspek kriteria.  |     | assessment sebelumnya.  |     |
| --- | --- | ---------------------------- | --- | ----------------------- | --- |
Tabel Rubrik  Information  Menampilkan daftar rubrik dari setiap  Data rubrik sudah tersedia di database atau sudah import data
|     |     | pertanyaan.  |     | assessement sebelumnya.  |     |
| --- | --- | ------------ | --- | ------------------------ | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Tabel I.8. GUI-25
| Kode UI    | GUI-25                                                                                                         | Kode FR  | FR-02  | Kode UC  UC-05  |     |
| ---------- | -------------------------------------------------------------------------------------------------------------- | -------- | ------ | --------------- | --- |
| Nama       | Peer Assessment – Detail Question                                                                              |          |        |                 |     |
| Deskripsi  | Halaman ini menampilkan detail dari setiap pertanyaan beserta rubrik dalam satu assessment yang telah dibuat.  |          |        |                 |     |
Modifikasi pada penelitian ini adalah penambahan opsi untuk mengatur aktivasi scaffolding dalam mendukung FR-02.
Design

Component
|     | Functional Type  | Purpose (Kegunaan)  |     |     | Keterangan Persyaratan  |
| --- | ---------------- | ------------------- | --- | --- | ----------------------- |
List
| Tittle Section  | Information  | Menampilkan judul utama dari halaman  |     | Harus sesuai dengan konteks halaman.  |     |
| --------------- | ------------ | ------------------------------------- | --- | ------------------------------------- | --- |
Toggle  Toggle Button  Mengaktifkan  atau  menonaktifkan  Jika  aktif  (biru),  scafolding  diterima  siswa  ketika  menulis  narasi
Scaffolding  scaffolding pada assessment.  feedback. Jika nonaktif (abu-abu), siswa tidak menerima scaffolding.
| Button  Start  | Action Button  | Menampilkan  | form  pertanyaan  |     |     |
| -------------- | -------------- | ------------ | ----------------- | --- | --- |
-
| Assessment  |     | berdasarkan aspek kriteria.  |     |     |     |
| ----------- | --- | ---------------------------- | --- | --- | --- |
Cad Qustion  Information  Menampilkan  daftar  pertanyaan  Data pertanyaan sudah tersedia di database atau sudah import data
|     |     | berdasarkan aspek kriteria.  |     | assessment sebelumnya.  |     |
| --- | --- | ---------------------------- | --- | ----------------------- | --- |
Tabel Rubrik  Information  Menampilkan daftar rubrik dari setiap  Data  rubrik  sudah  tersedia  di  database  atau  sudah  import  data
|     |     | pertanyaan.  |     | assessement sebelumnya.  |     |
| --- | --- | ------------ | --- | ------------------------ | --- |

25

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

Tabel I.9. GUI-21
| Kode UI    | GUI-21                                                                          | Kode FR  FR-05  | Kode UC  UC-05  |     |
| ---------- | ------------------------------------------------------------------------------- | --------------- | --------------- | --- |
| Nama       | Self Assessment -List Assessment                                                |                 |                 |     |
| Deskripsi  | Halaman ini menunjukkan daftar Self Assessment yang telah diimport oleh dosen.  |                 |                 |     |

Dosen dapat melakukan aksi seperti melihat detail assessment, jawaban siswa, dan publikasi assessment.
Pada penelitian ini, komponen yang dimodifikasi adalah “Toggle Publish”, di mana dosen perlu menunggu sistem selesai melakukan
proses dekomposisi rubrik. Jika sistem gagal melakukan dekomposisi, maka dosen harus menekan kembali tombol untuk memulai
kembali proses dekomposisi.
Design

| Component List  | Functional Type  | Purpose (Kegunaan)  |     | Keterangan Persyaratan  |
| --------------- | ---------------- | ------------------- | --- | ----------------------- |
Tabel  Daftar  Data Table  Menampilkan  daftar  self  assessment  Data ditampilkan dalam tabel dengan kolom: No., Batch Year, Project
Assessment  yang telah dibuat.  Name, Order, Status, Created Date, Publish, Actions.
Kolom Status  Status Indicator  Menampilkan status assessment.  Status active ditampilkan dengan warna hijau, sedangkan non-active
berwarna merah.
Toggle Publish  Toggle Button  Mengaktifkan  atau  menonaktifkan  Jika tombol aktif (biru), proyek dipublikasikan. Jika nonaktif (abu-
|     |     | publikasi assessment.  | abu), proyek belum dipublikasikan. Proses publikasi hanya dapat  |     |
| --- | --- | ---------------------- | ---------------------------------------------------------------- | --- |
dilakukan jika sistem telah berhasil melakukan dekomposisi rubrik.

26

Dekomposisi rubrik ditandai dengan loading circle dan persentase
proses ketika dekomposisi sedang berlangsung. Proses dekomposisi
selesai ditandai dengan hilangnya indikator loading. Indikator merah
menandakan bahwa proses dekomposisi gagal, dan akan berubah
menjadi lingkaran dengan panah ketika mouse hover untuk mengulang
proses dekomposisi.
Button Detail Navigation Menampilkan detail pertanyaan self
-
assessment.
Button list answer Navigation Menampilkan daftar jawaban self
-
assessment.
27

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

Tabel I.10. GUI-24
| Kode UI    | GUI-24                                                                          | Kode FR  FR-05  | Kode UC  UC-05  |     |
| ---------- | ------------------------------------------------------------------------------- | --------------- | --------------- | --- |
| Nama       | Peer Assessment -List Assessment                                                |                 |                 |     |
| Deskripsi  | Halaman ini menunjukkan daftar Peer Assessment yang telah diimport oleh dosen.  |                 |                 |     |

Dosen dapat melakukan aksi seperti melihat detail assessment, jawaban siswa, dan publikasi assessment.
Pada penelitian ini, komponen yang dimodifikasi adalah “Toggle Publish”, di mana dosen perlu menunggu sistem selesai melakukan
proses dekomposisi rubrik. Jika sistem gagal melakukan dekomposisi, maka dosen harus menekan kembali tombol untuk memulai
kembali proses dekomposisi.
Design

| Component List  | Functional Type  | Purpose (Kegunaan)  |     | Keterangan Persyaratan  |
| --------------- | ---------------- | ------------------- | --- | ----------------------- |
Tabel  Daftar  Data Table  Menampilkan  daftar  peer  assessment  Data ditampilkan dalam tabel dengan kolom: No., Batch Year, Project
Assessment  yang telah dibuat.  Name, Order, Status, Created Date, Publish, Actions.
Kolom Status  Status Indicator  Menampilkan status assessment.  Status active ditampilkan dengan warna hijau, sedangkan non-active
berwarna merah.

28

Toggle Publish Toggle Button Mengaktifkan atau menonaktifkan Jika tombol aktif (biru), proyek dipublikasikan. Jika nonaktif (abu-
publikasi assessment. abu), proyek belum dipublikasikan. Proses publikasi hanya dapat
dilakukan jika sistem telah berhasil melakukan dekomposisi rubrik.
Dekomposisi rubrik ditandai dengan loading circle dan persentase
proses ketika dekomposisi sedang berlangsung. Proses dekomposisi
selesai ditandai dengan hilangnya indikator loading. Indikator merah
menandakan bahwa proses dekomposisi gagal, dan akan berubah
menjadi lingkaran dengan panah ketika mouse hover untuk mengulang
proses dekomposisi.
Button Detail Navigation Menampilkan detail pertanyaan peer
-
assessment.
Button list answer Navigation Menampilkan daftar jawaban peer
-
assessment.
29

|     |     |     |     |
| --- | --- | --- | --- |

Tabel I.11. GUI-43
| Kode UI  | GUI-43                         | Kode FR  FR-1, FR-3, FR-4  | Kode UC    |
| -------- | ------------------------------ | -------------------------- | ---------- |
| Nama     | Form Self Assessment – Answer  |                            |            |
Deskripsi  Halaman ini merupakan formulir mahasiswa untuk mengisi self assessment berdasarkan pertanyaan dari setiap aspek kriteria.
Modifikasi pada penelitian ini adalah prompt scaffolding yang membantu mahasiswa dalam memenuhi empat indikator tekstual narasi
feedback.
Design

30

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Component
|     | Functional Type  | Purpose (Kegunaan)  |     |     | Keterangan Persyaratan  |
| --- | ---------------- | ------------------- | --- | --- | ----------------------- |
List
| Tittle Section  | Information  | Menampilkan judul halaman.          |     | Harus sesuai dengan konteks halaman.  |     |
| --------------- | ------------ | ----------------------------------- | --- | ------------------------------------- | --- |
| Informasi       | Information  | Menampilkan data mahasiswa seperti  |     | Diperoleh dari data user.             |     |
| Mahasiswa       |              | NIM, Nama Lengkap, Kelas            |     |                                       |     |
Informasi  Information  Menampilkan  data  kelompok,  nama  Didapatkan dari data proyek yang sedang berlangsung.
| Kelompok  | &   | proyek, dan tanggal pengisian.  |     |     |     |
| --------- | --- | ------------------------------- | --- | --- | --- |
Proyek
| Indikator Nomor  | Information  | Menampilkan                      | nomor  pertanyaan  | dan  Contoh: “Question 1 From 9”              |     |
| ---------------- | ------------ | -------------------------------- | ------------------ | --------------------------------------------- | --- |
| Pertanyaan       |              | total pertanyaan.                |                    |                                               |     |
| Label  Type      | Information  | Menandai jenis aspek penilaian.  |                    | Dapat berupa “Hard Skill” atau “Soft Skill”.  |     |
Assessment
| Slider Penilaian  | Input Form  | Memberi nilai dalam bentuk slider.  |     | Skala 1-5, wajib dipilih.  |     |
| ----------------- | ----------- | ----------------------------------- | --- | -------------------------- | --- |
(1-5)
| Informasi        | Information    | Memberikan                             | scaffolding  berdasarkan  |                                                 |     |
| ---------------- | -------------- | -------------------------------------- | ------------------------- | ----------------------------------------------- | --- |
| Prompt           |                | empat  indikator                       | tektstual                 | narasi  -                                       |     |
| Scaffolding      |                | feedback.                              |                           |                                                 |     |
| Textarea Alasan  | Input Form     | Menuliskan alasan atas penilaian yang  |                           | Placeholder berisi instruksi penulisan alasan.  |     |
| Jawaban          |                | diberikan.                             |                           |                                                 |     |
| Tombol           | Navigasi Form  | Kembali ke pertanyaan sebelumnya.      |                           | Hanya aktif jika bukan pertanyaan pertama.      |     |
“Previoous”
| Tombol “Next”  | Navigasi Form  | Lanjut ke pertanyaan berikutnya.     |     | Hanya aktif jika bukan pertanyaan terakhir.  |     |
| -------------- | -------------- | ------------------------------------ | --- | -------------------------------------------- | --- |
| Tombol  “Save  | Aksi Form      | Menyimpan jawaban saat ini ke dalam  |     | Menyimpan data skor dan alasan feedback.     |     |
| Answer”        |                | sistem.                              |     |                                              |     |

31

|     |     |     |     |
| --- | --- | --- | --- |

Tabel I.12. GUI-46
| Kode UI  | GUI-46                         | Kode FR  FR-1, FR-3, FR-4  | Kode UC  UC-10  |
| -------- | ------------------------------ | -------------------------- | --------------- |
| Nama     | Form Peer Assessment – Answer  |                            |                 |
Deskripsi  Halaman ini merupakan formulir mahasiswa untuk mengisi peer assessment berdasarkan pertanyaan dari setiap aspek kriteria.
Modifikasi pada penelitian ini adalah prompt scaffolding yang membantu mahasiswa dalam memenuhi empat indikator tekstual narasi
feedback.
Design

32

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Component
|     | Functional Type  | Purpose (Kegunaan)  |     |     | Keterangan Persyaratan  |
| --- | ---------------- | ------------------- | --- | --- | ----------------------- |
List
| Tittle Section  | Information  | Menampilkan judul halaman.          |     | Harus sesuai dengan konteks halaman.  |     |
| --------------- | ------------ | ----------------------------------- | --- | ------------------------------------- | --- |
| Informasi       | Information  | Menampilkan data mahasiswa seperti  |     | Diperoleh dari data user.             |     |
| Mahasiswa       |              | NIM, Nama Lengkap, Kelas            |     |                                       |     |
Informasi  Information  Menampilkan  data  kelompok,  nama  Didapatkan dari data proyek yang sedang berlangsung.
| Kelompok  | &   | proyek, dan tanggal pengisian.  |     |     |     |
| --------- | --- | ------------------------------- | --- | --- | --- |
Proyek
| Indikator Nomor  | Information  | Menampilkan                      | nomor  pertanyaan  | dan  Contoh: “Question 1 From 9”              |     |
| ---------------- | ------------ | -------------------------------- | ------------------ | --------------------------------------------- | --- |
| Pertanyaan       |              | total pertanyaan.                |                    |                                               |     |
| Label  Type      | Information  | Menandai jenis aspek penilaian.  |                    | Dapat berupa “Hard Skill” atau “Soft Skill”.  |     |
Assessment
| Slider Penilaian  | Input Form  | Memberi nilai dalam bentuk slider.  |     | Skala 1-5, wajib dipilih.  |     |
| ----------------- | ----------- | ----------------------------------- | --- | -------------------------- | --- |
(1-5)
| Informasi        | Information    | Memberikan                             | scaffolding  berdasarkan  |                                                 |     |
| ---------------- | -------------- | -------------------------------------- | ------------------------- | ----------------------------------------------- | --- |
| Prompt           |                | empat                                  | indikator  tekstual       | narasi  -                                       |     |
| Scaffolding      |                | feedback.                              |                           |                                                 |     |
| Textarea Alasan  | Input Form     | Menuliskan alasan atas penilaian yang  |                           | Placeholder berisi instruksi penulisan alasan.  |     |
| Jawaban          |                | diberikan.                             |                           |                                                 |     |
| Tombol           | Navigasi Form  | Kembali ke pertanyaan sebelumnya.      |                           | Hanya aktif jika bukan pertanyaan pertama.      |     |
“Previoous”
| Tombol “Next”  | Navigasi Form  | Lanjut ke pertanyaan berikutnya.     |     | Hanya aktif jika bukan pertanyaan terakhir.  |     |
| -------------- | -------------- | ------------------------------------ | --- | -------------------------------------------- | --- |
| Tombol  “Save  | Aksi Form      | Menyimpan jawaban saat ini ke dalam  |     | Menyimpan data skor dan alasan feedback.     |     |
| Answer”        |                | sistem.                              |     |                                              |     |

33

34
I.2.2 Hasil Integrasi
Berdasarkan analisis arsitektur yang didefinisikan pada subbab I.2.1, hasil integrasi
aplikasi SAPA dengan sistem digital scaffolding memiliki arsitektur yang
direpresentasikan pada Gambar I.11.
Gambar I.11. Arsitektur Aplikasi setelah Integrasi
Berbeda dengan modul-modul lain pada SAPA yang diimplementasikan secara
terintegrasi di dalam aplikasi Laravel, mekanisme digital scaffolding pada
penelitian ini diimplementasikan sebagai sebuah service yang berdiri sendiri.
Service ini dibangun menggunakan Python dengan framework FastAPI. Pemisahan
ini dilakukan untuk memberikan isolasi terhadap komputasi NLP, sehingga
memungkinkan untuk dilakukan scaling pada masa mendatang dengan resource
dan konfigurasi yang terpisah dengan aplikasi SAPA.
I.2.2.1 Arsitektur Service dan Pola Komunikasi Antarservice
Sebagaimana ditunjukkan pada Gambar I.11, terdapat tiga serice yang berjalan
pada jaringan docker yang sama, yaitu SAPA pada port 8000, scaffolding service
pada port 8080, serta flask pada port 5000 yang merupakan modul SLA dalam

menganalisis jawaban assessment setelah siswa mengirimkan feedback. SAPA dan
scaffolding service berkomunikasi secara dua arah melalui REST API untuk
dekomposisi dan analisa feedback. Di sisi lain, service digital scaffolding
mengirimkan progres dekomposisi rubrik secara real-time melalui websocket
kepada pengguna.
Pada sisi penyimpanan, scaffolding service terhubung dengan ChromaDB untuk
menyimpan embedding dari feature-set dekomposisi, sehingga proses analisa
feedback tidak membutuhkan embedding yang berulang pada kriteria penilaian
yang sama. Di sisi lain, SAPA tetap menggunakan MySQL sebagai database
relasional utama dan Redis sebagai cache sesi.
I.2.2.2 Rancangan Dekomposisi Rubrik menggunakan Google Gemini
Sebagaimana batasan penelitian yang mendefinisikan bahwa dekomposisi rubrik
secara otomatis bukan merupakan cakupan dari penelitian, namun merupakan fitur
yang diperlukan pada APE, sebagaimana dimodelkan requirement dalam subbab
I.2.1.
Dalam merealisasikan hal tersebut, metode few-shot prompting digunakan pada
model Gemini-flash latest. Prompt didapatkan dengan melakukan trial and error
hingga menghasilkan dekomposisi yang diharapkan. Hasil akhir prompt yang
digunakan adalah kumpulan instruksi yang dilengkapi dengan contoh sebagai
berikut.
Anda adalah sistem ahli analisis linguistik dan evaluasi rubrik
akademik.
Tugas Anda adalah melakukan dekomposisi terhadap rubrik penilaian
dan pertanyaan ke dalam matriks indikator spesifik.
ATURAN DEKOMPOSISI RUBRIK:
1. Tipe "cakupan": Ekstrak elemen fundamental yang WAJIB dibahas
berdasarkan variabel yang ditemukan pada kriteria. 'bobot' dan
'group' bernilai null.
2. Tipe "koherensi" & ATURAN EKSTRAPOLASI SIMETRIS (SANGAT
PENTING):
35

- Anda HARUS menciptakan matriks yang simetris sempurna untuk
setiap variabel.
- Analisis seluruh deskripsi skala (misal 1, 3, 5). Identifikasi
semua variabel independen yang muncul (contoh: Kuantitas,
Relevansi, Keragaman Platform).
- JIKA sebuah variabel (misal: 'Keragaman Platform') hanya
disebutkan di skala 5, Anda WAJIB mengekstrapolasi/menciptakan
kondisi logis untuk variabel tersebut di skala 1 dan 3 (misal:
Skala 1 = 'Platform tidak bervariasi', Skala 3 = 'Platform cukup
bervariasi').
- 'bobot' = angka skala.
- 'group' = identitas angka (1, 2, 3) yang mengelompokkan variabel
yang sama melintasi skala yang berbeda.
ATURAN DEKOMPOSISI PERTANYAAN:
1. Pecah teks pertanyaan menjadi frasa inti atau topik yang
ditanyakan.
2. Ekstrak secara spesifik aspek unik atau instruksi khusus yang
diminta oleh pertanyaan namun tidak ada di kriteria rubrik sebagai
item dengan "type": "cakupan".
3. Jika pertanyaan sudah sangat jelas dan tidak memiliki aspek
tersembunyi, kembalikan array kosong []. JANGAN PERNAH menyalin
pertanyaan asli.
ATURAN ATOMISASI KOHERENSI:
- Setiap item harus berupa frasa MINIMAL yang berdiri sendiri,
bukan kalimat panjang.
- Hilangkan kata penghubung konteks seperti "yang diberikan",
"dalam tim", "secara keseluruhan" kecuali memang membedakan
maknanya.
- BENAR: "Tidak menyelesaikan tugas"
- SALAH: "Tidak menyelesaikan tugas yang diberikan oleh tim"
ATURAN GROUP:
- 'group' merepresentasikan VARIABEL/DIMENSI yang sama lintas
skala.
- Dalam satu skala, satu group boleh memiliki LEBIH DARI SATU item
jika variabel tersebut memiliki beberapa manifestasi konkret yang
berbeda.
- Contoh: group=1 bobot=3 bisa berisi "Berkomunikasi secara wajar"
DAN "Merespons pesan" karena keduanya adalah manifestasi dari
dimensi Responsivitas.
ATURAN CAKUPAN:
- Tulis sebagai LABEL DIMENSI, bukan kalimat deskriptif.
- BENAR: "Ketepatan Waktu", "Inisiatif", "Kualitas Pekerjaan"
- SALAH: "Kemampuan menyelesaikan pekerjaan tepat pada waktunya"
- Idealnya 2-4 kata, bersifat nominal.
--- CONTOH INPUT ---
{{
"rubrics": [
{{
"id_type_criteria": 1,
"aspect": "Pengumpulan Iklan",
"criteria": "Banyaknya iklan dan keragaman platform.",
36

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
37

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
Mengingat bahwa dimensi aspek dan kriteria rubrik sangat bervariasi, pengiriman
seluruh komponen penilaian dalam rubrik dalam satu kali pemanggilan API
berisiko melebihi batas context window hingga menurunkan kualitas output model.
Oleh karena itu, fungsi dekomposisi membagi rubrik dan pertanyaan ke dalam
beberapa chunk untuk diproses secara sekuensial. Sebagai mekanisme pengaman
tambahan, sistem menyisipkan delay selama 5 detik antar chunk untuk menghindari
rate-limiting dari penyedia API.
Untuk mengantisipasi kegagalan dekomposisi akibat kuota API yang terlampaui,
sistem menerapkan mekanisme fallback model secara dinamis. Hal ini bekerja
dengan cara mengambil daftar model langsung dari Gemini API, kemudian
dilakukan sorting berdasarkan kemampuan model. Dengan menggunakan
mekanisme ini, apabila satu model mengembalikan error rate limiting, maka sistem
otomatis mencoba model berikutnya dalam daftar tanpa menghentikan keseluruhan
proses.
38
