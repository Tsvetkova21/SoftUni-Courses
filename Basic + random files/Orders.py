n = int(input())
all_price = 0

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsule_per_day <= 2000:
        continue
    price = days * capsule_per_day * price_per_capsule
    all_price += price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${all_price:.2f}')