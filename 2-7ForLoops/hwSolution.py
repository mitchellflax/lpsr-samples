# create my initial list
friends = ['Ilana', 'Will', 'Kim', 'Dad', 'Lena']

# make a variable for numbering
i = 1

# for each friend, print the number and string
# then, increase the numbering var (i) by 1
for person in friends:
	print(str(i) + ". " + person)
	i = i + 1

# add 5 friends
friends.append('Angela')
friends.append('Dan')
friends.append('Wendy')
friends.append('Korien')
friends.append('Mallory')

friends.sort()
friends.reverse()

for person in friends:
	print(person)
