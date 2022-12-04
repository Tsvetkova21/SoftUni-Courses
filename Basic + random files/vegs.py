price_kg_veg=float(input())
price_kg_fruits=float(input())
kg_vegs=int(input())
kg_fruits=int(input())
profit=(kg_vegs*price_kg_veg+kg_fruits*price_kg_fruits)/1.94
print(f'{profit:.2f}')
