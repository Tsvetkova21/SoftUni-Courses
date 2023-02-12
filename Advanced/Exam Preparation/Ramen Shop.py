from collections import deque

bowls_ramen = deque([int(x) for x in input().split(", ")])
customers= deque([int(x) for x in input().split(", ")])

while customers and bowls_ramen:
    bows = bowls_ramen.pop()
    customer = customers.popleft()
    if bows > customer:
        bows-=customer
        bowls_ramen.append(bows)
    elif bows < customer:
        customer-=bows
        customers.appendleft(customer)
    elif bows==customer:
        continue

if not customers and not bowls_ramen:
    print("Great job! You served all the customers.")
elif not customers and bowls_ramen:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
if not bowls_ramen and customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
