list = []
head = input()
body = input()
tail = input()

list = [head, body, tail]
list[0], list[2] = list[2], list[0]
print(list)