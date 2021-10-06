# passing reference

def pets(someParameter):
    someParameter.append('Dog')


animal = [1, 2, 3]
pets(animal)
print(animal)



