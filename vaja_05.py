"""
OSPR2 – vaje/praksa
Vaja 05  - vaja za ponovitev (zanke, nizi in seznami) 

VSE NALOGE REŠUJTE S FUNKCIJAMI, KO ODDAJATE KODO NAJ BODO ZAKOMENTIRANA NAVODILA IN KLICI VAŠIH FUNKCIJ (FUNKCIJE SAME NAJ NE BODO ZAKOMENTIRANE)


1. naloga
Napišite funkcijo zdruzevanje(niz1, niz2), ki združi dva seznama tako, da po vrsti združi istoležne znake prvega in drugega niza. Predpostavite, da sta oba seznama enako dolga in da so istoležni nizi enako dolgi.
Primer:
zdruzevanje('banana', 'hruška') vrne 'bharnuašnkaa')


2. naloga
Napišite funkcijo iskanje_podniza(sez, niz), ki za podan seznam in niz preveri, ali se niz nahaja v katerikoli vrstici gnezdenega seznama. Funkcija vrne True, če niz obstaja in False, če ne obstaja.  
Primer:
sez = [
['h', 'e', 'l', 'l', 'o'], 
['w', 'o', 'r', 'l', 'd'], 
['p', 'y', 't', 'h', 'o'], 
['p', 'r', 'o', 'g', 'r'], 
['a', 'm', 'm', 'i', 'n'] 
]
niz = 'prog'
iskanje_podnizov(sez, niz) vrne True


3. naloga
Napišite program, ki za vsak element v ugnezdenem seznamu prešteje, koliko sosednjih elementov je enakih podanemu ciljnemu elementu. Sosedi so elementi levo, desno, zgoraj, spodaj in diagonalno.
Primer:
sez = [
[1, 2, 2, 1],
[2, 2, 3, 1],
[1, 3, 3, 2], 
[1, 2, 1, 1]
]
cilj = 2
vrne – število sosedov za vsak element:
[
[3, 3, 2, 1],
[2, 3, 4, 2],
[3, 3, 3, 0],
[1, 0, 2, 1]
]


4. naloga
Napišite funkcijo sosednji_znaki(niz), ki za vsak znak v seznamu nizov prešteje, koliko sosednjih znakov je enakih temu znaku (sosedi so levo, desno, spodaj in zgoraj). Funkcija naj vrne seznam z vrednostmi števila sosedov.
Primer:
niz = 
[
'abba', 
'bbca', 
'accb', 
'baba'] 
sosednji_znaki(niz) vrne 
[
[0, 2, 2, 1],
[1, 2, 1, 1],
[0, 1, 2, 0],
[0, 0, 0, 0]
]


5. naloga
Napišite program, ki uporablja globalno spremenljivko za štetje klicev funkcije. Funkcija naj ob vsakem klicu poveča vrednost globalne spremenljivke za 1 in jo izpiše.
Primer:
def funkcija():
	#Koda za štetje klicev funkcije
funkcija()
funkcija()
funkcija()
Izpis:
1
2
3


6. naloga
Napišite funkcijo, ki uporablja globalni števec za sledenje skupnemu številu klicev več različnih funkcij. Vsaka funkcija naj ob klicu poveča globalni števec za 1.


7. naloga
Napišite funkcijo, ki spremeni elemente globalnega seznama. Seznam naj bo globalno dostopen, funkcija pa naj doda seznamu doda naključno število [1, 10].


8. naloga
Napišite funkcijo kalkulacija(operacija, *args), ki sprejme poljubno operacijo (seštevanje, odštevanje, množenje, deljenje) in poljubno število številskih argumentov ter izvede matematično operacijo nad temi števili. 
Primer:
kalkulacija('sestej', 1, 2, 3, 4) vrne 10
kalkulacija(odstej, 10, 5, 2) vrne 3


9. naloga
Napišite funkcijo vse_vsote(*args), ki sprejme poljubno število števil in vrne seznam vseh možnih vsot, ustvarjenih z dodajanjem poljubnih dveh različnih števil iz seznama argumentov.
Primer:
vse_vsote(1, 2, 3) vrne [3, 4, 5]
vse_vsote(1, 2, 3, 4) vrne [3, 4, 5, 5, 6, 7]


10. naloga
Napišite funkcijo, ki lahko prejme poljubno število seznamov in vrne vse združene v en seznam.
Primer: 
print(naloga_10([1, 3, 5], [2, 3, 6], [0, 7, 5]))  # Izpiše: [1, 3, 5, 2, 3, 6, 0, 7, 5]


11. naloga
Napišite funkcijo, ki lahko prejme poljubno število argumentov. Ti argumenti so lahko posamezna števila, seznami, nizi... Funkcija naj vse numeične argumente združi v en »sploščen« seznam (flattened list)
Primer:
result = splosci(None, '1, [2, 3], 'adsf ', [4, [5, 'x ', 6]], 7)
print(result) # izpiše: 1, 2, 3, 4, 5, 6, 7


12. naloga
Napišite program, ki iz podane binarne matrike (matrika z elementi 0 in 1) poišče največji pravokotnik, sestavljen iz samih 1-k. Program naj izpiše velikost pravokotnika (število elementov v njem). 
Primer:
sez = [
[1, 0, 1, 1, 1],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 1, 0]
]
vrne 9 (pravokotnik velikosti 3x3, sestavljen iz samih 1-k)
"""





