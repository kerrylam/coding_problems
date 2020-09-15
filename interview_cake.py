from collections import defaultdict 


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


class QueueTwoStacks(object):

	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def enqueue(self, item):
		self.in_stack.append(item)

	def dequeue(self):
		if len(self.out_stack) == 0:

			# move items from in_stack to out_stack, reversing order
			while len(self.in_stack) > 0:
				newest_in_stack_item = self.in_stack.pop()
				self.out_stack.append(newest_in_stack_item)

			# if out_stack is still empty, raise an error
			if len(self.out_stack) == 0:
				raise IndexError("Can't dequeue from empty queue!")

		return self.out_stack.pop()



class BinaryTreeNode(object):

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert_left(self, value):
		self.left = BinaryTreeNode(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTreeNode(value)
		return self.right


def is_balanced(tree_root):
	# A tree with no nodes is superbalanced, since there are no leaves
	if tree_root is None:
		return True

	# We short-circuit as soon as we find more than 2
	depths = []

	#We'll treat this list as a stack that will store tuples of (node, depth)
	nodes = []
	nodes.append((tree_root, 0))

	while len(nodes):
		# Pop n node and it's depth from the top of our stack
		node, depth = nodes.pop()

		# Case: we found a leaf
		if (not node.left) and (not node.right):
			# We only care if it's a new depth
			if depth not in depths:
				depths.append(depth)

			# Two ways we might now have an unbalanced tree:
			# 1) more than 2 different leaf depths
			# 2) 2 leaf depths that are more than 1 apart
				if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
					return False

		else:
			# Case: this isn't a leaf - keep stepping down
			if node.left:
				nodes.append((node.left, depth + 1))
			if node.right:
				nodes.append((node.right, depth + 1))

	return True


def is_binary_search_tree(tree_root):

	# Start at the root, with an arbitrarily low lower bound, and an arbitrarily high upper bound
	nodes_and_bounds_stack = [(tree_root, -float('inf'), float('inf'))]

	# Depth first traversal
	while len(nodes_and_bounds_stack):
		node, lower_bound, upper_bound = nodes_and_bounds_stack.pop()

		# If this node is invalid, we return false right away
		if (node.value <= lower_bound) or (node.value >= upper_bound):
			return False

		if node.left:
			# This node needs to be less than the current node
			nodes_and_bounds_stack.append((node.left, lower_bound, node.value))
		if node.right:
			# This node needs to be greater than the current node
			nodes_and_bounds_stack.append((node.right, node.value, upper_bound))

	# If none of the nodes were invalid, return true (we've checked all the nodes)
	return True


def find_largest(root_node):
	current = root_node

	while current:
		if not current.right:
			return current.value
		current = current.right


def find_second_largest(root_node):
	# This is O(lg n) time if tree is balanced, O(n) otherwise. O(1) space

	if (root_node is None or
			(root_node.left is None and root_node.right is None)):
		raise ValueError("Tree must have at least 2 nodes")

	current = root_node
	while current:
		# Case: current is largest and has a left subtree
		# 2nd largest is the largest in that subtree
		if current.left and not current.right:
			return find_largest(current.left)

		# Case: current is a parent of largest, and largest has no children,
		# so current is 2nd largest
		if (current.right and
				not current.right.left and
				not current.right.right):
			return current.right.value

		current = current.right


def get_max_profits(stock_prices):

	# we want the max profits
	# can only sell after we buy, no shorting
	# getting min and max won't work, what if we see [1, 4, 12, 2, 11] 12 - 4 = 8 but 11 - 2 = 9
	# so we want to keep track of current_max_profit at that time
	# so we can keep track of the min price, then see if we get a bigger profit than we've already seen
	max_profit = stock_prices[1] - stock_prices[0]
	# We have to start at index 0 because we need to buy before we sell, this is the earliest we can buy
	min_price = stock_prices[0]
	# We want to start our loop at index 1 since this is where we can first sell
	for price in stock_prices[1:]:
		profit = price - min_price
		if profit > max_profit:
			max_profit = profit
		# can also write max_profit = max(max_profit, profit)
		if price < min_price:
			min_price = price
		# can also write min_price = min(min_price, price)

	return max_profit


# def get_product_of_all_ints_except_at_index(int_list):

# 	# we want product of every integer except at the index without using division
# 	# brute force would be to multiply everything except the index
# 	# but then we'll be muliplying the same numbers over and over again.
# 	# so we want to use memoization, where we can temp store the result for easy access again later
# 	# start by keeping track of all the products at that index, that way we can add it to future ones
# 	# then we want to get the products of everything ahead of the index we're at,
# 	# then essentially adding them together

# 	#create a list as long as our int_list to save space
# 	if len(int_list) < 2:
# 		raise IndexError("Need at least two to calculate product so far")

# 	products_of_all_ints_except_at_index = [None] * len(int_list)

# 	product_so_far = 1

# 	for i in range(len(int_list)):
# 		products_of_all_ints_except_at_index[i] = product_so_far
# 		product_so_far *= int_list[i]

# 	product_so_far = 1
# 	# We want to now go backwards from the list to cover the right side of the index
# 	for i in range(len(int_list) - 1, -1, -1):
# 		products_of_all_ints_except_at_index[i] *= product_so_far
# 		product_so_far *= int_list[i]

# 	return products_of_all_ints_except_at_index



# Given a list of integers, find the highest product you can get from three of the integers.
# The input list of integers will always have at least three integers
def highest_product_of_3(int_list):

	if len(int_list) < 3:
		raise ValueError("less than 3 items!")

	# We're going to start at the 3rd item (at index 2)
	# so pre-populate highest and lowest based on the first 2 items
	# We could also start these at None and check below if they're set
	# But this is arguably cleaner
	highest = max(int_list[0], int_list[1])
	lowest_product_of_2 = int_list[0] * int_list[1]
	lowest = min(int_list[0], int_list[1])
	highest_product_of_2 = int_list[0] * int_list[1]
	
	# Except this one, we pre-populate it for the first 3 items
	# This means in our first pass it'll check against itself which is fine
	highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]

	# Walk through items starting at index 2
	for i in range(2, len(int_list)):
		current = int_list[i]

		# Do we have a new highest product of 3? 
		# It's either the current highest,
		# or the current times the highest product of two
		# or the current times the lowest product of two
		highest_product_of_3 = max(highest_product_of_3,
							 	   current * highest_product_of_2,
							 	   current * lowest_product_of_2)

		# Do we have a new highest product of two? 
		highest_product_of_2 = max(highest_product_of_2,
								   current * highest,
								   current * lowest)

		# Do we have a new lowest product of two?
		lowest_product_of_2 = min(lowest_product_of_2,
							      current * highest,
							      current * lowest)

		# Do we have a new highest? 
		highest = max(highest, current)

		# Do we have a new lowest? 
		lowest = min(lowest, current)

	return highest_product_of_3



def merge_ranges(meetings):

	# Start by sorting the start times (sorted creates a new list, sort modifies in place)
	# better to just use sorted so we can keep the order of the original list if necessary
	sorted_meetings = sorted(meetings)

	# Initialize merged_meetings with the earliest meeting
	merged_meetings = [sorted_meetings[0]]

	for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
		last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

		# If the current meeting overlaps with the last merged meeting, use the 
		# later end time of the two
		if (current_meeting_start <= last_merged_meeting_end):
			merged_meetings[-1] = (last_merged_meeting_start,
								   max(current_meeting_end,
								   	   last_merged_meeting_end))

		else:
			# Add current meeting since it doesn't overlap
			merged_meetings.append((current_meeting_start, current_meeting_end))

	return merged_meetings


def reverse_characters(message, left_index, right_index):

	while left_index < right_index:
		message[left_index], message[right_index] = message[right_index], message[left_index]

		left_index += 1
		right_index -= 1

# how would we reverse a list of chars of words with ' ' separating each word? 

def reverse_words(message):
	# First we want to reverse all the characters in the message
	reverse_characters(message, 0, len(message) - 1)

	# This gives us the right word order but with each word backward
	# Now we'll need to make the words forward again by reversing each word's characters
	# We hold the index of the *start* of the current word 
	# as we look for the *end* of the current word

	current_word_start_index = 0

	for i in range(len(message) + 1):
		# Found the end of the current word
		if (i == len(message)) or (message[i] == ' '):
			reverse_characters(message, current_word_start_index, i - 1)
			# If we haven't exhausted the message our next word's start is one character ahead
			current_word_start_index = i + 1


def reverse_linked_list(head):
	# We need to keep track of what's next and next next, since we need all 3 to reverse
	# we want the next node to be the cur node, then it becomes the 
	current_node = head
	next_node = None
	prev_node = None

	# Until we have "fallen off" the end of the list
	while current_node:
		# Copy a pointer to the next element
		# Before we overwrite current_node.next
		next_node = current_node.next

		# Reverse the 'next' pointer
		current_node.next = previous_node

		# Step foward in the list
		previous_node = current_node
		current_node = next_node

	return previous_node


def inorder_traversal(root_node):
	# inorder traversal is left, root, right

	result = []
	stack = []
	current = root_node

	while current or stack:
		if current: 
			stack.append(current)
			current = current.left

		else: 
			current = stack.pop()
			result.append(current.value)
			current = current.right

	return result


def find_range_overlap(point1, length1, point2, length2):
	# Find the highest start point and lowest end point
	# The highest ("rightmost" or "upmost") start point is the start point of the overlap
	# The lowest end point is the end point of the overlap
	highest_start_point = max(point1, point2)
	lowest_end_point = min(point1 + length1, point2 + length2)

	# Return null overlap if there is no overlap
	if highest_start_point >= lowest_end_point:
		return(None, None)

	# Comput the overlap length
	overlap_length = lowest_end_point - highest_start_point

	return (highest_start_point, overlap_length)



def find_rectangular_overlap(rect1, rect2):
	# Get the x and y overlap points and lengths
	x_overlap_point, overlap_width = find_range_overlap(rect1['left_x'],
													    rect1['width'],
													    rect2['left_x'],
													    rect2['width'])

	y_overlap_point, overlap_height = find_range_overlap(rect1['bottom_y'],
													     rect1['height'],
												  	     rect2['bottom_y'],
													     rect2['height'])

	# If they don't overlap, return None
	if not overlap_width or not overlap_height:
		return {
			'left_x': 	None,
			'bottom_y': None,
			'width': 	None,
			'height': 	None,
		}

	return {
		'left_x':	x_overlap_point,
		'bottom_y': y_overlap_point,
		'width': 	overlap_width,
		'height': 	overlap_height,
	}


def can_watch_two_movies(flight_length, movie_lengths):
	# Movie lengths we've seen so far
	movie_lengths_seen = set()

	for first_movie_length in movie_lengths:
		matching_second_movie_length = flight_length - first_movie_length
		if matching_second_movie_length in movie_lengths_seen:
			return True
		movie_lengths_seen.add(first_movie_length)

	# We never found a match, so return False
	return False


def max_duffel_bag_value(cake_tuples, weight_capacity):

	# We make a list to hold the maximum possible value at every duffle bag
	# weight capacity from 0 to weight_capacity
	# starting each index with a value 0
	max_values_at_capacities = [0] * (weight_capacity + 1)

	for current_capacity in range(weight_capacity + 1):
		# Set a variable to hold the max monetary value so far
		# for current_capacity
		current_max_value = 0

		for cake_weight, cake_value in cake_tuples:
			# If a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
			if cake_weight == 0 and cake_value != 0:
				return float('inf')

			# If the current cake weighs as much or less than the current weight capacity
			# it's possible taking the cake would get a better value
			if cake_weight <= current_capacity:

				# So we check: should we use the cake or not?
				# If we use the cake, the most kilograms we can include in addition to the cake
				# we're adding is the current capacity minus the cake weight. We find the max
				# value at that integer capacity in our list max_values_at_capacities
				max_value_using_cake = (cake_value + max_values_at_capacities[current_capacity - cake_weight])

				# Now we see if it's worth taking the cake, how does the value with the cake
				# compare to the current max_value?
				current_max_value = max(max_value_using_cake, current_max_value)

		#Add each capacity's max value to our list so we can use them when calculating
		# all the remaining capacities
		max_values_at_capacities[current_capacity] = current_max_value

	return max_values_at_capacities[weight_capacity]


def missing_drone(delivery_id_confirmations):
	delivery_dict = defaultdict(int)

	for delivery_id in delivery_id_confirmations:
		delivery_dict[delivery_id] += 1

	for key, value in delivery_dict.items():
		if value == 1:
			return key


def delete_node(node):
	next_node = node.next
	
	if next_node:
		node.value = next_node.value
		node.next = next_node.next
	else:
		raise Exception("Can't delete the last node with this technique")


def get_closing_paren(sentence, opening_paren_index):
	open_nested_parens = 0

	for position in range(opening_paren_index + 1, len(sentence)):
		char = sentence[position]

		if char == "(":
			open_nested_parens += 1

		elif char == ")":
			if open_nested_parens == 0:
				return position
			else:
				open_nested_parens -= 1

	raise Exception("No closing parenthesis: (")


def has_palindrome_permutatation(the_string):
	# Track characters we've seen an odd number of times
	unpaired_characters = set()

	for char in the_string:
		if char in unpaired_characters:
			unpaired_characters.remove(char)
		else:
			unpaired_characters.add(char)

	# The string has a palindrome permutation if it has one or zero characters without a pair
	return len(unpaired_characters) <= 1
