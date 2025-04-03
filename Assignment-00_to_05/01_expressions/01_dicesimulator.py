import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Total of two dice:", total)

def main():
    die1 = 10
    print("die1 in main() starts as: " + str(die1))

    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is: " + str(die1))
if __name__ == '__main__':
    main()