"""
File: some_sum.py
-------------------
This program reads in 10 numbers from the user and prints
out the sum of those 10 numbers.
"""


def main():
    """
    You should replace this comment with a better, more descriptive one.
    You should delete the `pass` line below before writing your code.
    """
    number_add = 1
    new_value = 0
    print("Enter 10 nums. I will show you the sum!")
    for i in range(10):
        values = input("Please enter integer number " + str(number_add) + " : ")
        new_value = int(values) + int(new_value)
        number_add += 1
    print("The sum is: " + str(new_value))






if __name__ == '__main__':
    main()
