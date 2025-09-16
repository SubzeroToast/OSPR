"""
OSPR2 – vaje/praksa
Vaja 02  - vaja za ponovitev (operatorji in odločitveni stavki) 
"""


# 1. naloga
# Napišite program, ki preveri hitrost vozila in na podlagi tega izpiše opozorilo. Upoštevaj naslednja pravila:
# •	Če je hitrost manjša od 30 km/h, izpiši 'Prepočasi!'
# •	Če je hitrost med 30 km/h in 50 km/h, izpiši 'V mejah dovoljene hitrosti.'
# •	Če je hitrost med 50 km/h in 90 km/h, izpiši Povišana hitrost, bodi previden!'
# •	Če je hitrost med 90 km/h in 130 km/h, izpiši Visoka hitrost, lahko dobiš kazen!'
# •	Če je hitrost več kot 130 km/h, izpiši 'Kaznovan boš!'
# Poskrbite, da ne boste imeli nepotrebnih preverjanj.

hitrost = int(input("Vpisi hitrost vozila: "))
if hitrost < 30:
    print("Prepocasi!")
elif hitrost > 29 and hitrost < 51:
    print("V mejah dovoljene hitrosti.")
elif hitrost > 50 and hitrost < 91:
    print("Povišana hitrost, bodi previden!")
elif hitrost > 90 and hitrost < 131:
    print("Visoka hitrost, lahko dobiš kazen!")
elif hitrost > 130:
    print("Kaznovan boš!")



# 2. naloga
# Napišite funkcijo obdavčenje(placa), ki izračuna mesečno plačo po progresivni davčni lestvici. Funkcija prejme bruto plačo in vrne davek, ki ga je potrebno plačati glede na naslednje meje:
# •	Do 1000 EUR se plača 10% davka.
# •	Od 1000 EUR do 2000 EUR se plača 20% davka.
# •	Nad 2000 EUR se plača 30% davka. 
# Poskrbite, da ne boste imeli nepotrebnih preverjanj.

def obdavcevanje(placa):
    if placa < 1001 and placa > 0:
        davek = placa * 0.1
    elif placa > 1000 and placa < 2001:
        davek = placa * 0.2
    else:
        davek = placa * 0.3
    return davek
davek = obdavcevanje(int(input("Vpisi koliko denarja si zasluzil: ")))
print(f"Obdavcitev je {davek} evrov.")


# 3. naloga
# Napišite program, ki preveri, ali je vneseno geslo veljavno. Veljavnost gesla je določena z naslednjimi pogoji:
# •	Dolžina gesla mora biti vsaj 8 znakov
# •	Vsebuje vsaj eno veliko črko
# •	Vsebuje vsaj eno malo črko
# •	Vsebuje vsaj eno številko 
# •	Vsebuje vsaj en poseben znak (!, @, #, $, %)

geslo = input("Vpisi geslo: ")
male = False
velike = False
simboli = False
stevilke = False
simboli_sez = "][\';!@#$%^&*(+_)\':[]"
stevilke_sez = "123456789"

for i in range(len(geslo)):
    if geslo[i].isupper():
        velike = True
    elif geslo[i].islower():
        male = True
    elif geslo[i] in simboli_sez:
        simboli = True
    elif geslo[i] in stevilke_sez:
        stevilke = True

if male and velike and simboli and stevilke and len(geslo)>7:
    print("Varno geslo!") 
else:
    print("Geslo ni varno!")
#koda za bruhat, popravi pozneje

# 4. naloga
# Napišite program za igraje igre 'Kamen, škarje, papir' med uporabnikom in računalnikom. Program naj določi zmagovalca.

import random

user = input("Vpisi kamen, skarje ali papir: ")
match user:
    case "kamen":
        indeks = 0
    case "skarje":
        indeks = 1
    case "papir":
        indeks = 2
seznam = ["kamen", "skarje", "papir"]
gamba = random.randint(1,3)
if gamba == 1:
    print(f"Remi! Racunalnik je odigral {user}.")
elif gamba == 2:
    print(f"Zmagal si! Racunalnik je odigral {seznam[(indeks+1)%3]}")
else:
    print(f"Zmagal si! Racunalnik je odigral {seznam[(indeks-1)%3]}")


# 5. naloga
# Napišite funkcijo kalulator(sez), ki uporablja match-case za izračun aritmetičnih izrazov, podanih kot seznam. Funkcija torej prejme seznam v obliki [operator, stevilo1, stevilo2], kjer je prvi element operator, ostala dva pa sta operanda ter vrne rezultat. 

seznam = ["+",17,5]
def kalkulator(sez):
    match sez[0]:
        case "*":
            return sez[1]*sez[2]
        case "-":
            return sez[1]-sez[2]
        case "+":
            return sez[1]+sez[2]
        case "/":
            return sez[1]/sez[2]
        case _:
            return "Operator ni podpiran."
print(kalkulator(seznam))


# 6. naloga
# Napišite funkcijo nadgradnjaKalkulatorja(sez), ki funkcijo iz prejšnje naloge nadgradi tako, da izračuna tudi gnezdene izraze. 
# Primer:
# nadgradnjaKalkulatorja(['+', 3, ['*', 2, 5]]) vrne 13

seznam = ["+",['*',3,4],5]
def nadgradnjaKalkulatorja(sez):
    if len(sez[1]) > 2:
        match sez[1][0]:
            case "*":
                rezultat = sez[1][1]*sez[1][2]
            case "-":
                rezultat = sez[1][1]-sez[1][2]
            case "+":
                rezultat = sez[1][1]+sez[1][2]
            case "/":
                rezultat = sez[1][1]/sez[1][2]
        match sez[0]:
            case "*":
                rezultat = rezultat*sez[2]
            case "-":
                rezultat = rezultat-sez[2]
            case "+":
                rezultat = rezultat+sez[2]
            case "/":
                rezultat = rezultat/sez[2]
        return rezultat
    elif len(sez[2]) > 2:
        match sez[2][0]:
            case "*":
                rezultat = sez[2][1]*sez[2][2]
            case "-":
                rezultat = sez[2][1]-sez[2][2]
            case "+":
                rezultat = sez[2][1]+sez[2][2]
            case "/":
                rezultat = sez[2][1]/sez[2][2]
        match sez[0]:
            case "*":
                rezultat = rezultat*sez[1]
            case "-":
                rezultat = rezultat-sez[1]
            case "+":
                rezultat = rezultat+sez[1]
            case "/":
                rezultat = rezultat/sez[1]
        return rezultat
    else:
         match sez[0]:
            case "*":
                return sez[1]*sez[2]
            case "-":
                return sez[1]-sez[2]
            case "+":
                return sez[1]+sez[2]
            case "/":
                return sez[1]/sez[2]

print(nadgradnjaKalkulatorja(seznam))


# 7. naloga
# Napišite program, ki preveri, ali je dan, mesec in leto veljavno. Upoštevaj dejansko število dni v posameznem mesecu, prav tako tudi to, da ima februar v navadnem letu 28 dni, v prestopnem letu pa 29 dni.

dan = int(input("Vpisi dan: "))
mesec = int(input("Vpisi mesec: "))
leto = int(input("Vpisi leto: "))
tocke = 0
mesci = [31,28,31,30,31,30,31,31,30,31,30,31]
if leto%4 == 0:
    if leto%100 == 0:
        if leto%400 == 0:
            prestopno = True
        else:
            prestopno = False
    else:
        prestopno = True
else:
    prestopno = False

if mesec == 2:
    if not(prestopno):
        if dan > 0 and dan < 29:
            pass
        else:
            print("Neveljaven vnos")
            quit()
    if prestopno:
        if dan > 0 and dan < 30:
            pass
        else:
            print("Neveljaven vnos")
            quit()
elif mesec < 13 and mesec > 0:  
    if dan <= mesci[mesec-1]:
        pass
    else:
        print("Neveljaven vnos")
        quit()      
else:
    print("Neveljaven vnos")
    quit()
print("Veljaven datum!")
# 8. naloga
# Napiši funkcijo magicen_kvadrat(sez), ki prejeme 2D seznam velikosti 3x3 in vrne True, če predstavlja 2D seznam magičen kvadrat in False, če ne. Magičen kvadrat je matrika, kjer je vsota števil v vsaki vrstici, stolpcu in diagonalah enaka. 
# Primer magicen_kvadrat([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) vrne True

seznam = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

def magicen_kvadrat(seznam):
    rezultat = seznam[0][0]+seznam[1][0]+seznam[2][0]
    for j in range(3):
        if not(rezultat == seznam[0][j]+seznam[1][j]+seznam[2][j]):
            return "Ni magicen kvadrat!"
        if not(rezultat == seznam[j][0]+seznam[j][1]+seznam[j][2]):
            return "Ni magicen kvadrat!"
    if not(rezultat == seznam[0][0]+seznam[1][1]+seznam[2][2]):
        return "Ni magicen kvadrat!"
    if not(rezultat == seznam[0][2]+seznam[1][1]+seznam[2][0]):
        return "Ni magicen kvadrat!"
    return "Je magicen kvadrat!"

print(magicen_kvadrat(seznam))


# 9. naloga
# Napišite program, ki pretvori dano število med 1 in 99 v besedo. 
# Primeri:
# 456 – štiri sto šestinpetdeset
# 123 – sto triindvajset
# Nasvet: Za vsako številko (1-9), desetico (10-90) in posebne primere (11-19) uporabite ločene if-else pogoje za pravilno sestavljanje besede.

stevilo = input("Vpisi stevilo za izpis v besedah [1-99]: ")
enice = ["ena","dva","tri","stiri","pet","sest","sedem","osem","devet"]
desetice = ["deset","dvajset","trideset","stirideset","petdeset","sestdeset","sedemdeset","osemdeset","devetdeset"]
najst = ["enajst","dvanajst","trinajst","stirinajst","petnajst","sestnajst","sedemnajst","osemnajst","devetnajst"]

def izpis(stevilo):
    if len(stevilo) == 1:
        return enice[int(stevilo)-1]
    elif len(stevilo) == 2:
        if int(stevilo)%10 == 0:
            return desetice[int(stevilo)//10-1]
        elif int(stevilo) > 10 and int(stevilo) < 20:
            return najst[int(stevilo[1])-1]
        else:
            return enice[int(stevilo[1])-1] + "in" + desetice[int(stevilo[0])-1]
    else:
        return "Napaka pri vnosu."

print(izpis(stevilo))

# 10.	naloga
# Napišite program, ki sprejme dva časa v obliki ur in minut in izračuna razliko med njima. Program naj preveri še, če je drugi čas pred prvim in v tem primeru izpiše napako.
ura1 = int(input("Vpisi uro: "))
minuta1 = int(input("Vpisi minuto: "))
ura2 = int(input("Vpisi uro 2: "))
minuta2 = int(input("Vpisi minuto 2: "))
if not(ura2 <= ura1 and minuta2 < minuta1):
    razlika_ur = ura2 - ura1
    razlika_minut = minuta2 - minuta1
    if razlika_minut < 0:
        razlika_ur -= 1
        razlika_minut += 60
    print(f"Razlika je {razlika_ur} ur in {razlika_minut} minut.")
else:
    print("Napaka, ura2 je pred uro1.")

# 11. naloga
# Napišite funkcijo veljavna_bančna(stevilka_bancne), ki preveri, ali je podana številka kreditne kartice veljavna in to tudi vrne v obliki True/False. Uporabite osnovno validacijo Luhnovega algoritma:
# •	Obrnite številko kartice
# •	Pomnožite vsako drugo številko z 2. Če je rezultat večji od 9, odštejte 9.
# •	Seštejte vse števke.
# •	Če je vsota deljiva z 10, je številka veljavna.
# Primer:
# veljavna_bancna(79927398713) vrne True
# veljavna_bancna(1234567812345670) vrne False

kartica = "79927398713"
def veljavna_bancna(kartica):
    kartica = kartica[::-1]
    novo = []
    for i in range(len(kartica)):
        if i%2 == 1:    
            kartica_racun = int(kartica[i])*2
        else:
            kartica_racun = kartica[i]
        if int(kartica_racun) > 9:
            kartica_racun -= 9    
        novo.append(int(kartica_racun))
    if sum(novo)%10 == 0:
        return True
    else:
        return False
print(veljavna_bancna(kartica))

# 12.	naloga
# Napišite funkcijo pretvorba(rimsko), ki prejme rimsko število in ga pretvori v arabsko ter ta rezultat vrne. Rimske številke se zapišejo s simboli: I (1), V (5), X(10), L (50), C (100), D (500), M (1000). Pazite še na posebnosti, kjer je potrebno vrednosti odšteti (IV = 4, IX = 9).
# Primer: pretvorba('MCMXCIV) vrne 1994
# """
