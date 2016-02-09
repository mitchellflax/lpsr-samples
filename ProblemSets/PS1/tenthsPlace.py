aDecimal = 5.67

# multiply by ten to move the decimal place one to the right
tenTimesADecimal = 10 * aDecimal

# chop everything to the right of the decimal place
# by converting to an int
tenTimesADecimal  = int(tenTimesADecimal)

# move the decimal place back to the left
aDecimal = tenTimesADecimal * .1 
print(aDecimal)

