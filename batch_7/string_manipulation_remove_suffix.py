#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
string_input = input("Please enter a text: ") #Requests string input from the user
suffix_input = input("What suffix would you like to be removed?: ") #Asks the user what suffix they would like to be removed

if string_input.endswith(suffix_input): #Use endswith to verify if string_input ends with suffix_input
    string_input = string_input[:-len(suffix_input)] #Removes the specified suffix from the original string input

print(string_input) #Prints output
