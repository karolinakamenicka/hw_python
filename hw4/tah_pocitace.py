from random import randrange
def tah_pocitace(pole):
    a = 0
    while a ==0:
        cislo_policka = randrange(len(pole))
        if pole[cislo_policka]== '-':
            pole = pole[:cislo_policka]+ 'o'+ pole[cislo_policka+1:]
            a = 1
    return pole

print(tah_pocitace('------------'))
    