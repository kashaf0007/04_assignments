import random

N: int = 10
MIN: int = 1
MAX: int = 100

def main():
    for _ in range(N):
        print(random.randint(MIN, MAX),end=" ")
if __name__ == '__main__':
     main()