import random
import string
print("password generator in python")
def generator(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(lenght))
    return password
lenght = int(input("Enter your password lenght: "))
print("Generated Password " , generator(lenght) )

