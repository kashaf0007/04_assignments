def main():
    number :list[int] = [1,2,3,4,5,6]
    for i in range(len(number)):
        index = number[i]
        number[i] = index * 2
    print(number)
    
if __name__ == '__main__':
    main()