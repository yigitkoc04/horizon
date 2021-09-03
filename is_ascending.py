"""
File: is_ascending.py
-------------------
This program prompts the user for numbers until they enter -1, and then
prints out the numbers and whether or not those numbers are in ascending order.
"""
def is_ascending(my_list):
    result = True
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1] :
            result = False
    return result

def main():
    my_list = []
    number = int(input("Enter a number: "))
    while number != -1:
        my_list.append(number)
        number = int(input("Enter a number: "))
    print(my_list)
    if is_ascending(my_list):
        print("Ascending!")
    else:
        print("Not Ascending!")


if __name__ == '__main__':
    main()
