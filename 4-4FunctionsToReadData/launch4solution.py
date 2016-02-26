class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

my_pets = []
my_pets.append(Pet("waldo", "parrot"))
my_pets.append(Pet("cyrus", "seal"))

pet_file = open("pets.petfile", "w")
for p in my_pets:
    pet_file.write(p.name + " " + p.species + "\n")

pet_file.close()
