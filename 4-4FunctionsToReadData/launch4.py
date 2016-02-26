class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

my_pets = []
my_pets.append(Pet("waldo", "parrot"))
my_pets.append(Pet("cyrus", "seal"))

pet_file = open("pets.petfile", "w")
for pet in my_pets:
    # you want this file to write each pet to your file on separate lines
    # write the line of code that will do this!
    pass

pet_file.close()
