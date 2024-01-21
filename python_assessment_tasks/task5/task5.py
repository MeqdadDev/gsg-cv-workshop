"""
Task 5:
1- Write a function to multiply two matrices.
2- Write a function to find the determinant of a 2x2 matrix.
3- Write a function to calculate the determinant of a 3x3 matrix. (Hint: you may need the function in the previous point).
4- Write a function to calculate the inverse of a 3x3 matrix. (Hint: you may need the functions in the previous point).
"""
########### Solution ###########
import numpy as np

mat1 = np.array([[1, 3],
                [4, 2]])

mat2 = np.array([[5, 7],
                [8, 6]])

#######################
### 1- Write a function to multiply two matrices.
def mul_two_mat(m1, m2):
    if m1.shape[1] != m2.shape[0]:      # Check if columns of m1 == rows of m2
        raise RuntimeError("Can't be multiplied, columns of matrix A != rows of matrix B.")
    return np.dot(m1, m2)

dot_mat = mul_two_mat(mat1, mat2)
print("mat1 X mat2 =")
print(dot_mat)
print("\n#######################")

#######################
### 2- Write a function to find the determinant of a 2x2 matrix.

def mat_determinant_2x2(m):
    # Check if m is a square matrix
    if m.shape[0] != m.shape[1]:
        raise RuntimeError("Can't calculate the determinant, not a square matrix.")
    
    return np.linalg.det(m)

mat_determinant = mat_determinant_2x2(mat2)
print("det[mat2] =", mat_determinant)
print("\n#######################")

#######################
### 3- Write a function to calculate the determinant of a 3x3 matrix.

mat3 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

def mat_determinant_3x3(m):
    # Check if m is a square matrix
    if m.shape[0] != m.shape[1]:
        raise RuntimeError("Can't calculate the determinant, not a square matrix.")
    
    return np.linalg.det(m)

mat3_determinant = mat_determinant_3x3(mat3)
print("det[mat3] =", mat3_determinant)
print("\n#######################")

#######################
### 4- Write a function to calculate the inverse of a 3x3 matrix.

mat4 = np.array([[1, 2, 3],
                [0, 1, 4],
                [5, 6, 0]])

def mat_inverse(m):
    if np.linalg.det(m) == 0:
        raise RuntimeError("This matrix has no inverse (singular).")
    return np.linalg.inv(m)

mat4_inv = mat_inverse(mat4)
print("inv[mat4] =")
print(mat4_inv)
print("\n#######################")


print("By: Meqdad A. Darwish")
print("Computer Vision Workshop by GSG")
