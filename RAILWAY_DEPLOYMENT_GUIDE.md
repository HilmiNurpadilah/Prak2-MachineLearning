# 🚀 Railway Deployment Guide - Prak2-MachineLearning

## ✅ Project Berhasil di-Push ke GitHub!

**Repository**: [https://github.com/HilmiNurpadilah/Prak2-MachineLearning](https://github.com/HilmiNurpadilah/Prak2-MachineLearning)

## 🎯 Langkah-langkah Deployment ke Railway

### Step 1: Login ke Railway
1. Buka [railway.app](https://railway.app)
2. Login dengan GitHub account Anda
3. Authorize Railway untuk mengakses repository

### Step 2: Create New Project
1. Klik **"New Project"**
2. Pilih **"Deploy from GitHub repo"**
3. Cari repository: `HilmiNurpadilah/Prak2-MachineLearning`
4. Pilih branch: `main`
5. Railway akan otomatis detect Python project

### Step 3: Configure Deployment
Railway akan otomatis detect:
- ✅ **Python project** (detected from requirements.txt)
- ✅ **Flask app** (detected from app.py)
- ✅ **Dependencies** (from requirements.txt)
- ✅ **Start command** (from Procfile)

### Step 4: Deploy
1. Railway akan otomatis:
   - Install dependencies dari `requirements.txt`
   - Build aplikasi dengan gunicorn
   - Deploy ke production
2. Tunggu deployment selesai (2-3 menit)
3. Dapatkan URL aplikasi: `https://your-app.railway.app`

## 📁 File yang Sudah Siap untuk Railway

### ✅ Core Application Files
- `app.py` - Flask application (production ready)
- `model_mpg_berat.pkl` - Machine learning model
- `auto-mpg.csv` - Dataset
- `templates/` - HTML templates (base.html, index.html, about.html)

### ✅ Railway Deployment Files
- `Procfile` - Railway process configuration
- `railway.json` - Railway deployment settings
- `requirements.txt` - Dependencies dengan gunicorn
- `runtime.txt` - Python version specification
- `nixpacks.toml` - Build configuration

### ✅ Documentation & Scripts
- `README.md` - Project documentation
- `DEPLOYMENT.md` - Detailed deployment guide
- `QUICK_DEPLOY.md` - Quick deployment guide
- `RAILWAY_DEPLOYMENT_STEPS.md` - Railway deployment steps
- `setup_venv.bat` - Virtual environment setup
- `run_with_venv.bat` - Run with virtual environment
- `run_app.bat` - Run without virtual environment

## 🧪 Testing Setelah Deployment

### 1. Web Interface Test
- Buka URL Railway yang diberikan
- Test prediksi dengan berat mobil: `3500`
- Expected result: MPG sekitar `19.54`

### 2. API Test
```bash
curl -X POST https://your-app.railway.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"weight": 3500}'
```

**Expected Response:**
```json
{
  "success": true,
  "weight": 3500,
  "predicted_mpg": 19.54,
  "model_info": {
    "intercept": 47.2005,
    "coefficient": -0.0079
  }
}
```

## 🔧 Railway Configuration

### Procfile
```
web: python app.py
```

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

### requirements.txt
```
Flask==2.3.3
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
joblib==1.3.2
gunicorn==21.2.0
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
blinker==1.6.2
```

## 🎯 Expected Results

### Homepage Features
- Modern responsive design dengan Bootstrap 5
- Input form untuk berat mobil
- Real-time prediction dengan AJAX
- Results dengan interpretasi efisiensi
- About page dengan informasi model

### API Endpoints
- `GET /` - Homepage
- `POST /predict` - Web form prediction
- `POST /api/predict` - JSON API
- `GET /about` - About page

### Machine Learning Features
- ✅ Linear Regression model
- ✅ Input validation (1-10000 lbs)
- ✅ Error handling
- ✅ Model information display
- ✅ Performance metrics (R² = 0.65, RMSE = 4.21)

## 🐛 Troubleshooting

### Build Errors
- Check Railway logs di dashboard
- Pastikan semua dependencies ada di requirements.txt
- Verify Python version compatibility

### Runtime Errors
- Check application logs
- Verify model file exists
- Check environment variables

### Performance Issues
- Monitor Railway metrics
- Check memory usage
- Consider upgrading plan

## 📊 Monitoring

### Railway Dashboard
- **Metrics**: CPU, Memory, Network
- **Logs**: Real-time application logs
- **Deployments**: History dan status
- **Settings**: Environment variables

### Health Check
- Railway otomatis check endpoint `/`
- Restart otomatis jika gagal
- Monitoring 24/7

## 🔄 Updates

Untuk update aplikasi:
1. Edit code di local
2. Commit changes: `git commit -m "Update"`
3. Push to GitHub: `git push origin main`
4. Railway auto-deploy

## 🎉 Success Criteria

- [ ] Application deployed successfully
- [ ] Web interface accessible
- [ ] Prediction functionality working
- [ ] API endpoints responding
- [ ] No critical errors in logs
- [ ] Performance acceptable

---

## 🚀 Ready for Railway!

**Status**: ✅ **Project siap 100% untuk deployment ke Railway!**

**Repository**: [https://github.com/HilmiNurpadilah/Prak2-MachineLearning](https://github.com/HilmiNurpadilah/Prak2-MachineLearning)

**Next Step**: 
1. Go to [railway.app](https://railway.app)
2. Deploy from GitHub repository: `HilmiNurpadilah/Prak2-MachineLearning`
3. Deploy dan enjoy! 🎉
