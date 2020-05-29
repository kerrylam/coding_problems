def reverse(list_of_chars):

	left_index = 0
	right_index = len(list_of_chars) - 1

	while left_index < right_index:
		#swap characters
		list_of_chars[left_index], list_of_chars[right_index] = \
		list_of_chars[right_index], list_of_chars[left_index]
		#move towards middle
		left_index += 1
		right_index -= 1
