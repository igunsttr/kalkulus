from sympy import symbols, diff
import numpy as np
import matplotlib.pyplot as plt

# Definisikan simbol-simbol
h, m, w, l, t = symbols('h m w l t')

# Definisikan fungsi keuntungan
K = 100*h + 50*m + 80*w + 20*l + 15*t - 0.1*h**2 - 0.05*m**2 - 0.08*w**2

# Hitung gradien K terhadap setiap variabel
grad_h = diff(K, h)
grad_m = diff(K, m)
grad_w = diff(K, w)
grad_l = diff(K, l)
grad_t = diff(K, t)

# Tampilkan persamaan gradien
print("Gradien Fungsi Keuntungan:")
print(f"dL/dh = {grad_h}")
print(f"dL/dm = {grad_m}")
print(f"dL/dw = {grad_w}")
print(f"dL/dl = {grad_l}")
print(f"dL/dt = {grad_t}")

# Contoh nilai untuk setiap variabel
h_val = 5  # Harga tiket 5 ribu rupiah
m_val = 10 # Jumlah mainan anak
w_val = 1  # Ada wahana air
l_val = 8  # Skor lokasi 8
t_val = 7  # Kualitas transportasi 7

# Hitung nilai gradien pada titik tertentu
grad_h_val = grad_h.subs({h: h_val, m: m_val, w: w_val, l: l_val, t: t_val})
grad_m_val = grad_m.subs({h: h_val, m: m_val, w: w_val, l: l_val, t: t_val})
grad_w_val = grad_w.subs({h: h_val, m: m_val, w: w_val, l: l_val, t: t_val})
grad_l_val = grad_l.subs({h: h_val, m: m_val, w: w_val, l: l_val, t: t_val})
grad_t_val = grad_t.subs({h: h_val, m: m_val, w: w_val, l: l_val, t: t_val})

print("\nNilai Gradien pada Titik (h={}, m={}, w={}, l={}, t={}):".format(h_val, m_val, w_val, l_val, t_val))
print(f"dL/dh = {grad_h_val}")
print(f"dL/dm = {grad_m_val}")
print(f"dL/dw = {grad_w_val}")
print(f"dL/dl = {grad_l_val}")
print(f"dL/dt = {grad_t_val}")

# Visualisasi 2D (Contoh pengaruh harga tiket terhadap keuntungan)
h_range = np.linspace(1, 10, 100) # Rentang harga tiket
K_values = [K.subs({h: val, m: m_val, w: w_val, l: l_val, t: t_val}) for val in h_range]
grad_h_values = [grad_h.subs({h: val, m: m_val, w: w_val, l: l_val, t: t_val}) for val in h_range]

plt.figure(figsize=(10, 6))
plt.plot(h_range, K_values, label='Keuntungan (K)')
plt.plot(h_range, grad_h_values, label='Gradien Keuntungan terhadap Harga Tiket (dL/dh)')
plt.xlabel('Harga Tiket (ribu rupiah)')
plt.ylabel('Nilai')
plt.title('Pengaruh Harga Tiket terhadap Keuntungan dan Gradiennya')
plt.grid(True)
plt.legend()
plt.show()

# Visualisasi 2D (Contoh pengaruh jumlah mainan anak terhadap keuntungan)
m_range = np.linspace(1, 20, 100) # Rentang jumlah mainan anak
K_values_m = [K.subs({h: h_val, m: val, w: w_val, l: l_val, t: t_val}) for val in m_range]
grad_m_values = [grad_m.subs({h: h_val, m: val, w: w_val, l: l_val, t: t_val}) for val in m_range]

plt.figure(figsize=(10, 6))
plt.plot(m_range, K_values_m, label='Keuntungan (K)')
plt.plot(m_range, grad_m_values, label='Gradien Keuntungan terhadap Jumlah Mainan (dL/dm)')
plt.xlabel('Jumlah Mainan Anak')
plt.ylabel('Nilai')
plt.title('Pengaruh Jumlah Mainan Anak terhadap Keuntungan dan Gradiennya')
plt.grid(True)
plt.legend()
plt.show()