from sys import argv

# Gets the file from the user
script, read_string = argv

# Creates a dictionary from the given file where the keys are the variables and 
# the equation and the values are the values of the given variable. Should try
# to store it as a boolean value (True or False) for each variable rather then
# a string as it would be when directly read of the file. Should also be able
# to recognize if the variables given are ill-formed (cannot be defined). The
# output will be the solution to the equation.
def compute(read_string):
	read_file = read_string
	read = open(read_file, 'r')
	boolean_dict = {}
	
	for line in read:
		x = line.split()
		if x[0] == 'Variable':
			y = x[2:len(x)]
			boolean_dict[x[1]] = y
		elif x[0] == 'Equation':
			equation_name = x[1]
			equation = x[2:len(x)]
	
	# Do the True, False values first
	for i in boolean_dict.keys():
		if boolean_dict[i] == ['True']:
			boolean_dict[i] = [True]
		elif boolean_dict[i] == ['False']:
			boolean_dict[i] = [False]

	# Put in the values of independent variables into the dependent variables first
	for i in boolean_dict.keys():
		y = boolean_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x in boolean_dict.keys():
					k = boolean_dict[x]
					if k == [True] or k == [False]:
						y[j] = k[0]
					#else:
						#print "This is not a valid set of variables."
						#exit(-1)
		
	# Do the not operations second
	for i in boolean_dict.keys():
		y = boolean_dict[i]
		l = len(y)
		if y != [True] or y != [False]:
			for j in range(0, l):
				if j >= len(y):
					break
				x = y[j]
				if x == 'not':
					z = y[j+1]
					if z == True or z == False:
						y[j:j+2] = [not z]
					#else:
						#print "This is not a valid set of variables."
						#exit(-1)
	
	# Do the and operations next
	for i in boolean_dict.keys():
		y = boolean_dict[i]
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
						y[j-1:j+2] = [z]
					#else:
						#print "This is not a valid set of variables."
						#exit(-1)
	
	# Do the or operations last
	for i in boolean_dict.keys():
		y = boolean_dict[i]
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
						y[j-1:j+2] = [z]
					#else:
						#print "This is not a valid set of variables."
						#exit(-1)
	
	l = len(equation)
	for i in range(0, l):
		if i >= len(equation):
					break
		x = equation[i]
		if x in boolean_dict.keys():
			equation[i] = boolean_dict[equation[i]][0]
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x == 'not':
			equation[i:i+2] = [not equation[i+1]]
	for i in range(0, l):
		if i >= len(equation):
			break
		x = equation[i]
		if x == 'and':
			equation[i-1:i+2] = [equation[i-1] and equation[i+1]]
	for i in range(0, l):
		if i >= len(equation):
			break	
		x = equation[i]
		if x == 'or':
			equation[i-1:i+2] = [equation[i-1] and equation[i+1]]
	
	solution = equation[0]
	print boolean_dict
	print equation
	
	read.close()
	return solution, equation_name

# Runs the functions with the input given
solution, equation_name = compute(read_string)
print "The solution to the equation, %s, is: %r" %(equation_name, solution)