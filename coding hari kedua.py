nama = "INDAH (D0222321)"
gaji_pokok =1000000
gaji_lembur_per_jam = 5000
lama_lembur = 30
gaji_lembur = gaji_lembur_per_jam * lama_lembur

gaji_kotor = gaji_pokok + gaji_lembur
pajak = 9/100
potongan = int(gaji_pokok * 9/100)
gaji_bersih = gaji_kotor - potongan

print ("NAMA : ",nama)
print ("GAJI POKOK :Rp. ",gaji_pokok)
print ("GAJI LEMBUR :Rp. ",gaji_lembur)
print ("GAJI KOTOR :Rp. ",gaji_kotor)
print ("PAJAK : ",pajak)
print ("POTONGAN :Rp. ",potongan)
print ("GAJI BERSIH :Rp.  ",gaji_bersih)
