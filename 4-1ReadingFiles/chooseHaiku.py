print('Hi, welcome to the Haiku Reader!')
print('Choose...')
print('(3) For a haiku about a silly person.')
print('(4) For a haiku about writing haikus.')
choice = int(raw_input())

if choice == 3:
	my_haiku = open('haiku3.txt', 'r')
else:
	my_haiku = open('haiku4.txt', 'r')

print(my_haiku.read())

my_haiku.close()
