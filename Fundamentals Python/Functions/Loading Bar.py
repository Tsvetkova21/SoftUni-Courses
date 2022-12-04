percentage = int(input())
loading =''
number=int(percentage/10)
if number<10:
    for i in range(number):
        loading+='%'

    for i in range(10-number):
        loading+='.'
    print(f'{percentage}% [{loading}]')
    print('Still loading...')
else:
    for i in range(number):
        loading+='%'
    print(f'{percentage}% Complete!')
    print(f'[{loading}]')