import numpy as np # we commonly use the np abbreviation when referring to numpy

def multiply(A, B):
    """
    Multiplies two polynomials

    Arguments:
    A: Coefficients of the first polynomial
    B: Coefficients of the second polynomial

    Returns:
    C: The coefficients of A*B
    """

    ### BEGIN SOLUTION

    # Find the coefficients of both the polynomials
    na = np.shape(A)[0]
    nb = np.shape(B)[0]

    # Pad the smaller array with 0s
    # N = max(na, nb)
    # A_padded = np.pad(A, (0, N - na), 'constant', constant_values=0)
    # B_padded = np.pad(B, (0, N - nb), 'constant', constant_values=0)

    # Initialize the output array with 0s
    C = np.zeros((na + nb -1))

    B_flipped = np.flip(B)


    # Perform the multiplication
    # You might want to break the loop over i into two separate phases
    for i in range(len(C)):
        for j in range(max(0, i-nb+1), min(na, i+1)):
            C[i] += A[j] * B_flipped[nb - 1 - (i-j)]


    # Remove any extra 0s from the back of C
    C = np.trim_zeros(C, 'b')

    ### END SOLUTION

    return C


if __name__ == '__main__':
    A_1 = np.array([1, 2])
    B_1 = np.array([3, 4])
    A_2 = np.array([5, 6])
    B_2 = np.array([1, 3, 5, 9])
    print(f"Test 1: {multiply(A_1, B_1)}")
    print(f"Test 2: {multiply(A_2, B_2)}")