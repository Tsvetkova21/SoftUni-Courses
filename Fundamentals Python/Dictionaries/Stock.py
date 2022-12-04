elements = input().split(" ")
bakery = { } #bakery = dict ()
products = input().split(" ")
for i in range(0, len(elements),2):
    key = elements[i]
    value = elements[i+1]
    bakery[key]=int(value)

for product in products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")