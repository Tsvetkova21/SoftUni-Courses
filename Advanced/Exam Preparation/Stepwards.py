from collections import deque

letter = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
rotations = 0
seat_maches = []
while True:
    if rotations==10:
        break
    if len(seat_maches)==3:
        break
    first = first_sequence.popleft()
    second = second_sequence.pop()
    sum = first+second
    letter_match_first = f'{first}'+chr(sum)
    letter_match_second =f'{second}'+chr(sum)
    for seat in [letter_match_first,letter_match_second]:
        if seat in seat_maches:
            break
        if seat in letter:
            letter.remove(seat)
            seat_maches.append(seat)
            break
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)
    rotations+=1

print(f"Seat matches: {', '.join(str(x) for x in seat_maches)}")
print(f"Rotations count: {rotations}")