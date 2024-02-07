#Find the mimimum of the 2 entered numbers

a=int(input('Please enter first number: '))
b=int(input('Please enter second number: '))

minimum = a if a < b else b

print(f'Mimimum Number is: {minimum}')