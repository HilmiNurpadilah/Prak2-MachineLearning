# Aplikasi Prediksi Efisiensi Bahan Bakar (MPG)

Aplikasi web Flask untuk memprediksi efisiensi bahan bakar mobil berdasarkan berat kendaraan menggunakan model machine learning regresi linear.

## 🚗 Fitur

- **Prediksi MPG**: Masukkan berat mobil untuk mendapatkan prediksi efisiensi bahan bakar
- **Interface Modern**: Desain responsif dengan Bootstrap 5
- **API Endpoint**: Endpoint untuk integrasi dengan aplikasi lain
- **Validasi Input**: Validasi data input untuk memastikan akurasi prediksi
- **Interpretasi Hasil**: Kategorisasi hasil prediksi (rendah/sedang/tinggi)

## 📊 Model Machine Learning

- **Algoritma**: Linear Regression
- **Dataset**: Auto MPG Dataset (392 sampel)
- **Akurasi**: R² = 0.6533, RMSE = 4.2064
- **Rumus**: MPG = 47.2005 + (-0.0079 × Berat Mobil)

## 🛠️ Teknologi

- **Backend**: Python Flask
- **ML Library**: scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib

## 📋 Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package installer)

## 🚀 Instalasi dan Menjalankan

### 1. Clone atau Download Project
```bash
# Jika menggunakan git
git clone <repository-url>
cd TA-02

# Atau download dan extract file project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Pastikan Model File Ada
Pastikan file `model_mpg_berat.pkl` ada di direktori project. File ini berisi model yang sudah dilatih.

### 4. Jalankan Aplikasi
```bash
python app.py
```

### 5. Akses Aplikasi
Buka browser dan kunjungi: `http://localhost:5000`

## 📱 Cara Penggunaan

### Interface Web
1. Buka aplikasi di browser
2. Masukkan berat mobil dalam pound (lbs)
3. Klik tombol "Prediksi MPG"
4. Lihat hasil prediksi dan interpretasinya

### API Endpoint
```bash
# Prediksi menggunakan API
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"weight": 3500}'
```

**Response:**
```json
{
  "success": true,
  "weight": 3500,
  "predicted_mpg": 19.55,
  "model_info": {
    "intercept": 47.2005,
    "coefficient": -0.0079
  }
}
```

## 📁 Struktur Project

```
TA-02/
├── app.py                 # Aplikasi Flask utama
├── model_mpg_berat.pkl    # Model machine learning
├── auto-mpg.csv          # Dataset training
├── requirements.txt       # Dependencies Python
├── README.md             # Dokumentasi
└── templates/            # Template HTML
    ├── base.html         # Template dasar
    ├── index.html        # Halaman utama
    └── about.html        # Halaman tentang
```

## 🔧 Konfigurasi

### Port dan Host
Aplikasi berjalan di:
- **Host**: 0.0.0.0 (semua interface)
- **Port**: 5000
- **Debug Mode**: Aktif (untuk development)

### Mengubah Konfigurasi
Edit file `app.py` pada bagian terakhir:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## 📊 Interpretasi Hasil

| MPG Range | Kategori | Warna |
|-----------|----------|-------|
| < 15 | Efisiensi Rendah | Merah |
| 15-25 | Efisiensi Sedang | Orange |
| ≥ 25 | Efisiensi Tinggi | Hijau |

## 🐛 Troubleshooting

### Model Tidak Ditemukan
```
Model tidak ditemukan! Pastikan file model_mpg_berat.pkl ada.
```
**Solusi**: Pastikan file `model_mpg_berat.pkl` ada di direktori yang sama dengan `app.py`

### Port Sudah Digunakan
```
Address already in use
```
**Solusi**: 
- Ganti port di `app.py`: `app.run(port=5001)`
- Atau matikan aplikasi yang menggunakan port 5000

### Dependencies Error
```
ModuleNotFoundError: No module named 'flask'
```
**Solusi**: Install dependencies dengan `pip install -r requirements.txt`

## 📈 Pengembangan Lebih Lanjut

### Fitur yang Bisa Ditambahkan
- [ ] Visualisasi grafik prediksi
- [ ] Export hasil ke PDF/Excel
- [ ] Multiple model comparison
- [ ] User authentication
- [ ] Database untuk menyimpan history prediksi
- [ ] Docker containerization

### Deployment
- **Heroku**: Tambahkan `Procfile` dan `runtime.txt`
- **AWS**: Gunakan Elastic Beanstalk atau EC2
- **Docker**: Buat `Dockerfile` untuk containerization

## 📝 Lisensi

Project ini dibuat untuk keperluan pembelajaran machine learning.

## 👨‍💻 Author

Dibuat untuk Tugas Akhir Machine Learning - Prediksi Efisiensi Bahan Bakar

---

**Happy Coding! 🚗💨**
