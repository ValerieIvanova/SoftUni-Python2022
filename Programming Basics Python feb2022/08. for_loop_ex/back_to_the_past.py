heritage = float(input())
final_year = int((input()))
starting_year = 1800
money_spent = 0
age = 18

for i in range(starting_year, final_year + 1):
    if i % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * age
    age += 1

diff = abs(heritage - money_spent)

if money_spent <= heritage:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")