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

# [105, 42, 30, 70] 
print(get_products_of_all_ints_except_at_index([2, 5, 7, 3]))

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
			if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1] > 1)):
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



	


