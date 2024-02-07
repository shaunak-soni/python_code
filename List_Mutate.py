#Mutate the lists in data to add one more element indicating the distance between the two integer numbers (i.e. the absolute value fo the difference)
#Determine on which date this newly calculate value was the largest.

data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)

for row in data:
    row.append(abs(row[1] - row[2]))
data

max_spread = data[0][-1]
max_date = data[0][0]

for dt, num_1, num_2, spread in data[1:]:
    if spread > max_spread:
        # found a new high
        max_spread = spread
        max_date = dt
		
print(f'The Data is : {data}')
print(f'Max spread in the List is {max_spread} and the corresponding date is {max_date}')
        
