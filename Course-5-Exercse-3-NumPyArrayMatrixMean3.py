
import numpy as np


def mean_naive(X):
    "Compute the mean for a dataset X nby iterating over the data points"
    # X is of size (D,N) where D is the dimensionality and N the number of data points
    D, N = X.shape
    mean = np.zeros((D, 1))
    for n in range(N):  # iterate over the dataset
        mean += X[:, n].reshape(D, 1)  # Add current data point to the mean
    mean /= N  # Divide by the number of data points to compute the mean
    return mean



if __name__ == '__main__':
    X_1 = np.array([[0., 1., 1.],
                  [1., 2., 1.]])
    expected_mean_1 = np.array([0.5, 1.5, 1.])
    X_2 = np.array([[0., 1., 0.],
                  [2., 3., 1.]])
    expected_mean_2 = np.array([1., 2., 0.5])
    test_1 = mean_naive(X_1)
    test_2 = mean_naive(X_2)
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_mean_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_mean_2}")

