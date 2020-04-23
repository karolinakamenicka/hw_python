def tah(pole,cislo_policka,symbol):
    pole = pole[:cislo_policka] +symbol+ pole[cislo_policka+1:]
    return pole

novepole = tah('---xx---oxx----ooo--',0, 'x')
print(novepole)
