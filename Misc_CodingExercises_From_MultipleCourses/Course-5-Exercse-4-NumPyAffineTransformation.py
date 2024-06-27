import numpy as np
from numpy.testing import assert_allclose


def affine_mean(mean, A, b):
    """Compute the mean after affine transformation
    Args:
        mean: `ndarray` of shape (D,), the sample mean vector for some dataset.
        A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x
    Returns:
        sample mean vector of shape (D,) after affine transformation.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    ### Edit the code below to compute the mean vector after affine transformation
    affine_m = np.zeros(mean.shape) # affine_m has shape (D,)
    ### Update affine_m
    affine_m = A @ mean + b
    ###
    return affine_m


def affine_covariance(S, A, b):
    """Compute the covariance matrix after affine transformation

    Args:
        S: `ndarray` of shape (D, D), the sample covariance matrix for some dataset.
        A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x

    Returns:
        the sample covariance matrix of shape (D, D) after the transformation
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    ### EDIT the code below to compute the covariance matrix after affine transformation
    affine_cov = np.zeros(S.shape)  # affine_cov has shape (D, D)
    ### Update affine_cov

    affine_cov = A @ S @ A.T

    ###
    return affine_cov


if __name__ == '__main__':

    A = np.array([[0, 1], [2, 3]])
    b = np.ones(2)
    m = np.full((2,), 2)
    S = np.eye(2)*2

    expected_affine_mean = np.array([ 3., 11.])
    expected_affine_cov = np.array(
        [[ 2.,  6.],
        [ 6., 26.]])

    assert_allclose(affine_mean(m, A, b), expected_affine_mean, rtol=1e-4)
    assert_allclose(affine_covariance(S, A, b),
                    expected_affine_cov, rtol=1e-4)