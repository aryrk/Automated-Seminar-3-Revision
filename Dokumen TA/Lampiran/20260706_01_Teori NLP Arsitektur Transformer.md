TEORI NATURAL LANGUAGE PROCESSING DAN
ARSITEKTUR TRANSFORMER
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
DAFTAR RUMUS ............................................................................................... iii
BAB I NLP DAN ARSITEKTUR TRANSFORMER......................................... 4
I.1 Natural Language Processing (NLP) dan Arsitektur Transformer ................ 4
I.1.1 Vector Embedding Sebagai Representasi ............................................... 6
I.1.2 Cosine Similiarity untuk Eksploitasi Ruang Vektor ............................... 8
I.1.3 Landasan Komputasional ........................................................................ 9
I.1.4 Metrik Evaluasi Kinerja Model dan Kalibrasi Threshold ..................... 11
DAFTAR PUSTAKA ........................................................................................... 13
i

DAFTAR GAMBAR
Gambar I.1. Arsitektur SBERT untuk Regresi Teks 5
Gambar I.2. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder 6
Gambar I.3. Rerpesentasi Ruang Vektor 7
Gambar I.4. Cosine Similarity dalam Ruang Vektor 8
Gambar I.5. Representasi Pipeline Penelitian 10
Gambar I.6. Balancing Preccision dan Recall untuk F1-Score 12
ii

DAFTAR RUMUS
Pemetaan Ruang Vektor .......................................................................................... 6
Rumus Cosine Similiarity ....................................................................................... 8
Rumus Pipeline Penelitan ....................................................................................... 9
Formula F1 Score .................................................................................................. 11
Formula Precission ................................................................................................ 11
Formula Recall ...................................................................................................... 11
iii

BAB I
NLP DAN ARSITEKTUR TRANSFORMER
Lampiran ini menyajikan landasan teoretis komprehensif mengenai Natural
Language Processing (NLP) dan arsitektur Transformer yang menjadi dasar
komputasional dalam penelitian. Penjabaran pada lampiran ini difokuskan pada
aspek teknis model semantic embedding dan metrik evaluasi kinerja.
I.1 Natural Language Processing (NLP) dan Arsitektur Transformer
Natural Language Processing (NLP) merupakan bagian dari ilmu komputer dan
artificial intelligence yang memungkinkan mesin untuk memahami, memproses,
dan menganalisis bahasa alami yang digunakan manusia (C. Manning & Hinrich,
1999), seperti yang dikutip oleh Torfi et al. (2021). Salah satu komponennya adalah
Natural Language Understanding (NLU), yang berfokus pada ekstraksi makna
semantik dari teks sehingga sistem dapat menginterpretasikan isi bahasa secara
komputasional.
Perkembangan NLP didorong oleh penggunaan arsitektur transformer, yang
memungkinkan pembentukan representasi teks yang bersifat kontekstual melalui
mekanisme pemrosesan yang mempertimbangkan hubungan antar elemen dalam
satu sequence secara menyeluruh (Vaswani et al., 2023). Arsitektur ini menjadi
dasar bagi berbagai model embedding pre-trained, termasuk Sentence Bidirectional
Encoder Representations from Transformers (SBERT) (Reimers & Gurevych,
2019), yang memanfaatkan pemahaman dua arah untuk menangkap hubungan
kontekstual dalam teks, dengan Gambar I.1 menggambarkan arsitektur SBERT Commented [AR1]: (Dilingkari)
-Bu Ani
untuk mencari kesamaan dalam dua teks.
Commented [AR1R2]: I guess wordnya aneh, gambar
menggambarkan
4

Gambar I.1. Arsitektur SBERT untuk Regresi Teks
Dalam implementasinya, terdapat dua pendekatan utama dalam pemrosesan
pasangan teks, yaitu cross-encoder dan bi-encoder. Pendekatan cross-encoder
memproses dua teks secara bersamaan sehingga memungkinkan interaksi penuh
antar token, namun memiliki kompleksitas komputasi yang tinggi. Sebaliknya,
pendekatan bi-encoder merepresentasikan setiap teks secara independen ke dalam
ruang vektor yang sama, sehingga memungkinkan perbandingan semantik
dilakukan secara efisien tanpa memerlukan pemrosesan ulang terhadap seluruh
pasangan teks (Devlin et al., 2019; T. Gao et al., 2022; Reimers & Gurevych, 2019).
Ilustrasi kedua pendekatan tersebut disajikan pada Gambar I.2.
5

Gambar I.2. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder
Dalam penelitian ini, komponen NLU diimplementasikan melalui pendekatan
berbasis bi-encoder untuk menghasilkan representasi vektor (embedding) dari teks
yang lebih lanjut dijelaskan pada subbab I.1.1. Representasi ini kemudian
digunakan untuk mengukur hubungan semantik antar teks secara kuantitatif.
Kesamaan semantik antara dua teks diukur menggunakan cosine similarity yang
dijelaskan lebih lanjut pada subbab I.1.2. Pendekatan ini memungkinkan sistem
membandingkan makna narasi feedback mahasiswa dengan deskripsi kriteria secara
matematis terlepas dari perbedaan kata yang digunakan, dan hasilnya digunakan
sebagai dasar dalam mekanisme pengambilan keputusan berbasis semantik dalam
sistem.
I.1.1 Vector Embedding Sebagai Representasi
Fondasi komputasional dari pemahaman semantik teks adalah representasi teks
sebagai vektor dalam ruang berdimensi. Secara formal, diberikan suatu teks (cid:1)
sebuah fungsi representasi (cid:2) memetakan teks tersebut ke dalam ruang vektor
(cid:3)
berdimensi (cid:4), dipetakan pada rumus I.1.
(cid:2) (cid:3)(cid:5)(cid:1)(cid:6)→ℝ(cid:9) ( I.1)
Prinsip dasar dari pendekatan ini berakar pada distributional hypothesis bahwa
kata-kata atau ekspresi yang muncul dalam konteks serupa cenderung memiliki
6

makna yang berdekatan (Harris, 1954). Gambar I.3 merepresentasikan bagaimana
teks feedback dalam penelitian ini disimpan ke dalam representasi vektor
menggunakan model embedding, narasi "Iklan yang dikumpulkan amir
dikumpulkan dari platform yang beragam" dilakukan transformasi menjadi nilai
matematis berupa koordinat dalam ruang vektor.
Gambar I.3. Rerpesentasi Ruang Vektor
Transformasi ini mengubah data teks yang bersifat simbolik menjadi data numerik.
Tanpa representasi vektor, sistem tidak dapat melakukan operasi matematika untuk
mengukur semantic similarity. Dengan representasi ini, narasi “Sangat baik” dan
“Luar biasa” akan memiliki posisi koordinat yang berdekatan dalam ruang vektor.
Sebagai contoh, jika terdapat narasi (cid:10)=”Rekan saya berhasil mengumpulkan 30
data iklan”, maka fungsi (cid:2) akan melakukan transformasi teks menjadi sebuah
(cid:3)
koordinat vektor seperti [0.12,−0.45,…,0.89] dengan panjang dimensi (cid:4)=1024
tergantung pada arsitektur model yang digunakan.
Representasi vektor memiliki properti yang tidak dimiliki representasi simbolik di
mana ia memungkinkan pengukuran gradasi kemiripan antar konsep. Dalam
penelitian ini, fungsi representasi diimplementasikan menggunakan model pre-
trained yang parameternya tidak dimodifikasi selama pipeline beroperasi.
Konsekuensinya, kualitas representasi semantik yang dihasilkan termasuk sejauh
mana vektor narasi mahasiswa dapat dibandingkan secara bermakna dengan vektor
deskripsi rubrik sepenuhnya bergantung pada geometri ruang yang telah dikodekan
7

model selama pre-training. Pilihan model pre-trained yang tepat menjadi
keputusan desain kritis dalam penelitian ini dan dibahas lebih lanjut pada Bab IV.
I.1.2 Cosine Similiarity untuk Eksploitasi Ruang Vektor
Cosine similarity mengukur sudut antara dua vektor tanpa bergantung pada
magnitudonya (C. D. Manning et al., 2009). Formula cosine similarity disajikan
pada Rumus I.2.
(cid:25)(cid:26)(cid:27)(cid:28)(cid:29)
(cid:30)
,(cid:29)
(cid:31)
=
"#(cid:5)$%(cid:6) . "#(cid:5)$&(cid:6)
( I.2)
'|"#(cid:5)$%(cid:6)|'.)'"#(cid:5)$&(cid:6)')
Di mana (cid:2) merupakan fungsi embedding yang didefinisikan pada subbab I.1.1.
(cid:3)
Nilai akhir similarity berada dalam rentang [-1,1], Invarians terhadap magnitude
menjadikannya lebih robust untuk teks dengan panjang berbeda dibandingkan
dengan Euclidean distance karena komponen yang diukur adalah arah/orientasi
maknanya dalam ruang vektor (C. D. Manning et al., 2009). Cosine similarity
mengeksploitasi properti ruang vektor yang sudah terstruktur secara semantik
(Weinberger & Saul, 2009).
Contoh penggunaan rumus disajikan pada Gambar I.4, dua teks dalam ruang vektor
dapat dikomputasi menggunakan cosine similarity untuk mengukur derajat sudut
yang menentukan persentase similarity terhadap teks tersebut.
Gambar I.4. Cosine Similarity dalam Ruang Vektor
8

Dalam penelitian ini, cosine similarity digunakan sebagai alat ukur objektif untuk
menentukan apakah sebuah feedback telah mencakup aspek yang diminta oleh
rubrik. Sebagai contoh, terdapat dua vektor hasil embedding, yaitu vektor narasi
mahasiswa ((cid:25) ) dan vektor deskripsi rubrik (, ), jika hasil perhitungan rumus I.2
*+* (cid:30),(cid:31)
mendekati nilai 1, misalnya 0,92, maka kedua teks tersebut dianggap memiliki
semantic similarity yang sangat tinggi. Sebaliknya, jika mendekati 0, misalnya 0,15,
maka narasi mahasiswa dianggap tidak berkaitan dengan kriteria rubrik tersebut.
I.1.3 Landasan Komputasional
Komponen embedding dan cosine similiarity yang telah dijabarkan pada subbab
I.1.1 dan I.1.2 menghasilkan sinyal numerik berupa nilai similiarity antar dua unit
teks. Subbab ini menjelaskan bagaimana sinyal tersebut berfungsi sebagai basis Commented [AR2]: (Digarisbawahi)
- Bu Ani
inferensi yaitu bagaimana nilai kontinu yang dihasilkan ruang vektor dapat di
transformasikan menjadi sebuah keputusan.
Nilai similiarity yang dihasilkan merupakan ukuran angular closeness atau sudut
orientasi dalam ruang representasi vektor untuk memprediksi kemiripan.
Transformasi dari kedekatan ini menjadi keputusan yang dapat ditindaklanjuti
memerlukan tambahan yang dibangun di atas lapisan embedding. Alur transformasi
dinyatakan pada
(cid:1)→(cid:29)
+
→(cid:25)(cid:26)(cid:27)(cid:28)(cid:29)
+
,(cid:29)
"%
→- ( I.3)
Dengan contoh penggunaan,
1. (cid:1): Mahasiswa menulis narasi “Data diambil dari LinkedIn”.
1. (cid:29) : Teks diubah menjadi vektor [0.11,0.54,…].
+
2. (cid:25)(cid:26)(cid:27)(cid:5)(cid:29) ,(cid:29) (cid:6): Vektor dibandingkan dengan vektor kriteria rubrik ((cid:29) )
. "% "%
“Keragaman Platform”, menghasilkan similarity score 0,87.
3. -: Karena skor 0,87 ≥ threshold (misalnya 0,84), maka sistem mengambil
keputusan (-) bahwa kriteria tersebut terpenuhi.
9

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

| Di mana teks (cid:1) dipetakan menjadi representasi vektor (cid:29) |     |     |     | , dibandingkan dalam  |     |
| ------------------------------------------------------------------- | --- | --- | --- | --------------------- | --- |
+
| ruang yang sama pada vektor (cid:29) |     | , dan menghasilkan suatu keputusan (-) yang  |     |     |     |
| ------------------------------------ | --- | -------------------------------------------- | --- | --- | --- |
"%
| bergantung  pada  | mekanisme  | yang  akan  dibangun  | diatasnya  | sehingga  | dapat  |
| ----------------- | ---------- | --------------------- | ---------- | --------- | ------ |
dikatakan bahwa komponen embedding hanya bertugas menghasilkan sinyal dan
interpretasi atas sinyal merupakan tanggung jawab lapisan sistem yang lebih tinggi.

Rumus ini merepresentasikan pipeline evaluasi semantik dalam sistem, yaitu
mencakup indikator cakupan rubrik, koherensi skor-narasi, dan relevansi topik.
Indikator kedalaman elaborasi tidak melalui transformasi ruang vektor ini karena
dievaluasi secara independen menggunakan aturan heuristik berbasis jumlah kata.
Kegunaannya adalah untuk menunjukkan bahwa komponen embedding hanya
bertugas menghasilkan sinyal, sementara keputusan akhir (-) untuk memicu atau
tidak memicu scaffolding merupakan tanggung jawab lapisan logika sistem yang
| membandingkan  | sinyal  tersebut  | dengan  threshold  | tertentu.  | Alur  | komputasi  |
| -------------- | ----------------- | ------------------ | ---------- | ----- | ---------- |
komponen dalam penelitian ini disajikan pada Gambar I.5.

Gambar I.5. Representasi Pipeline Penelitian

| Properti ini  | menilai  kualitas inferensi  | yang  dihasilkan  |             | dibatasi  oleh  | kualitas  |
| ------------- | ---------------------------- | ----------------- | ----------- | --------------- | --------- |
| representasi  | yang  dihasilkan             | model,  sehingga  | diperlukan  | pemilihan       | model     |
embedding yang akan dikalibrasi pada data aktual. Selain itu pendekatan ini
memiliki batasan interpretabilitas. Representasi vektor yang dihasilkan bersifat
laten dan tidak memiliki padanan linguistik eksplisit pada tingkat token atau frasa
(Senel et al., 2018) . Keterbatasan ini diterima sebagai konsekuensi yang dapat
dikelola selama sinyal yang dihasilkan menunjukkan keselarasan yang memadai
dengan penilaian manusia pada data anotasi yang dievaluasi melalui F1 score pada
subbab I.1.4.

10

I.1.4 Metrik Evaluasi Kinerja Model dan Kalibrasi Threshold
Dalam klasifikasi teks pada NLP, terutama pada dataset yang memiliki class
imbalance, penggunaan F1-Score menjadi metrik utama untuk mengevaluasi
kinerja model. F1-Score merupakan harmonic mean dari precission dan recall
menggunakan I.4 (Riyanto et al., 2023) yang diilustrasikan pada Gambar I.6.
Precision mengukur ketepatan model dalam memprediksi kelas positif dari
keseluruhan hasil yang diprediksi positif oleh sistem, sedangkan Recall mengukur
banyaknya kelas positif yang dideteksi dengan benar, dibandingkan dengan total
data positif yang sebenarnya.
2 × 7452(cid:26)(cid:25)(cid:25)(cid:26)38 × 952:;;
01 12345=
( I.4)
7452(cid:26)(cid:25)(cid:25)(cid:26)38+952:;;
Dimana precission merupakan ukuran untuk mengukur akurasi prediksi yang benar
menggunakan rumus I.5.
(cid:10)7
7452(cid:26)(cid:25)(cid:25)(cid:26)38=
( I.5)
(cid:10)7+07
Sementara recall mengukur kemampuan untuk menemukan semua kemungkinan
prediksi yang benar menggunakan rumus I.6.
(cid:10)7
952:;;=
( I.6)
(cid:10)7 + 0=
Dengan, Commented [AR3]: , keterangan
1. (cid:10)7 atau true positive merupakan jumlah label “TRUE” yang diidentifikasi - Bu Ani
dengan benar.
2. 07 atau false positive adalah jumlah label “FALSE”, namun diidentifikasi
sebagai “TRUE”.
3. 0= atau false negative adalah jumlah label “TRUE”, namun diidentifikasi
sebagai “FALSE”.
11

Gambar I.6. Balancing Preccision dan Recall untuk F1-Score
Dalam skenario multi-label classification berbasis pasangan narasi dan kriteria pada
penelitian ini, evaluasi F1-Score dilakukan menggunakan kerangka micro-
averaging, di mana setiap pasangan diperlakukan secara setara tanpa diberikan
bobot berbeda (Sokolova & Lapalme, 2009). Pendekatan ini dipilih karena
distribusi pasangan antar aspek rubrik tidak seimbang, sehingga aspek rubrik
dengan kriteria yang lebih banyak akan menghasilkan pasangan kriteria evaluasi
yang lebih banyak.
Lebih lanjut, dalam arsitektur digital scaffolding, F1-Score merupakan nilai acuan
utama yang digunakan untuk melakukan kalibrasi threshold. Karena nilai cosine
similarity yang dihasilkan oleh representasi vector embedding berupa nilai kontinu,
sistem memerlukan mekanisme untuk menetapkan batas diskrit yang menentukan
apakah suatu feedback memerlukan intervensi prompt atau tidak. Melalui
pendekatan eksperimen optimasi seperti metode F1 sweep, untuk mencari threshold
optimal yang memaksimalkan nilai F1-Score pada data anotasi (X. Gao et al.,
2025).
12

13
DAFTAR PUSTAKA
Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding.
http://arxiv.org/abs/1810.04805
Gao, T., Yao, X., & Chen, D. (2022). SimCSE: Simple Contrastive Learning of
Sentence Embeddings. http://arxiv.org/abs/2104.08821
Gao, X., Member, S., Xie, D., Zhang, Y., Wang, Z., Chen, C., He, C., Yin, H.,
Member, S., & Zhang, W. (2025). A Comprehensive Survey on Imbalanced
Data Learning. https://doi.org/10.1007/s11704-025-50274-7
Harris, Z. S. (1954). Distributional Structure. WORD, 10(2–3), 146–162.
https://doi.org/10.1080/00437956.1954.11659520
Manning, C. D., Raghavan, P., & Schütze, H. (2009). An Introduction to
Information Retrieval. https://nlp.stanford.edu/IR-
book/pdf/irbookonlinereading.pdf
Manning, C., & Hinrich, S. (1999). Foundations of statistical natural language
processing (C. Manning & S. Hinrich, Eds.). MIT Press.
Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using
Siamese BERT-Networks. http://arxiv.org/abs/1908.10084
Riyanto, S., Sitanggang, I. S., Djatna, T., & Atikah, T. D. (2023). Comparative
Analysis using Various Performance Metrics in Imbalanced Data for Multi-
class Text Classification. In IJACSA) International Journal of Advanced
Computer Science and Applications (Vol. 14, Number 6).
http://gcancer.org/pdr
Senel, L. K., Utlu, I., Yucesoy, V., Koc, A., & Cukur, T. (2018). Semantic Structure
and Interpretability of Word Embeddings.
https://doi.org/10.1109/TASLP.2018.2837384
Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance
measures for classification tasks. Information Processing & Management,
45(4), 427–437. https://doi.org/10.1016/J.IPM.2009.03.002

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

Torfi, A., Shirvani, R. A., Keneshloo, Y., Tavaf, N., & Fox, E. A. (2021). Natural
| Language  | Processing  Advancements  | By  Deep  | Learning:  | A  Survey.  |
| --------- | ------------------------- | --------- | ---------- | ----------- |
http://arxiv.org/abs/2003.01200
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
| Kaiser,  | L.,  &  Polosukhin,  | I.  (2023).  Attention  | Is  All  You  | Need.  |
| -------- | -------------------- | ----------------------- | ------------- | ------ |
http://arxiv.org/abs/1706.03762
Weinberger, K. Q., & Saul, L. K. (2009). Distance Metric Learning for Large
Margin Nearest Neighbor Classification. In Journal of Machine Learning
Research (Vol. 10).

14
