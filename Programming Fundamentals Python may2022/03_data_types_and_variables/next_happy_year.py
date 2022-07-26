year = int(input())
is_happy_year = False

while not is_happy_year:
    year += 1
    # set adds unique elements
    set_year = set(str(year))
    is_happy_year = len(str(year)) == len(set_year)

print(year)