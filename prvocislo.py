cislo= int(input('Zadej cislo'))
a = 0
for i in range(cislo-2):
    if cislo%(i+2) ==0:
        a = 1
if a ==0:
    print('je prvocislo.')
else:
    print('Neni prvocislo.')
    
