# Model prediksi sederhana menggunakan regresi linier
# Model ini hanya untuk ilustrasi dasar, bukan untuk produksi nyata
# Gunakan data yang sudah ditambahkan fitur teknikalnya

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Menggunakan data ma_5, ma_20, dan volatilitas untuk memprediksi harga penutupan yang disesuaikan (Adj Close)

def latih_model_sederhana(df):
    X = df[['MA_5', 'MA_20', 'Volatilitas']]
    y = df['Adj Close']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = LinearRegression()
    
    model.fit(X_train, y_train)
    
    prediksi = model.predict(X_test)
    
    mse = mean_squared_error(y_test, prediksi)
    rmse = np.sqrt(mse)
    
    # Tampilan hasil RMSE untuk evaluasi sederhana
    
    print(f"Rata-rata kesalahan prediksi: Rp {rmse:.2f}")
    
    return model, y_test, prediksi