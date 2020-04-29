with open('zvirata.txt', encoding = 'utf-8') as f:
    anim_str = []
    for line in f.readlines():
            animal = line.replace("\n", "")
            anim_str.append(animal)

with open('zvirata2.txt', encoding = 'utf-8') as f2:
    anim_str2 = []
    for line in f2.readlines():
            animal = line.replace("\n", "")
            anim_str2.append(animal)

def more_list(a,b):
    list_cup = list(set(a).union(set(b)))
    list_minusab = list(set(a).difference(set(b)))
    #list_minusba = list(set(b).difference(set(a)))
    return list_cup,list_minusab #list_minusba

def test_more_list():
    assert more_list([0,1,2,3],[2,3,4]) == ([0,1,2,3,4], [0,1])
