# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:53:48 2025

@author: office
"""

from sympy import symbols, diff, sqrt, ln
import numpy as np
import matplotlib.pyplot as plt

# Definisikan simbol
x, y, z, l, t = symbols('x y z l t')

# Definisikan koefisien
a = 0.5
b = 1.2
c = 0.2
d = 0.8
e = 0.3
C = 50

# Definisikan fungsi jumlah pengunjung
N = 1000 - 10 * x

# Definisikan fungsi keuntungan
K = (a * x + b * sqrt(y) + c * z * x + d * ln(l) + e * t) * N - C

# 1. Fungsi keuntungan eksplisit
print("1. Fungsi Keuntungan Harian:")
print(K)
print("-" * 30)

# 2. Gradien fungsi keuntungan
gradien_K_x = diff(K, x)
gradien_K_y = diff(K, y)

print("2. Gradien Fungsi Keuntungan terhadap Harga Tiket (x):")
print(gradien_K_x)
print("\nInterpretasi Gradien terhadap Harga Tiket:")
print("Gradien ini menunjukkan tingkat perubahan keuntungan terhadap perubahan kecil pada harga tiket. Jika nilainya positif, kenaikan harga tiket akan meningkatkan keuntungan (pada titik tertentu), dan sebaliknya.")
print("-" * 30)

print("\nGradien Fungsi Keuntungan terhadap Jumlah Mainan Anak (y):")
print(gradien_K_y)
print("\nInterpretasi Gradien terhadap Jumlah Mainan Anak:")
print("Gradien ini menunjukkan tingkat perubahan keuntungan terhadap perubahan kecil pada jumlah mainan anak. Nilai positif menunjukkan penambahan mainan anak akan meningkatkan keuntungan.")
print("-" * 30)

# 3. Prediksi keuntungan
harga_tiket = 50  # dalam ribuan rupiah
jumlah_mainan = 9
wahana_air = 1
lokasi_indeks = 8
transportasi_indeks = 7

keuntungan_prediksi = K.subs({x: harga_tiket, y: jumlah_mainan, z: wahana_air, l: lokasi_indeks, t: transportasi_indeks}).evalf()
print(f"3. Prediksi Keuntungan Harian:")
print(f"   Harga Tiket (x): Rp {harga_tiket}.000")
print(f"   Jumlah Mainan Anak (y): {jumlah_mainan}")
print(f"   Wahana Air (z): {'Ada' if wahana_air == 1 else 'Tidak Ada'}")
print(f"   Indeks Lokasi (l): {lokasi_indeks}")
print(f"   Indeks Transportasi (t): {transportasi_indeks}")
print(f"   Keuntungan Prediksi: Rp {keuntungan_prediksi:.2f} juta")
print("-" * 30)

# 4. Analisis limit
limit_keuntungan_x_100 = K.limit(x, 100)
print("4. Limit Keuntungan jika Harga Tiket Mendekati Rp 100.000:")
print(f"   lim (x->100) K(x, y, z, l, t) = {limit_keuntungan_x_100}")
print("\nImplikasi Limit:")
print("Limit ini menunjukkan perilaku keuntungan saat harga tiket terus meningkat mendekati Rp 100.000. Dalam kasus ini, karena faktor jumlah pengunjung (N = 1000 - 10x) menjadi nol pada x = 100, keuntungan akan cenderung menurun atau bahkan negatif setelah melewati titik optimal. Pengelola perlu berhati-hati dalam menaikkan harga tiket terlalu tinggi karena dapat mengurangi jumlah pengunjung secara signifikan.")
print("-" * 30)

# 5. Pengaruh penambahan satu unit mainan anak
# Evaluasi gradien terhadap y pada kondisi saat ini
gradien_y_saat_ini = gradien_K_y.subs({x: harga_tiket, y: jumlah_mainan, z: wahana_air, l: lokasi_indeks, t: transportasi_indeks}).evalf()
print("5. Pengaruh Penambahan Satu Unit Mainan Anak:")
print(f"   Gradien Keuntungan terhadap Jumlah Mainan Anak saat ini: {gradien_y_saat_ini:.2f}")
print("\nInterpretasi:")
print(f"Nilai gradien sebesar {gradien_y_saat_ini:.2f} menunjukkan bahwa dengan penambahan satu unit mainan anak (dari 9 menjadi 10), keuntungan harian diperkirakan akan meningkat sekitar Rp {gradien_y_saat_ini:.2f} juta, dengan asumsi faktor lain tetap konstan.")
print("-" * 30)

# Grafik untuk menunjukkan pengaruh harga tiket terhadap keuntungan (dengan faktor lain tetap)
harga_tiket_range = np.linspace(10, 90, 100)
keuntungan_values_harga = [K.subs({x: h, y: jumlah_mainan, z: wahana_air, l: lokasi_indeks, t: transportasi_indeks}).evalf() for h in harga_tiket_range]

plt.figure(figsize=(10, 6))
plt.plot(harga_tiket_range, keuntungan_values_harga, label='Keuntungan')
plt.xlabel('Harga Tiket (ribu Rp)')
plt.ylabel('Keuntungan Harian (juta Rp)')
plt.title('Pengaruh Harga Tiket terhadap Keuntungan')
plt.grid(True)
plt.legend()
plt.show()

# Grafik untuk menunjukkan pengaruh jumlah mainan anak terhadap keuntungan (dengan faktor lain tetap)
jumlah_mainan_range = np.linspace(1, 20, 100)
keuntungan_values_mainan = [K.subs({x: harga_tiket, y: j, z: wahana_air, l: lokasi_indeks, t: transportasi_indeks}).evalf() for j in jumlah_mainan_range]

plt.figure(figsize=(10, 6))
plt.plot(jumlah_mainan_range, keuntungan_values_mainan, label='Keuntungan')
plt.xlabel('Jumlah Mainan Anak')
plt.ylabel('Keuntungan Harian (juta Rp)')
plt.title('Pengaruh Jumlah Mainan Anak terhadap Keuntungan')
plt.grid(True)
plt.legend()
plt.show()