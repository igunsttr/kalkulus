# -*- coding: utf-8 -*-
"""
Created on Sun May 11 14:54:26 2025

@author: office
"""

import sympy

# Definisikan simbol-simbol variabel
h, m, a, l, t = sympy.symbols('h m a l t')

# Definisikan persamaan keuntungan
K = (h - 5000) * (100 + 2*m + 0.5*a + 10*l + 50*t) - 200000

# 1. Hitung keuntungan pada kondisi tertentu
harga_tiket = 30000
jumlah_mainan = 5
luas_wahana_air = 200
skor_lokasi = 8
kualitas_transportasi = 0.7

keuntungan = K.subs({h: harga_tiket, m: jumlah_mainan, a: luas_wahana_air, l: skor_lokasi, t: kualitas_transportasi})
print(f"1. Keuntungan harian yang diprediksi: Rp {keuntungan}")

# 2. Hitung turunan parsial keuntungan terhadap harga tiket (h)
turunan_h = sympy.diff(K, h)
print(f"\n2. Turunan parsial terhadap harga tiket (∂K/∂h): {turunan_h}")

# 3. Hitung turunan parsial keuntungan terhadap jumlah mainan anak (m)
turunan_m = sympy.diff(K, m)
print(f"3. Turunan parsial terhadap jumlah mainan anak (∂K/∂m): {turunan_m}")

# 4. Bandingkan pengaruh perubahan harga tiket dan jumlah mainan pada kondisi awal
pengaruh_harga = turunan_h.subs({h: harga_tiket, m: jumlah_mainan, a: luas_wahana_air, l: skor_lokasi, t: kualitas_transportasi})
pengaruh_mainan = turunan_m.subs({h: harga_tiket, m: jumlah_mainan, a: luas_wahana_air, l: skor_lokasi, t: kualitas_transportasi})

print(f"\n4. Pengaruh perubahan harga tiket pada kondisi awal: {pengaruh_harga}")
print(f"   Pengaruh perubahan jumlah mainan pada kondisi awal: {pengaruh_mainan}")

if pengaruh_harga > pengaruh_mainan:
    print("   Perubahan harga tiket memiliki pengaruh lebih besar terhadap keuntungan per unit perubahan.")
elif pengaruh_mainan > pengaruh_harga:
    print("   Perubahan jumlah mainan anak memiliki pengaruh lebih besar terhadap keuntungan per unit perubahan.")
else:
    print("   Perubahan harga tiket dan jumlah mainan anak memiliki pengaruh yang sama terhadap keuntungan per unit perubahan.")