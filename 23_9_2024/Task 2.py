inv = { }


def add_inv(item , price , quant):
    inv[item] = ( "₹" + str(price), quant )

def update(item_update , sale_quant, quant):
    inv[item_update] = ( "₹" + str(price), quant - sale_quant )
    
    

n = int(input("Enter no. of items : "))

for i in range(n):
    item = input(" Enter item : ")
    price = int(input(" Enter price : "))
    quant = int(input(" Enter quantity : "))
    print()
    add_inv(item, price, quant)
    print(f"Inventory : {inv}")
    print()
    
item_update = input("Enter item to update quantity : ")
sale_quant = int(input(" Enter sale quantity : "))
update(item_update, sale_quant, quant)
print(inv)


    
