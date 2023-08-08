import numpy as np

#Q1--------------------------

arr = np.array([0,1,2,3,4,5,6,7,8])

print(arr)

arr1 = arr.reshape(3,3)

print(arr1)


#Q2----------------------------

arr2 = np.array([0,1,2,3,4,5,6,7,8,9])

arr2[arr2 % 2 != 0] = -1

print(arr2)


#Q3----------------------------

x = np.array([21,64,86,22,74,55,81,79,90,89])
y = np.array([21,7,3,45,10,29,55,4,37,18])

arr_comp1 = np.nonzero(x > y)[0]

print(arr_comp1)

arr_comp2 = np.nonzero(x == y)[0]

print(arr_comp2)


#Q4----------------------------


assign4 = np.arange(100).reshape(5,-1)

print(assign4)

print(assign4[:,[0,1,2,3]])