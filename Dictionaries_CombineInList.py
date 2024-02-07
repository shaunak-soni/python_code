#For the given Dictionay construct two lists one containing all the keys of both dictionaries and one containing all the values of each dictionary

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 40, 'g': 50}


keys = list(d1.keys())
values = list(d1.values())

for d in (d2, d3):
    keys.extend(d.keys())
    values.extend(d.values())

print(f'The First Dictionary D1 is: \n {d1}')		
print(f'The Second Dictionary D2 is: \n {d2}')			
print(f'The Third Dictionary D3 is: \n {d3}')
				
print(f'The Combined List of Keys is: \n {keys}')		
print(f'The Combined List of Values is: \n {values}')		
	
	
	