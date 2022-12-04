price_maiden_party = float(input())
count_love_letters = int(input())
count_roses = int(input())
count_keychain = int(input())
count_cartoons = int(input())
count_surprices = int(input())
all_price = 0
diff = 0

all_count = count_love_letters +count_roses + count_keychain\
            + count_cartoons +count_surprices

if all_count >= 25:
    all_price = count_love_letters*0.6 + count_roses*7.2+\
                count_keychain*3.6 + count_cartoons*18.2 + count_surprices*22
    all_price = all_price*(1-0.35)

else:
    all_price = count_love_letters * 0.6 + count_roses * 7.2 + \
                count_keychain * 3.6 + count_cartoons * 18.2 + count_surprices * 22

if all_price*0.9>=price_maiden_party:
    diff = all_price*0.9 - price_maiden_party
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = price_maiden_party - all_price*0.9
    print(f"Not enough money! {diff:.2f} lv needed.")
