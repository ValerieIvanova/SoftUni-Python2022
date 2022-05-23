from math import ceil

number_of_people = int(input())
tax = float(input())
price_for_a_sunbed = float(input())
price_for_an_umbrella = float(input())

total_tax = number_of_people * tax
total_sunbeds = ceil(number_of_people * 0.75) * price_for_a_sunbed
total_umbrellas = ceil(number_of_people / 2) * price_for_an_umbrella
total_price = total_tax + total_sunbeds + total_umbrellas
print(f'{total_price:.2f} lv.')