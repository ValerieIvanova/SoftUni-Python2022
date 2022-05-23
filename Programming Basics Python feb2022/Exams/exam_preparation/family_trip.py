budget = float(input())
days = int(input())
price_per_day = float(input())
percent_other_costs = int(input())

if days > 7:
    price_per_day -= price_per_day * 0.05

costs = days * price_per_day
other_costs = (budget * percent_other_costs / 100)
total_costs = costs + other_costs
diff = abs(budget - total_costs)
if total_costs <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
elif total_costs > budget:
    print(f"{diff:.2f} leva needed.")