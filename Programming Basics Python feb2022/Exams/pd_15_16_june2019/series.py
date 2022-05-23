budget = float(input())
number_of_series = int(input())
enough_budget = True
for i in range(1, number_of_series + 1):
    series_name = input()
    price = float(input())
    if series_name == 'Thrones':
        price -= price * 0.5
    elif series_name == 'Lucifer':
        price -= price * 0.4
    elif series_name == 'Protector':
        price -= price * 0.3
    elif series_name == 'TotalDrama':
        price -= price * 0.2
    elif series_name == 'Area':
        price -= price * 0.1
    budget -= price
    if budget < 0:
        enough_budget = False
if enough_budget:
    print(f'You bought all the series and left with {budget:.2f} lv.')
else:
    print(f'You need {abs(budget):.2f} lv. more to buy the series!')