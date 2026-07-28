# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)

    return result

print("PART A — Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


print("\nPART B — Matrix Addition")

print("Enter dimensions for matrices to add:")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A:")
matrix_a = read_matrix(rows, cols)

print("\nEnter Matrix B:")
matrix_b = read_matrix(rows, cols)

print("\nMatrix A + Matrix B:")
display_matrix(add_matrices(matrix_a, matrix_b))


print("\nPART C — Matrix Multiplication")

print("Enter Matrix A dimensions:")
rows_a = int(input("Enter number of rows: "))
cols_a = int(input("Enter number of columns: "))

print("\nEnter Matrix A:")
matrix_a = read_matrix(rows_a, cols_a)


print("\nEnter Matrix B dimensions:")
rows_b = int(input("Enter number of rows: "))
cols_b = int(input("Enter number of columns: "))

if cols_a != rows_b:
    print("Error: Columns of Matrix A must equal rows of Matrix B.")
else:
    print("\nEnter Matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)

    print("\nMatrix A x Matrix B:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))