price_for_trip = float(input())
number_of_puzzles = int(input())
number_of_talking_doll = int(input())
number_of_teddy_bear = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

order_sum = (number_of_puzzles * 2.60) + (number_of_talking_doll * 3) \
            + (number_of_teddy_bear * 4.10) + (number_of_minions * 8.20) \
                                      + (number_of_trucks * 2)
toys_count = number_of_puzzles + number_of_talking_doll + number_of_teddy_bear + number_of_minions + number_of_trucks

if toys_count >= 50:
    order_sum -= order_sum * 0.25

rent = order_sum * 0.10
profit = order_sum - rent
money_left = abs(profit - price_for_trip)

if profit >= price_for_trip:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print (f'Not enough money! {money_left:.2f} lv needed.')