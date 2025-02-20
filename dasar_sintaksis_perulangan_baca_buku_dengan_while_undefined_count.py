"""
Program perulangan membaca buku dengan while sampai paham
"""
book_count = 10
print('Ibu berkata, "Baca semua bukumu"')
read_count = 0

understood_count = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham + 1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")

if jumlah_paham == book_count:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_paham} buku"')

print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")