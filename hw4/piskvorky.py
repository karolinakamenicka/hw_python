def vyhodnot(stri):
    a = 0
    for i in range(18):
        if stri[i]== 'o' and stri[i+1]== 'o' and stri[i+2]== 'o':
          print('vyhral kolecko')
          a = 1
        elif stri[i]== 'x' and stri[i+1]== 'x' and stri[i+2]== 'x':
            print('vyhral krizek')
            a = 1


    if stri.find('-')==-1 and a==0:
      print('nikdo nevyhral, konec hry')     
    elif a==0:
      print('nikdo zatim nevyhral, hra neskoncila')

vyhodnot('---xx---oxx----ooo--')