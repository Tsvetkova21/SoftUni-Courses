Peter_budget=float(input())
video_cards=int(input())
processors=int(input())
ram_memory=int(input())
if video_cards>processors:
    price=(video_cards*250+processors*250*0.35*video_cards
           +ram_memory*250*0.1*video_cards)*0.85
else:
    price = video_cards * 250 + processors * 250*video_cards * 0.35\
            + ram_memory *video_cards* 250 * 0.1
if Peter_budget>=price:
    left_price=Peter_budget-price
    print(f"You have {left_price:.2f} leva left!")
else:
    need_price= price - Peter_budget
    print(f"Not enough money! You need {need_price:.2f} leva more!")


