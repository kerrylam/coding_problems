from collections import defaultdict

def is_valid_sub_sudoku(mat):

	mat_length = len(mat)
	col_dict = defaultdict(set)

	for row_list in mat:
		row_set = set()
		col_index = 0

		for num in row_list:
			if (num < 1) or (num > mat_length):
				return "INVALID"
			else:
				col_dict[col_index].add(num)
				row_set.add(num)
				col_index += 1
		if len(row_set) != mat_length:
			return "INVALID"
			
	for column in col_dict.values():
		if len(column) != mat_length:
			return "INVALID"
	return "VALID"


