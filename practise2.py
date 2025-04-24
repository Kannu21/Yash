import numpy as np

# Create the initial array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 1. Extract the sub-array containing first two rows and first two columns
sub_array = array[0:2, 0:2]
print("Sub-array (2x2):")
print(sub_array)

# 2. Extract all even elements
even_elements = array[array % 2 == 0]
print("\nEven elements:")
print(even_elements)

# 3. Swap first and last rows
swapped_rows = array.copy()
swapped_rows[[0, -1]] = swapped_rows[[-1, 0]]
print("\nArray with first and last rows swapped:")
print(swapped_rows)

# 4. Reverse the order of columns
reversed_columns = array[:, ::-1]
print("\nArray with reversed columns:")
print(reversed_columns)