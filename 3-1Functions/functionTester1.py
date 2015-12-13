def doubleIt(myNum):
  myResult = myNum * 2
  return myResult
 
print(doubleIt(3))
print(doubleIt(5))
 
print("Enter a number.")
num = int(raw_input())
print("Ok, here you go: " + str(doubleIt(num)))
