print("*** Welcome To Number Guessing Game ***")

import random

number = random.randint(1, 100)
attempt = 0
max_attempts = 3

print("Hint: You have 3 attempts to guess the number.")

while attempt < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))
    attempt += 1

    if guess > number:
        print("The number you guessed is high.")

    elif guess < number:
        print("The number you guessed is low.")

    else:
        print("You Won! ")
        break

    if attempt < max_attempts:
        print(f"Warning: You have {max_attempts - attempt} attempt(s) left.")

else:
    print(f"You Lost! The number was {number}.")

print(f"Game is over. You used {attempt} attempt(s).")
