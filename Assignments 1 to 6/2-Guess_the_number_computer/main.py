import random

def guess(x):
    print("🎯 Welcome to the Guess the Number Game!")
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(" 📉 Too low. Try again.")
        elif guess > random_number:
            print(" 📈 Too high. Try again.")

    print(f"🎉 Congratulations! You guessed the number {random_number} correctly!")
guess(10)
