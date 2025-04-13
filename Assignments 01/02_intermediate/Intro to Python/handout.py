Gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0
}

def main():
    print("Welcome to the Planetary Weight Calculator ")
    print("--------------------------------")
    earth_weight = float(input("Enter your weight on Earth: "))
    choice = input("Calculate weight on Mars (1) or another planet (2)? ")

    if choice == "1":
        planet = "Mars"
    elif choice == "2":
        planet = input("Enter the planet name: ")
    else:
        print("Invalid choice!")
        return

    gravity = Gravity.get(planet, 1.0) 

    
    planetary_weight = round(earth_weight * gravity, 2)
    print(f"Your weight on {planet}: {planetary_weight}")

if __name__ == "__main__":
    main()