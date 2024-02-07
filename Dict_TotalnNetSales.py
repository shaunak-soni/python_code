#In the given list find total sold quantity per item and net sold quantity per item

transactions = [
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
    {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'refund', 'quantity': 1},
]

print(f'The List of Item Sale/Refund Qunatity is :\n {transactions}')

total_sold = {}  # empty dictionary

for transaction in transactions:
    item = transaction['item']
    is_sale = transaction['trans_type'] == 'sale'

    quantity = transaction['quantity']
    
    if is_sale:
        if item in total_sold:
            # item already present, update sold count by quantity
            total_sold[item] = total_sold[item] + quantity
        else:
            # item not present - create it and set sold count to quantity
            total_sold[item] = quantity
            
print(f'The total sold is: {total_sold}')

net_sales = {}

for transaction in transactions:
    item = transaction['item']
    is_sale = transaction['trans_type'] == 'sale'
    quantity = transaction['quantity']
    
    if not is_sale:
        # this was a refund - make quantity negative
        quantity = -quantity
        
    if item in net_sales:
            # item already present, update cnet_sales value by quantity
            net_sales[item] = net_sales[item] + quantity
    else:
        # item not present - create it and set sold count to quantity
        net_sales[item] = quantity

print(f'The net sales is: {net_sales}')		
print(net_sales)