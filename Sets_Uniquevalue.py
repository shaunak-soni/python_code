#Genearte unique values from a list of characters or string

l=input('Please enter the string for which you wish to find unique list of characters: ')
ci=int(input('Please enter 1 for Case Insensitive and 2 for Case Sensitive (1/2): '))

print(f'\nThe original string or list is: \n {l}')

if ci==1:
        l2 = []
        for symbol in l:
                l2.append(symbol.casefold())
        unique_values = set(l2)
elif ci==2:
        unique_values = set(l)
else:
        print('Invalid Option Selected')

print(f'\nThe list with only unique elements is: \n {unique_values}')		