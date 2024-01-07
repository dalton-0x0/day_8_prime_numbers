"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
They are numbers that have only 2 positive factors.

https://en.wikipedia.org/wiki/Prime_number

e.g.
2 is a prime number because it's only divisible by 1 and 2.
1 is not a prime number because it does not have 2 positive factors.
But 4 is not a prime number because it has more than 2 factors - 1, 2 and 4.
"""


def prime_checker(number):
    """This function checks if the number passed is a prime number or not."""
    is_prime = True
    if number == 1:
        #  1 is not a prime number
        is_prime = False
    for i in range(2, number):
        if number % i == 0:
            # i.e. the is divisible by a number other than 1 and itself
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number 🎉")
    else:
        print(f"{number} is not a prime number 😐")


# input est run
num = int(input("Check prime number: "))
prime_checker(num)
