# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:58:10 2025

@author: office
"""

from sympy import symbols, integrate
import numpy as np
import matplotlib.pyplot as plt

# Definisikan simbol-simbol
p, w, l, q, m, t, c, hari = symbols('p w l q m t c hari')

# Definisikan fungsi harga tiket
harga_tiket_func = 20 + 0.5*w + 0.2*l

# Definisikan fungsi jumlah pengunjung
jumlah_pengunjung_func = (5000 * m * t**(1/2)) / p

# Definisikan fungsi biaya operasional harian
biaya_operasional_func = 500 + 10*w + 5*m

# Definisikan variabel tetap
lokasi_tetap = 8
transportasi_tetap = 4
jumlah_hari = 30

# Substitusi nilai tetap
harga_tiket = harga_tiket_func.subs({l: lokasi_tetap})
jumlah_pengunjung = jumlah_pengunjung_func.subs({t: transportasi_tetap})
biaya_operasional = biaya_operasional_func

# Asumsikan variasi linear w dan m terhadap waktu (hari)
w_awal = 2
w_akhir = 5
m_awal = 10
m_akhir = 20

w_harian = w_awal + (w_akhir - w_awal) * (hari - 1) / (jumlah_hari - 1)
m_harian = m_awal + (m_akhir - m_awal) * (hari - 1) / (jumlah_hari - 1)

# Substitusi w_harian dan m_harian
harga_tiket_harian = harga_tiket.subs({w: w_harian})
jumlah_pengunjung_harian = jumlah_pengunjung.subs({p: harga_tiket_harian, m: m_harian})
biaya_operasional_harian = biaya_operasional.subs({w: w_harian, m: m_harian})

# Fungsi Keuntungan Harian
keuntungan_harian = harga_tiket_harian * jumlah_pengunjung_harian - biaya_operasional_harian

# Prediksi Keuntungan Total dengan Integral
total_keuntungan = integrate(keuntungan_harian, (hari, 1, jumlah_hari))

print(f"Prediksi Keuntungan Total selama {jumlah_hari} hari (dalam ribuan Rupiah): {total_keuntungan}")

# Visualisasi Keuntungan Harian
hari_array = np.arange(1, jumlah_hari + 1)
keuntungan_harian_numeric = []
for h in hari_array:
    keuntungan_harian_val = keuntungan_harian.subs({hari: h}).evalf()
    keuntungan_harian_numeric.append(keuntungan_harian_val)

plt.figure(figsize=(10, 6))
plt.plot(hari_array, keuntungan_harian_numeric, label='Keuntungan Harian (ribu Rp)')
plt.xlabel('Hari')
plt.ylabel('Keuntungan (ribu Rp)')
plt.title('Prediksi Keuntungan Harian Tempat Wisata')
plt.grid(True)
plt.legend()
plt.show()