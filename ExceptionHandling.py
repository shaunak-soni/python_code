#Capture and handle exceptions


name = input('Enter name (5 chars min): ')

if len(name) < 5:
    raise ValueError(f'{name} is not 5 characters or more...')
    
print(f'Hello {name}!')	
	
try:
	num1 = int(input('Enter divident: '))
	num2 = int(input('Enter divisor (not-zero): '))
    c= num1 / num2
except ZeroDivisionError as ex:
    print(f'Exception occured: {type(ex)}, {ex}')
print(f'\nDivident is: {num1}')	
print(f'\nDivisor is: {num2}')
print(f'\nnDivident/nDivisor = is: {c}')

l = [1, 2, 3, 4, 5]	
	
try:
    while True:
        print(l.pop())
except IndexError:
    # index error means our list is empty - that was expected to happen
    print('all done')	
	
