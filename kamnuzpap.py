from random import randrange
vstup = input('Zadej kamen, nuzky nebo papir: ')
cislo = randrange(3)
if cislo == 0:
    pocitac = 'kamen'
elif cislo == 1:
    pocitac = 'nuzky'
else: 
    pocitac = 'papir'

print('Pocitac zadal: ' + pocitac)

if vstup == pocitac:
    vysledek = 'plichta'
elif (vstup == 'kamen' and pocitac == 'nuzky') or (vstup == 'nuzky' and pocitac =='papir') or (vstup =='papir' and pocitac =='kamen'):
    vysledek = 'vyhral jsi'
else :
    vysledek = 'vyhral pocitac'
print('Vysledek zapasu je: ' +vysledek)
