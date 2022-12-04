name = input()
password = input()
data = input()

while data!=password:
    data = input()

    if data==password:
        break
print(f"Welcome {name}!")
