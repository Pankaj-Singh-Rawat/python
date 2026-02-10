"""
Numpy : used with arrays
"""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

print(type(arr))

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# 0-D array:
arr0 = np.array(32)
print(arr0)
print()

#1-D array:
arr1 = np.array([1,2,3,4,5])
print(arr1)
print()

#2-D array:
arr2 = np.array([[1,2],[3,4]])
print(arr2)
print()

#3-D array:
arr3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr3)
print()

# to check number of dimensions -> arr.ndim
print("arr3 is of", arr3.ndim, "dimensions")
print()


# When the array is created, you can define the number of dimensions by using the ndmin argument.
arr4 = np.array([1,2,3,4], ndmin= 5)
print(arr4)
print("number of dimensions here are:", arr4.ndim)

# to check which data type is used in numpy arrays -> arr.dtype
print(arr4.dtype)
print()

# astype is used for copying array and type casting it into different data type
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)