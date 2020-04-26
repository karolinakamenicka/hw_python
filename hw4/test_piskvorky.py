from ai import tah_pocitace 

def vyhodnot(stri):
    a = 0
    for i in range(len(stri)-2):
        if stri[i]== 'o' and stri[i+1]== 'o' and stri[i+2]== 'o':
          #print('vyhral kolecko')
          a = 1
        elif stri[i]== 'x' and stri[i+1]== 'x' and stri[i+2]== 'x':
           # print('vyhral krizek')
            a = 2


    if stri.find('-')==-1 and a==0:
      #print('nikdo nevyhral, konec hry')   
      a = 3  
    #elif a==0:
      #print('nikdo zatim nevyhral, hra neskoncila')
    return a 

def test_vyhodnot():
    assert vyhodnot('---xxx---') == 2
    assert vyhodnot('ooo-') == 1
    assert vyhodnot('oxox') == 3


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

def test_tah_hrace():
    assert tah_hrace('---x--',0) == 'x--x--'


def piskvorky1d():
    pole = '--------------------'
    konec = False
    b = 2
    print('aktualni pole: '+ pole)
    while konec ==False: 
        
        if b%2 == 0:
            pole = tah_hrace(pole, int(input('zadej policko tahu, jsi x: ')))
        else: 
            pole = tah_pocitace(pole)
            print('Hral pocitac')
        
        print('aktualni pole: '+ pole)
        if vyhodnot(pole)== 1:
            print('vyhral pocitac')
            konec = True
        elif vyhodnot(pole)== 2:
            print('vyhral jsi')
            konec = True
        elif vyhodnot(pole)== 3:
            print('konec hry nikdo nevyhral')
            konec = True
        b = b+1









        