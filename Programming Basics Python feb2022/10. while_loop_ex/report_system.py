required_money = int(input())
paying_counter = 0
card_payment = 0
card_counter = 0
cash_payment = 0
cash_counter = 0
total_saved = 0
while True:
    price = input()
    paying_counter += 1
    if price == 'End':
        if total_saved >= required_money:
            avr_card = card_payment / card_counter
            avr_cash = cash_payment / cash_counter
            print(f'Average CS: {avr_cash:.2f}')
            print(f'Average CC: {avr_card:.2f}')
        else:
            print('Failed to collect required money for charity.')
        break
    if paying_counter % 2 == 0:
        if int(price) >= 10:
            card_payment += int(price)
            card_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    else:
        if int(price) <= 100:
            cash_payment += int(price)
            cash_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    total_saved = card_payment + cash_payment
    if total_saved >= required_money:
        avr_card = card_payment / card_counter
        avr_cash = cash_payment / cash_counter
        print(f'Average CS: {avr_cash:.2f}')
        print(f'Average CC: {avr_card:.2f}')
        break