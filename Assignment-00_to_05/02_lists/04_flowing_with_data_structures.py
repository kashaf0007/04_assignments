def add_three(list ,data):
    for i in range(3):
        list.append(data)
def main():
    message = input("Enter your message to copy :" )
    list = []
    print("before list :" , list)
    add_three(list , message)
    print("After list :" ,list)

if __name__ == "__main__":
    main()
