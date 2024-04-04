
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

import numpy as np


def normalize(X):
    N, D = X.shape
    mu = np.mean(X, axis=0)  # <-- EDIT THIS, compute the mean of X
    Xbar = X - mu  # <-- EDIT THIS, compute the normalized data Xbar by subtracting mu from each row of X
    return Xbar, mu


def PCA_high_dim(X, num_components):
    """Compute PCA for small sample size but high-dimensional features.
    Args:
        X: ndarray of size (N, D), where D is the dimension of the sample,
           and N is the number of samples
        num_components: the number of principal components to use.
    Returns:
        X_reconstruct: (N, D) ndarray. the reconstruction
        of X from the first `num_components` pricipal components.
    """
    # YOUR CODE HERE
    # Uncomment and modify the code below
    N, D = X.shape
    # Normalize the dataset
    X_normalized, mean = normalize(X)
    # Find the covariance matrix
    S = np.dot(X_normalized, X_normalized.T) / N

    # Next find eigenvalues and corresponding eigenvectors for S
    eig_vals, eig_vecs = np.linalg.eigh(S)
    # Make sure that you only take the first D eigenvalues/vectors
    idx = eig_vals.argsort()[::-1]
    eig_vals = eig_vals[idx]
    eig_vecs = eig_vecs[:, idx]
    top_eig_vecs = eig_vecs[:, :num_components]
    V = eig_vecs[:, :num_components]

    # You can also take a look at the eigenvalues beyond column (D-1) and they should be
    # zero (or a very small number due to finite floating point precision)

    # Compute the eigenvalues and eigenvectors for the original system
    # eig_vecs = None

    #     Compute the eigenvectors for the original covariance matrix


    # Normalize U


    # Normalize the eigenvectors to have unit-length
    # Take the top `num_components` of the eigenvalues / eigenvectors
    # as the principal values and principal components




    principal_components = np.dot(X_normalized.T, V)
    principal_components = principal_components / np.linalg.norm(principal_components, axis=0)
    principal_values = eig_vals[:num_components]
    projected_data = np.dot(X_normalized, principal_components)
    # Due to precision errors, the eigenvectors might come out to be complex, so only take their real parts


    # reconstruct the images from the lower dimensional representation
    # Remember to add back the sample mean
    reconst = np.dot(projected_data, principal_components.T) + mean
    return reconst, mean, principal_values, principal_components





