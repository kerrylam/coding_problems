# from collections import defaultdict

# def is_valid_sub_sudoku(mat):

# 	mat_length = len(mat)
# 	col_dict = defaultdict(set)

# 	for row_list in mat:
# 		row_set = set()
# 		col_index = 0

# 		for num in row_list:
# 			if (num < 1) or (num > mat_length):
# 				return "INVALID"
# 			else:
# 				col_dict[col_index].add(num)
# 				row_set.add(num)
# 				col_index += 1
# 		if len(row_set) != mat_length:
# 			return "INVALID"
			
# 	for column in col_dict.values():
# 		if len(column) != mat_length:
# 			return "INVALID"
# 	return "VALID"



from collections import defaultdict

# Args:
#    matrix: an NxN list of lists containing the matrix to check
# Returns:
#    The string "VALID" if matrix contains a valid sub-sudoku solution, and
#    "INVALID" otherwise

def check_sub_sudoku(mat):
  """check if sub-Sudoku is valid
  
  1. loop through each row of the matrix
  2. check if the values are between 1...N
  3. check if the row properly contains a unique set of 1...N (via length of set)
  4. add to a dictionary that contains key: column_index, value: set(column_numbers)
  5. check if every column properly contains a unique set of 1...N (via length of set)
  6. return "VALID" if all sets are of N length
  """

  mat_length = len(mat)
  col_dict = defaultdict(set)

  #loop through every row in the matrix
  for row_list in mat:
    #create a set for this row to check for duplicate numbers
    row_set = set()
    col_index = 0
    
    #loop through each number in the row
    for num in row_list:
      #if the number is not between 1...N, return "INVALID" immediately  
      if (num < 1) or (num > mat_length):
        return "INVALID"
      #else map the values to its column
      else:
        col_dict[col_index].add(num)
        row_set.add(num)
        col_index += 1
    
    #return "INVALID" if this row is incomplete
    if len(row_set) != mat_length:
      return "INVALID"
  
  #return "INVALID" if any column is incomplete
  for column in col_dict.values():
    if len(column) != mat_length:
      return "INVALID"
    
  return "VALID"