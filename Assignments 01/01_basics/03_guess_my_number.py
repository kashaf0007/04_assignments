import random
def main():
    secret_num = random.randint(1,100)
    print("I am thinking of a number between 1 and 99...")
    guess_number = int(input("Enter a guess number: "))

    while guess_number != secret_num:
        if guess_number < secret_num:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")
    
    guess_number= int(input("Enter a new guess: ")) 
        
    print(f"Congrats! The number was: " + str(secret_num))
    
if __name__ == '__main__':
    main()