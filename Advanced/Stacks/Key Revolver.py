from collections import deque

price_of_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(b) for b in input().split(" ")]
locks = deque([int(l) for l in input().split(" ")])
value_intelligence = int(input())
current_barrel = size_gun_barrel
while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        quit()
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet>current_lock:
        print("Ping!")
        locks.insert(0, current_lock)
    else:
        print("Bang!")
    value_intelligence -= price_of_bullet
    current_barrel -=1
    if current_barrel<=0 and bullets:
        print("Reloading!")
        current_barrel = size_gun_barrel

print(f"{len(bullets)} bullets left. Earned ${value_intelligence}")
