c: int = 299792458
def main():
  mass_in_kg : float = float (input("Enter mass in kg: "))
  energy:float = mass_in_kg * (c**2)
  print("e = m * c^2")
  print("m = " + str(mass_in_kg) +  "kg")
  print("c = " + str(c) + " m/s")
  print(str(energy) + " joules ")
if __name__ == '__main__':
    main()