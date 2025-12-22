import pandas as pd

def tambah_fitur(df):
    """
    Menambahkan indikator teknikal standar untuk prediksi saham:
    1. Daily Return (Keuntungan Harian)
    2. Moving Average (Tren Rata-rata)
    3. Volatilitas (Risiko)
    """
    df = df.copy()
    
    # 1. Target yang mau diprediksi: Return Harian (berdasarkan Adj Close)
    # Kita pakai log return atau pct_change. Di sini pct_change lebih umum.
    
    df['Return'] = df['Adj Close'].pct_change()
    
    # 2. Tren Jangka Pendek (Moving Average 5 Hari - Seminggu kerja)
    
    df['MA_5'] = df['Adj Close'].rolling(window=5).mean()
    
    # 3. Tren Jangka Menengah (Moving Average 20 Hari - Sebulan kerja)
    
    df['MA_20'] = df['Adj Close'].rolling(window=20).mean()
    
    # 4. Momentum Volatilitas (Standar Deviasi 20 hari)
    
    df['Volatilitas'] = df['Return'].rolling(window=20).std()
    
    df_bersih = df.dropna()
    
    return df_bersih