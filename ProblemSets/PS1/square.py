import sys

# creates a variable called base_str, which is the string the user entered at the command line 
base_str = sys.argv[1]
# creates a variable called base_int and sets it equal to base_str, converted to an integer
base_int = int(base_str)

# prints base_int squared
print(base_int ** 2)
