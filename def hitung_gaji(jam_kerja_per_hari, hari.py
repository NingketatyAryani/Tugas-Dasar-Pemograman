def hitung_gaji(jam_kerja_per_hari, hari_kerja_per_minggu, gaji_per_jam, lembur_per_hari):
    total_jam_kerja_per_minggu = jam_kerja_per_hari * hari_kerja_per_minggu
    total_jam_lembur_per_minggu = max(total_jam_kerja_per_minggu - (jam_kerja_per_hari * 5), 0)
    gaji_pokok_per_minggu = total_jam_kerja_per_minggu * gaji_per_jam
    gaji_lembur_per_minggu = total_jam_lembur_per_minggu * (gaji_per_jam * 1.5)
    total_gaji_per_minggu = gaji_pokok_per_minggu + gaji_lembur_per_minggu
    total_gaji_per_bulan = total_gaji_per_minggu * 4
    return total_gaji_per_bulan

alamat = input("Masukkan alamat pegawai: ")
kantor = input("Masukkan kantor pegawai: ")
jam_kerja_per_hari = int(input("Masukkan jam kerja per hari: "))
hari_kerja_per_minggu = int(input("Masukkan jumlah hari kerja dalam seminggu: "))
gaji_per_jam = float(input("Masukkan gaji per jam: "))
lembur_per_hari = int(input("Masukkan jumlah hari lembur dalam sebulan: "))

total_gaji = hitung_gaji(jam_kerja_per_hari, hari_kerja_per_minggu, gaji_per_jam, lembur_per_hari)

formatted_gaji = "{:,.2f}".format(total_gaji)
print("\nRincian Gaji:")
print(f"Alamat: {alamat}")
print(f"Kantor: {kantor}")
print(f"Total gaji per bulan adalah: Rp {formatted_gaji}")
