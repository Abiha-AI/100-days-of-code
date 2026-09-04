# Day 7: Password Validator
# Practicing while loop and string methods

password = input("Create a password (min 6 chars): ")

while len(password) < 6:
    print("Too short! Try again.")
    password = input("Create a password (min 6 chars): ")

print("Password accepted!")
