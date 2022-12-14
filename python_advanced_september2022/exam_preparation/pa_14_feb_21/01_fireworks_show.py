from collections import deque

fireworks_effects = deque(int(x) for x in input().split(', '))
explosive_power = deque(int(x) for x in input().split(', '))

fireworks_count = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

perfect_show = False

while fireworks_effects and explosive_power:
    if fireworks_effects[0] <= 0:
        fireworks_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    effect = fireworks_effects.popleft()
    power = explosive_power.pop()
    current_sum = effect + power

    if current_sum % 15 == 0:
        fireworks_count["Crossette Fireworks"] += 1
    elif current_sum % 3 == 0:
        fireworks_count["Palm Fireworks"] += 1
    elif current_sum % 5 == 0:
        fireworks_count["Willow Fireworks"] += 1
    else:
        effect -= 1
        fireworks_effects.append(effect)
        explosive_power.append(power)

    if all([fireworks_count["Palm Fireworks"] >= 3,
            fireworks_count["Willow Fireworks"] >= 3,
            fireworks_count["Crossette Fireworks"] >= 3]):
        perfect_show = True
        break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for type, value in fireworks_count.items():
    print(f"{type}: {value}")
