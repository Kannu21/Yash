import numpy as np

# Create example arrays
print("Creating Arrays:")
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Array a:", a)
print("Array b:", b)
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("\n")

# Basic Arithmetic Operations
print("Basic Arithmetic Operations:")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Integer Division (a // b):", a // b)
print("Modulus (b % a):", b % a)
print("Power (a ** 2):", a ** 2)
print("\n")

# Matrix Operations
print("Matrix Operations:")
print("Matrix Addition:\n", matrix1 + matrix2)
print("Matrix Subtraction:\n", matrix1 - matrix2)
print("Element-wise Matrix Multiplication:\n", matrix1 * matrix2)
print("Matrix Multiplication (dot product):\n", np.dot(matrix1, matrix2))
print("Matrix Transpose of matrix1:\n", matrix1.T)
