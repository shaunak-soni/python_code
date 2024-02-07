#Given the following iterable of vectors, create a list that contains the magnitude of each vector using comprehensions
#Compare the performance using for loop vs using comprehensions.

from math import sqrt
from time import perf_counter

vectors = [(0,0), (0,1), (1, 0), (1, 1)]

print(f'\nThe given Vector is : \n {vectors}')

print(f'\nChecking Performance and time taken in for loop ')

start = perf_counter()
for i in range(100_000):
    magnitudes = []
    for vector in vectors:
        magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
        magnitudes.append(magnitude)
end = perf_counter()

elapsed_time = end - start
print(f'The magnitude for the vector is : {elapsed_time}')
print(f'The total elapsed time in for loop is : {elapsed_time}')


print(f'\nChecking Performance and time taken in comprehension ')

start = perf_counter()
for i in range(100_000):
    magnitudes = [sqrt(vector[0] + vector[1]) for vector in vectors]
end = perf_counter()

elapsed_time = end - start

print(f'The magnitude for the vector is : {elapsed_time}')
print(f'The total elapsed time in comprehension is : {elapsed_time}')