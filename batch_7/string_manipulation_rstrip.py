#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
user_input = input("Please enter a text: ")

while user_input and user_input[-1] == " ": #A loop that continues if the last character is an empty space
    user_input = user_input[:-1] #Manually deletes the last character of the input until it detects a non-empty space

print(f"'{user_input}'") #Prints result. Uses single quotes to indicate changes made to the output from the input