# Use a dictionary to count the frequency of the characters a-z A-Z in a given string.

s=input('Please enter the string for which you wish to check the frequency of characters: ')
ci=int(input('Please enter 1 if you wish the counts to be Case Insensitive and 2 if you wish to have the counts to be Case Sensitive (1/2): '))

counts = {}

if ci==1:
    for c in s.lower():
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            counts[c] = counts.get(c, 0) + 1
elif ci==2:
    for c in s:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            counts[c] = counts.get(c, 0) + 1

print(f'The charater counts for string {s} are : {counts}')
