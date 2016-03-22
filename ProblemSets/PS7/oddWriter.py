# oddWriter.py
# a little program to write the odds from 1 to 100 to file

def isOdd(myNum):
    if myNum % 2 == 0:
        return False
    return True

myFile = open("odds.txt", "w")
for n in range(1, 101):
    if isOdd(n):
        myFile.write(str(n) + "\n")

myFile.close()

