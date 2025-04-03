def get_first_element(list):
    print(list[0])

def get_list():
    list = []
    element: str = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return list
def main():
    list = get_list()
    get_first_element(list)

if __name__ == '__main__':
    main()

