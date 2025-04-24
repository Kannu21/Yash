import numpy as np

# 1. NumPy Array Manipulation
print("1. NumPy Array Manipulation:")
# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Original 1D array:", arr1)
print("Original 2D array:\n", arr2)

# Indexing
print("\nIndexing:")
print("First element of 1D array:", arr1[0])
print("Element at position [1,2] in 2D array:", arr2[1,2])

# Slicing
print("\nSlicing:")
print("First three elements:", arr1[0:3])
print("Second row of 2D array:", arr2[1,:])

# Array operations
print("\nArray operations:")
print("Sum of all elements:", arr2.sum())
print("Mean of array:", arr2.mean())
print("Maximum value:", arr2.max())
print("\n")

# 2. NumPy Array Resizing
print("2. NumPy Array Resizing:")
arr = np.array([[1, 2], [3, 4]])
print("Original array:\n", arr)

# Resize using resize() method
resized_arr = np.resize(arr, (3, 2))
print("\nResized to 3x2:\n", resized_arr)

# Append elements
print("\nAppend elements:")
appended_arr = np.append(arr, [[5, 6]], axis=0)
print(appended_arr)

# Insert elements
print("\nInsert elements:")
inserted_arr = np.insert(arr, 1, [5, 6], axis=0)
print(inserted_arr)
print("\n")

# 3. NumPy Array Broadcasting
print("3. NumPy Array Broadcasting:")
# Create arrays of different shapes
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])

print("Array a:\n", a)
print("Array b:", b)
print("\nAfter broadcasting (a + b):\n", a + b)

# Broadcasting with scalar
print("\nBroadcasting with scalar:")
print("Array * 2:\n", a * 2)
print("\n")

# 4. NumPy reshape() function
print("4. NumPy reshape() function:")
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", arr)

# Reshape to 2D array
reshaped_2d = arr.reshape(2, 3)
print("\nReshaped to 2x3:\n", reshaped_2d)

# Reshape to 3D array
reshaped_3d = arr.reshape(2, 1, 3)
print("\nReshaped to 2x1x3:\n", reshaped_3d)

# Using -1 in reshape
print("\nUsing -1 in reshape:")
auto_reshaped = arr.reshape(-1, 2)  # automatically calculates the number of rows
print(auto_reshaped)
