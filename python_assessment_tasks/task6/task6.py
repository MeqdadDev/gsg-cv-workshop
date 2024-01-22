"""
Task 6:
1- Given a set of linear equations in matrix form Ax=b, implement a function to find the solution vector x.
(Hint: you may need the functions you wrote in Task 5).

2- Use that function to solve the following system of equations (after writing them in the matrix form):

x + 2y + 3z = 10
2x + 5y + 3z = 15
2x + 8z = 20

"""
########### Solution ###########
import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

b = np.array([8, 9, 10])

#######################
### 1- Given a set of linear equations in matrix form Ax=b,
#       implement a function to find the solution vector x.

def has_inverse(m):
    if np.linalg.det(m) == 0:
        print("This matrix has no inverse (singular).\nNo unique solution.")
        return False
    return True

def solve_equation(A, b):
    if has_inverse(A):
        x = np.linalg.solve(A, b)
        return x

vector_x = solve_equation(A, b)
print("vector_x =", vector_x)


print("\n#######################")

#######################
"""
2- Use that function to solve the following system of equations (after writing them in the matrix form):

x + 2y + 3z = 10
2x + 5y + 3z = 15
2x + 8z = 20
"""

# (Coefficient)
A = np.array([[1, 2, 3],
              [2, 5, 3],
              [2, 0, 8]])


b = np.array([10, 15, 20])

result = solve_equation(A, b)

print("Result =", result)

print("\n#######################")

print("By: Meqdad A. Darwish")
print("Computer Vision Workshop by GSG")
