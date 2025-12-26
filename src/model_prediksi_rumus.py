# File: src/model_prediksi_rumus.py

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np

def latih_model(train_data, test_data):
    
    """
    Fungsi ini bertugas:
    1. Mengambil data latih (X_train, y_train).
    2. Menyuruh komputer 'learning' mencari rumus (Fit).
    3. Mengembalikan model yang sudah pintar.
    """
    
    # Fitur (X): Data yang dipakai untuk menebak (Indikator)
    
    fitur = ['MA_5', 'MA_20', 'Volatilitas']
    
    # Target (y): Data yang ingin ditebak (Harga)
    
    target = 'Adj Close'
    
    # Siapkan Data Train
    
    X_train = train_data[fitur]
    y_train = train_data[target]
    
    # Siapkan Data Test
    
    X_test = test_data[fitur]
    y_test = test_data[target]
    
    print("Machine sedang belajar mencari pola dari tahun 2015-2023...")
    model = LinearRegression()
    
    # .fit() adalah perintah untuk "Mencari Rumus"
    
    model.fit(X_train, y_train)
    
    print("Proses belajar selesai!")
    
    # rumus
    
    print(f"-> Koefisien MA_5       : {model.coef_[0]:.4f}")
    print(f"-> Koefisien MA_20      : {model.coef_[1]:.4f}")
    print(f"-> Koefisien Volatilitas: {model.coef_[2]:.4f}")
    
    return model, X_test, y_test