inpt = input()
numbers_str = inpt.split(' ')
numbers =[]
numbers_exch=[]
exch = 0
max = 0
max_even =0
min = 0
min_even=0
max_index=0
max_index_even=0
min_index=0
min_index_even=0

for elements in  numbers_str:
   numbers.append(int(elements))
while inpt!='End':
  inpt = input()
  if "exchange" in inpt:
      exch=int(inpt.replace("exchange",""))
      for i in range(len(numbers)):
          if  exch<0 or exch >= len(numbers):
              print("Invalid index")
              break
          if i==exch:
              for x in range(i+1, len(numbers)):
                  numbers_exch.append(numbers[x])
              for y in range(i+1):
                  numbers_exch.append(numbers[y])
  if "max" in inpt:
      if "odd" in inpt:
          for i in range (len(numbers_exch)):
              print(i)
              if numbers_exch[i]%2!=0:
                  if numbers_exch[i]>=max:
                      max=numbers_exch[i]
                      max_index=i
          print(max_index)
      if "even" in inpt:
          for i in range(len(numbers_exch)):
              if numbers_exch[i]%2==0:
                  if numbers_exch[i]>=max_even:
                      max_even=numbers_exch[i]
                      max_index_even=i
          print(max_index_even)
print(numbers_exch)