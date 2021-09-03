"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""

import sys
def main(n):
    print(fizzbuzz(n))

def fizzbuzz(n):
    """
    Plays the fizzbuzz game up to and including n.  It prints out numbers from 1 to n,
    except if the number is divisible by 3, it instead prints "Fizz", if the number
    is divisible by 5, it instead prints "Buzz", and if it is both, instead it prints "FizzBuzz".
    This function returns the count of numbers that were replaced.
    """
    fizzed_buzzed = 0
    for i in range(0,n):
        if i % 3 == 0 and i%5 == 0:
            return "fizz buzz"
            fizzed_buzzed += 1
        elif i % 3 == 0:
            return "fizz"
            fizzed_buzzed += 1
        elif i % 5 == 0:
            return "buzz"
            fizzed_buzzed += 1
        else:
            return i
    





if __name__ == "__main__":
    main(int(sys.argv[1]))
