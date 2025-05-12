# -*- coding: utf-8 -*-
"""
Created on Sun May 11 14:58:03 2025

@author: office
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definisi fungsi keuntungan (contoh)
def jumlah_pengunjung(h, m, w, l, t, n0=1000, alpha=2, beta=5, gamma=3, delta=200, epsilon=50):
    return n0 - alpha * h**2 + beta * m + gamma * w + delta * l + epsilon * t

def biaya_operasional(m, w, c1=10, c2=5):
    return c1 * m + c2 * w

def keuntungan(params):
    h, m, w, l, t = params
    if h < 0 or m < 0 or w < 0 or l < 0 or l > 1 or t not in [0, 1]:
        return np.inf  # Mengembalikan nilai tak hingga untuk parameter yang tidak valid
    pendapatan_per_pengunjung = 1.5 * h + 2 * np.sqrt(m) + 0.8 * np.log(w + 1) + 10 * l + 20 * t
    jumlah = jumlah_pengunjung(h, m, w, l, t)
    biaya = biaya_operasional(m, w)
    return -(pendapatan_per_pengunjung * jumlah - biaya) # Negatif karena minimize mencari nilai minimum

# Nilai awal untuk variabel
initial_guess = [50, 10, 20, 0.7, 1]

# Batasan untuk variabel (opsional)
bounds = ((10, 100), (0, 50), (0, 100), (0, 1), (0, 1))

# Melakukan optimasi
result = minimize(keuntungan, initial_guess, bounds=bounds, method='L-BFGS-B')

# Mendapatkan hasil optimal
if result.success:
    h_optimal, m_optimal, w_optimal, l_optimal, t_optimal = result.x
    keuntungan_optimal = -result.fun
    jumlah_pengunjung_optimal = jumlah_pengunjung(h_optimal, m_optimal, w_optimal, l_optimal, t_optimal)
    biaya_optimal = biaya_operasional(m_optimal, w_optimal)

    print("Hasil Optimal:")
    print(f"Harga Tiket Optimal: ${h_optimal:.2f}")
    print(f"Jumlah Mainan Anak Optimal: {int(m_optimal)}")
    print(f"Luas Wahana Air Optimal: {w_optimal:.2f} unit")
    print(f"Indeks Lokasi: {l_optimal:.2f}")
    print(f"Ketersediaan Transportasi Umum: {int(t_optimal)}")
    print(f"Jumlah Pengunjung Optimal: {jumlah_pengunjung_optimal:.2f}")
    print(f"Biaya Operasional Optimal: ${biaya_optimal:.2f}")
    print(f"Keuntungan Harian Optimal: ${keuntungan_optimal:.2f}")
else:
    print("Optimasi gagal:", result.message)

# Visualisasi (Contoh pengaruh satu variabel terhadap keuntungan dengan variabel lain tetap)
h_range = np.linspace(10, 100, 100)
keuntungan_h = [-keuntungan([h, initial_guess[1], initial_guess[2], initial_guess[3], initial_guess[4]]) for h in h_range]

plt.figure(figsize=(10, 6))
plt.plot(h_range, keuntungan_h)
plt.xlabel("Harga Tiket Masuk ($)")
plt.ylabel("Keuntungan Harian ($)")
plt.title("Pengaruh Harga Tiket terhadap Keuntungan (Variabel Lain Tetap)")
plt.grid(True)
plt.show()

# Visualisasi pengaruh jumlah mainan anak terhadap keuntungan
m_range = np.linspace(0, 50, 51)
keuntungan_m = [-keuntungan([initial_guess[0], m, initial_guess[2], initial_guess[3], initial_guess[4]]) for m in m_range]

plt.figure(figsize=(10, 6))
plt.plot(m_range, keuntungan_m)
plt.xlabel("Jumlah Mainan Anak")
plt.ylabel("Keuntungan Harian ($)")
plt.title("Pengaruh Jumlah Mainan Anak terhadap Keuntungan (Variabel Lain Tetap)")
plt.grid(True)
plt.show()

# ... (Anda dapat menambahkan visualisasi untuk variabel lainnya)