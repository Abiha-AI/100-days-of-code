# Day 7: Password Validator
# Practicing while loop and string methods

password = input("Create a password (min 6 chars): ")

while len(password) < 6:
    print("Too short! Try again.")
    password = input("Create a password (min 6 chars): ")

print("Password accepted!")
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True

if has_digit:
    print("Strength: Medium")
else:
    print("Strength: Weak (add a number)")
