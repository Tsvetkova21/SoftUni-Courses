x=float(input())
y=float(input())
h=float(input())
green_paint=(x*x*2+y*x*2-1.5*1.5*2-1.2*2)/3.4
red_paint=(x*h/2*2+y*x*2)/4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')