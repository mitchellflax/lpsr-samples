# this should be in the folder...
# class-samples/4-1ReadingFiles
# and named fileReader.py

# shows how file reading works in python

# make a file object
myHaiku = open("haiku1.txt", "r")

print(myHaiku.read())

myHaiku.close()

