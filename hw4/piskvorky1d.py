from tah_pocitace import tah_pocitace 
from piskvorky import vyhodnot 
from tah_hrace import tah_hrace 


def piskvorky1d():
    pole = '--------------------'
    b = 2
    print('aktualni pole: '+ pole)
    while True:
        
        if b%2 == 0:
            pole = tah_hrace(pole, int(input('zadej policko tahu, jsi x: ')))
        else: 
            pole = tah_pocitace(pole)
            print('Hral pocitac')
        
        print('aktualni pole: '+ pole)
        if vyhodnot(pole)== 1:
            print('vyhral pocitac')
            return
        elif vyhodnot(pole)== 2:
            print('vyhral jsi')
            return
        elif vyhodnot(pole)== 3:
            print('konec hry nikdo nevyhral')
            return
        b = b+1
        
piskvorky1d()