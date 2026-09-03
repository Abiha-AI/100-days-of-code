# Day 6: Multiplication Table
# Practicing for loop and range()

num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
