# get the users' shows

print("Enter your 5 favorite TV shows.")

# start with a counter, i, and an empty list
i = 1
showList = []

# each time through the loop, ask the user for a new show
while i <= 5:
	print("Enter a show name:")
	showList.append(raw_input())
	i = i + 1

# give user back the raw list
print("OK, here's what you entered:")
print(showList)

# add a couple of important shows and sort the list
showList.append("The Wire")
showList.append("Breaking Bad")
showList.sort()

# number the list and output each show on a numbered line
i = 1
print("We've added a couple of important shows. Here's your list:")
for show in showList:
	print(str(i) + ". " + show)
	i = i + 1
