# Program

To create a program that can perform deductive logic. Deductive Logic operates on boolean variables (that is variables that can only be 0/1 or false/true) using the OR and AND binary operators instead of Addition and Multiplication. This program will be reading input from a file that specifies some initial boolean variables and then specifies some equations it wants answers to.

Part I of the program is to first make sure you can read and compute the variables. For example the following input

Variable B not A
Variable C False
Variable A True
Equation Example ( A or B ) and C

Should output

Equation Example is False

## Input:

Generally each line of the input will look like

[Variable or Equation][Space][Name][Space][Value]

Where

[Name] = Is a word without a space starting with a capital letter.
[Value] = [True or False or Formula]
[Formula] = Is a Formula using the [Name]s joined with ['or' or 'and' or '~'] with paranthesis to group expressions. Such as 

( A or B ) and ( B and ( A or not C ) )


## Notes:
Remeber that the input can be ill-formed. For instance, if the example above was

Variable B not A
Variable C A or B
Variable A C and B
Equation Example (A or B) and C

Should output

Equation Example cannot be solved!

When you are done you have to also provide 5 example input files and expected answers that tests various possible input conditions of this program. I've tried to be brief about the program so clarify with me about the input format and what the program can and can't do. Remember that it's worth writing these various input files first and confirming with me that they are right before writing the program that will compute it!

## To Run:
You can run the test.py file. You can add new tests by using the following format in test.py: runTest([Name], [Result], [The Test])

Or

You can run the parsing file with a variable and equation file with the following command:
python Parsing.py [File name]
