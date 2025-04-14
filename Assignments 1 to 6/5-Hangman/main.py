
import random

def hangman():
    word = random.choice(['python', 'hangman', 'keyboard'])
    guessed = []
    tries = 6

    print("welcome Hangman Game!")

    while tries > 0:
        display = [letter if letter in guessed else '_' for letter in word]
        print("Word:", ' '.join(display))

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.append(guess)

        if guess not in word:
            tries -= 1
            print(f"Wrong! Tries left: {tries}")

        if all(letter in guessed for letter in word):
            print(f"🎉 You won! The word was '{word}'.")
            break
    else:
        print(f"💀 You lost! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
