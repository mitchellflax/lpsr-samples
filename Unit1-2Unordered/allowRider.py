# get user age
print("How old are you?")
age = int(input())

# get user height
print("How many inches tall are you?")
height = int(input())


# if tall enough to ride, allow it
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
# if not, tell the user they are out of luck
else:
	print("Sorry, you can't ride.")

