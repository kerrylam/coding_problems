def reverse(list_of_chars):
	"""Takes a list of characters and reverses them in place."""

	left_index = 0
	right_index = len(list_of_chars) - 1

	while left_index < right_index:
		#swap characters
		list_of_chars[left_index], list_of_chars[right_index] = \
		list_of_chars[right_index], list_of_chars[left_index]
		#move towards middle
		left_index += 1
		right_index -= 1

def reverse(list_of_chars):
	"""Takes a list of characters and reverses them in place."""

	left_index = 0
	right_index = len(list_of_chars) - 1

	while left_index < right_index:
		#swap characters 
		list_of_chars[left_index], list_of_chars[right_index] = \
		list_of_chars[right_index], list_of_chars[left_index]
		#move towards middle
		left_index += 1
		right_index -= 1
"""
chars = ['a', 'b', 'c', 'd', 'e']
		[ 0    1    2    3    4 ]

reverse(chars) ->

left_index = 0 -> 'a'
right_index = 4 -> 'e'

while 0 < 3 swap the characters

0 -> 'e'	4 -> 'a'

chars = ['e', 'b', 'c', 'd', 'a']
		[ 0    1    2    3    4 ]

1 < 3

left_index = 1 -> 'b'
right_index = 3 -> 'd'

1 -> 'd'
3 -> 'b'

chars = ['e', 'd', 'c', 'b', 'a']
		[ 0    1    2    3    4 ]

2 !< 2 so stop here

When reversing, doesn't matter if it's odd or even, if we just use divide and conquer we
will always come up with the solution. 
"""


def get_products_of_all_ints_except_at_index(int_list):

# Make a list with the products
	if len(int_list) < 2:
		raise IndexError()

#this creates an empty list of the exact length we need, saving space
	products_of_all_ints_except_at_index = [None] * len(int_list)

#for each integer, we find the product of all the integers before it
#storing the total product so far each time
	product_so_far = 1
	for i in range(len(int_list)):
		products_of_all_ints_except_at_index[i] = product_so_far
		product_so_far *= int_list[i]

#now for each integer, we find the product of all the integers after it
#since each index in products already has the product of all the integers before it
#now we're storing the total product of all the other integers
	product_so_far = 1
	for i in range(len(int_list) - 1, -1, -1):
		products_of_all_ints_except_at_index[i] *= product_so_far
		product_so_far *= int_list[i]

	return products_of_all_ints_except_at_index


def fib(n):
	#takes an integer n and returns the nth Fibonacci

	#we want to add to the sequence
	# we want to add the two previous indexes
	# so we need to make sure there are 2 before our index
	# if there isn't 2 before, then it has to be 0 or 1, then we can start after that
	if n < 0:
		raise Exception()

	elif n in [0, 1]:
		return n

	prev_prev = 0
	prev = 1

	for _ in range(n - 1):
		current = prev_prev + prev
		prev_prev = prev
		prev = current


	return current



