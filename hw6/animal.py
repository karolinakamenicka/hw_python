with open('zvirata.txt', encoding = 'utf-8') as file:
    
    def shortanimal(animal_stri):
        animal_stri = list(animal_stri)
        short_anim = []  
        for animal_one in animal_stri:
            if len(animal_one)<6:
                short_anim = short_anim.append(animal_one)
        return short_anim

    print(shortanimal(file))