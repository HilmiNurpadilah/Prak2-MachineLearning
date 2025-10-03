# 🐍 Virtual Environment Guide

## 📋 Status Saat Ini

### ❌ Sebelumnya: Tidak Ada venv
- Project berjalan dengan Python global
- Dependencies terinstall di sistem global
- Risiko konflik dependencies

### ✅ Sekarang: Virtual Environment Tersedia
- Folder `venv/` telah dibuat
- Script helper untuk setup dan running
- Isolasi dependencies yang aman

## 🚀 Cara Menggunakan Virtual Environment

### 1. Setup Virtual Environment (Sekali Saja)
```bash
# Method 1: Gunakan script helper
setup_venv.bat

# Method 2: Manual
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 2. Menjalankan Aplikasi dengan venv
```bash
# Method 1: Gunakan script helper
run_with_venv.bat

# Method 2: Manual
venv\Scripts\activate.bat
python app.py
deactivate
```

### 3. Development dengan venv
```bash
# Aktifkan venv
venv\Scripts\activate.bat

# Install package baru
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt

# Deactivate
deactivate
```

## 📁 Struktur Project dengan venv

```
TA-02/
├── venv/                  # ✅ Virtual environment
│   ├── Scripts/
│   ├── Lib/
│   └── pyvenv.cfg
├── app.py
├── model_mpg_berat.pkl
├── requirements.txt
├── setup_venv.bat        # ✅ Setup script
├── run_with_venv.bat     # ✅ Run script
├── run_app.bat          # ✅ Run without venv
└── templates/
```

## 🔧 Script Helper

### setup_venv.bat
- Membuat virtual environment
- Mengaktifkan venv
- Install semua dependencies
- Siap untuk development

### run_with_venv.bat
- Mengaktifkan virtual environment
- Menjalankan Flask app
- Deactivate otomatis saat selesai

### run_app.bat (Tanpa venv)
- Menjalankan app dengan Python global
- Untuk testing cepat

## 🚀 Deployment ke Railway

### Dengan Virtual Environment
Railway akan otomatis:
1. Detect Python project
2. Create virtual environment
3. Install dependencies dari `requirements.txt`
4. Run aplikasi dengan gunicorn

### File yang Diperlukan
- ✅ `requirements.txt` - Dependencies
- ✅ `Procfile` - Railway process
- ✅ `railway.json` - Railway config
- ✅ `app.py` - Production ready

## 🎯 Rekomendasi Workflow

### Development
```bash
# 1. Setup venv (sekali saja)
setup_venv.bat

# 2. Development
venv\Scripts\activate.bat
# ... coding ...
deactivate

# 3. Run app
run_with_venv.bat
```

### Production (Railway)
```bash
# 1. Test locally
run_with_venv.bat

# 2. Push to Git
git add .
git commit -m "Update with venv"
git push origin main

# 3. Railway auto-deploy
```

## ⚠️ Important Notes

### Git Repository
- `venv/` folder **TIDAK** di-commit ke Git
- Railway akan create venv sendiri saat deployment
- Local development tetap menggunakan venv

### Dependencies
- Selalu update `requirements.txt` setelah install package baru
- Railway menggunakan `requirements.txt` untuk install dependencies
- Virtual environment di Railway terpisah dari local

### Best Practices
1. **Development**: Selalu gunakan venv
2. **Testing**: Test dengan dan tanpa venv
3. **Deployment**: Railway handle venv otomatis
4. **Dependencies**: Keep `requirements.txt` updated

## 🐛 Troubleshooting

### venv tidak aktif
```bash
# Error: 'venv' is not recognized
# Solution: Pastikan folder venv ada
dir venv
```

### Dependencies tidak terinstall
```bash
# Error: ModuleNotFoundError
# Solution: Aktifkan venv dan install
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Railway deployment gagal
```bash
# Check requirements.txt
# Pastikan semua dependencies ada
# Railway akan create venv sendiri
```

---

## 🎉 Summary

**Status**: ✅ Virtual Environment siap digunakan!

**Next Steps**:
1. Run `setup_venv.bat` untuk setup
2. Use `run_with_venv.bat` untuk development
3. Deploy ke Railway dengan confidence!

**Benefits**:
- ✅ Isolasi dependencies
- ✅ Reproducible environment
- ✅ Production-ready deployment
- ✅ No conflicts dengan system Python
