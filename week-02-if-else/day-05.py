# Day 5: Simple Calculator with Menu
# Practicing if/elif/else with user input and error checking

print("    Calculator    ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

choice = input(" Pick 1-4: ")
num1 = float(input(" First number: "))
num2 = float(input(" Second number: "))

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid choice. Pick 1-4.")
