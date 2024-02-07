#Reverse a string input by the user and find out if it is a Palindrome

s =input('Please enter the string you wish to reverse: ')

rev_string = s[::-1]

print(f'The reversed string is {rev_string}')

if s==rev_string:
	print(f'The string {s} is a Palindrome')
else
	print(f'The string {s} is Not a Palindrome')