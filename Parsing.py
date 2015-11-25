from sys import argv

script, read_string = argv

# Creates two dictionarys, one for the variables and its values and another dictionary
# for the equation and the formula.
def store(read_string):
	variable_dict = {}
	equation_dict = {}
	read_file = read_string
	read = open(read_file, 'r')			# Opens the file
	
	# This loop puts the the objects from the file into the dictionarys.
	for line in read:
		x = line.split()
		if x[0] == 'Variable':
			y = x[2:len(x)]
			variable_dict[x[1]] = y
		elif x[0] == 'Equation':
			equation_name = x[1]
			equation_dict[equation_name] = x[2:len(x)]
	
	# This loop changes the independent variables from strings to boolean values
	for i in variable_dict.keys():
		if variable_dict[i] == ['True']:
			variable_dict[i] = [True]
		elif variable_dict[i] == ['False']:
			variable_dict[i] = [False]
	
	read.close()			# Closes the file
	return variable_dict, equation_dict, equation_name

# This function puts the values of independent variables into the dependent variables
def insert_tf(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x in variable_dict.keys():
					k = variable_dict[x]
					if k == [True] or k == [False]:
						y[j] = k[0]
	
	return variable_dict

# This function computes all the 'not' logic statements 
def compute_not(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x == 'not':
					z = y[j+1]
					if z == True or z == False:
						y[j:j+2] = [not z]			# This combines the elements into 1
	
	return variable_dict

# This function computes all the 'and' logic statements
def compute_and(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x == 'and':
					m = y[j-1]
					n = y[j+1]
					if (m == True or m == False) and (n == True or n == False):
						z = m and n
						y[j-1:j+2] = [z]			# This combines the elements into 1
	
	return variable_dict

# This function computes all the 'or' logic statements
def compute_or(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x == 'or':
					m = y[j-1]
					n = y[j+1]
					if (m == True or m == False) and (n == True or n == False):
						z = m or n
						y[j-1:j+2] = [z]			# This combines the elements into 1
	
	return variable_dict

# This function solves the equation that the user wants.
def solve(variable_dict, equation_dict, equation_name):
	equation = equation_dict[equation_name]
	l = len(equation)
	
	# This loop puts in the boolean values for all the variables in the formula
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x in variable_dict.keys():
			equation[i] = variable_dict[equation[i]][0]
	
	# This loop does the 'not' statements first
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x == 'not':
			equation[i:i+2] = [not equation[i+1]]			# This combines the elements
			
	# This loop does the 'and' statements next
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x == 'and':
			equation[i-1:i+2] = [equation[i-1] and equation[i+1]]
			# The above line combines the elements used into one element
	
	# This loop does the 'or' statements last
	for i in range(0, l):
		if i >= len(equation):
			break	
		x = equation[i]
		if x == 'or':
			equation[i-1:i+2] = [equation[i-1] or equation[i+1]]
			# The above line combines the elements used into one element
	
	solution = equation[0]			# Solution to the formula
	
	return solution, equation_dict

# This function checks the variable dictionary to see if all the elements are
# only True or False. This is used to continuosly loop the above functions,
# the ones that deal with the logic statements in the variables, to compute
# variables that are dependent on other dependant variables.
def check_dict(variable_dict):
	check = 0
	chk_value = None
	for i in variable_dict.keys():
		y = variable_dict[i]
		if y == [True] or y == [False]:
			check = check + 1
	
	if check == len(variable_dict.keys()):
		chk_value = True
	else:
		chk_value = False
		
	return chk_value, check

# The function to run to solve the problem.
def main():
	variable_dict, equation_dict, equation_name = store(read_string)
	
	chk_value, check1 = check_dict(variable_dict)
	
	# This while loop keeps looping the logic functions until all variables have
	# been solved.
	while chk_value == False:
		chk_value, check2 = check_dict(variable_dict)
		
		variable_dict = insert_tf(variable_dict)
		variable_dict = compute_not(variable_dict)
		variable_dict = compute_and(variable_dict)
		variable_dict = compute_or(variable_dict)
		
		chk_value, check1 = check_dict(variable_dict)
		
		# This if statement makes a check to see if the variables are valid
		if check1 == check2:
			print "This is not a valid set of variables."
			exit(-1)
		
	# Solves the equation
	solution, equation_dict = solve(variable_dict, equation_dict, equation_name)
	
	#print variable_dict
	#print equation_dict
	
	print "The solution to the equation, %s, is: %r" %(equation_name, solution)
	
main()