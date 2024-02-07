#Find all the unique keys in the sub-dictionaries in the below data structure

data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}

print(f'\nThe original data structure is: \n {data}')	

#recover the keys of dictionary using the keys() method
data['d1'].keys()

#union these keys across all three dictionaries:
data['d1'].keys() | data['d2'].keys() | data['d3'].keys()

#loop over the values in data - those will be the sub-dictionaries:
print(f'\nThe sub-dictionaries are: \n ')
for d in data.values():
    print(d)

#start with an empty set and keep replacing this set with it's union with the keys of each dictionary:	
result = set()
for d in data.values():
    result = result | d.keys()

print(f'\nThe list with unique keys in the sub-dictionaries is: \n {result} \n')	