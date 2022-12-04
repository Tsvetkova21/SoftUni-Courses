n = int(input())
count_p1=0
count_p2=0
count_p3=0
count_p4=0
count_p5=0

for i in range(0,n):
    num = int(input())
    if num<200:
        count_p1+=1
    if 200<=num<=399:
        count_p2+=1
    if 400<=num<=599:
        count_p3+=1
    if 600<=num<=799:
        count_p4+=1
    if num>=800:
        count_p5+=1
print (f'{((count_p1/n)*100):.2f}%')
print (f'{((count_p2/n)*100):.2f}%')
print (f'{((count_p3/n)*100):.2f}%')
print (f'{((count_p4/n)*100):.2f}%')
print (f'{((count_p5/n)*100):.2f}%')