#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
string_input = input("Please enter a text: ") #Asks the user for string input
substring_input = input("Enter substring: ") #Asks the user for the substring to count

substring_count = 0 #Initialize a count set to 0

substring_length = len(substring_input) #Gets the length of the substring_input

for i in range(len(string_input) - substring_length + 1): #Loops through the whole string_input
    if string_input[i:i + substring_length] == substring_input: #Extracts a part of the string with the using the length of the substring and compares
        substring_count += 1 #Adds to the count

print(f"Your substring '{substring_input}' has been found {substring_count} times.") #Prints the output