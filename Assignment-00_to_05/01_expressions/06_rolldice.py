import random 
dice_size : int = 6 

def main():
  dice1 : int = random.randint (1,dice_size)
  dice2 : int = random.randint (1 ,dice_size)
  total = dice1 + dice2
  print("Dice have", dice_size, "sides each.")
  print("First dice:", dice1)
  print("Second dice:", dice2)
  print(f"the total num of the dice is {total}")
if __name__ == '__main__':
  main()