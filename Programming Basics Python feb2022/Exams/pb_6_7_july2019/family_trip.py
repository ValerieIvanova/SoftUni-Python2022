budget = float(input())
days = int(input())
price_per_day = float(input())
percent_other_expenses = int(input())
if days > 7:
    price_per_day -= price_per_day * 0.05
total_days_price = days * price_per_day
other_expenses = (percent_other_expenses / 100) * budget
total_costs = total_days_price + other_expenses
diff = abs(total_costs - budget)
if total_costs <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')