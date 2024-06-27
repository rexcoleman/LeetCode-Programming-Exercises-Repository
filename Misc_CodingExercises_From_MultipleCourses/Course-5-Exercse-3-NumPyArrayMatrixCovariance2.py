import numpy as np


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def cov(X):
    """Compute the sample covariance for a dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset.
        N is the size of the dataset (the number of data points)
        and D is the dimensionality of each data point.
    Returns:
        ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
    """
    # YOUR CODE HERE

    # It is possible to vectorize our code for computing the covariance with matrix multiplications,
    # i.e., we do not need to explicitly
    # iterate over the entire dataset as looping in Python tends to be slow
    # We challenge you to give a vectorized implementation without using np.cov, but if you choose to use np.cov,
    # be sure to pass in bias=True.
    ### Uncomment and edit the code below

    N, D = X.shape
    # Centering the data by subtracting the mean
    X_centered = X - np.mean(X, axis=0)

    # Compute the covariance matrix using matrix multiplication
    covariance_matrix = (X_centered.T @ X_centered) / (N)

    return covariance_matrix




if __name__ == '__main__':
    X_1 = np.array([[0., 1.],
                  [1., 2.],
                  [0., 1.],
                  [1., 2.]])
    expected_cov_1 = np.array(
        [[0.25, 0.25],
         [0.25, 0.25]])
    X_2 = np.array([[0., 1.],
                  [2., 3.]])
    expected_cov_2 = np.array(
        [[1., 1.],
         [1., 1.]])
    X_3 = np.array([[0., 1.],
                  [0., 1.],
                  [0., 1.]])
    expected_cov_3 = np.zeros((2, 2))

    test_1 = cov(X_1)
    test_2 = cov(X_2)
    test_3 = cov(X_3)
    print(f"\nTest 1 Output:\n{test_1} \nExpected Output:\n{expected_cov_1}")
    print(f"\nTest 2 Output:\n{test_2} \nExpected Output:\n{expected_cov_2}")
    print(f"\nTest 3 Output:\n{test_3} \nExpected Output:\n{expected_cov_3}")