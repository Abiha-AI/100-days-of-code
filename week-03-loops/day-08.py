# Day 8: Guessing Game with Limited Attempts
# Practicing while loop, break, and counter

import random

secret = random.randint(1, 20)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input(f"Guess (attempt {attempts + 1}/{max_attempts}): "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You won in {attempts} tries!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if guess != secret:
    print(f"Game over! The number was {secret}")
