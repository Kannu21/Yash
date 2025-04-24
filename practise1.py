import numpy as np

# Create the array
array = np.array([[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]])

# 1. Extract element at row index 2 and column index 3
element_at_2_3 = array[2, 3]
print("Element at row 2, column 3:", element_at_2_3)  # Should print 13

# 2. Extract the third row
third_row = array[2]
print("Third row:", third_row)  # Should print [10 11 12 13 14]

# 3. Extract the second column
second_column = array[:, 1]
print("Second column:", second_column)  # Should print [ 1  6 11 16 21]

# 4. Extract 2x2 subarray starting from element (1,1)
subarray_2x2 = array[1:3, 1:3]
print("2x2 subarray:\n", subarray_2x2)  # Should print [[6  7]
                                        #                [11 12]]

# 5. Extract elements greater than 10
elements_greater_than_10 = array[array > 10]
print("Elements greater than 10:", elements_greater_than_10)

# 6. Extract elements at specific positions
positions = [(0, 0), (1, 2), (3, 4)]
elements_at_positions = array[tuple(zip(*positions))]
print("Elements at positions:", elements_at_positions)  # Should print [0 7 19]
