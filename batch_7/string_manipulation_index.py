#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
string_input = input("Please enter a statement: ") #Asks the user for string input
character_to_find = input("What would you like to know the index of? ") #Asks the user which character they would like to know the position of 

character_location = string_input.find(character_to_find) #Finds the first location of the character in the string

print(f"'{character_to_find}' was first found at index: {character_location}") #Prints the output



