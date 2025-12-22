# Gunakan framework ini untuk mengunduh data saham dari Yahoo Finance
# Pastikan Anda menginput parameter yang benar dan sesuai kebutuhan analisis Anda

import yfinance as yf
import pandas as pd

def unduh_data_lengkap(ticker, tgl_mulai, tgl_akhir):
    """
    Mengunduh data saham OHLCV + Adj Close dari Yahoo Finance.
    """
    try:
        # auto_adjust=False agar 'Adj Close' muncul terpisah dari 'Close'
        data = yf.download(ticker, start=tgl_mulai, end=tgl_akhir, auto_adjust=False, progress=False)
        
        # Merapikan Header: Mengubah MultiIndex (2 baris judul) menjadi 1 baris
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        # Memastikan format tanggal bersih
        if data.index.tz is not None:
            data.index = data.index.tz_localize(None)

        return data.dropna()
        
    except Exception as e:
        print(f"Error: {e}")
        return None