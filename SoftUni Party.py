def collect_data_for_arrived_guests():
    arrived_guest_list = []
    while True:
        data = input()
        if data == 'END':
            break
        else:
            arrived_guest_list.append(data)
    return arrived_guest_list
def print_func(not_arrived_guests_data):
    print(len(not_arrived_guests_data))
    for guest_number in sorted(not_arrived_guests_data):
        print(guest_number)

n = int(input())
guest_reservation_list = [input() for _ in range(n)]
arrived_guest = collect_data_for_arrived_guests()

not_arrived_guests = set(guest_reservation_list).difference(arrived_guest)
print_func(not_arrived_guests)