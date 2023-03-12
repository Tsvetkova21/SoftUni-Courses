def operate (operator, *args):
    if args:
        if operator == "+":
            result = 0
            for num in args:
                result +=num
        if operator == "-":
            result,*others_res = args
            for num in others_res:
                result-=num
        if operator == "*":
            result = 1
            for num in args:
                result*=num
        if operator == "/":
            result,*others_res = args
            if result!=0:
                for num in others_res:
                    if num!=0:
                        result/=num
                    else:
                        quit()
        return result

print(operate("/", 3, 4))
print(operate("/"))
print(operate("/", 2, 3))