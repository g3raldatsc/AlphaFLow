# File: src/evaluasi_model.py

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluasi_performa(model, X_test, y_test):
    
    """
    Fungsi ini bertugas:
    1. Menyuruh model melakukan prediksi pada Data Test untuk cek keakuratan (Predict).
    2. Membandingkan jawaban model dengan kenyataan (y_test).
    3. Menghitung nilai errornya.
    """
    
    # Lakukan prediksi
    # AI mencoba menebak harga berdasarkan X_test (MA5, MA20, Vol)
    
    y_prediksi = model.predict(X_test)
    
    # Hitung error atau nilai keakuratan
    
    # MAE (Mean Absolute Error): Rata-rata meleset berapa Rupiah?
    
    mae = mean_absolute_error(y_test, y_prediksi)
    
    # RMSE (Root Mean Squared Error): Error standar (lebih sensitif kalau ada error besar)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_prediksi))
    
    # MAPE (Mean Absolute Percentage Error): Meleset berapa Persen?
    # Rumus manual: Rata-rata dari |(Asli - Prediksi) / Asli|
    
    mape = np.mean(np.abs((y_test - y_prediksi) / y_test)) * 100
    
    # Kembalikan hasil prediksi dan nilai errornya
    
    return y_prediksi, mae, rmse, mape