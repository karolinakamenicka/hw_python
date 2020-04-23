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

#vyhodnot('---xx---oxx----ooo--')