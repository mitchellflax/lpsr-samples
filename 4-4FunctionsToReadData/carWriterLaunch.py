make = "Honda"
model = "Civic"
color = "Green"
year = 2015

carFile = open("cars.txt", "a")
carFile.write(make + " " + model + " " + color + " " + str(year) + "\n")
carFile.close()

#Q1: Why did I add '\n' at the end of line 7?
#Q2: Suppose I run the python script, then change the variables in line 1-4 for an orange 2011 GMC Denali.
# After I run the script again, what will I see when I run "cat cars.txt" at the command line?
