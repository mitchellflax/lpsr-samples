# Make string telling people 5 top friends and family plus make list for names and numbers
print("These are the 5 friends and family I spend the most time with:")
FF = ["Ivan", "Carlos", "Ramiro", "Angela", "Mom"] 
Num = [ 1,2,3,4,5]
print(FF)

for words,numbers in zip(FF,Num):
    print(str(numbers) + "." + words)


# Adds new variables to the list such as the new 5 names and five new numbers
FF.append("Sergio")
FF.append("Dad")
FF.append("Dani")
FF.append("Vanessa")
FF.append("Fernando")
Num.append(6)
Num.append(7)
Num.append(8)
Num.append(9)
Num.append(10)

# sorts new list from alphabetical and then reverses the order
FF.sort()
FF.reverse()

#prints the words in FF and used zip to get two lists together
for words,numbers in zip(FF,Num):
    print(str(numbers) + "." + words)


