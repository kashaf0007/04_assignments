import random 
print(" welcome to rock, paper ,scissors game!")

option =['rock' , "paper" , "scissor"]
user = computer = 0
print("let's play")

while True:
    user_input = input("Choose rock, paper or scissors: ").lower()
    if user_input not in option:
        print("❗ Invalid choice. Please choose rock, paper or scissors.")
        continue   

    computer_choice = random.choice(option)

    print(f"\nYou chose: {user_input}")
    print(f"Computer chose: {computer_choice}\n")

    if user_input == computer_choice:
        print("It's a tie! ")
    elif (
        (user_input == "rock" and computer_choice == "scissors") or
        (user_input == "paper" and computer_choice == "rock") or
        (user_input == "scissors" and computer_choice == "paper")
    ):
        print("You win! 🎉")
        user += 1
    else:
        print("You lose!")
        computer += 1


