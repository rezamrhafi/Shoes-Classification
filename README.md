# Klasifikasi Sepatu - ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-FF6F20?style=for-the-badge&logo=TensorFlow&logoColor=white)

Repositori ini berisi proyek segmentasi bentuk sepatu berdasarkan brand menggunakan teknik Deep Learning dan Computer Vision. Proyek ini bertujuan untuk menganalisis bentuk brand sepatu dan mengkategorikan brand sepatu yang sesuai berdasarkan analisis tersebut. Repositori ini mencakup file Jupyter Notebook yang menjelaskan proses secara menyeluruh, mulai dari eksplorasi data hingga penerapan model deep learning.

---

## Link Terkait Project ⛓️‍💥

- [Dataset](https://www.kaggle.com/datasets/die9origephit/nike-adidas-and-converse-imaged)
- [Deployment](https://huggingface.co/spaces/RezaMRhafi/GC7)

---

## Project Overview 📝

Dalam proyek ini, saya menggunakan teknik Deep Learning untuk menganalisis bentuk wajah pengguna dan merekomendasikan kacamata yang sesuai. Beberapa langkah utama yang dicakup dalam proyek ini adalah:

1. **Import Libraries dan Eksplorasi Data**:
    - Memuat dataset dan melakukan eksplorasi awal untuk memahami struktur dan karakteristik data.

2. **Preprocessing Data**:
    - Melakukan pembersihan dan persiapan data, termasuk penanganan gambar dan normalisasi.

3. **Training Base Model**:
    - Membangun dan melatih model deep learning untuk mengidentifikasi bentuk sepatu.

4. **Evaluasi Base Model**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

5. **Tuning Model**:
    - Membangun dan melatih model deep learning dengan beberapa hyperparameter tuning untuk mengidentifikasi bentuk sepatu.

6. **Evaluasi Model yang Dituning**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

7. **Pengambilan Keputusan**:
    - Mengambil keputusan terhadap performa model.
  

## Latar Belakang Masalah 🧐
alam industri retail, proses penerimaan barang di gudang merupakan tahap krusial dalam manajemen rantai pasokan. Kesalahan dalam identifikasi produk, khususnya sepatu dengan merek tertentu seperti Converse, Nike, dan Adidas, dapat menyebabkan ketidaktepatan dalam pencatatan stok, distribusi, serta pelayanan pelanggan. Oleh karena itu, diperlukan sistem otomatis yang mampu mengenali brand sepatu berdasarkan gambar guna meningkatkan efisiensi dan akurasi dalam operasional gudang.

Dalam upaya mengatasi permasalahan tersebut, sebuah model klasifikasi berbasis kecerdasan buatan dikembangkan untuk mengidentifikasi merek sepatu secara otomatis dari citra produk yang diterima di gudang. Model ini dibangun dengan pendekatan pembelajaran mesin menggunakan TensorFlow dan diuji dengan dua metode: tanpa augmentasi data dan dengan augmentasi data. Augmentasi data digunakan untuk meningkatkan variasi dalam dataset guna membuat model lebih robust terhadap berbagai kondisi pencahayaan, sudut, dan latar belakang.

Model terbaik, yakni model dengan augmentasi data, akan digunakan dalam tahap deployment guna memastikan akurasi yang optimal dalam kondisi nyata di gudang. Dengan penerapan model ini, diharapkan proses identifikasi produk menjadi lebih cepat, mengurangi kesalahan manusia, serta meningkatkan efisiensi operasional perusahaan.
  
## Metode yang Digunakan 🛠️

- Deep Learning
- Computer Vision
- Klasifikasi Gambar
- Visualisasi Data

## Kesimpulan 💡
- setelah model dicobakan dengan inference, model masih sering salah dalam mebedakan antara sepatu adidas dan nike. untuk sepatu converse model lebih mudah untuk mengenalinya. 
- dari 3 optimizer, adamax adalah optimizer yang paling optimal untuk dataset ini daripada menggunakan adam dan nadam.
- model menjadi tidak bagus ketika parameter augmentasi yang terlalu ekstrim dikarenakan model sulit untuk membedakan tiap class.
- menggunakan layer yang terlalu banyak dapat mengurangi akurasi model dalam memprediksi suatu class
- apabila kebanyakan epoch, model dapat menjadi overfit 
- tanpa adanya augmentasi, model akan menjadi sangat overfit




