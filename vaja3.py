# Naloga 1. Napišite funkcijo stevilo_besed(niz), ki vrne število besed v danem nizu. Nalogo na dva načina, 
# prvi z zanko in drugi z uporabo metode split()
# Primer: stevilo_besed('Python je zabaven') vrne 3

def stevilo_besed(niz):
    dolzina = len(niz.split())
    print(dolzina)

def stevilo_besed2(niz):
    stevec = 1
    for i in range(len(niz)):
        if niz[i] == " ":
            stevec += 1
    print(stevec)


stevilo_besed("Zivijo svet.")
stevilo_besed2("Zivijo svet.")

# Naloga 2. Napišite funkcijo najdaljsa_beseda(niz), ki v danem nizu ugotovi, katera beseda je najdaljša in to besedo vrne.
# Primer:najdaljsa_beseda('Danes je čudovit dan za učenje novih stvari.') vrne čudovit

def najdaljsa_beseda(niz):
    niz = niz.split()
    maks = 0
    for i in range(len(niz)):
        if len(niz[i]) > maks:
            maks = len(niz[i])
            beseda = niz[i]
    return beseda
print(najdaljsa_beseda('Danes je čudovit dan za učenje novih stvari.'))

# Naloga 3. Napišite program, ki uredi elemente seznama glede na njihovo dolžino (od najkrajšega do najdaljšega).
# Primer: ['banana', 'jabolko', 'kivi'] -> [kivi, banana, jabolko]

elementi = ['banana', 'jabolko', 'kivi']
prev = 0
curr = 0
zacetek = 0
for i in range(len(elementi)):
    for i in range(zacetek,len(elementi)-1):
        prev = elementi[i]
        curr = elementi[i+1]
        if len(curr)<len(prev):
            elementi[i],elementi[i+1] = elementi[i+1],elementi[i]
print(elementi)


# Naloga 4. Napišite funkcijo prvo_vecje_prastevilo(n), ki poišče in vrne prvo praštevilo, ki je večje od n.
# Primer: prvo_vecje_prastevilo(10) vrne 11

def prvo_vecje_prastevilo(n):
    stevec = n
    while True:
        stevec += 1
        prime = True
        for i in range(2,n//2+1):
                if stevec%i == 0:
                    prime = False
        if prime == True:
            return stevec
print(prvo_vecje_prastevilo(109))

# Naloga 5. Napišite funkcijo piramida(n), ki izriše piramido z n vrsticami z uporabo zvezdic.
# Primer: piramida(5)

#     *
#    **
#   ***
#  ****
# *****

n = int(input("Vpisi n: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()


# Naloga 6. Napišite funkcijo Caesarjeva_sifra(niz, n), ki izvede Caesarjevo šifro nad danim nizom. Uporabnik vnese niz in število, s katerim naj se črke rotirajo (premaknejo po abecedi). Program naj rotira črke v nizu, ohrani pa presledke in ločila.
# Primer: Caesarjeva_sifra('hello world', 3) vrne 'khoor zruog'

def caesarjeva_sifra(niz, n):
    niz2=""
    for i in range(len((niz))):
        niz2 += chr(ord(niz[i])+n)
    print(niz2)
caesarjeva_sifra("a",3)

# Naloga 7. Napišite funkcijo mediana(sez), ki poišče mediano danega seznama števil, vendar brez uporabe vgrajene funkcije sort(). Poiščite mediano s pomočjo zanke in iskanja minimumov in maksimumov.
# Primer: mediana[7, 1, 3, 5, 9] vrne 5


# Naloga 8. Napišite funkcijo odstrani_podvojene(sez), ki iz danega seznama odstrani podvojene elemente.
# Primer: odstrani_podvojene([1, 2, 2, 3, 4, 4, 5] vrne [1, 2, 3, 4, 5]


# Naloga 9. Napišite funkcijo najdaljse_podzaporedje(sez), ki najde najdaljše naraščajoče podzaporedje v danem seznamu števil.
# Primer: sez = [3, 10, 2, 1, 20] vrne [3, 10, 20]


# Naloga 10. Napišite funkcijo prastevila(n), ki z uporabo Eratostenovega sita poišče vsa praštevila do števila n. Eratostenovo sito je algoritem, ki uporablja seznam za sledenje številom, ki so bila prečrtana kot deljiva.
# Primer: n = 30 vrne [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# Naloga 11. Napišite program, ki preveri, ali se lahko dani niz ciklično permutira v drugega. 
# Primeri: 
# 'abcde' in 'deabc' sta ciklična permutacija
# 'abc' in 'acb' nista ciklična permutacija


# Naloga 12. Napišite program, ki izpiše elemente podane matrike spiralno (začne se v zgornjem levem kotu in se premila v smeri urnega kazalca proti središču).
# Primer:
# [ [1, 2, 3], 
#   [4, 5, 6],
#   [7, 8, 9] ]
# Izpis: [1, 2, 3, 6, 9, 8, 7, 4, 5]
