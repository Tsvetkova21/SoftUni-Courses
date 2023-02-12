def shopping_cart(*products):
    shopping_products = {}
    is_empty = True
    allowed_products={
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }
    for el in products:
        if el=="Stop":
            break
        if el[0] not in shopping_products:
            shopping_products[el[0]]=[]
        if len(shopping_products[el[0]])<allowed_products[el[0]]:
            if el[1] not in shopping_products[el[0]]:
                shopping_products[el[0]].append(el[1])
                is_empty=False
        else:
            continue
    for key in allowed_products:
        if key not in shopping_products:
            shopping_products[key]=[]
    output = ''
    for key, value in sorted(shopping_products.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{key}:\n"
        for item in sorted(value):
            output += f" - {item}\n"
    if is_empty:
        return "No products in the cart!"
    return output

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))






