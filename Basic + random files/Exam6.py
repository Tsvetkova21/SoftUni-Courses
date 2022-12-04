K = int(input())
L = int(input())
M = int(input())
N = int(input())
first_number = ' '
second_number = ' '
counter = 0

for i in range (K,8+1):
        if i%2==0:
            for j in range (9, L-1, -1):
                if j%2 !=0:
                    first_number=str(i)+str(j)
                    for k in range (M,8+1):
                        if k%2 == 0:
                            for l in range (9,N-1,-1):
                                if l%2 != 0:
                                    second_number = str(k) + str(l)
                                    if first_number == second_number:
                                        print("Cannot change the same player.")
                                    else:
                                        counter += 1
                                        print(f'{first_number} - {second_number}')
                                        if counter==6:
                                            quit()





