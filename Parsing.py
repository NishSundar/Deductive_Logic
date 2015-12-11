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
			
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if y[j] == 'False':
					y[j] = False
				elif y[j] == 'True':
					y[j] = True
	
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
					variable_dict = compute_not(variable_dict)			# Computes multiple nots'
					break
				x = y[j]
				if x == 'not':
					z = y[j+1]
					if z == True or z == False:
						y[j:j+2] = [not z]			# This combines the elements into 1
					elif z == '(':			# Computes what is in the brackets
						k = len(y)
						q = 1			# Number of open brackets
						w = 0			# Number of close brackets
						for o in range(j+2, k):			# Finds out what is in the brackets
							if y[o] == '(':
								q = q + 1
							if y[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = y[j+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							z = interim_dict['intermediate'][0]
							n = not z
							y[j:d+1] = [n]
	
	return variable_dict

# This function computes all the 'and' logic statements
def compute_and(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					variable_dict = compute_and(variable_dict)			# Computes multiple ands'
					break
				x = y[j]
				if x == 'and':
					m = y[j-1]
					n = y[j+1]
					if (m == True or m == False) and (n == True or n == False):
						z = m and n
						y[j-1:j+2] = [z]			# This combines the elements into 1
					elif (m == True or m == False) and (n == '('):			# Computes brackets
						k = len(y)
						q = 1			# Number of open brackets
						w = 0			# Number of close brackets
						for o in range(j+2, k):			# Finds out what is in the brackets
							if y[o] == '(':
								q = q + 1
							if y[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = y[j+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							n = interim_dict['intermediate'][0]
							z = m and n
							y[j-1:d+1] = [z]
					
	return variable_dict

# This function computes all the 'or' logic statements
def compute_or(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					variable_dict = compute_or(variable_dict)			# Computes multiple ors'
					break
				x = y[j]
				if x == 'or':
					m = y[j-1]
					n = y[j+1]
					if (m == True or m == False) and (n == True or n == False):
						z = m or n
						y[j-1:j+2] = [z]			# This combines the elements into 1
					elif (m == True or m == False) and (n == '('):			# Computes brackets
						k = len(y)
						q = 1			# Number of open brackets
						w = 0			# Number of close brackets
						for o in range(j+2, k):			# Finds out what is in the brackets
							if y[o] == '(':
								q = q + 1
							if y[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = y[j+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							n = interim_dict['intermediate'][0]
							z = m or n
							y[j-1:d+1] = [z]
	
	return variable_dict
	
# To compute the brackets in the values
# Add to this function: the ability to recurr this function so that it can compute brackets inside
# brackets. This way we don't need to do a separate loop inside each logic computing function
def compute_brackets(variable_dict, interim_dict):
	solution, interim_dict = solve(variable_dict, interim_dict, 'intermediate')
	intermediate = False
	
	if solution == [True] or solution == [False]:
		interim_dict['intermediate'] = solution
		intermediate = True
	
	return interim_dict, intermediate
	
def compute_brackets_2(variable_dict):
	for i in variable_dict.keys():
		y = variable_dict[i]
		l = len(y)
		if y[0] == '(':
			k = len(y)
			q = 1			# Number of open brackets
			w = 0			# Number of close brackets
			for o in range(1, k):			# Finds out what is in the brackets
				if y[o] == '(':
					q = q + 1
				if y[o] == ')':
					w = w + 1
				if q == w:
					d = o
					break
			c = y[1:d]
			interim_dict = {}
			interim_dict['intermediate'] = c
			interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
			if intermediate == True:
				z = interim_dict['intermediate'][0]
				y[0:d+1] = [z]
		
	return variable_dict

# This function solves the equation that the user wants.
# Change the loops in this function in order to be able to do brackets in the formula. Just be
# able to do at least one bracket in this function because then any number of brackets inside
# brackets can be done since the compute_brackets will be used to solve the first bracket, and
# the compute_bracket function will again call the solve function recurring it for multiple
# brackets.
def solve(variable_dict, equation_dict, equation_name):
	equation = equation_dict[equation_name]
	l = len(equation)
	interim_eq = {}
	
	# This loop puts in the boolean values for all the variables in the formula
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x in variable_dict.keys():
			y = variable_dict[equation[i]]
			if y == [True] or y == [False]:
				equation[i] = y[0]
	
	# Changes True, False strings into boolean values
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation
		if x[i] == 'False':
			x[i] = False
		elif x[i] == 'True':
			x[i] = True
				
	for i in range(0, l):
		if i >= len(equation):
			break
		if equation[0] == '(':
			k = len(equation)
			q = 1			# Number of open brackets
			w = 0			# Number of close brackets
			for o in range(1, k):			# Finds out what is in the brackets
				if equation[o] == '(':
					q = q + 1
				if equation[o] == ')':
					w = w + 1
				if q == w:
					d = o
					break
			c = equation[1:d]
			interim_dict = {}
			interim_dict['intermediate'] = c
			interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
			if intermediate == True:
				z = interim_dict['intermediate'][0]
				equation[0:d+1] = [z]
	
	l = len(equation)
	# This loop does the 'not' statements first
	for i in range(0, l):
		interim_eq['eq'] = equation
		if i >= len(equation):
			equation, interim_eq = solve(variable_dict, interim_eq, 'eq')
			break
		x = equation[i]
		if x == 'not':
			if equation[i+1] == True or equation[i+1] == False:
				equation[i:i+2] = [not equation[i+1]]			# This combines the elements
			elif equation[i+1] == '(':			# Computes what is in the brackets
						k = len(equation)
						# change the following loop so that if there are multiple brackets, it can
						# correctly determine the right closing bracket
						for o in range(i+2, k):			# Finds out what is in the brackets
							q = 1			# Number of open brackets
							w = 0			# Number of close brackets
							if equation[o] == '(':
								q = q + 1
							if equation[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = equation[i+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							z = interim_dict['intermediate'][0]
							n = not z
							equation[i:d+1] = [n]	
	
	l = len(equation)
	# This loop does the 'and' statements next
	for i in range(0, l):
		interim_eq['eq'] = equation
		if i >= len(equation):
			equation, interim_eq = solve(variable_dict, interim_eq, 'eq')
			break
		x = equation[i]
		if x == 'and':
			m = equation[i-1]
			n = equation[i+1]
			if (m == True or m == False) and (n == True or n == False):
				equation[i-1:i+2] = [equation[i-1] and equation[i+1]]
			# The above line combines the elements used into one element
			elif (m == True or m == False) and (n == '('):			# Computes brackets
						k = len(equation)
						q = 1			# Number of open brackets
						w = 0			# Number of close brackets
						for o in range(i+2, k):			# Finds out what is in the brackets
							if equation[o] == '(':
								q = q + 1
							if equation[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = equation[i+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							n = interim_dict['intermediate'][0]
							z = m and n
							equation[i-1:d+1] = [z]
	
	l = len(equation)
	# This loop does the 'or' statements last
	for i in range(0, l):
		interim_eq['eq'] = equation
		if i >= len(equation):
			equation, interim_eq = solve(variable_dict, interim_eq, 'eq')
			break	
		x = equation[i]
		if x == 'or':
			m = equation[i-1]
			n = equation[i+1]
			if (m == True or m == False) and (n == True or n == False):
				equation[i-1:i+2] = [equation[i-1] or equation[i+1]]
			elif (m == True or m == False) and (n == '('):			# Computes brackets
						k = len(equation)
						q = 1			# Number of open brackets
						w = 0			# Number of close brackets
						for o in range(i+2, k):			# Finds out what is in the brackets
							if equation[o] == '(':
								q = q + 1
							if equation[o] == ')':
								w = w + 1
							if q == w:
								d = o
								break
						c = equation[i+2:d]
						interim_dict = {}
						interim_dict['intermediate'] = c
						interim_dict, intermediate = compute_brackets(variable_dict, interim_dict)
						if intermediate == True:
							n = interim_dict['intermediate'][0]
							z = m or n
							equation[i-1:d+1] = [z]
			# The above line combines the elements used into one element
	
	solution = equation			# Solution to the formula
	
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
		variable_dict = compute_brackets_2(variable_dict)
		variable_dict = compute_not(variable_dict)
		variable_dict = compute_and(variable_dict)
		variable_dict = compute_or(variable_dict)
		
		chk_value, check1 = check_dict(variable_dict)

		# This if statement makes a check to see if the variables are valid
		if check1 == check2:
			print "This is not a valid set of variables."
			print check2, check1
			exit(-1)
		
	# Solves the equation
	solution, equation_dict = solve(variable_dict, equation_dict, equation_name)
	
	#print variable_dict
	print equation_dict
	
	print "The solution to the equation, %s, is: %r" %(equation_name, solution[0])
	
main()