# haikuGenerator.py

# Ask the user for the lines of the haiku
print('Welcome to the Haiku generator!')
print('Provide the first line of your haiku:')
haiku_ln1 = raw_input()
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

