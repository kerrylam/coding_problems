"""Write a function get_products_of_all_ints_except_at_index() that takes a list of 
integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
"""

""" Approach: 
- keep track of index 
- while looping, if not index, multiply
- append that number to the resulting list
- return the list
"""


def get_products_of_all_ints_except_at_index(nums):
    index = 0
    result = []
    while index < len(nums):
        product = 1
        for i, num in enumerate(nums):
            if i != index:
                product *= num
        result.append(product)
        index += 1
    return result
