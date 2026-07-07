PERBAIKAN ANTARMUKA APLIKASI PENDUKUNG

EKSPERIMEN PASCA ESPERIMEN

LAMPIRAN TUGAS AKHIR

Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan

Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di

Jurusan Teknik Komputer dan Informatika

Oleh:

Aryo Rakatama

221524003

Muhammad Rama Nurimani

221524021

PROGRAM SARJANA TERAPAN

PROGRAM STUDI TEKNIK INFORMATIKA

JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA

POLITEKNIK NEGERI BANDUNG

2026

DAFTAR ISI

DAFTAR ISI ........................................................................................................... i

DAFTAR GAMBAR ............................................................................................. ii

DAFTAR TABEL ................................................................................................ iii

BAB I PERBAIKAN ANTARMUKA APLIKASI .............................................. 4

I.1 Hasil Perbaikan Aplikasi Pendukung Eksperimen ........................................ 4

i

DAFTAR GAMBAR

Gambar I.1. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

Gambar I.2. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

6
7

ii

DAFTAR TABEL

Tabel I.1. Keluhan Subjek yang menyatakan Distraksi

4

iii

BAB I

PERBAIKAN ANTARMUKA APLIKASI

Lampiran  ini  mendokumentasikan  tindak  lanjut  desain  berupa  modifikasi

antarmuka Aplikasi Pendukung Eksperimen (APE). Modifikasi ini didasarkan pada

umpan  balik  kualitatif  subjek  eksperimen  mengenai  isu  ergonomi  kognitif  yang

dirasakan selama penggunaan sistem.

I.1 Hasil Perbaikan Aplikasi Pendukung Eksperimen

Hasil kuesioner mengidentifikasi adanya keluhan pengguna yang berkaitan dengan

distraksi berupa disrupsi fokus (split-attention effect) dan auto-scroll issue selama

proses penulisan narasi feedback., sehingga mengganggu proses penulisan narasi

feedback mahasiswa. Hal ini didukung oleh saran subjek yang disajikan pada Tabel

I.1

No

1

Tabel I.1. Keluhan Subjek yang menyatakan Distraksi

Bagian Sistem yang
Mengganggu

Contoh
pembuka/sentence starter

kalimat

2

Keseluruhan scaffolding utuh

3

Peringatan  diagnosis  kekurangan
narasi yang ditulis

Keluhan Subjek Eksperimen

Sesaat setelah mengetik agak terganggu dengan teks
AI  yang  muncul,  yang  membuat  konsentrasi  agak
pecah untuk menulis yang ada dipikiran
Saran  posisi  rekomendasi  fitur  AI  mungkin  bisa  di
bagian bawah inputan. Karena ketika mengetik, fitur
AI  yang  mulai  bekerja  otomatis  menggulir  halaman
kebawah.
karena  kadang  peringatannya  terlalu  cepat  padahal
masih mikir untuk nulis apa

Sebagai  respons  terhadap  temuan  tersebut,  dilakukan  modifikasi  pada  GUI

pengisian  assessment  yang  telah  dimodelkan.  Modifikasi  yang  dilakukan  berupa

transformasi contrainer scaffolding menjadi elemen collapsible yang dapat ditutup

dan dibuka sesuai keinginan pengguna. Secara default, scafolding akan tertutup dan

hanya  menampilkan  status  dari  empat  indikator  tekstual,  sebagaimana  disajikan

pada  Gambar  I.1.  Dalam  kondisi  ini,  tombol  panah  collapsible  akan  bercahaya

untuk  pertama  kali  sebagai  upaya  menarik  perhatian  pengguna  untuk  membuka

gulir  scaffolding.  Jika  mahasiswa  menekan  tombol  collapsible,  maka  container

4

scaffolding akan tetap terbuka meskipun pertanyaan berganti hingga tombol ditekan

kembali, sebagaimana disajikan pada Gambar I.2 Pendekatan antarmuka adaptif ini

diterapkan  untuk  mengurangi  potensi  distraksi  visual  yang  dilaporkan  pengguna

tanpa menghilangkan visibilitas terhadap status pemenuhan indikator rubrik.

Perlu dicatat bahwa modifikasi dilakukan setelah seluruh data eksperimen selesai

dikumpulkan. Oleh karena itu, perubahan tersebut tidak memengaruhi hasil analisis

yang digunakan untuk menjawab research question, melainkan berfungsi sebagai

tindak  lanjut  desain  berdasarkan  masukan  subjek  eksperimen  yang  diperoleh

selama eksperimen.

5

6

Gambar I.1. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

6

Gambar I.2. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

7

8


