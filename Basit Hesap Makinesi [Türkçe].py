def menu():
	print("""Menu
---------
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Çıkış""")

def yapilansecim(secim):
	if secim == 1:
		print("Toplama seçildi")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		toplam=int(x)+int(y)
		print(toplam)
		

	elif secim == 2:
		print("çıkarma seçildi")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		çıkar=int(x)-int(y)
		print(çıkar)

	elif secim == 3:
		print("Çarpma seçildi")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		carp=int(x)*int(y)
		print(carp)

	elif secim == 4:
		print("bölme seçildi")
		x=input("Birinci Sayı : ")
		y=input("İkinci Sayı : ")
		bol=int(x)/int(y)
		print(bol)
		
	elif secim == 5:
	    print("Çıkış Seçildi")
	    pass
	    
	    
secim=0

while int(secim) != 5:
    menu()
    secim=input("Seçiminizi yapınız : ")
    yapilansecim(int(secim))
    
	    








    


    


