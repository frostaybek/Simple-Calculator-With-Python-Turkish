def menu():
	print("""Ayaz Aybek yapımı
	
-----------
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Çıkış
-----------
""")

def yapilansecim(secim):
	if secim == 1:
		print("""
TOPLAMA SEÇİLDİ
""")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		toplam=int(x)+int(y)
		print(toplam)
		
	elif secim == 2:
		print("""
ÇIKARMA SEÇİLDİ
""")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		çıkar=int(x)-int(y)
		print(çıkar)

	elif secim == 3:
		print("""
ÇARPMA SEÇİLDİ
""")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		carp=int(x)*int(y)
		print(carp)

	elif secim == 4:
		print("""
BÖLME SEÇİLDİ
""")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		bol=int(x)/int(y)
		print(bol)
		
	elif secim == 5:
	    print("ÇIKIŞ SEÇİLDİ")
	    pass
	    
secim=0

while int(secim) != 5:
    menu()
    secim=input("Seçiminizi yapınız : ")
    yapilansecim(int(secim))