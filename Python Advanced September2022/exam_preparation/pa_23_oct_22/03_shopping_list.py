def shopping_list(budget: int, **kwargs):
    if not budget >= 100:
        return "You do not have enough budget."
    basket = 0
    output = ''

    for item, info in kwargs.items():
        if basket + 1 > 5:
            break
        elif basket == len(kwargs):
            break
        price = float(info[0])
        quantity = int(info[1])
        total = quantity * price
        if total <= budget:
            basket += 1
            budget -= total
            output += f"You bought {item} for {total:.2f} leva.\n"

    return output


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
