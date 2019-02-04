### dictionary2.py
### a dictionary is a collection of key = value pairs
### the value for a key can be list
### remember, elements of a list are indexed from zero

def main():

    inventory = {'B1234':['PNY','16GB Flash Drive',6.99,12],
                 'F0007':['Epson','Printer',49.99,8],
                 'C9876':['Asus','Ethernet Adapter',29.99,16],
                 'K2468':['Amazon','Kindle Fire',59.99,10],
                 'G1357':['Belkin','Ethernet Hub',24.99,20],
                 'A4567':['Acer','Gaming Monitor',599.99,6]
                }

    print('\nHere are the items in stock (crudely)')
    for item in inventory:
        print('SKU',item,':',inventory[item])
   
    hi_price = 0            ### to find the most pricey item 
    stock_value = 0         ### accumulator

    print('\nHere are the items in stock (elegantly)')
    for item,desc in inventory.items():
        print('SKU',item,':',desc[0],desc[1],end='')
        print(', $',desc[2],', ',desc[3],' in stock',sep='')
        ### accumulate the inventory value
        stock_value += desc[2] * desc[3]
        if desc[2] > hi_price:
            ### set new high price
            hi_price = desc[2]
            ### and store description of item
            hi_item = inventory[item][0] + ' ' + inventory[item][1]
    
    ### report highest priced item in stock
    print('Most expensive item: ',hi_item,', $',hi_price,sep='')
    print('Current inventory value $',format(stock_value,',.2f'),sep='')

main()



    
