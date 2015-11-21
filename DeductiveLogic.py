from sys import argv

# Gets the file from the user
script, read_file = argv

# Creates a dictionary from the given file where the keys are the variables and 
# the equation and the values are the values of the given variable. Should try
# to store it as a boolean value (True or False) for each variable rather then
# a string as it would be when directly read of the file. Should also be able
# to recognize if the variables given are ill-formed (cannot be defined). The
# output will be the dictionary created.
def store(read_file):
	boolean_dict = {}
	return boolean_dict

# This will compute the Equation given in the file. The output should be printed
# as follows: [The equation] = [The value]
def compute(boolean_dict):
	pass

# Runs the functions with the input given
boolean_dict = store(read_file)
compute(boolean_dict)