#Create Identity Matrix of a given size. 

n = in(input('Please enter the Size of the Indentity Matrix that we should generate: ') 

matrix = []  # start with just an empty list

for row_idx in range(n):
    row = []  # create an empty row
    for col_idx in range(n):
        # build up each item
        # diagonal elements are 1, otherwise 0
        # on the diagonal if row_index = col_index
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    # done buiding row, so append it to the matrix
    matrix.append(row)
	
print(f'The Identity Matrix is : {matrix}')	