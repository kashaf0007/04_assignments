def add_num(numbers)-> int :
    total :int = 0
    for i in numbers:
        total += i
    return total
def main():
    numbers: list[int] = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
    sum_num = add_num(numbers)
    print(sum_num)

if __name__ == '__main__':
    main()