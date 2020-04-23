
def tah_hrace(pole, cislo_policka):
    i=0
    while i == 0 :
        if cislo_policka <0 :
            print('Zadal jsi spatne cislo')
            
        elif cislo_policka>= len(pole):
            print('Zadal jsi spatne cislo')
           
        elif pole[cislo_policka] != '-':
            print('Zadal uz obsazene')
            print('pole vypada: '+ pole)
            
        else: 
            pole = pole[:cislo_policka] +'x'+ pole[cislo_policka+1:]
            a=1
            break
        cislo_policka= int(input('zadej nove cislo'))
    return pole

#pole2 = tah_hrace('x------------------', int(input('zadej pozici hrani')))

##print(pole2)