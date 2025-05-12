from sympy import symbols, diff
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definisikan simbol untuk variabel
x1, x2, x3, x4, x5 = symbols('x1 x2 x3 x4 x5')

# Definisikan persamaan keuntungan
P = 50000000 + 5000000*x1 + 2500000*x2 + 15000000*x3 + 10000000*x4 + 7500000*x5

# Hitung gradien menggunakan SymPy
grad_P = [diff(P, var) for var in [x1, x2, x3, x4, x5]]
print("Gradien Keuntungan:", grad_P)

# Contoh nilai variabel untuk menghitung keuntungan pada titik tertentu
harga_tiket = 5  # Dalam ribuan Rupiah
jumlah_mainan = 3
ada_wahana_air = 1
lokasi_strategis = 1
mudah_transportasi = 1

keuntungan_prediksi = P.subs({
    x1: harga_tiket,
    x2: jumlah_mainan,
    x3: ada_wahana_air,
    x4: lokasi_strategis,
    x5: mudah_transportasi
})
print("Prediksi Keuntungan:", keuntungan_prediksi)

# Visualisasi (hanya bisa memvisualisasikan hubungan antara dua variabel dan keuntungan)
# Kita akan memvisualisasikan pengaruh harga tiket (x1) dan jumlah mainan (x2) terhadap keuntungan

harga_tiket_range = np.linspace(0, 10, 100) # Rentang harga tiket dari 0 hingga 10 ribu
jumlah_mainan_range = np.linspace(0, 5, 100) # Rentang jumlah mainan dari 0 hingga 5
X1, X2 = np.meshgrid(harga_tiket_range, jumlah_mainan_range)

# Hitung keuntungan berdasarkan rentang harga tiket dan jumlah mainan (asumsi variabel lain konstan)
P_values = np.array([[P.subs({x1: h, x2: j, x3: ada_wahana_air, x4: lokasi_strategis, x5: mudah_transportasi})
                     for h in harga_tiket_range] for j in jumlah_mainan_range])

# Buat plot 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, P_values, cmap='viridis')
ax.set_xlabel('Harga Tiket (ribu Rp)')
ax.set_ylabel('Jumlah Mainan Anak')
ax.set_zlabel('Keuntungan (Rp)')
ax.set_title('Pengaruh Harga Tiket dan Jumlah Mainan terhadap Keuntungan')
fig.colorbar(surf, ax=ax, label='Keuntungan (Rp)')
plt.show()

# Visualisasi pengaruh satu variabel (misalnya harga tiket) terhadap keuntungan
harga_tiket_range_1d = np.linspace(0, 10, 100)
P_values_1d = np.array([P.subs({x1: h, x2: jumlah_mainan, x3: ada_wahana_air, x4: lokasi_strategis, x5: mudah_transportasi})
                        for h in harga_tiket_range_1d])

plt.figure(figsize=(8, 6))
plt.plot(harga_tiket_range_1d, P_values_1d)
plt.xlabel('Harga Tiket (ribu Rp)')
plt.ylabel('Keuntungan (Rp)')
plt.title('Pengaruh Harga Tiket terhadap Keuntungan (Variabel Lain Konstan)')
plt.grid(True)
plt.show()