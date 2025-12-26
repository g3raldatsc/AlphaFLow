# File: src/visualisasi.py

import matplotlib.pyplot as plt

def plot_analisis_teknikal(df, ticker):
    
    """
    Membuat visualisasi lengkap:
    1. Grafik Harga vs Moving Average (Untuk lihat Tren)
    2. Grafik Volatilitas (Untuk lihat Risiko)
    """
    
    plt.figure(figsize=(14, 10))

    # Grafik harga vs MA
    
    plt.subplot(2, 1, 1)
    
    # Plot Harga Asli
    
    plt.plot(df.index, df['Adj Close'], label='Harga Close', color='blue', alpha=0.5)
    
    # Plot Indikator
    
    plt.plot(df.index, df['MA_5'], label='MA 5 (Tren Mingguan)', color='orange', linestyle='--', linewidth=1.5)
    plt.plot(df.index, df['MA_20'], label='MA 20 (Tren Bulanan)', color='red', linestyle='-', linewidth=2)
    
    plt.title(f'Analisis Tren Harga Saham: {ticker}', fontsize=14)
    plt.ylabel('Harga (Rp)')
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)

    # Grafik Volatilitas
    
    plt.subplot(2, 1, 2)
    
    plt.plot(df.index, df['Volatilitas'], label='Volatilitas Pasar', color='gold')
    
    plt.title('Tingkat Risiko (Volatilitas)', fontsize=14)
    plt.ylabel('Standar Deviasi')
    plt.xlabel('Tahun')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()