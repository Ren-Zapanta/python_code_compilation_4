#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
string_input = input("Please enter a statement: ") #Requests user input
prefix_input = input("Enter a prefix for verification: ") #Asks for prefix to check

prefix_length = len(prefix_input) #Gets the length of the preefix_input

actual_prefix = string_input[:prefix_length] #Extracts the starting characters by slicing the string according to the prefix input



