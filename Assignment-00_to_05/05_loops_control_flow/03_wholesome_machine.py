correct_affermation = "I am capable of doing anything .I put my mind too."
def main ():
    print("Welcome to the Wholesome Machine ")
    while True:
       input = input("Please type the following affermation: " + correct_affermation)
       if input == correct_affermation :
        print("That\'s right! ")
        break
       else:
        print("That was not the correct affermation !")

if __name__ == '__main__':
    main()