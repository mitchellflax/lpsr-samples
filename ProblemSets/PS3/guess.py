import random

# choose random number
magic_num = random.randint(1,1000)

#debugging!
print(magic_num)

print("I'm thinking of a number between 1 and 1000. Enter your guess!")

guess = int(raw_input())

while guess != magic_num:
	if guess > magic_num:
		print("Nope, too high! Guess again.")
	else:
		print("Nope, too low! Guess again.")
	guess = int(raw_input())

print("Hooray, you won!")
	
