vstup = input('Zadej tri cisla oddelena mezerou:')

mez = [i for i in range(len(vstup)) if vstup.startswith(' ', i)]

c1 = int(vstup[0:mez[0]])
c2 = int(vstup[mez[0]+1:mez[1]])
c3 = int(vstup[mez[1]+1:])
if c1+c2+c3 < 10:
    print('Soucet zadanych cisle je mensi nez 10')
else:
    print('Soucet zadanych cisel je vetsi nez deset')