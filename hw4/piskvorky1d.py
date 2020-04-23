from tah_pocitace import tah_pocitace 
from piskvorky import vyhodnot 
from tah_hrace import tah_hrace 


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
        
piskvorky1d()