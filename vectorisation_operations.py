import numpy as np

def example1_scalar_addition():
    print("Example 1: Adding a Scalar to an Array")
    array = np.array([1, 2, 3, 4, 5])
    scalar = 10
    result = array + scalar
    print("Original Array:", array)
    print("Scalar:", scalar)
    print("Result:", result)
    print()

def example2_array_addition():
    print("Example 2: Adding Two Arrays of Different Shapes")
    array2d = np.array([[1, 2], [3, 4], [5, 6]])
    array1d = np.array([[10], [20], [30]])  # Column vector for broadcasting
    result = array2d + array1d
    print("2D Array:\n", array2d)
    print("1D Array:\n", array1d)
    print("Result:\n", result)
    print()

def example3_array_multiplication():
    print("Example 3: Multiplying Arrays of Different Shapes")
    array2d = np.array([[1], [2], [3]])
    array1d = np.array([10, 20, 30])
    result = array2d * array1d
    print("2D Array:\n", array2d)
    print("1D Array:", array1d)
    print("Result:\n", result)
    print()

def example4_normalizing_data():
    print("Example 4: Normalizing Data")
    data = np.array([[1.0, 2.0, 3.0],
                     [4.0, 5.0, 6.0],
                     [7.0, 8.0, 9.0]])
    mean = data.mean(axis=0)
    std = data.std(axis=0)
    normalized_data = (data - mean) / std
    print("Original Data:\n", data)
    print("Mean:", mean)
    print("Standard Deviation:", std)
    print("Normalized Data:\n", normalized_data)
    print()

def example5_subtracting_row_mean():
    print("Example 5: Subtracting Row Mean")
    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
    row_means = data.mean(axis=1, keepdims=True)
    result = data - row_means
    print("Original Data:\n", data)
    print("Row Means:\n", row_means)
    print("Result:\n", result)
    print()

def example6_outer_product():
    print("Example 6: Outer Product")
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    result = np.outer(vector1, vector2)
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Outer Product:\n", result)
    print()

def example7_broadcasting():
    print("Example 7: Broadcasting with Higher Dimensions")
    # Create arrays with compatible shapes for broadcasting
    A = np.random.rand(2, 3, 4)
    B = np.random.rand(1, 3, 4)  # Shape compatible with broadcasting
    result = A + B
    print("Array A (2, 3, 4):\n", A)
    print("Array B (1, 3, 4):\n", B)
    print("Result (A + B):\n", result)
    print()

# Run all examples
example1_scalar_addition()
example2_array_addition()
example3_array_multiplication()
example4_normalizing_data()
example5_subtracting_row_mean()
example6_outer_product()
example7_broadcasting()