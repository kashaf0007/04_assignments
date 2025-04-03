"""
Program: Division Result and Remainder
--------------------------------------
This program asks the user for two integers, divides the first number by the second,
and prints both the result of the division and the remainder.
"""

def main():
  dividend : int = int (input("Enter an integer to be divided: "))
  divisor : int = int(input("Enter an integer to divide by: "))

  quotient = dividend // divisor
  remainder = dividend % divisor
  print(" The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
  main()