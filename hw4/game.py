from random import randrange
i=0
j=0
k=0
randomnum =0
randomnum2 =0
randomnum3 =0
while randomnum != 6:
    randomnum = randrange(6)+1
    i =i+1
while randomnum2 != 6:
    randomnum2 = randrange(6)+1
    j =j+1
while randomnum3 != 6:
    randomnum3 = randrange(6)+1
    k =k+1   

print('prvni hrac potreboval hodu '+str(i)) 
print('druhy hrac potreboval hodu '+str(j)) 
print('treti hrac potreboval hodu '+str(k)) 

if i >= j:
    if i >=k:
        print('vyhral prvni hrac')
    else:
        print('vyhral treti hrac')
else:
    if j>= k: 
        print('vyhral druhy hrac')
    else:
        print('vyhral treti hrac')   

        