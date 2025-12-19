# AlphaFlow: Kerangka Kerja Analisis dan Prediksi Saham

AlphaFlow adalah sebuah kerangka kerja (*framework*) berbasis Python yang dirancang khusus untuk melakukan analisis data saham secara sistematis. Proyek ini memfasilitasi pengambilan data, pemrosesan awal, hingga pemodelan statistik untuk berbagai emiten di bursa saham dan menemukan insightnya.

---

## Struktur Proyek
Proyek ini menggunakan struktur direktori modular untuk memastikan skalabilitas dan kemudahan pemeliharaan kode:

* **`data/`**: Menyimpan dataset mentah dan hasil pemrosesan dalam format CSV.
* **`models/`**: Direktori penyimpanan untuk model *machine learning* yang telah dilatih (.pkl).
* **`notebooks/`**: Digunakan untuk eksperimen data, analisis eksploratif (EDA), dan visualisasi.
* **`src/`**: Berisi kode sumber utama berupa fungsi-fungsi Python yang dapat digunakan kembali untuk berbagai analisis saham.

---

## Fitur Utama
- **Pengambilan Data Otomatis**: Integrasi dengan API Yahoo Finance untuk mendapatkan data harga historis.
- **Pemrosesan Data**: Pembersihan data otomatis dan perhitungan *return* harian.
- **Arsitektur Modular**: Pemisahan antara logika bisnis (pada direktori `src`) dan implementasi analisis (pada direktori `notebooks`).

---

## Instalasi
1. Klon repositori ini.
2. Instal pustaka yang diperlukan: pip install yfinance pandas scikit-learn dan lain-lain. Simpan di venv.
3. Jalankan skrip melalui direktori notebooks/.

---

## Tags
`Python` `Data Science` `Framework`

---

*Author:* [@g3raldatsc](https://github.com/g3raldatsc)
<p align="center">
  <img src="https://media.tenor.com/8b2-2a17wIAAAAAM/wow-world-of-warcraft.gif" width="200" alt="Anime Gif">
</p>
