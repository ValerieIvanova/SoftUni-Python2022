people_waiting = int(input())
lift_state = list(map(int, input().split()))
total_free_spots = 4 * len(lift_state) - sum(lift_state)

for place in range(len(lift_state)):
    if people_waiting > 0 and total_free_spots > 0:
        if lift_state[place] < 4:
            diff = 4 - lift_state[place]
            people_going = diff if diff <= people_waiting else people_waiting
            lift_state[place] += people_going
            total_free_spots -= people_going
            people_waiting -= people_going
if people_waiting <= 0 and total_free_spots > 0:
    print(f"The lift has empty spots!\n"
          f"{' '.join([str(state) for state in lift_state])}")
elif people_waiting > 0 and total_free_spots <= 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n"
          f"{' '.join([str(state) for state in lift_state])}")
else:
    print(*lift_state, sep=' ')