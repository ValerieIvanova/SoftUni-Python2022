shirt_price = float(input())
goal_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2
total_sum = shirt_price + shorts_price + socks_price + shoes_price
sum_with_discount = total_sum - (total_sum * 0.15)
if sum_with_discount >= goal_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f'His sum is {sum_with_discount:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    diff = abs(goal_sum - sum_with_discount)
    print(f'He needs {diff:.2f} lv. more.')