from collections import deque
number_petrol_stations = int(input())
stations = deque()
left_petrol = 0
for n in range(number_petrol_stations):
    information_petrol_stations = input().split(" ")
    amount_petrol=int(information_petrol_stations[0])+left_petrol
    kilometers_next_station = int(information_petrol_stations[1])
    if amount_petrol>=kilometers_next_station:
        stations.append(n)
        left_petrol = amount_petrol -kilometers_next_station
print(stations.popleft())
