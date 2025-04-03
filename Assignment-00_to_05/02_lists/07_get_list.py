def main ():
    list = []
    val = input("Enter your value here : ")
    while val:
        list.append(val)
        val = input("Enter your value here : ")
    print("Here's the list:" , list)

if __name__ == '__main__':
    main()
