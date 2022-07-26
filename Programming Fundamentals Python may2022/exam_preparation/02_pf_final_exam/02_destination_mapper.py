import re

map_places = input()
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
valid_places = re.findall(pattern, map_places)

travel_points = 0
places = []
for place in valid_places:
    travel_points += int(len(place[1]))
    places.append(place[1])
print('Destinations: ', end='')
print(*places, sep=', ')
print(f'Travel Points: {travel_points}')