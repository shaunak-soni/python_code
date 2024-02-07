#Print all Even numbes in a given Range if range more than 100 then stop processing. 

range_start = int(input('Please enter the start of the Range to Print Even Numbers only: '))
range_end = int(input('Please enter a number less than 100 as the end of the Range: '))

for i in range(range_start, range_end+1):
	if i > 100:
        print('breaking out of loop after 100')
        break
    if i % 2 == 1:
        # odd number - skip this
        continue
    print(i)
print('done')	
	
	