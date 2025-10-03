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
    return render_template('index.html')

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
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
