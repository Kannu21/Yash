import numpy as np

# 1. Create a 1D array of integers from 1 to 5 with data type int32
arr1 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("1D array of integers:")
print(arr1)
print("Data type:", arr1.dtype)
print()

# 2. Create a 2D array of shape (3, 3) with data type float64 where all elements are zero
arr2 = np.zeros((3, 3), dtype=np.float64)
print("2D array of zeros:")
print(arr2)
print("Data type:", arr2.dtype)
print()

# 3. Create a 3D array of shape (2, 2, 2) with random integers between 0 and 100 with data type int8
arr3 = np.random.randint(0, 101, size=(2, 2, 2), dtype=np.int8)
print("3D array of random integers:")
print(arr3)
print("Data type:", arr3.dtype)
print()

# 4. Convert a 1D array of integers to an array of floats
int_arr = np.array([1, 2, 3, 4, 5])
float_arr = int_arr.astype(np.float64)
print("Original integer array:")
print(int_arr)
print("Converted to float:")
print(float_arr)
print("New data type:", float_arr.dtype)
print()

# 5. Create a 2D array of shape (2, 3) with data type float32 and then convert it to int32
arr5 = np.array([[1.5, 2.7, 3.2],
                 [4.9, 5.1, 6.8]], dtype=np.float32)
print("Original float32 array:")
print(arr5)
print("Data type:", arr5.dtype)

arr5_int = arr5.astype(np.int32)
print("\nConverted to int32:")
print(arr5_int)
print("New data type:", arr5_int.dtype)
