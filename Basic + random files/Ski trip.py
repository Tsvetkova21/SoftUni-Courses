days=int(input())
room=input()
report=input()
discount=0
if room=='room for one person':
    tax=18
elif room=='apartment':
    tax=25
    if days<10:
        discount=0.3
    if 10<=days<=15:
        discount=0.35
    if days>15:
        discount = 0.5
elif room=='president apartment':
    tax=35
    if days<10:
        discount=0.1
    if 10<=days<=15:
        discount=0.15
    if days>15:
        discount =0.2
price=(days-1)*(1-discount)*tax

if report=='positive':
    price=price+price*(0.25)
elif report=='negative':
    price=price-price*(0.1)
print(f'{price:.2f}')