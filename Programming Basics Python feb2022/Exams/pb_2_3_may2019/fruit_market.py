strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
berries_kg = float(input())
strawberries_kg = float(input())

berries_price = strawberries_price / 2
oranges_price = berries_price - (berries_price * 0.40)
bananas_price = berries_price - (berries_price * 0.80)
total_price = (strawberries_kg * strawberries_price) + (bananas_kg * bananas_price) + (oranges_price * oranges_kg) \
              + (berries_price * berries_kg)
print(f'{total_price:.2f}')