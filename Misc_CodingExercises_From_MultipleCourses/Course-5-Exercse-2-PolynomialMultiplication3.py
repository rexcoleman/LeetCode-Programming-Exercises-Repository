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
    C = np.convolve(A, B)

    return C


if __name__ == '__main__':
    A_1 = np.array([1, 2])
    B_1 = np.array([3, 4])
    A_2 = np.array([5, 6])
    B_2 = np.array([1, 3, 5, 9])
    print(f"Test 1: {multiply(A_1, B_1)}")
    print(f"Test 2: {multiply(A_2, B_2)}")