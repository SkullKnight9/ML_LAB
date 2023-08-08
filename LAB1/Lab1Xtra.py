#Q1--------------------------

import numpy as np

arr = np.random.randint(30,41,10)
print(arr)

#Q2--------------------------

A = ((1,2,3),(4,5,6),(7,8,19))
B = ((7,8,10), (4,5,6), (1,2,3))

C = np.add(A,B)
E = np.subtract(A,B)

print(C)
print(E)

F = np.sum(A)

print(F)

print(np.sum(B, axis = 0))
print(np.sum(C, axis = 1))

D = np.matmul(A, B)

print(D)

print(np.sort(C, axis = 0))
print(E)
print(np.transpose(E))