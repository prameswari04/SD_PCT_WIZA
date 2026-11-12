# Menentukan batas awal dan akhir deret
awal = 1
akhir = 100

# Menggunakan rumus deret aritmatika: n * (awal + akhir) / 2
# Operator // digunakan agar hasilnya berupa bilangan bulat (integer)
total = akhir * (awal + akhir) // 2

# Menampilkan hasil
print(f"Jumlah deret bilangan dari {awal} sampai {akhir} adalah: {total}")
