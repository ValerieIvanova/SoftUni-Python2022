budget = float(input())
payment = 0
enough_budget = True
while True:
    actor_name = input()
    if actor_name == 'ACTION':
        break
    if len(actor_name) <= 15:
        payment = float(input())
        budget -= payment
    elif len(actor_name) > 15:
        payment = budget * 0.20
        budget -= payment
    if budget < 0:
        enough_budget = False
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break
if enough_budget:
    print(f'We are left with {abs(budget):.2f} leva.')