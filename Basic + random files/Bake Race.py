count_juniors_bakers = int(input())
count_seniors_bakers = int(input())
trace = input()

if trace == 'trail':
    price_juniors = 5.50
    price_seniors = 7
elif trace == 'cross-country':
    price_juniors = 8
    price_seniors = 9.5
elif trace == 'downhill':
    price_juniors = 12.25
    price_seniors = 13.75
elif trace == 'road':
    price_juniors = 20
    price_seniors = 21.5

if trace == 'cross-country' and \
        (count_seniors_bakers+count_juniors_bakers)>=50:
    price_juniors=price_juniors*0.75
    price_seniors=price_seniors*0.75

all_price = (price_juniors*count_juniors_bakers \
            + price_seniors*count_seniors_bakers)*0.95
print(f'{all_price:.2f}')