number_chicken_menu = int(input())
number_fish_menu = int(input())
number_veggie_menu = int(input())

chicken_menu_price = number_chicken_menu * 10.35
fish_menu_price = number_fish_menu * 12.40
veggie_menu_price = number_veggie_menu * 8.15
total_menu_price = chicken_menu_price + fish_menu_price + veggie_menu_price

desert_price = total_menu_price * 0.2

order_price = total_menu_price +desert_price + 2.50

print(order_price)