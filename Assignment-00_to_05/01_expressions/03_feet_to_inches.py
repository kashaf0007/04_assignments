inches_per_foot: int = 12

def main():
    feet = int(input("Enter number of feet: "))
    inches = inches_per_foot * feet
    print("Inches in foot:", inches)

if __name__ == '__main__':
    main()
