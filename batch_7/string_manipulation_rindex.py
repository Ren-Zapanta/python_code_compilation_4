#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
string_input = input("Please enter a string: ") #Asks the user for a string
character_to_find = input("Which character would you like to find? ") #Asks the user which character within the string they would like to find

character_location = string_input.rindex(character_to_find) #Finds where the specified character last appears in the string

print(f"'{character_to_find}' last appears on index: {character_location}") #Prints the result