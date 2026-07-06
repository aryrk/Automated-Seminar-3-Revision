<div align="center">

# LAMPIRAN 9
## PERBAIKAN ANTARMUKA APLIKASI PENDUKUNG EKSPERIMEN (APE) PASCA-EKSPERIMEN

</div>

---

### Daftar Tabel
- Tabel L9.1: Keluhan Subjek yang menyatakan Distraksi

### Daftar Gambar
- Gambar L9.1: Dalam kondisi ini, tombol panah collapsible akan bercahaya untuk pertama kali sebagai upaya menarik perhatian pengguna untuk membuka gulir scaffolding. Jika mahasiswa menekan tombol collapsible, maka container scaffolding akan tetap terbuka meskipun pertanyaan berganti hingga tombol ditekan kembali, sebagaimana disajikan pada Gambar L9.2 Pendekatan antarmuka adaptif ini diterapkan untuk mengurangi potensi distraksi visual yang dilaporkan pengguna tanpa menghilangkan visibilitas terhadap status pemenuhan indikator rubrik.
- Gambar L9.2: Pendekatan antarmuka adaptif ini diterapkan untuk mengurangi potensi distraksi visual yang dilaporkan pengguna tanpa menghilangkan visibilitas terhadap status pemenuhan indikator rubrik.

---

Lampiran ini mendokumentasikan tindak lanjut desain (design follow-up) berupa modifikasi antarmuka Aplikasi Pendukung Eksperimen (APE). Modifikasi ini didasarkan pada umpan balik kualitatif subjek eksperimen mengenai isu ergonomi kognitif yang dirasakan selama penggunaan sistem.

## L9.1 Hasil Perbaikan Aplikasi Pendukung Eksperimen

Subbab ini merupakan implementasi dari tahap yang didefinisikan dalam tahapan tindak lanjut desain berdasarkan pembahasan hasil eksperimen yang dipetakan pada hasil pengujian.

Pembahasan hasil eksperimen sebelumnya mengidentifikasi adanya keluhan pengguna yang berkaitan dengan distraksi berupa disrupsi fokus (split-attention effect) dan auto-scroll issue selama proses penulisan narasi feedback., sehingga mengganggu proses penulisan narasi feedback mahasiswa. Hal ini didukung oleh saran subjek yang disajikan pada Tabel L9.1

Tabel L9.1. Keluhan Subjek yang menyatakan Distraksi

No  |  Bagian Sistem yang Mengganggu  |  Keluhan Subjek Eksperimen
1  |  Contoh kalimat pembuka/sentence starter  |  Sesaat setelah mengetik agak terganggu dengan teks AI yang muncul, yang membuat konsentrasi agak pecah untuk menulis yang ada dipikiran
2  |  Keseluruhan scaffolding utuh  |  Saran posisi rekomendasi fitur AI mungkin bisa di bagian bawah inputan. Karena ketika mengetik, fitur AI yang mulai bekerja otomatis menggulir halaman kebawah.
3  |  Peringatan diagnosis kekurangan narasi yang ditulis  |  karena kadang peringatannya terlalu cepat padahal masih mikir untuk nulis apa

Sebagai respons terhadap temuan tersebut, dilakukan modifikasi pada GUI-43 dan GUI-46 yang telah dimodelkan pada subbab L4.2.1G. Modifikasi yang dilakukan berupa transformasi contrainer scaffolding menjadi elemen collapsible yang dapat ditutup dan dibuka sesuai keinginan pengguna. Secara default, scafolding akan tertutup dan hanya menampilkan status dari empat indikator tekstual, sebagaimana disajikan pada Gambar L9.1. Dalam kondisi ini, tombol panah collapsible akan bercahaya untuk pertama kali sebagai upaya menarik perhatian pengguna untuk membuka gulir scaffolding. Jika mahasiswa menekan tombol collapsible, maka container scaffolding akan tetap terbuka meskipun pertanyaan berganti hingga tombol ditekan kembali, sebagaimana disajikan pada Gambar L9.2 Pendekatan antarmuka adaptif ini diterapkan untuk mengurangi potensi distraksi visual yang dilaporkan pengguna tanpa menghilangkan visibilitas terhadap status pemenuhan indikator rubrik.

Perlu dicatat bahwa modifikasi dilakukan setelah seluruh data eksperimen selesai dikumpulkan. Oleh karena itu, perubahan tersebut tidak memengaruhi hasil analisis yang digunakan untuk menjawab research question, melainkan berfungsi sebagai tindak lanjut desain berdasarkan masukan subjek eksperimen yang diperoleh selama eksperimen.

Gambar L9.1. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup

Gambar L9.2. Hasil Modifikasi GUI pada Kondisi Scaffolding Tertutup
