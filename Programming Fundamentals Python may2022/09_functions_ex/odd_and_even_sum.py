def sum_of_all_numbers(a):
    sum_of_evens = 0
    sum_of_odds = 0
    for digit in a:
        if int(digit) % 2 == 0:
            sum_of_evens += int(digit)
        else:
            sum_of_odds += int(digit)
    return sum_of_odds, sum_of_evens


number = input()
odds, evens = sum_of_all_numbers(number)
print(f'Odd sum = {odds}, Even sum = {evens}')