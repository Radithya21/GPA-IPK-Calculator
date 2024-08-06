# Kamus konversi nilai huruf ke angka
konversi_nilai = {
    'A': 4.0,
    'A-': 3.75,
    'B+': 3.5,
    'B': 3.0,
    'B-': 2.75,
    'C+': 2.5,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

# Inisialisasi total nilai dan total SKS
total_nilai = 0
total_sks = 0

# Input jumlah mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

# Input nilai dan SKS untuk setiap mata kuliah
for i in range(jumlah_mata_kuliah):
    nilai_huruf = input(f"Masukkan nilai huruf untuk mata kuliah {i+1} (A, A-, B+, B, B-, C+, C, D, F): ").upper()
    sks = int(input(f"Masukkan jumlah SKS untuk mata kuliah {i+1}: "))
    
    # Validasi nilai huruf
    if nilai_huruf in konversi_nilai:
        nilai_angka = konversi_nilai[nilai_huruf]
        total_nilai += nilai_angka * sks
        total_sks += sks
    else:
        print("Nilai huruf tidak valid. Harap masukkan nilai yang benar (A, B, C, D, F).")
        break

# Hitung dan tampilkan Indeks Prestasi
if total_sks > 0:
    indeks_prestasi = total_nilai / total_sks
    print("Indeks Prestasi kamu: {:.2f}".format(indeks_prestasi))
else:
    print("Total SKS tidak boleh nol.")
