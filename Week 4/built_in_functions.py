# Starting message
print("Program Started")
# Ask the user to enter a character
print("Please enter a standard character:")
character = input()
# Used the len (length) function to check if more than one character is typed by the user
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("Enter only one character.")   # Error mesage in case user enters more than one character
print("Program Ended")

# Task 2
print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())
if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII value {code} is:"f" {chr(code)}")
else:
    print("The character cannot be displayed.")
print("Program Ended!")
