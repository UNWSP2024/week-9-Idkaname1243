
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).
import random

def random_num_added():
    counter = 0
    desired_num = int(input("enter how many random numbers to add to the file up to 1000:   "))
    if desired_num > 1000:
        desired_num = int(input("enter how many random numbers to add to the file up to 1000:   "))
    try:
        with open('random_num.txt','a') as file:
            while counter < desired_num:
                counter += 1
                file.write(str(random.randint(1,500))+'\n')
        with open('random_num.txt','r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file random_num.txt was not found")
if __name__ == '__main__':
    random_num_added()
with open('random_num.txt', 'w') as file:
    pass
