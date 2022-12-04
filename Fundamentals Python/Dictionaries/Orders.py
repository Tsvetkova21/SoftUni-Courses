products={}
command = input()
final_value = 1
while command != "buy":
    input_product = command.split(" ")
    name, price, quantity = input_product[0],input_product[1],input_product[2]
    if name not in products:
        products[name]={}
        products[name]['price']=float(price)
        products[name]['quantity'] = int(quantity)
    else:
        products[name]['price']=float(price)
        products[name]['quantity']+=int(quantity)
    command = input()
for (key,value) in products.items():
    for nested_key in value:
        print(f"{key} -> {(value['price']*value['quantity']):.2f}")
        break

