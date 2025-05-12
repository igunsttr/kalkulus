# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:14:45 2025

@author: office
"""

import numpy as np
import matplotlib.pyplot as plt

# Definisi fungsi pendapatan
def pendapatan(params, k1=1.5, k2=2, k3=0.8, k4=10, k5=20, n0=1000, alpha=5, beta=3, gamma=2, delta=150, epsilon=40):
    h, m, w, l, t = params
    pendapatan_per_pengunjung = k1 * h + k2 * np.sqrt(m) + k3 * np.log(w + 1) + k4 * l + k5 * t
    jumlah_pengunjung = n0 - alpha * h + beta * m + gamma * w + delta * l + epsilon * t
    return pendapatan_per_pengunjung * jumlah_pengunjung

# Definisi fungsi biaya
def biaya(m, w, c1=8, c2=4):
    return c1 * m + c2 * w

# Definisi fungsi keuntungan
def keuntungan(params):
    h, m, w, l, t = params
    if h < 0 or m < 0 or w < 0 or l < 0 or l > 1 or t not in [0, 1]:
        return -np.inf # Mengembalikan nilai negatif tak hingga untuk parameter tidak valid
    return pendapatan(params) - biaya(m, w)

# Definisi gradien fungsi keuntungan (turunan parsial)
def gradien_keuntungan(params, delta=1e-6):
    h, m, w, l, t = params
    grad = np.zeros_like(params, dtype=float)

    # Turunan parsial terhadap h
    params_h_plus = np.array([h + delta, m, w, l, t])
    params_h_minus = np.array([h - delta, m, w, l, t])
    grad[0] = (keuntungan(params_h_plus) - keuntungan(params_h_minus)) / (2 * delta)

    # Turunan parsial terhadap m
    params_m_plus = np.array([h, m + delta, w, l, t])
    params_m_minus = np.array([h, m - delta, w, l, t])
    grad[1] = (keuntungan(params_m_plus) - keuntungan(params_m_minus)) / (2 * delta)

    # Turunan parsial terhadap w
    params_w_plus = np.array([h, m, w + delta, l, t])
    params_w_minus = np.array([h, m, w - delta, l, t])
    grad[2] = (keuntungan(params_w_plus) - keuntungan(params_w_minus)) / (2 * delta)

    # Turunan parsial terhadap l
    params_l_plus = np.array([h, m, w, l + delta, t])
    params_l_minus = np.array([h, m, w, l - delta, t])
    grad[3] = (keuntungan(params_l_plus) - keuntungan(params_l_minus)) / (2 * delta)

    # Turunan parsial terhadap t
    params_t_plus = np.array([h, m, w, l, t + delta if t == 0 else t - delta])
    params_t_minus = np.array([h, m, w, l, t - delta if t == 1 else t + delta])
    grad[4] = (keuntungan(params_t_plus) - keuntungan(params_t_minus)) / (2 * delta)

    return grad

# Inisialisasi parameter
params = np.array([50.0, 10.0, 20.0, 0.7, 1.0])
learning_rate = 0.001
n_iterations = 1000
keuntungan_history = []
params_history = []

# Gradient Ascent
for i in range(n_iterations):
    grad = gradien_keuntungan(params)
    params = params + learning_rate * grad

    # Memastikan batasan variabel
    params[0] = np.clip(params[0], 10, 100) # Batas harga tiket
    params[1] = np.clip(params[1], 0, 50)   # Batas jumlah mainan
    params[2] = np.clip(params[2], 0, 100)  # Batas luas wahana air
    params[3] = np.clip(params[3], 0, 1)    # Batas indeks lokasi
    params[4] = np.round(np.clip(params[4], 0, 1)) # Batas transportasi (0 atau 1)

    keuntungan_current = keuntungan(params)
    keuntungan_history.append(keuntungan_current)
    params_history.append(params.copy())

# Hasil optimal
h_optimal, m_optimal, w_optimal, l_optimal, t_optimal = params
keuntungan_optimal = keuntungan(params)

print("Hasil Optimal (dengan Gradient Ascent):")
print(f"Harga Tiket Optimal: ${h_optimal:.2f}")
print(f"Jumlah Mainan Anak Optimal: {(m_optimal)}")
print(f"Luas Wahana Air Optimal: {w_optimal:.2f} unit")
print(f"Indeks Lokasi Optimal: {l_optimal:.2f}")
print(f"Ketersediaan Transportasi Umum Optimal: {(t_optimal)}")
print(f"Keuntungan Harian Optimal: ${keuntungan_optimal:.2f}")

# Visualisasi Konvergensi Keuntungan
plt.figure(figsize=(10, 6))
plt.plot(range(n_iterations), keuntungan_history)
plt.xlabel("Iterasi")
plt.ylabel("Keuntungan Harian ($)")
plt.title("Konvergensi Keuntungan selama Gradient Ascent")
plt.grid(True)
plt.show()

# Visualisasi Perubahan Parameter (Contoh Harga Tiket)
plt.figure(figsize=(10, 6))
harga_tiket_history = [p[0] for p in params_history]
plt.plot(range(n_iterations), harga_tiket_history)
plt.xlabel("Iterasi")
plt.ylabel("Harga Tiket ($)")
plt.title("Perubahan Harga Tiket selama Gradient Ascent")
plt.grid(True)
plt.show()

# ... (Anda dapat menambahkan visualisasi untuk parameter lainnya)