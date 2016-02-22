print("What's your middle name?")
mname = raw_input()
print("What's the name of the street where you grew up?")
street = raw_input()

myFile = open('spynames.txt', 'a')
myFile.write(mname + " " + street + '\n')
# myFile.close()
