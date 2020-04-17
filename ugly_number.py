"""Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

    Example 1:

    Input: 6
    Output: true
    Explanation: 6 = 2 × 3
    Example 2:

    Input: 8
    Output: true
    Explanation: 8 = 2 × 2 × 2
    Example 3:

    Input: 14
    Output: false 
    Explanation: 14 is not ugly since it includes another prime factor 7.

Note:
- 1 is typically treated as an ugly number.
- Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""

""" Approach: 
prime number is a number only divisible by itself and 1
take number, is it divisible by 2, 3 or 5? if yes, is the remainder also divisible
by 2, 3, or 5? continue until either no longer divisible or remainder is not 
2, 3, or 5.
how to get prime factors?
how to know if it's a prime number?
"""

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return true
    else:
        for x in range(num):
            if num % x == 0:
                return False
            else:
                return True

def ugly_number(num):
    """return true if prime factors of num are 2, 3, or 5"""

    ugly_factors = [2, 3, 5]   
    if num < 1:
        return False
    else:
        for factor in ugly_factors:
            while num % factor == 0:
                num = num / factor
        return num == 1

