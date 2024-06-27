import numpy as np


x = [3, 2, 2]


# Define the basis vectors
b1 = [1, 0, 0]
b2 = [0, 1, 1]
# Form the matrix B whose columns are the basis vectors
B = np.column_stack((b1, b2))

# Calculate B^T B
BTB = B.T @ B
# Calculate the inverse of B^T B
BTB_inv = np.linalg.inv(BTB)
# Calculate the projection matrix P
P = B @ BTB_inv @ B.T
projection_point = P @ x

# Calculate the rank of the projection matrix P
rank_P = np.linalg.matrix_rank(P)

print(P)

P1D = (projection_point @ projection_point.T) / np.sqrt((projection_point.T @ projection_point))
