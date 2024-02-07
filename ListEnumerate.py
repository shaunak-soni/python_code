#in the given list 
#If the first number of a row is higher than the second number of the previous row, append the string up to the row
#If the first number of a row is lower than the second number of the previous row, append the string down to the row
#Otherwise, append same to the row.

data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]

for idx, (op, cl) in enumerate(data):
    if idx == 0:
        print(f'{idx}: no previous row')
    else:
        print('-----')
        prev_op, prev_cl = data[idx-1]
        print(f'{idx}: open={op}, close={cl}')
        print(f'{idx-1}: open={prev_op}, close={prev_cl}')


for idx, (op, cl) in enumerate(data):
    if idx == 0:
        data[idx].append('')
    else:
        # we have to watch out here, since we appended an extra element to the previous
        # row in the previous iteration, we now actually have 3 values to unpack!
        prev_op, prev_cl, trend = data[idx-1]
        if op > prev_cl:
            data[idx].append('up')
        elif op < prev_cl:
            data[idx].append('down')
        else:
            data[idx].append('same')

print(f'(The modified list is:  {data}')