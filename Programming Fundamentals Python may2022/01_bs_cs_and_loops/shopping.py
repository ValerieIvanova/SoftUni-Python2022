budget = int(input())

while True:
    price = input()
    if price == 'End':
        print("You bought everything needed.")
        break
    if int(price) > budget:
        print("You went in overdraft!")
        break
    budget -= int(price)