import numpy as np


# create an array using the array method.
def create_array():
    # one dimensional array
    arr = np.array([1, 2, 4, 4, 8, 9, 0])

    print(f"One dimensional array {arr}")

    arr = np.array([[2, 12, 10, 11, 35, 16], [2, 12, 6, 43, 76, 1]])

    print(f"two dimensional array {arr}")


def matrix_multiplication():
    arr1 = np.random.randn(3, 4)
    arr2 = np.random.randn(4, 2)

    print(f"matrix multiplication {arr1} X {arr2} =  {np.dot(arr1, arr2)}")


def dot_product():
    arr1 = np.array([1, 2, 3, 5, 6, 3])
    arr2 = np.array([19, 23, 54, 5, 7, 12, ])

    print(f"Dot Product {np.dot(arr2, arr1)}")


if __name__ == "__main__":
    # create_array()
    # matrix_multiplication()
    dot_product()