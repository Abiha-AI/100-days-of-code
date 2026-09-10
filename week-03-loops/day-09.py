# Day 9: Shopping Cart Total
# Practicing while loop with break and running totals

total = 0
item_count = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Price of {item}: "))
    total += price
    item_count += 1
    print(f"Added {item}: ${price:.2f}")

print(f"\nYou bought {item_count} items.")
print(f"Total bill: ${total:.2f}")
