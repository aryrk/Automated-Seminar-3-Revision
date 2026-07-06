<div align="center">

# LAMPIRAN 4 & 5
## ANALISIS SISTEM BERJALAN DAN PERANCANGAN TEKNIS APE

</div>

---

### Daftar Tabel
- Tabel L4.1: Aspek Komponen yang terlibat  Interface GUI-43 (Form Self Assessment) dan GUI-46 (Form Peer Assessment) GUI-22 (Detail Question Self Assessment) dan GUI-25 (Detail Question Peer Assessment) GUI-21 (List Self Assessment) dan GUI-24 (List Peer Assessment) Logika Bisnis AssessmentController (menangani UC-10 Answer Assessment) pada SD-10 (Self Assessment) dan SD-11(Peer Assessment)) Basis Data (Data) Entitas Tabel 'Criteria' , 'Assessment' dan 'Reflective Assessment'
- Tabel L4.2: Tabel L4.2. Komponen Yang Dimodifikasi
- Tabel L4.3: menyajikan komponen yang ditambahkan terhadap arsitektur SAPA berdasarkan identifikasi titik integrasi pada Tabel L4.1.
- Tabel L4.4: menyajikan functional requirement untuk memfasilitasi sistem digital scaffolding, hal ini dilakukan untuk memastikan proses eksperimen dapat dilaksanakan, sebagaimana didefinisikan pada prosedur operasional eksperimen.
- Tabel L4.5: FR-02: Sistem harus menyediakan mekanisme bagi dosen untuk mengaktifkan atau menonaktifkan fitur scaffolding untuk setiap assessment.
- Tabel L4.6: menggunakan konfigurasi akhir pipeline digital scaffolding. Komputasi dilakukan dengan mekanisme debounce 1,5 detik dan interval maksimum 1,5 detik.
- Tabel L4.7: berfungsi untuk membantu sistem digital scaffolding pada penelitian ini.
- Tabel L4.8: menyajikan use case scenario untuk UC-17 (Receive Digital Scaffolding Prompt).
- Tabel L4.9: dan
- Tabel L4.10: Akibatnya, siswa tidak mendapatkan prompt scaffolding selama mengisi self/peer assessment. Implementasi hal tersebut digunakan untuk membantu proses eksperimen terhadap kelompok mahasiswa dalam penelitian ini.
- Tabel L4.11: GUI- dan Tabel L4.12. Jika scaffolding aktif, maka mahasiswa akan mendapatkan teks prompt tepat di atas kolom narasi untuk membantu meningkatkan pemenuhan keempat indikator tekstual narasi feedback.
- Tabel L4.12: Jika scaffolding aktif, maka mahasiswa akan mendapatkan teks prompt tepat di atas kolom narasi untuk membantu meningkatkan pemenuhan keempat indikator tekstual narasi feedback.
- Tabel L4.13: GUI-21
- Tabel L4.14: GUI-24

### Daftar Gambar
- Gambar L4.1: Berdasarkan abstraksi Business Process Model and Notation (BPMN) yang telah dirancang, siklus operasional SAPA telah dirancang dengan alur yang sistematis untuk memfasilitasi evaluasi sumatif. Alur bisnis direpresentasikan mulai dari tahap inisiasi di mana dosen menyusun proyek dan instrumen rubrik penilaian, dilanjutkan oleh fase pengerjaan evaluasi oleh mahasiswa, dan diakhiri dengan pemrosesan rekomendasi skor menggunakan SLA Algorithm oleh sistem sebagai material analis bagi dosen.
- Gambar L4.2: BPMN to-be Setelah APE diintegrasikan
- Gambar L4.3: Gambar L4.3. Use Case Diagram APE yang Akan Dikembangkan
- Gambar L4.4: menyajikan keseluruhan arsitektur class diagram SAPA, dengan komponen berwarna hitam merepresentasikan bagian existing yang telah tersedia, sementara komponen berwarna merah merepresentasikan penambahan atau modifikasi untuk memfasilitasi pipeline digital scaffolding. Untuk meningkatkan visibilitas, Gambar L4.4 menyajikan class diagram yang terisolasi terhadap komponen terdampak.
- Gambar L4.5: Class Diagram Bagian Modifikasi
- Gambar L4.6: ERD Keseluruhan SAPA
- Gambar L4.7: menyajikan diagram yang terisolasi pada entitas terdampak.
- Gambar L4.8: serta Gambar L4.9, dan juga proses manage assessment pada Gambar L4.10.
- Gambar L4.9: Gambar L4.10. Sequence Diagram UC-05 Manage Assessment
- Gambar L4.10: Dalam aplikasi SAPA yang sudah ada, saat proses manage assessment oleh dosen berlangsung, assessment ditambahkan dengan cara mengunggah file Excel yang berisi detail rubrik assessment. Rubrik tersebut mencakup berbagai aspek seperti pertanyaan, jenis assessment, jenis skill, hingga aspek yang dinilai serta kriteria yang digunakan untuk setiap pertanyaan. Dalam penelitian ini, proses import melibatkan tahapan untuk melakukan dekomposisi rubrik sesuai dengan prinsip dekomposisi rubrik. Proses ini berjalan secara asynchronous di latar belakang, sehingga pengguna tidak perlu menunggu pada halaman SAPA hingga proses selesai, seperti yang ditunjukkan pada Gambar L4.10.
- Gambar L4.11: Gambar L4.11. Arsitektur Aplikasi setelah Integrasi

---

Lampiran ini menyajikan dokumentasi rekayasa perangkat lunak (software engineering) dari integrasi sistem scaffolding ke dalam lingkungan Aplikasi Pendukung Eksperimen (APE). Pembahasan mencakup pemodelan Business Process Model and Notation (BPMN) sistem berjalan, arsitektur integrasi, Use Case, dan rancangan antarmuka GUI.

## L4.1 Hasil Analisis Sistem Berjalan

Analisis Sistem Existing bertujuan untuk mengidentifikasi lingkungan tempat sistem scaffolding diintegrasikan untuk isolasi modifikasi kode. Tahapan ini dilakukan dengan meninjau dokumen SRS (Software Requirement Specification), SDD (Software Design Documentation), manual book, source code, dan dokumen laporan penelitian.

### L4.1.1 Deskripsi Sistem Existing

Aplikasi SAPA merupakan platform berbasis web yang dirancang untuk mendukung pengisian self dan peer assessment mahasiswa JTK Polban. Aplikasi ini memungkinkan dosen untuk mengelola proyek (mata kuliah), membuat dan membagikan formulir assessment, serta memantau dan mengevaluasi hasil assessment. Keseluruhan proses bisnis SAPA disajikan pada Gambar L4.1.

Berdasarkan abstraksi Business Process Model and Notation (BPMN) yang telah dirancang, siklus operasional SAPA telah dirancang dengan alur yang sistematis untuk memfasilitasi evaluasi sumatif. Alur bisnis direpresentasikan mulai dari tahap inisiasi di mana dosen menyusun proyek dan instrumen rubrik penilaian, dilanjutkan oleh fase pengerjaan evaluasi oleh mahasiswa, dan diakhiri dengan pemrosesan rekomendasi skor menggunakan SLA Algorithm oleh sistem sebagai material analis bagi dosen.

Gambar L4.1. Proses Bisnis SAPA

### L4.1.2 Identifikasi Titik Integrasi

Berdasarkan tinjauan yang dilakukan terhadap dokumen SRS, SDD, serta source code ditemukan titik integrasi untuk kebutuhan digital scaffolding terhadap enam halaman, sebagaimana disajikan pada Tabel L4.1.

Aspek Komponen yang terlibat  Interface GUI-43 (Form Self Assessment) dan GUI-46 (Form Peer Assessment) GUI-22 (Detail Question Self Assessment) dan GUI-25 (Detail Question Peer Assessment) GUI-21 (List Self Assessment) dan GUI-24 (List Peer Assessment) Logika Bisnis AssessmentController (menangani UC-10 Answer Assessment) pada SD-10 (Self Assessment) dan SD-11(Peer Assessment)) Basis Data (Data) Entitas Tabel 'Criteria' , 'Assessment' dan 'Reflective Assessment'

Tabel L4.1. Titik Integrasi

Titik integrasi digital scaffolding berada pada fase pengisian narasi feedback sebelum mahasiswa melakukan operasi simpan jawaban. Hal ini diimplementasikan dengan menambahkan event yang menangkap perubahan narasi pada UC-10 (Answer Assessment) pada SD-10 dan SD 11.

### L4.1.3 Komponen yang Dimodifikasi

Untuk melakukan integrasi sistem digital scaffolding terhadap aplikasi SAPA, beberapa komponen yang tersedia perlu dimodifikasi sebagaimana disajikan pada Tabel L4.2.

Tabel L4.2. Komponen Yang Dimodifikasi

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Aspek  |  Komponen  |  Modifikasi
kondisi teks narasi mahasiswa sebagai input sistem digital scaffolding.
Proses  |  UC-10 pada SD-10 dan SD-11  |  Modifikasi yang diterapkan berupa penambahan relasi < <extends>&gt; pada UC-17. Di sisi lain, UC-10 melakukan proses pemanggilan terhadap API pipeline digital scaffolding.</extends>

### L4.1.4 Komponen yang Ditambahkan

Sebagai ekstensi dari subbab L4.1.3, Tabel L4.3 menyajikan komponen yang ditambahkan terhadap arsitektur SAPA berdasarkan identifikasi titik integrasi pada Tabel L4.1.

Tabel L4.3. Komponen Yang Ditambahkan

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

## L4.2 Hasil Perancangan dan Integrasi Konponen

Subbab ini menjelaskan perancangan sistem yang diusulkan sebagai pengembangan dari aplikasi SAPA dengan penambahan fitur conditional scaffolding, sebagai manifestasi dari tahapan perancangan metodologi. Perancangan dilakukan berdasarkan kebutuhan sistem yang telah diidentifikasi sebelumnya.

### L4.2.1 Arsitektur Aplikasi Pendukung Eksperimen

Pada kondisi saat ini (as-is), aplikasi SAPA mendukung proses self dan peer assessment di mana mahasiswa mengisi jawaban kuantitatif dan narasi feedback secara langsung tanpa adanya intervensi atau bantuan selama proses penulisan, sebagaimana direpresentasikan oleh Gambar L4.1. Evaluasi terhadap kualitas narasi hanya terjadi secara implisit dan umumnya baru terlihat pada hasil akhir penilaian atau umpan balik dari dosen.

Kondisi yang diusulkan (to-be) pada Gambar L4.2, dengan simbol berwarna merepresentasikan komponen yang ditambahkan untuk mendukung mekanisme digital scaffolding yang terintegrasi dalam proses pengisian narasi. Sistem secara aktif mengevaluasi input narasi mahasiswa secara real-time menggunakan rubrik yang telah didekomposisi, kemudian memberikan conditional prompt apabila ditemukan bahwa feedback belum memenuhi indikator yang diharapkan. Integrasi dilakukan pada level fitur aplikasi SAPA sebagaimana didefinisikan pada subbab L4.1.3.

Lebih jauh, untuk mempertahankan standar dan konsistensi proses integrasi, analisis pada functional requirements, non-functional requirements, use case diagram, class diagram, database, sequence diagram, hingga perancangan antarmuka didefinisikan pada subbab L4.2.1A hingga IV.4.2.1G.

Melalui perubahan ini seluruh komponen dan fitur lainnya yang telah tersedia pada aplikasi SAPA, seperti pengumpulan assessment, perhitungan nilai, dan pemberian feedback oleh dosen tetap berjalan sebagaimana mestinya tanpa adanya modifikasi.

Gambar L4.2. BPMN to-be Setelah APE diintegrasikan

**A. Functional Requirements**

Tabel L4.4 menyajikan functional requirement untuk memfasilitasi sistem digital scaffolding, hal ini dilakukan untuk memastikan proses eksperimen dapat dilaksanakan, sebagaimana didefinisikan pada prosedur operasional eksperimen.

Tabel L4.4. Functional Requirements

Kode FR: Deskripsi
FR-01: Sistem harus dapat menampilkan teks scaffolding (conditional prompt) dengan kode template 0001 hingga 1111 sesuai hasil analisis indikator saat mahasiswa mengisi narasi kualitatif assessment, sebagaimana didefinisikan pada Tabel L4.5.
FR-02: Sistem harus menyediakan mekanisme bagi dosen untuk mengaktifkan atau menonaktifkan fitur scaffolding untuk setiap assessment.
FR-03: Sistem harus dapat melakukan komputasi empat indikator tekstual narasi, sebagaimana didefinisikan pada Tabel L4.6 menggunakan konfigurasi akhir pipeline digital scaffolding. Komputasi dilakukan dengan mekanisme debounce 1,5 detik dan interval maksimum 1,5 detik.
FR-04: Sistem harus dapat menggunakan template dengan kode 0000 ketika seluruh indikator tekstual narasi terpenuhi, sebagaimana didefinisikan pada Tabel L4.5.
FR-05: Sistem dapat melakukan proses dekomposisi rubrik secara otomatis menggunakan API Gemini berdasarkan prosedur dekomposisi rubrik.
FR-06: Sistem harus merekam data log interaksi (behavioral log) secara sekuensial selama sesi penulisan aktif, yang mencakup riwayat perubahan teks narasi, modifikasi skor kuantitatif, riwayat pemicu prompt scaffolding per indikator, serta timestamp interaksi.

**B. Non Functional Requirements**

Non-functional requirement yang disajikan pada Tabel L4.7 berfungsi untuk membantu sistem digital scaffolding pada penelitian ini.

Tabel L4.7. Non Functional Requirements

Kode NFR: Deskripsi
NFR-01: Sistem harus memproses dan mengembalikan hasil evaluasi scaffolding dalam
waktu maksimum 5 detik sejak permintaan diterima oleh pipeline digital
scaffolding.
NFR-02: Model embedding yang digunakan pada pipeline digital scaffolding, sebagaimana didefinisikan konfigurasi akhir pipeline digital scaffolding, harus dipastikan tersedia selama siklus hidup layanan tanpa perlu pemuatan ulang pada setiap request analisa feedback.
NFR-03: Sistem hanya memproses feedback yang unik dalam satu sesi mahasiswa pada
setiap pertanyaan assessment.
NFR-04: Aplikasi menerapkan mekanisme caching menggunakan kombinasi skor dan
teks narasi sebagai key untuk mencegah pemanggilan API yang redundan dan
mengurangi beban komputasi server.

**C. Use Case Diagram**

Sebagai ekstensi fitur aplikasi SAPA, pipeline digital scafolding digambarkan sebagai UC-17 (Receive Scaffolding) yang berelasi extend terhadap UC-10 (Answer Assessment) dalam use case diagram SAPA yang disajikan pada Gambar L4.3.

Gambar L4.3. Use Case Diagram APE yang Akan Dikembangkan

Untuk mendukung use case diagaram pada Gambar L4.3, Tabel L4.8 menyajikan use case scenario untuk UC-17 (Receive Digital Scaffolding Prompt).

Tabel L4.8. Use Case Scenario Receive Scaffolding (UC-17)

Use Case section Comment Use case Name
UC-17 Receive Digital Scaffolding
Scope: Aplikasi Existing (SAPA)
Level: Sub Function
Primary Actor: Mahasiswa
Stakeholder and Interest: 1. Mahasiswa ingin mendapatkan bantuan selama menulis narasi feedback.
Precondition 1.: Mahasiswa berada di tahapan mengisi assessment (UC-10) 2. Target assessment (self/peer) sudah dipilih
Success Guarantee: Teks scaffolding berhasil ditampilkan saat skor kualitatif/narasi tidak memenuhi minimal satu dari empat indikator tekstual narasi feedback
pada: Teks scaffolding dengan kode 0000, sebagaimana didefinisikan Tabel L4.5 ditampilkan saat skor kuantitaif/narasi memenuhi seluruh empat indikator tekstual narasi feedback
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

Class diagram memetakan struktur teknis sistem dengan mendetailkan atribut dan metode pada setiap kelas serta cara kelas-kelas tersebut berinteraksi. Gambar L4.4 menyajikan keseluruhan arsitektur class diagram SAPA, dengan komponen berwarna hitam merepresentasikan bagian existing yang telah tersedia, sementara komponen berwarna merah merepresentasikan penambahan atau modifikasi untuk memfasilitasi pipeline digital scaffolding. Untuk meningkatkan visibilitas, Gambar L4.4 menyajikan class diagram yang terisolasi terhadap komponen terdampak.

Berdasarkan gambar tersebut, salah satu komponen yang terdampak adalah type criteria yang menyimpan komponen penilaian rubrik, modifikasi dilakukan dengan menambahkan atribut status dekomposisi. Komponen lain yang terdampak yaitu assessment dan reflective, modifikasi dilakukan dengan menambahkan toggle aktivasi scaffolding dan status dekomposisi pada level pertanyaan. Class assessment berfungsi untuk menyimpan informasi mengenai self dan peer assessment, di sisi lain, class reflective adalah ekstensi dari self assessment dengan komponen yang serupa.

Untuk menyimpan hasil dekomposisi rubrik, sebagaimana prosedur dekomposisi rubrik, class question decomposition dan rubric decomposition diperlukan untuk menyimpan feature-set cakupan rubrik dan relevansi topik (åçU-, ) serta feature-set koherensi skor dan narasi (åçé-, ). Kedua class tersebut menjadi salah satu input komputasi pipeline digital scaffolding, sebagaimana didefinisikan pada arsitektur pipeline komputasional.

Gambar L4.4. Class Diagram Keseluruhan (to-be)

Gambar L4.5. Class Diagram Bagian Modifikasi

**E. Entity Relationship Diagram**

Basis data keseluruhan aplikasi sapa dengan modifikasi yang telah disesuaikan disajikan pada Gambar L4.6, dengan komponen yang memiliki warna merah merepresentasikan modifikasi/penambahan yang dilakukan berdasarkan analisis pada subbab L4.1. Untuk meningkatkan visibilitas diagram, Gambar L4.7 menyajikan diagram yang terisolasi pada entitas terdampak.

Sistem menggunakan dua tabel dekomposisi yang memiliki peran yang berbeda. Rubric\_decomposition merupakan tabel yang menyimpan feature-set untuk indikator cakupan rubrik, relevansi, dan koherensi skor dari aspek rubrik spesifik. Di sisi lain, question\_decomposition menyimpan feature-set untuk indikator cakupan rubrik yang dimiliki oleh pertanyaan feedback, terlepas dari rubrik maupun bobot aspek pada rubrik. Pemisahan kedua tabel dekomposisi tersebut bertujuan untuk mencegah adanya duplikasi ataupun konflik pada pertanyaan yang berbeda namun menggunakan aspek rubrik yang sama.

Gambar L4.6. ERD Keseluruhan SAPA

Gambar L4.7. ERD Bagian Modifikasi

**F. Sequence Diagram**

Sequence Diagaram menunjukkan cara objek berkomunikasi satu sama lain dalam sistem. Pada penelitian ini, diagram dibuat berdasarkan modifikasi dari sistem existing pada Lampiran 2, meliputi proses pengisian self dan peer assessment pada Gambar L4.8 serta Gambar L4.9, dan juga proses manage assessment pada Gambar L4.10.

Dalam aplikasi SAPA yang sudah ada, saat proses manage assessment oleh dosen berlangsung, assessment ditambahkan dengan cara mengunggah file Excel yang berisi detail rubrik assessment. Rubrik tersebut mencakup berbagai aspek seperti pertanyaan, jenis assessment, jenis skill, hingga aspek yang dinilai serta kriteria yang digunakan untuk setiap pertanyaan. Dalam penelitian ini, proses import melibatkan tahapan untuk melakukan dekomposisi rubrik sesuai dengan prinsip dekomposisi rubrik. Proses ini berjalan secara asynchronous di latar belakang, sehingga pengguna tidak perlu menunggu pada halaman SAPA hingga proses selesai, seperti yang ditunjukkan pada Gambar L4.10.

Selanjutnya, ketika mahasiswa mengisi self ataupun self assessment, aplikasi yang sudah ada memiliki perilaku seperti formulir pada umumnya, yaitu pengguna dapat mengisi atau mengubah isi formulir hingga proses submit assessment. Dalam penelitian ini, mahasiswa diberikan prompt scaffolding yang bertujuan untuk meningkatkan feedback literacy ketika siswa melakukan menulis narasi, yang ditampilkan pada Gambar L4.8 dan Gambar L4.9.

Gambar L4.10. Sequence Diagram UC-05 Manage Assessment

Gambar L4.8. Sequence Diagram UC-10 Answer Peer Assessment

Gambar L4.9. Sequence Diagram UC-10 Answer Self Assessment

**G. Perancangan Antarmuka**

Perancangan antarmuka didasari oleh aplikasi SAPA existing berdasarkan pada subbab L4.1.3. Setelah dosen mengunggah file excel yang berisikan rubrik dan pertanyaan assessment, aplikasi akan memulai proses dekomposisi rubrik menggunakan API Gemini, sebagaimana dijabarkan sesuai prinsip pemrosesan bahasa alami. Kemudian, dosen dapat menuju antarmuka pada GUI-22 ataupun GUI-24 untuk melihat daftar assessment, mencoba mengisi assessment, hingga melakukan publikasi assessment. Publikasi tidak dapat dilakukan sebelum sistem selesai melakukan dekomposisi rubrik, ditandai dengan indikator loading pada bagian kanan dari toggle publikasi.

Secara default, setiap assessment memiliki scaffolding ketika mahasiswa mengisi narasi. Namun, dosen dapat menonaktifkan fitur scaffolding pada antarmuka di Tabel L4.9 dan

Tabel L4.10. Akibatnya, siswa tidak mendapatkan prompt scaffolding selama mengisi self/peer assessment. Implementasi hal tersebut digunakan untuk membantu proses eksperimen terhadap kelompok mahasiswa dalam penelitian ini.

Pada sudut pandang mahasiswa ketika mengisi assessment, dengan antarmuka pada Tabel L4.11. GUI- dan Tabel L4.12. Jika scaffolding aktif, maka mahasiswa akan mendapatkan teks prompt tepat di atas kolom narasi untuk membantu meningkatkan pemenuhan keempat indikator tekstual narasi feedback.

Tabel L4.9. GUI-22

Tabel L4.10. GUI-25

Tabel L4.13. GUI-21

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Tabel L4.14. GUI-24

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

[Tabel tidak terbaca: teks terfragmentasi di PDF asli — lihat dokumen sumber]

Tabel L4.11. GUI-43

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

Tabel L4.12. GUI-46

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

### L4.2.2 Hasil Integrasi

Berdasarkan analisis arsitektur yang didefinisikan pada subbab L4.2.1, hasil integrasi aplikasi SAPA dengan sistem digital scaffolding memiliki arsitektur yang direpresentasikan pada Gambar L4.11.

Gambar L4.11. Arsitektur Aplikasi setelah Integrasi

Berbeda dengan modul-modul lain pada SAPA yang diimplementasikan secara terintegrasi di dalam aplikasi Laravel, mekanisme digital scaffolding pada penelitian ini diimplementasikan sebagai sebuah service yang berdiri sendiri. Service ini dibangun menggunakan Python dengan framework FastAPI. Pemisahan ini dilakukan untuk memberikan isolasi terhadap komputasi NLP, sehingga memungkinkan untuk dilakukan scaling pada masa mendatang dengan resource dan konfigurasi yang terpisah dengan aplikasi SAPA.

**A. Arsitektur Service dan Pola Komunikasi Antarservice**

Sebagaimana ditunjukkan pada Gambar L4.11, terdapat tiga serice yang berjalan pada jaringan docker yang sama, yaitu SAPA pada port 8000, scaffolding service pada port 8080, serta flask pada port 5000 yang merupakan modul SLA dalam menganalisis jawaban assessment setelah siswa mengirimkan feedback. SAPA dan scaffolding service berkomunikasi secara dua arah melalui REST API untuk dekomposisi dan analisa feedback. Di sisi lain, service digital scaffolding mengirimkan progres dekomposisi rubrik secara real-time melalui websocket kepada pengguna.

Pada sisi penyimpanan, scaffolding service terhubung dengan ChromaDB untuk menyimpan embedding dari feature-set dekomposisi, sehingga proses analisa feedback tidak membutuhkan embedding yang berulang pada kriteria penilaian yang sama. Di sisi lain, SAPA tetap menggunakan MySQL sebagai database relasional utama dan Redis sebagai cache sesi.

**B. Rancangan Dekomposisi Rubrik menggunakan Google Gemini**

Sebagaimana batasan penelitian yang mendefinisikan bahwa dekomposisi rubrik secara otomatis bukan merupakan cakupan dari penelitian, namun merupakan fitur yang diperlukan pada APE, sebagaimana dimodelkan requirement dalam subbab L4.2.1.

Dalam merealisasikan hal tersebut, metode few-shot prompting digunakan pada model Gemini-flash latest. Prompt didapatkan dengan melakukan trial and error hingga menghasilkan dekomposisi yang diharapkan sesuai dengan tahapan dekomposisi rubrik. Hasil akhir prompt yang digunakan adalah kumpulan instruksi yang dilengkapi dengan contoh sebagai berikut.

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
