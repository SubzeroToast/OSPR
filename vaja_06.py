# OSPR2 – vaje/praksa
# Vaja 06 - vaja za ponovitev (seznami) 
# VSE NALOGE REŠUJTE S FUNKCIJAMI, KO ODDAJATE KODO NAJ BODO ZAKOMENTIRANA NAVODILA IN KLICI VAŠIH FUNKCIJ (FUNKCIJE SAME NAJ NE BODO ZAKOMENTIRANE)


# 1. Naloga
# Napišite funkcijo uredi_po_dolzini(seznam), ki prejme seznam nizov in ga uredi glede na dolžino nizov od najkrajšega do najdaljšega. Uporabite mehurčkasto urejanje (bubble sort).
# Primer:
# uredi_po_dolzini(['banana', 'borovnica', 'jabolko', 'kivi']) vrne ['kivi', 'banana', 'jabolko', 'borovnica']

elementi = ['banana', 'borovnica', 'jabolko']
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

# 2. Naloga
# Napišite funkcijo uredi_po_zadnji_crki(seznam), ki prejme seznam nizov in ga uredi glede na zadnjo črko vsakega niza. Urejeno naj bo od ž do a. Uporabite urejanje z vstavljanjem (insertion sort).
# Primer:
# uredi_po_zadnji_crki(['jabolko', 'kivi', 'banana', 'breskev'] vrne ['breskev', 'jabolko', 'kivi', 'banana']

def uredi_po_zadnji_crki(seznam):
    for i in range(1,len(seznam)):
        for j in range(len(seznam)):
            if seznam[i-j][-1] < seznam[i-j-1][-1]:
                seznam[i-j],seznam[i-j-1] = seznam[i-j-1],seznam[i-j]
            else:
                break
    return seznam[::-1]
print(uredi_po_zadnji_crki(['jabolko', 'kivi', 'banana', 'breskev']))

# 3. Naloga
# Napišite funkcijo uredi_in_filtriraj(seznam, meja), ki uredi tiste elemente seznama, ki so večji kot podana meja. Elemente seznama, ki niso večji od podane meje naj iz seznama izloči. Uporabite urejanje z izbiranjem (selection sort).
# Primer:
# uredi_in_filtriraj([3, 1, 9, 1, 5, 4, 2], 3) vrne [4, 5, 9]

# 4. Naloga
# Napišite funkcijo uredi_po_max(seznam), ki prejme ugnezden seznam in ga uredi glede na največjo vrednost v vsakem ugnezdenem seznamu.
# Primer:
# uredi_po_max([[3, 1], [7, 5, 8], [2, 9]] vrne [[3, 1], [7, 5, 8], [2, 9]]

# 5. Naloga
# Napišite funkcijo uredi_2D(seznam), ki prejme dvodimenzionalni (ugnezdeni) seznam in uredi vsako vrstico posebej po naraščajočem vrstnem redu. Funkcija naj vrne nov urejen seznam.
# Primer:
# uredi_2D([3, 2, 1], [6, 5, 4], [8, 9, 7]] vrne [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def uredi_2D(seznam):
    sez = []
    for i in seznam:
        i.sort()
        sez.append(i)
    return sez
print(uredi_2D([[3, 2, 1],[6, 5, 4],[8, 9, 7]]))

# 6. Naloga 
# Napišite funkcijo uredi_po_povprecju(seznam), ki prejme ugnezden seznam in ga uredi glede na povprečno vrednost elementov v vsakem ugnezdenem seznamu.
# Primer:
# uredi_po_povprecju([3, 5], [1, 2, 3], [10, 0]] vrne [[1, 2, 3], [3, 5], [10, 0]]

def povp(e):
    return e

def uredi_po_povprecju(seznam):
    sez = []
    for i in seznam:
        i.sort(key=povp)
        sez.append(i)
    return sez
print(uredi_po_povprecju([[3, 5], [1, 2, 3], [10, 0]]))

# 7. Naloga
# Napišite funkcijo poisci_element(seznam, element), ki preveri, ali se element nahaja v padajoče urejenem seznamu. V kolikor se element nahaja v seznamu naj funkcija vrne mesto, kjer se le-ta nagaja, sicer pa naj vrne -1.
# Primer: 
# poisci_element([30, 25, 20, 15, 10, 5], 5) vrne 6

# 8. Naloga
# Napišite funkcijo poisci_palindrome(niz), ki prejme niz dolžine vsaj 2 in poišče vse palindrome v njem. Funkcija naj vrne seznam vseh palindromov.
# Primer:
# poisci_palindrome('mkdmadamprvlevelkdrnoonkdc') vrne['ada', 'level', 'eve', 'noon', 'oo')

# 9. Naloga
# Napišite funkcijo odstrani_dvojnike(sez), ki vrne seznam z odstranjenimi ponovitvami elementov. Elemente iz seznama odstranite brez, da ustvarite nov seznam.
# Primer:
# odstrani_dvojike([3, 9, 'ab', 5, 'mmm', 0, 9, 'lda', 'mmm', 0]) vrne [3, 9, 'ab', 5, 'mmm', 0, 'lda']

# 10. Naloga
# Napišite funkcijo podseznami_z_vsoto(seznam, cilj), ki poišče in vrne vse podsezname v seznamu, katerih vsota je enaka podanemu cilju.
# Primer:
# podseznami_z_vsoto([1, 2, 3, 4, 5], 9) vrne [[2, 3, 4], [4, 5]]

# 11. Naloga
# Napišite funkcijo najpogostejsi_element(seznam), ki prejme seznam in poišče elemet, ki se v seznamu najpogosteje pojavlja. Če je v seznamu več elementov z enakim številom pojavitev, vrni tistega z najnižjo vrednostjo.
# Primer:
# najpogostejsi_element([1, 3, 2, 3, 2, 2, 4]) vrne 2

# 12. Naloga
# Napišite funkcijo najdaljse_zaporeje(seznam), ki vrne najdaljše naraščajoče zaporedje elementov.
# Primer:
# najdaljse_zaporedje([1, 2, 3, 5, 2, 3, 6, 8, 10, 5, 6, 4, 8, 10]) vrne [2, 3, 6, 8, 10]