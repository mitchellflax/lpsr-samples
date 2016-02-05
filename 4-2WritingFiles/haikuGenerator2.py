# haikuGenerator.py

import random

# Ask the user for the lines of the haiku
print('Welcome to the Haiku generator!')

print('Would you like to write your haiku from scratch or get a randomized first line?')
print('(1) I\'ll write it from scratch')
print('(2) Start me with a random line')
user_choice = int(raw_input())

# if the user wants to write from scratch, keep it simple
if user_choice == 1:
	print('Provide the first line of your haiku:')
	haiku_ln1 = raw_input()
# if the user is into getting a random starter, we have some work to do
else:
	# open the rando file and bring in the random lines
	starters_file = open('haikuStarters.txt', 'r')
	starters_list = []

	# get the starter lines and add them to a list
	line = starters_file.readline()
	while line: 
		starters_list.append(line)
		line = starters_file.readline()

	# spit the line back to the user
	print('All right, here\'s your first line:')
	haiku_ln1 = starters_list[random.randint(0,len(starters_list))]
	print(haiku_ln1)

print('Provide the second line of your haiku:')
haiku_ln2 = raw_input()
print('Provide the third line of your haiku:')
haiku_ln3 = raw_input()

# Ask the user for the filename
print('What file would you like to write your haiku to?')
filename = raw_input()

# Write the haiku to a file
my_file = open(filename, 'w')
my_file.write(haiku_ln1 + '\n')
my_file.write(haiku_ln2 + '\n')
my_file.write(haiku_ln3 + '\n')

# Success! Close the file.
my_file.close()
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")

