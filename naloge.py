"""
OSPR2 – vaje/praksa
Vaja 01  - vaja za ponovitev (izpisi z oblikovanjem)
"""

# 1. naloga
# Napišite program, ki s standardnega vhoda prebere znesek v evrih in ga pretvori v ameriške dolarje. Za pravilno pretvorbo
# na spletu poiščite trenutni menjalni tečaj. Rezultat izpišite z uporabo metode .format()
# primer izpisa: 100.00 EUR je enako 117.20 USD

znesek = float(input("Vpisi znesek: "))
znesek2 = znesek*1.16
tekst = "{cena:.2f} EUR je enako {cena2:.2f} USD"
print(tekst.format(cena = znesek, cena2 = znesek2))


# 2. naloga
# Napišite program, ki prebere, koliko denarja imate, in koliko stane določen izdelek (kolicinaDenarja in cenaIzdelka). 
# Izračunajte, koliko izdelkov lahko kupite, in rezultat z metodo .format() izpišite v naslednji obliki:
# primer izpisa: Imam 1500 evrov, zato lahko kupim 4 izdelke po ceni 350 evrov.

kolicinaDenarja = int(input("Vpisi kolicino denarja: "))
cenaIzdelka = int(input("Vpisi koliko stane en izdelka: "))
steviloIzdelkov = kolicinaDenarja//cenaIzdelka
txt = "Lahko kupis {izdelki:.2f} izdelkov."
print(txt.format(izdelki = steviloIzdelkov))


# 3. naloga
# Napišite program, ki pretvori podano število sekund v ure, minute in sekunde. Rezultat izpišite s pomočjo operatorja % v naslednji obliki:
# primer izpisa: 7354 sekund je enako 2 ur, 2 minut in 34 sekund.

sekunde = int(input("Koliko sekund: "))
vse_sekunde = sekunde
ure = sekunde//3600
sekunde = sekunde%3600
minute = sekunde//60
sekunde = sekunde%60
print("%d sekund je enako %d ur, %d minut, in %d sekund"%(vse_sekunde, ure, minute, sekunde))

# 4. naloga
# Napišite program, v katerega vnesete polmer kroga. Program naj izračuna obseg in ploščino ter z uporabo f-stringa izpiše rezultat v naslednji obliki:
# primer izpisa: Polmer kroga je 5 cm, obseg kroga je 31.42 cm, ploščina kroga pa je 78.5 cm2.



# 5. naloga
# Napišite program, ki z uporabo f-stringa izpiše trenutni datum in uro v naslednji obliki:
# primer izpisa: Danes je 1. 9. 2025, ura je 13:45.
# *uporabite datetime.now()



# 6. naloga
# Napišite program, ki izračuna hipotenuzo pravokotnega trikotnika z danima katetama. Rezultat izpišite z uporabo metode .format() v naslednji obliki:
# primer izpisa: Pri katetah a = 3 in b = 4 je hipotenuza enaka 5.00.



# 7. naloga
# Napišite program, ki reši kvadratno enačbo oblike ax² + bx + c = 0. Korene enačbe izpišite s pomočjo operatorja % v spodnji obliki:
# primer izpisa:
# Za enačbo 2x² + 4x + 2 = 0 sta korena:
# x1 = -1.0
# x2 = -1.0



# 8. naloga
# Napišite program, ki prebere dve kompleksni števili in s pomočjo operatorja % izpiše njuno vsoto, razliko in produkt v naslednji obliki:
# primer izpisa za kompleksni števili 2+3j in 1-1j:
# Vsota: 3+2j  
# Razlika: 1+4j  
# Produkt: 5+1j  



# 9. naloga
# Napišite program, ki izračuna vsoto prvih n členov geometrijskega zaporedja z začetnim členom a in količnikom k. Rezultat izpišite z uporabo f-stringa v naslednji obliki:
# primer izpisa: Vsota prvih 5 členov geometrijskega zaporedja z začetnim členom 2 in količnikom 3 je 242.
# *formulo lahko poiščete na spletu



# 10. naloga
# Napišite program, ki izračuna vsoto vseh števil v seznamu in izpiše rezultat z uporabo metode .format().
# Pri tem si pomagajte tudi s parametroma end in sep.
# primer izpisa: Vsota števil 4, 7, 1, 3 je 15.



# 11. naloga
# Napišite program, ki preveri, ali so števila v danem seznamu deljiva s podanim deliteljem. Rezultat izpišite s pomočjo operatorja % v naslednji obliki:
# primer:
# stevilke = [10, 15, 23, 42, 55] # začetni seznam
# deljitelj = 5 #določen delitelj
# deljiva_st = [10, 15, 55] # rešitev vaše kode



# 12.	Napišite program, ki sešteje dve 2x2 matriki in rezultat izpiše s pomočjo f-string. Dve matriki se seštejeta tako, da se seštejejo njuni istoležni elementi. Primer:
# Matrika A:		Matrika B:
# [1, 2]			[5, 6]
# [3, 4]			[7, 8]
# Vsota matrik A in B:
# [6, 8]
# [10, 12]



# Vse naloge nadgradite tako, da se rezultati zapišejo v datoteko »rešitve_vaja_01.txt«. Po vsaki rešitvi naj bo ena vrstica prazna).