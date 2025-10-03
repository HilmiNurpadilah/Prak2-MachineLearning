# 🚀 Deployment Guide - Railway

Panduan lengkap untuk deploy aplikasi Flask Prediksi MPG ke Railway.

## 📋 Prasyarat

1. **Akun Railway**: Daftar di [railway.app](https://railway.app)
2. **Git Repository**: Pastikan project sudah di-push ke GitHub/GitLab
3. **Model File**: Pastikan `model_mpg_berat.pkl` ada di repository

## 🛠️ Persiapan Deployment

### 1. File yang Sudah Disiapkan

✅ **Procfile** - Konfigurasi untuk Railway
✅ **railway.json** - Konfigurasi deployment Railway
✅ **requirements.txt** - Dependencies dengan gunicorn
✅ **app.py** - Updated untuk production
✅ **.gitignore** - File yang diabaikan Git

### 2. Struktur Project untuk Railway

```
TA-02/
├── app.py                 # ✅ Flask app (production ready)
├── model_mpg_berat.pkl    # ✅ Model ML (harus ada!)
├── auto-mpg.csv          # ✅ Dataset
├── requirements.txt       # ✅ Dependencies + gunicorn
├── Procfile              # ✅ Railway process
├── railway.json          # ✅ Railway config
├── .gitignore            # ✅ Git ignore
├── README.md             # ✅ Documentation
├── DEPLOYMENT.md         # ✅ This file
└── templates/            # ✅ HTML templates
    ├── base.html
    ├── index.html
    └── about.html
```

## 🚀 Langkah-langkah Deployment

### Step 1: Push ke Git Repository

```bash
# Inisialisasi Git (jika belum)
git init

# Add semua file
git add .

# Commit
git commit -m "Initial commit: Flask MPG Prediction App"

# Add remote repository (GitHub/GitLab)
git remote add origin https://github.com/username/repository-name.git

# Push ke repository
git push -u origin main
```

### Step 2: Deploy ke Railway

1. **Login ke Railway**
   - Buka [railway.app](https://railway.app)
   - Login dengan GitHub/GitLab

2. **Create New Project**
   - Klik "New Project"
   - Pilih "Deploy from GitHub repo"
   - Pilih repository yang sudah di-push

3. **Configure Deployment**
   - Railway akan otomatis detect Python project
   - Pastikan build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

4. **Environment Variables** (Opsional)
   - `FLASK_ENV=production`
   - `PORT` (Railway akan set otomatis)

### Step 3: Verifikasi Deployment

1. **Check Logs**
   - Buka tab "Deployments"
   - Lihat build logs untuk memastikan tidak ada error

2. **Test Application**
   - Klik domain yang diberikan Railway
   - Test prediksi dengan berat mobil contoh (3500 lbs)

3. **API Testing**
   ```bash
   curl -X POST https://your-app.railway.app/api/predict \
     -H "Content-Type: application/json" \
     -d '{"weight": 3500}'
   ```

## 🔧 Konfigurasi Railway

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app:app",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Procfile
```
web: python app.py
```

## 📊 Monitoring & Maintenance

### 1. Railway Dashboard
- **Metrics**: CPU, Memory, Network usage
- **Logs**: Real-time application logs
- **Deployments**: History dan status deployment

### 2. Health Check
- Endpoint: `GET /`
- Railway otomatis check setiap 30 detik
- Jika gagal, Railway akan restart aplikasi

### 3. Scaling
- **Automatic**: Railway auto-scale berdasarkan traffic
- **Manual**: Bisa set resource limits di dashboard

## 🐛 Troubleshooting

### Build Errors

**Error: Model file not found**
```
Model tidak ditemukan! Pastikan file model_mpg_berat.pkl ada.
```
**Solusi**: Pastikan `model_mpg_berat.pkl` ada di root directory dan di-commit ke Git.

**Error: Module not found**
```
ModuleNotFoundError: No module named 'flask'
```
**Solusi**: Pastikan `requirements.txt` lengkap dan dependencies terinstall.

### Runtime Errors

**Error: Port binding**
```
Address already in use
```
**Solusi**: Railway akan handle port secara otomatis, pastikan kode menggunakan `os.environ.get('PORT')`.

**Error: Memory limit**
```
Process killed due to memory limit
```
**Solusi**: Upgrade plan Railway atau optimize model size.

### Performance Issues

**Slow response time**
- Check Railway metrics
- Consider caching predictions
- Optimize model loading

**High memory usage**
- Monitor model size
- Consider model compression
- Use lighter ML libraries

## 🔄 Update Deployment

### 1. Update Code
```bash
# Make changes to your code
git add .
git commit -m "Update: Add new features"
git push origin main
```

### 2. Railway Auto-Deploy
- Railway akan otomatis detect changes
- Build dan deploy versi baru
- Zero-downtime deployment

### 3. Rollback (jika perlu)
- Buka Railway dashboard
- Pilih deployment sebelumnya
- Klik "Redeploy"

## 💰 Cost Optimization

### Free Tier Limits
- **Build time**: 500 minutes/month
- **Deploy time**: 100 hours/month
- **Bandwidth**: 100 GB/month

### Tips Menghemat
1. **Optimize dependencies**: Hapus yang tidak perlu
2. **Compress model**: Gunakan model yang lebih kecil
3. **Cache predictions**: Implement caching untuk prediksi yang sama
4. **Monitor usage**: Check Railway dashboard regularly

## 🔐 Security Best Practices

### 1. Environment Variables
- Jangan hardcode sensitive data
- Gunakan Railway environment variables
- Rotate secrets regularly

### 2. Input Validation
- Validasi semua input user
- Rate limiting untuk API
- Sanitize user input

### 3. HTTPS
- Railway otomatis provide HTTPS
- SSL certificate auto-renewal
- Secure headers

## 📈 Performance Optimization

### 1. Model Optimization
```python
# Load model once at startup
model = joblib.load("model_mpg_berat.pkl")

# Cache predictions
from functools import lru_cache

@lru_cache(maxsize=1000)
def predict_mpg(weight):
    return model.predict([[weight]])[0]
```

### 2. Database (Optional)
- Untuk production scale, consider database
- Store prediction history
- User analytics

### 3. CDN
- Railway provide global CDN
- Static assets served from edge
- Faster loading times

## 🎯 Next Steps

### Advanced Features
- [ ] User authentication
- [ ] Prediction history
- [ ] Batch predictions
- [ ] Model versioning
- [ ] A/B testing
- [ ] Analytics dashboard

### Monitoring
- [ ] Error tracking (Sentry)
- [ ] Performance monitoring
- [ ] User analytics
- [ ] Business metrics

---

## 🆘 Support

Jika mengalami masalah:

1. **Check Railway Logs**: Dashboard → Deployments → Logs
2. **Test Locally**: Pastikan app jalan di local
3. **Railway Docs**: [docs.railway.app](https://docs.railway.app)
4. **Community**: Railway Discord/Forum

**Happy Deploying! 🚀**
