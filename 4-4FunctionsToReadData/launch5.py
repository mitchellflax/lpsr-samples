poem_file = open("poem.txt", "r")

my_line = poem_file.readline()

while my_line != "":
    my_words = my_line.split()
    print(my_words[0])
    my_line = poem_file.readline()

poem_file.close()
