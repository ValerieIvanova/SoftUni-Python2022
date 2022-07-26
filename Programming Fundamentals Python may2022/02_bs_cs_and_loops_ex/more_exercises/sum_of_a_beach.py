string = input().lower()
sum_of_sand = string.count('sand')
sum_of_water = string.count('water')
sum_of_fish = string.count('fish')
sum_of_sun = string.count('sun')
sum_of_a_beach = sum_of_sun + sum_of_sand + sum_of_fish + sum_of_water
print(sum_of_a_beach)