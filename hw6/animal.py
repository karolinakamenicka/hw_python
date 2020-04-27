with open('zvirata.txt', encoding = 'utf-8') as f:
    for line in f.readlines():
        animal = line.replace("\n", "")
        if len(animal) < 6:
            print(animal)