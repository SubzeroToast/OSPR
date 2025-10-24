glasovalka = ["Španija", "Norveška", "Slovenija"]
prejemnica = ["Gruzija", "Švedska", "Danska"]
tocke = [3, 12, 4]
leto = [2007, 2013, 2019]

def kratica(prejemnica,leto,indeks=2):
    print(f"{leto[indeks]}-{prejemnica[indeks][0:3]}")
    
 
 
#kratica(prejemnica,leto,2)

def izpis(glasovalka,prejemnica,tocke,leto,lt):
    if lt in leto:
        for i in range(len(leto)):
            if leto[i] == lt:
                indueks = i
        print(f"{lt}:{glasovalka[indueks]}->{prejemnica[indueks]}({tocke[indueks]})")
    else:
        print(f"{lt}:ni zapisov")
#izpis(glasovalka,prejemnica,tocke,leto,2025)