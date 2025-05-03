# -*- coding: utf-8 -*-
"""
Created on Sat May  3 08:43:06 2025

@author: office
"""

#spidometer
import numpy as np
import matplotlib.pyplot as plt

def posisi(t):

  """
  Fungsi yang merepresentasikan posisi objek sebagai fungsi waktu.
  Dalam kasus nyata, ini akan menjadi data sensor dari spidometer.
  Contoh: Gerak dengan percepatan konstan
  """
  a = 2  # Percepatan (m/s^2)
  v0 = 5 # Kecepatan awal (m/s)
  s0 = 0 # Posisi awal (m)
  return 0.5 * a * t**2 + v0 * t + s0

def kecepatan_sesaat_numerik(posisi_fungsi, waktu, delta_t=0.001):
  """
  Memperkirakan kecepatan sesaat pada waktu tertentu menggunakan pendekatan numerik
  dari definisi turunan (limit).
  """
  # Kecepatan sesaat didekati oleh perubahan posisi dibagi perubahan waktu
  # dalam interval waktu yang sangat kecil.
  return (posisi_fungsi(waktu + delta_t) - posisi_fungsi(waktu)) / delta_t
       #    misal, posisi=5, waktu=2, (5(2+0.001) - 5(2))  / 0.001
       
       
# Contoh Penggunaan
waktu_titik = 2  # Waktu di mana kita ingin memperkirakan kecepatan sesaat
kecepatan = kecepatan_sesaat_numerik(posisi, waktu_titik)
print(f"Perkiraan kecepatan sesaat pada waktu {waktu_titik} detik: {kecepatan:.2f} m/s")

# Visualisasi (opsional)
waktu_arr = np.linspace(0, 5, 500)
#print(waktu_arr);
posisi_arr = posisi(waktu_arr)
kecepatan_arr_numerik = [kecepatan_sesaat_numerik(posisi, t) for t in waktu_arr]
#print ("kecepatan_arr_numerik:", kecepatan_arr_numerik)
# Kecepatan analitik untuk perbandingan (turunan sebenarnya dari fungsi posisi)
def kecepatan_analitik(t):
  a = 2
  v0 = 5
  return a * t + v0

kecepatan_arr_analitik = kecepatan_analitik(waktu_arr)

plt.figure(figsize=(10, 6))
#garis biru dibentuk oleh baris ke 56
plt.plot(waktu_arr, posisi_arr, label='Posisi (s(t))')
#print("waktu_arr, posisi_arr:",waktu_arr, posisi_arr);
plt.plot(waktu_arr, kecepatan_arr_numerik, label='Kecepatan Numerik (v(t) ≈ Δs/Δt)')
plt.plot(waktu_arr, kecepatan_arr_analitik, '--', label='Kecepatan Analitik (v(t) = ds/dt)')
plt.scatter(waktu_titik, kecepatan, color='red', label=f'Kecepatan Numerik di t={waktu_titik:.2f} s')
plt.xlabel('Waktu (t)')
plt.ylabel('Posisi dan Kecepatan')
plt.title('Perkiraan Kecepatan Sesaat Menggunakan Pendekatan Numerik Turunan')
plt.legend()
plt.grid(True)
plt.show()