from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model yang sudah dilatih
model_path = "model_mpg_berat.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Model berhasil dimuat!")
else:
    print("Model tidak ditemukan! Pastikan file model_mpg_berat.pkl ada.")
    model = None

@app.route('/')
def home():
    """Halaman utama aplikasi"""
    try:
        return render_template('index.html')
    except Exception as e:
        # Fallback jika template tidak ada
        return f"""
        <html>
        <head><title>MPG Prediction App</title></head>
        <body>
            <h1>MPG Prediction App</h1>
            <p>Status: Running</p>
            <p>Model Loaded: {model is not None}</p>
            <p>Error: {str(e)}</p>
        </body>
        </html>
        """, 200

@app.route('/health')
def health():
    """Health check endpoint untuk Railway"""
    try:
        return jsonify({
            'status': 'healthy',
            'message': 'Flask MPG Prediction App is running',
            'model_loaded': model is not None,
            'timestamp': pd.Timestamp.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint untuk prediksi MPG berdasarkan berat mobil"""
    try:
        # Ambil data dari form
        weight = float(request.form['weight'])
        
        # Validasi input
        if weight <= 0:
            return jsonify({
                'error': 'Berat mobil harus lebih dari 0',
                'success': False
            })
        
        if weight > 10000:  # Batas atas yang masuk akal
            return jsonify({
                'error': 'Berat mobil terlalu besar (maksimal 10,000 lbs)',
                'success': False
            })
        
        # Lakukan prediksi
        if model is not None:
            # Reshape data untuk model (model mengharapkan 2D array)
            weight_array = np.array([[weight]])
            predicted_mpg = model.predict(weight_array)[0]
            
            # Bulatkan hasil prediksi
            predicted_mpg = round(predicted_mpg, 2)
            
            # Interpretasi hasil
            if predicted_mpg < 15:
                interpretation = "Efisiensi bahan bakar rendah"
                color = "red"
            elif predicted_mpg < 25:
                interpretation = "Efisiensi bahan bakar sedang"
                color = "orange"
            else:
                interpretation = "Efisiensi bahan bakar tinggi"
                color = "green"
            
            return jsonify({
                'success': True,
                'weight': weight,
                'predicted_mpg': predicted_mpg,
                'interpretation': interpretation,
                'color': color,
                'model_info': {
                    'intercept': round(model.intercept_, 4),
                    'coefficient': round(model.coef_[0], 4)
                }
            })
        else:
            return jsonify({
                'error': 'Model tidak tersedia',
                'success': False
            })
            
    except ValueError:
        return jsonify({
            'error': 'Masukkan berat mobil yang valid (angka)',
            'success': False
        })
    except Exception as e:
        return jsonify({
            'error': f'Terjadi kesalahan: {str(e)}',
            'success': False
        })

@app.route('/about')
def about():
    """Halaman tentang aplikasi"""
    return render_template('about.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint untuk prediksi (JSON)"""
    try:
        data = request.get_json()
        weight = float(data['weight'])
        
        if weight <= 0:
            return jsonify({
                'error': 'Berat mobil harus lebih dari 0',
                'success': False
            })
        
        if model is not None:
            weight_array = np.array([[weight]])
            predicted_mpg = model.predict(weight_array)[0]
            
            return jsonify({
                'success': True,
                'weight': weight,
                'predicted_mpg': round(predicted_mpg, 2),
                'model_info': {
                    'intercept': round(model.intercept_, 4),
                    'coefficient': round(model.coef_[0], 4)
                }
            })
        else:
            return jsonify({
                'error': 'Model tidak tersedia',
                'success': False
            })
            
    except Exception as e:
        return jsonify({
            'error': f'Terjadi kesalahan: {str(e)}',
            'success': False
        })

if __name__ == '__main__':
    import os
    import sys
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print("=" * 50)
    print("FLASK MPG PREDICTION APP STARTUP")
    print("=" * 50)
    print(f"Port: {port}")
    print(f"Debug mode: {debug}")
    print(f"Model loaded: {model is not None}")
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    
    if os.path.exists('templates'):
        print(f"Templates directory exists: {os.listdir('templates')}")
    else:
        print("Templates directory NOT found!")
    
    print("=" * 50)
    
    try:
        print("Starting Flask application...")
        app.run(debug=debug, host='0.0.0.0', port=port)
    except Exception as e:
        print(f"CRITICAL ERROR starting Flask app: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
