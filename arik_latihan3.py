# SOAL 1

stok = [12, 5, 0, 7, 20]
for jumlah in stok:
    if jumlah == 0:
        print("Stok Habis")
    elif jumlah < 10:
        print("Stok Menipis")
    else:
        print("Stok Aman")

print("\n")

# SOAL 2

karyawan = {"nama": "Andi", "nilai_kinerja": 78, "kehadiran": 85}

if karyawan["nilai_kinerja"] >= 80 and karyawan["kehadiran"] >= 85:
    print("LAYAK PROMOSI")
else:
    print("Belum Layak Promosi")


print("\n")
# SOAL 3

nomor_antrian = 1
while nomor_antrian <= 10:
    if nomor_antrian % 4 == 0:
        print(f"Antrian {nomor_antrian} - pemeriksaan khusus")
    else:
        print(f"Antrian {nomor_antrian} - pemeriksaan normal")
    nomor_antrian += 1


print("\n")
# SOAL 4

nilai = [45, 67, 80, 90, 55, 72]
for n in nilai:
    if n < 60:
        print(f"nilai {n} - Tidak Lulus")
    else:
        print(f"nilai {n} - Lulus")


print("\n")
# SOAL 5

username_input = "user123"
password_input = "admin123"
akun_aktif = True

username_benar = "user123"
password_benar = "admin123"
if (username_input == username_benar and
        password_input == password_benar and
        akun_aktif):
    print("Login Berhasil")
else:
    print("Login Gagal")


print("\n")
# SOAL 6

suhu = [28, 30, 35, 33, 26]
for s in suhu:
    if s > 32:
        print(f"suhu {s} - Suhu Tinggi")
    elif 27 <= s <= 32:
        print(f"suhu {s} - Suhu Normal")
    else:
        print(f"suhu {s} - Suhu Rendah")


print("\n")
# SOAL 7

malam = False
ruangan_gelap = True
if malam or ruangan_gelap:
    print("Lampu Menyala")
else:
    print("Lampu Mati")


print("\n")
# SOAL 8

absensi = {
    "Senin": True,
    "Selasa": True,
    "Rabu": False,
    "Kamis": True,
    "Jumat": False
}
for hari, hadir in absensi.items():
    if hadir:
        print(f"{hari} - Hadir")
    else:
        print(f"{hari} - Tidak Hadir")


print("\n")
# SOAL 9

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Angka {i} - Spesial")
    else:
        print(f"Angka {i} - Biasa")


print("\n")
# SOAL 10

jumlah_produksi = 1
while True:
    if jumlah_produksi > 8:
        break
    if jumlah_produksi % 2 != 0:
         print(f"Jumlah Produksi {jumlah_produksi} - Mesin Aktif")
    else:
        print(f"Jumlah Produksi {jumlah_produksi} - Mesin Pendingin")
    jumlah_produksi =+ 1
    # jumlah_produksi = jumlah_produksi + 1
