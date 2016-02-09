# the one and only place where the numbers are set and appear
donuts = 92
people = 21

# create string versions for printing
donuts_str = str(donuts)
people_str = str(people)

# calculate the right number of donuts per person
donuts_per_person = donuts / people
donuts_per_person_str = str(donuts_per_person)

# print the results, neatly
print("Our party has " + people_str + " people and " + donuts_str + " donuts.")
print("Each person at the party gets " + donuts_per_person_str + " donuts.")
