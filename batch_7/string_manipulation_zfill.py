#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
string_input = input("Please enter a statement: ") #Asks user for string input
desired_length = int(input("Enter length: ")) #Asks the user for desired string length

length_of_input = len(string_input) #Gets the length of the string input

if length_of_input < desired_length: #verifies if the length_of_input is shorter than the desired_length input
    zeros_to_add = "0" * (desired_length - length_of_input) #Computes needed amount of zeros to satisfy desired_length
    string_output = zeros_to_add + string_input #Concatenates zeros_to_add and string_input for the output
else: 
    string_output = string_input #Makes the output the same as the input if length of the input is the same with the desired length

print(string_output) #Prints the output


