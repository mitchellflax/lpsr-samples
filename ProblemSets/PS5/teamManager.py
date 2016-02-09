# a Player on a team has a name, an age, and a number of goals so far this season
class Player(object):

	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals

	def printStats(self):
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))

# default doesn't matter, we'll set it again
user_choice = 1
my_players = []

while user_choice != 0:
	print("What do you want to do? Enter the # of your choice and press Enter.")
	print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Print average number of goals for all players")
	print("(0) Leave the program and delete all players")
	user_choice = int(raw_input())

	# if the user wants to add a player, collect their data and make a Player object
	if user_choice == 1:
		print("Enter name:")
		player_name = raw_input()
		print("Enter age:")
		player_age = int(raw_input())
		print("Enter number of goals scored this season:")
		player_goals = int(raw_input())
		my_players.append(Player(player_name, player_age, player_goals))
		print("Ok, player entered.")

	# if the user wants to print the players, call printStats for each Player
	if user_choice == 2:
		print("Here are all the players...")
		for player in my_players:
			player.printStats()
	
	if user_choice == 3:
		# average = sum of all goals divided by count of players
		sum = 0
		count = 0
		for player in my_players:
			sum += player.goals
			count += 1
		avg = sum / count

		print("Average goals: " + str(avg))

