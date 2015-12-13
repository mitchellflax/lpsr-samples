def square(x):
	return x ** 2

print("Here are the squares:")
oneToTen = range(1,11)

for num in oneToTen:
	print(num, square(num))
