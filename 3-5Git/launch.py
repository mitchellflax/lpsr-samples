import random

reindeer = ['Rudolph', 'Donner', 'Blitzen', 'Dancer', 'Prancer', 'Comet']
count = 0
while count < 10:
	index = random.randint(0,6)
	print(reindeer[index])
	count = count + 1
