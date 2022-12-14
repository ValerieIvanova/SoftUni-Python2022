number_of_guests = int(input())
guest_list = set()
arrived_guests = set()

for i in range(number_of_guests):
    guest_list.add(input())

while True:
    command = input()
    if command == 'END':
        break
    arrived_guests.add(command)

missing_guests = guest_list.difference(arrived_guests)
print(len(missing_guests))

[print(guest) for guest in sorted(missing_guests)]