# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

1. Tingginya angka dropout siswa (32.1% dari total siswa) yang merugikan reputasi dan keberlanjutan institusi.
2. Belum adanya sistem deteksi dini untuk mengidentifikasi siswa yang berpotensi dropout.
3. Kurangnya pemahaman mengenai faktor-faktor utama yang mempengaruhi keputusan siswa untuk dropout.

### Cakupan Proyek

1. Analisis eksplorasi data (EDA) untuk memahami karakteristik siswa dropout vs graduate vs enrolled.
2. Pembangunan model machine learning (Random Forest & Gradient Boosting) untuk prediksi dropout.
3. Pembuatan business dashboard untuk monitoring performa siswa.
4. Deployment prototype sistem prediksi menggunakan Streamlit.

### Persiapan

Sumber data: [UCI Machine Learning Repository - Predict students' dropout and academic success](https://doi.org/10.24432/C5MC89)

Setup environment:

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan Streamlit app
streamlit run app.py
```

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** untuk membantu Jaya Jaya Institut dalam memahami data dan memonitor performa siswa. Dashboard menampilkan:
- Distribusi status siswa (Dropout, Enrolled, Graduate) dalam bentuk pie chart
- Tingkat dropout berdasarkan gender (stacked bar chart)
- Pengaruh beasiswa terhadap status siswa (stacked bar chart)
- Pengaruh pembayaran SPP terhadap status siswa (stacked bar chart)
- Rata-rata nilai per semester berdasarkan status (bar chart)
- Rata-rata mata kuliah lulus per status (bar chart)
- Distribusi usia saat enrollment per status (stacked bar chart)
- Distribusi nilai masuk (admission grade) per status (stacked bar chart)
- Ringkasan jumlah siswa Dropout, Graduate, dan Enrolled (scalar cards)

### Akses Dashboard Metabase

- **Email**: `root@mail.com`
- **Password**: `root123`

File database Metabase (`metabase.db.mv.db`) telah disertakan dalam repositori ini. Untuk menjalankan dashboard:

```bash
# Jalankan Metabase menggunakan Docker
docker run -d -p 3000:3000 \
  -v $(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db \
  -e "MB_DB_FILE=/metabase.db/metabase.db" \
  --name metabase metabase/metabase:v0.46.6.4
```

Kemudian akses dashboard di `http://localhost:3000/dashboard/2`.

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning dibuat menggunakan Streamlit. Untuk menjalankan prototype:

```bash
# 1. Pastikan semua dependencies terinstal
pip install -r requirements.txt

# 2. Jalankan aplikasi Streamlit
streamlit run app.py
```

Cara penggunaan:
1. Isi data siswa pada sidebar (informasi demografis, akademik, finansial, dan performa semester).
2. Klik tombol "Prediksi" untuk melihat hasil prediksi.
3. Sistem akan menampilkan status prediksi (Dropout/Enrolled/Graduate) beserta probabilitasnya.

## Conclusion

Berdasarkan analisis yang telah dilakukan, diperoleh kesimpulan sebagai berikut:

1. **Tingkat Dropout**: Dari 4.424 siswa, 32.1% (1.421 siswa) mengalami dropout, 17.9% (794 siswa) masih enrolled, dan 49.9% (2.209 siswa) berhasil graduate.

2. **Faktor Utama Dropout**: Faktor yang paling berpengaruh terhadap status dropout siswa adalah:
   - **Performa akademik semester 1 & 2**: Jumlah mata kuliah yang lulus (approved) dan nilai rata-rata (grade) di kedua semester merupakan indikator terkuat. Siswa dropout cenderung memiliki jumlah MK lulus yang sangat rendah (median 0-2 MK).
   - **Status pembayaran SPP (Tuition fees)**: 87% siswa yang tidak membayar SPP tepat waktu mengalami dropout.
   - **Usia saat enrollment**: Siswa yang lebih tua saat mendaftar memiliki risiko dropout yang lebih tinggi.
   - **Admission grade**: Siswa dengan nilai masuk yang lebih rendah cenderung memiliki risiko dropout lebih tinggi.

3. **Model Machine Learning**: Random Forest Classifier dipilih sebagai model terbaik dengan accuracy 77.7%. Model ini mampu mengidentifikasi siswa dropout dengan precision 81% dan recall 77%.

4. **Perbedaan Gender**: Siswa laki-laki memiliki tingkat dropout yang lebih tinggi (45%) dibandingkan siswa perempuan (25%).

5. **Pengaruh Beasiswa**: Penerima beasiswa memiliki tingkat dropout yang jauh lebih rendah (~10%) dibandingkan non-penerima beasiswa (~39%).

### Rekomendasi Action Items

Berikut adalah rekomendasi action items yang harus dilakukan Jaya Jaya Institut:

1. **Implementasi Sistem Early Warning**: Terapkan model prediksi dropout ini sebagai sistem peringatan dini. Siswa yang diprediksi dropout harus segera diidentifikasi di awal semester untuk diberikan intervensi khusus.

2. **Program Bimbingan Akademik Intensif**: Fokuskan bimbingan pada siswa yang memiliki jumlah mata kuliah lulus rendah di semester 1. Data menunjukkan bahwa performa semester awal sangat menentukan keberhasilan siswa.

3. **Bantuan Finansial dan Monitoring Pembayaran**: Berikan perhatian khusus pada siswa yang menunggak pembayaran SPP karena 87% dari mereka berakhir dropout. Pertimbangkan program cicilan atau bantuan keuangan darurat.

4. **Perluasan Program Beasiswa**: Tingkatkan cakupan program beasiswa karena data menunjukkan penerima beasiswa memiliki tingkat kelulusan yang jauh lebih tinggi.

5. **Program Mentoring untuk Siswa Laki-laki**: Berikan program mentoring khusus untuk siswa laki-laki yang memiliki risiko dropout lebih tinggi, termasuk dukungan akademik dan psikososial.

6. **Monitoring Intensif Siswa Usia Lebih Tua**: Siswa yang mendaftar di usia lebih tua memerlukan perhatian khusus karena mereka mungkin memiliki tanggung jawab lain (pekerjaan, keluarga) yang bersaing dengan studi mereka.