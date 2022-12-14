from collections import deque

seats = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])
taken_seats = []
rotations = 0
while True:
    if len(taken_seats) == 3 or rotations == 10:
        break
    num1 = first_sequence.popleft()
    num2 = second_sequence.pop()
    letter = chr(num1 + num2)
    seat = str(num1)+letter
    seat2 = str(num2)+letter
    rotations += 1
    if seat in seats:
        if seat not in taken_seats:
            taken_seats.append(seat)
    elif seat2 in seats:
        if seat2 not in taken_seats:
            taken_seats.append(seat2)
    else:
        first_sequence.append(num1)
        second_sequence.appendleft(num2)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")