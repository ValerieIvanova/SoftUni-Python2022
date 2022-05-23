last_sector = input()
rows_in_sector_a = int(input())
odd_seats_count = int(input())
even_seats_count = odd_seats_count + 2
next_sector_rows = 0
seats = 0

for s in range(ord('A'), ord(last_sector) + 1):
    sector = chr(s)
    for r in range(1, rows_in_sector_a + 1):
        row = r
        if r % 2 == 0:
            for even_s in range(ord('a'), ord('a') + even_seats_count):
                seat = chr(even_s)
                seats += 1
                print(f'{sector}{row}{seat}')
        else:
            for odd_s in range(ord('a'), ord('a') + odd_seats_count):
                seat = chr(odd_s)
                seats += 1
                print(f'{sector}{row}{seat}')
    rows_in_sector_a += 1
print(seats)
