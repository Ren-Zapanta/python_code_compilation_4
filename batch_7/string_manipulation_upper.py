#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
user_input = input("Please enter a statement: ") #Requests input from the user

formatted_text = "" #Initialize empty string to store formatted text

for character in user_input: #Loops through the characters in the user_input
    if 'a' <= character <= 'z': #verifies if lowercase characters are present in the input
        formatted_text += chr(ord(character) - 32) #Converts lower case letters to uppercase using ascii
    else:
        formatted_text += character #Keeps the already uppercase letters in the input

print(formatted_text) #Prints output