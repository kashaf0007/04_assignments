import random 
def guess_the_number ():
    print("welcome to guess the number game by computer")
    random_number = random.randint(1 , 50)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-50): "))
            attempts += 1
            if guess > random_number:
                print("Too high! 📈 Try again.")
            elif guess < random_number:
                print("Too low! 📉 Try again.")
            else:
               print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
               break
        except ValueError:
            print("❗ Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()