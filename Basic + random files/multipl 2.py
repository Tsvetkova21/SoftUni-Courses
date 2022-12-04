num = 0
while num>=0:
    num = float(input())
    if num < 0:
        print('Negative number!')
        break
    print(f'Result: {(num*2):.2f}')


