import numpy as np


def pairwise_distance_matrix(X, Y):
    """Compute the pairwise distance between rows of X and rows of Y

    Arguments
    ----------
    X: ndarray of size (N, D)
    Y: ndarray of size (M, D)

    Returns
    --------
    D: matrix of shape (N, M), each entry D[i,j] is the distance between
    X[i] and Y[j] using the dot product.
    """
    N, D = X.shape
    M, _ = Y.shape

    # Compute squared norms of each row in X and Y
    X_norm = np.sum(X ** 2, axis=1).reshape((N, 1))  # Shape (N, 1)
    Y_norm = np.sum(Y ** 2, axis=1).reshape((1, M))  # Shape (1, M)

    # Use the broadcasting and the formula ||x-y||^2 = ||x||^2 + ||y||^2 - 2<x,y>
    # to compute the squared distance matrix
    squared_dist_matrix = X_norm + Y_norm - 2 * np.dot(X, Y.T)

    # Taking the square root gives the Euclidean distance matrix
    distance_matrix = np.sqrt(np.maximum(squared_dist_matrix, 0))  # Ensure no negative values

    return distance_matrix


# Example test
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
result = pairwise_distance_matrix(X, Y)
