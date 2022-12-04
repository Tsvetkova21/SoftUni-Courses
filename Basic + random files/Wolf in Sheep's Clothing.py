list_sheeps=list((input().split(", ")))
list_sheeps.reverse()
n=0
if list_sheeps.index("wolf")==0:
    print('Please go away and stop eating my sheep')
else:
    n=list_sheeps.index("wolf")
    print(f'Oi! Sheep number {n}! You are about to be eaten by a wolf!')