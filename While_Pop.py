#Delete last element from list till the list is empty. 

data = [100, 200, 300, 400, 500]

print(f'The List is {data}')

while len(data) > 0:
    last_element = data.pop()  # retrieves and removes last list element
    print(f'processing element: {last_element}')
	
print('All Elements have been popped from the List')	