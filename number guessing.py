import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print(" Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess the number!")

while True:
    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(" Congratulations! You guessed the correct number!")
        break