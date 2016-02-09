# PS 3 number 4 solution
# written by Mr. Flax @ LPS Richmond

# welcome the user
print("Welcome to Josephina's Quest!")

# get the inputs from the user for name, strength, health, luck
print("Enter the name of your character:")
name = raw_input()

print("Enter strength (1-10):")
strength = int(raw_input())

print("Enter health (1-10):")
health = int(raw_input())

print("Enter luck (1-10):")
luck = int(raw_input())

# check if the user's values add up to a max of 15
if strength + luck + health > 15:
  # if too much, set each one to 5 and tell user
  strength = 5
  luck = 5
  health = 5
  print("You have given your character too many points!")
  print("Default values have been assigned, " + name + ":")
  print("strength: " + str(strength) + ", health: " + str(health) + ", luck: " + str(luck))
else:
  # otherwise, just report back the scores for the user
  print("Ok, your values have been set, " + name + ":")
  print("strength: " + str(strength) + ", health: " + str(health) + ", luck: " + str(luck))


# now, we come to a fork in the road
# ask the user if they want to go 'left' or 'right'
print(name + ", you've come to a fork in the road. Do you want to go right or left? Enter 'right' or 'left'.")
forkChoice = raw_input()

# if they fork right, decide based on health
# otherwise, decide based on strength
if forkChoice == "right":
  if health < 6:
    print(name + ", you met a dragon in the road, but your health wasn't high enough to survive its fire breath. You lost the game!")
  else:
    print(name + ", congratulations! You escaped from a dragon and won the game!")
else:
  if strength > 6:
    print(name + ", congratulations! You climbed the big mountain and won the game!")
  else:
    print(name + ", your strength wasn't high enough, and you collapsed on the mountain. You lost the game!")
    
print("Game over. Please play again!")
