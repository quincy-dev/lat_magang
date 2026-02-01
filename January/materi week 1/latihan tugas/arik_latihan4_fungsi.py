# SOAL 1 – Function Void (Studi Kasus Sistem Notifikasi)

def show_notification(notif):
    print(f"sistem alert : " + notif)

show_notification("kebakaran")

print("\n")

# SOAL 2 – Function Return (Studi Kasus Perhitungan Diskon)

def hitung_diskon(total_belanja):
    diskon = total_belanja * 10 /100

    return total_belanja - diskon
print(hitung_diskon(100000))

print("\n")

# SOAL 3 – Function Default Parameter (Studi Kasus Sistem User)

def buat_user(username, role = "user"):
    print(f"Identitas {username} dengan role {role}")

buat_user("azka", "admin")

print("\n")

# SOAL 4 – Recursive Function (Studi Kasus Jumlah Data)

def jumlahkan(angka):
    if angka == 1:
        return 1
    return angka + jumlahkan(angka - 1)
print(jumlahkan(4))

print("\n")

# SOAL 5 – Recursive vs Loop (Analisis Logika)

def pangkat_recursive(x, n):
    if n == 0:
        return 1
    return x * pangkat_recursive(x, n - 1)
def pangkat_looping(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
print(pangkat_recursive(2, 3))
print(pangkat_looping(2, 3))

