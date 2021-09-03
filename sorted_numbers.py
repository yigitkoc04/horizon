"""
File: sorted_numbers.py
-------------------
This program prompts the user for 10 numbers, and then
prints out those numbers in sorted order.
"""


def main():
    number_list = []
    for i in range(10):
        number = int(input("Select a number:"))
        number_list.append(number)
        number_list.sort()
    print(number_list)


if __name__ == '__main__':
    main()
