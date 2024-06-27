import numpy as np

# GRADED FUNCTION: DO NOT EDIT THIS LINE
def cov_naive(X):
    """Compute the sample covariance for a dataset by iterating over the dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset.
        N is the size of the dataset (the number of data points)
        and D is the dimensionality of each data point.
    Returns:
        ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    N, D = X.shape
    ### Edit the code below to compute the covariance matrix by iterating over the dataset.
    covariance = np.zeros((D, D))

    # Compute the mean of each dimension
    mean = np.mean(X, axis=0)

    # i, j = (0, 1)
    #
    # for n in range(N):
    #     covariance[i, j] += (X[n, i] - mean[i]) * (X[n, j] - mean[j])


    for i in range(D):
        for j in range(D):
            for n in range(N):
                covariance[i, j] += (X[n, i] - mean[i]) * (X[n, j] - mean[j])
            covariance[i, j] /= N

    ### Update covariance

    ###
    return covariance



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

    test_1 = cov_naive(X_1)
    test_2 = cov_naive(X_2)
    test_3 = cov_naive(X_3)
    print(f"\nTest 1 Output:\n{test_1} \nExpected Output:\n{expected_cov_1}")
    print(f"\nTest 1 Output:\n{test_2} \nExpected Output:\n{expected_cov_2}")
    print(f"\nTest 1 Output:\n{test_3} \nExpected Output:\n{expected_cov_3}")