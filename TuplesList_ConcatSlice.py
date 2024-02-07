# Concatenate the given tuples into a single tuple and replcae the odd values with 0

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

l1 = list(t1)
l2 = list(t2)
l3 = list(t3)

l1[::2] = [0] * len(l1[::2])
l2[::2] = [0] * len(l2[::2])
l3[::2] = [0] * len(l3[::2])

result = tuple(l1 + l2 + l3)

print(f'The first tuple is {t1}')
print(f'The second tuple is {t2}')
print(f'The third tuple is {t3}')
print(f'The result tuple is {result}')
