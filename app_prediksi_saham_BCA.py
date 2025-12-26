import pandas as pd
import yfinance as yf
import joblib
import os
import sys

def main():
    print("Aplikasi Prediksi Saham BCA (BBCA.JK) dengan Model Gerald")

    path_model = os.path.join('models', 'model_prediksi_saham_BCA_linear.pkl')

    if not os.path.exists(path_model):
        print(f"\nFile model tidak ditemukan!")
        print(f"Sistem mencari di: {path_model}")
        print("Pastikan file ini (app_prediksi_saham_BCA.py) ada di folder utama,")
        print("sejajar dengan folder 'models'.")
        input("\nTekan Enter untuk keluar...")
        return

    ticker = 'BBCA.JK'
    print(f"\nSedang mengunduh data pasar langsung untuk {ticker}...")
    
    try:
        df = yf.download(ticker, period="3mo", progress=False, auto_adjust=False)
        
        if isinstance(df.columns, pd.MultiIndex):
            try:
                df.columns = df.columns.get_level_values('Price')
            except:
                df.columns = df.columns.get_level_values(0)
        
        if 'Adj Close' not in df.columns:
            df['Adj Close'] = df['Close']

        df['MA_5'] = df['Adj Close'].rolling(window=5).mean()
        df['MA_20'] = df['Adj Close'].rolling(window=20).mean()
        df['Return'] = df['Adj Close'].pct_change()
        df['Volatilitas'] = df['Return'].rolling(window=20).std()

        data_terakhir = df.iloc[[-1]].copy()
        
        tanggal = data_terakhir.index[0].strftime('%d-%m-%Y')
        harga_close = data_terakhir['Adj Close'].values[0]

        print(f"Data Terkini: {tanggal}")
        print(f"Harga Penutupan: Rp {harga_close:,.0f}")

        print("\nModel sedang menghitung probabilitas...")
        
        model = joblib.load(path_model)
        
        X_input = data_terakhir[['MA_5', 'MA_20', 'Volatilitas']]
        
        harga_prediksi = model.predict(X_input)[0]

        selisih = harga_prediksi - harga_close
        
        print("\n" + "-"*40)
        print(f"Prediksi Harga Saham Bank BCA untuk hari besok kerja:")
        print(f"Rp {harga_prediksi:,.2f}")
        print("-"*40)
        
        if selisih > 20:
            print("Potensi Naik (Bullish)")
            print(f"Target kenaikan: +Rp {selisih:.0f}")
        elif selisih < -20:
            print("Potensi Turun (Bearish)")
            print(f"Target penurunan: Rp {selisih:.0f}")
        else:
            print("Sideways (Datar)")
            print("Harga diprediksi stabil, belum ada tren kuat.")

    except Exception as e:
        print(f"\nTerjadi Error: {e}")
        print("Cek koneksi internet Anda.")

    print("\n" + "="*50)
    input("Tekan Enter untuk menutup aplikasi...")

if __name__ == "__main__":
    main()