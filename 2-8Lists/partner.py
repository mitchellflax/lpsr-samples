colors = ["red", "blue", "green", "purple"]
ages = [14, 15, 15, 16, 16, 13, 18, 14, 15, 15, 14]

# 1 - what happens when you print a list?
print(colors)

# 2 - how do you do something for each item in a list?
for current_color in colors:
	print(current_color)

# 3 - how do we access a specific item of a list?
print(colors[2])
print(colors[1])
print(ages[5])

# 4 - how do we change the value of a specific item in a list?
print(colors)
colors[2] = "orange"
print(colors)

# 5 - how do we remove an item from the list?
print(colors)
del colors[2]
print(colors)

# 6 - what happens when we use the + operator  on a list?
print(colors)
kitchenSink = colors + ages
print(kitchenSink)

# 7 - what happens when we use the * operator  on a list?
print(colors)
colors = colors * 3
print(colors)




