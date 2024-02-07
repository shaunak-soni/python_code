#Create Multiplication Table till the Range of number entered by the user.

m=int(input('Please enter the number till which you wish to generate Multiplication Table: '))

for row in range(1, m + 1):
    for col in range(1, 11):
        print(f'{row} x {col} = {row * col}')
    print('-' * 15)