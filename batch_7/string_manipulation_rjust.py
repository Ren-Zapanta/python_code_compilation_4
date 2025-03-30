#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
string_input = input("Please enter a statement: ") #Asks user for string input
desired_length = int(input("Enter length: ")) #Asks user how far to the right they want their output to be

current_length = len(string_input) #Gets the length of the string input

if current_length < desired_length: #Checks if string input is shorter than the desired length
    padding = " " * (desired_length - current_length) #Gets number of needed padding according to the difference of desired and current length
    output_string = padding + string_input #Concatenates the padding to the original string_input; creating the output
else:
    output_string = string_input #Keeps the original input as the output if the current_length is greater than the desired_length

print(f"'{output_string}'")#Prints the output. Uses single quotes to indicate spaces added to the string"







