#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
user_input = input("Please enter a statement: ") #Requests user input

assume_lowercase = True #Initial assumption of the input's casing

for character in user_input: #Loops through all characters in the user_input
    if "A" <= character <= "Z": #Verifies if the characters are in upper casing
        assume_lowercase = False #Sets the initial assumption to false if uppercased letter is detected
        break #Breaks loop

#Prints corresponding message for each result
if assume_lowercase == False: 
    print("Your input is not in lowercase")
else:
    print("Your input is in lowercase")

