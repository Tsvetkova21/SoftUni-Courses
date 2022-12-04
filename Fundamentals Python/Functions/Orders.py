product = input()
quantity = int(input())
def calculation(product, quantity):
    if product == "coffee":
        return 1.5*quantity
    elif product == "water":
        return 1*quantity
    elif product == "coke":
        return 1.4*quantity
    elif product == "snacks":
        return 2*quantity
print(f"{calculation(product,quantity):.2f}")
