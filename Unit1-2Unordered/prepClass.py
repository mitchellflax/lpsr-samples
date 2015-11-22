# we're running an ACT prep class
# ask the user for their ACT score
print("Hi! What's your ACT score?")
score = int(input())


if score >= 1 and score < 26:
  print("Welcome to ACT prep class!")
elif score < 30:
  print("Thanks for coming, but you probably don't need this class.")
elif score == 32:
  print("Whoa, you *really* don't need this class. Nice work.")
else:
  print("You must be lying. The top score on the ACT is 32!")