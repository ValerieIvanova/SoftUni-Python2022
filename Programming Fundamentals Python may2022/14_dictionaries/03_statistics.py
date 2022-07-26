from collections import defaultdict

products_dict = defaultdict(int)

while True:
    product = input()
    if product == 'statistics':
        print(f"Products in stock:")
        for key, value in products_dict.items():
            print(f"- {key}: {value}")
        print(f"Total Products: {len(products_dict)}")
        print(f"Total Quantity: {sum(products_dict.values())}")
        break
    key, value = product.split(': ')
    products_dict[key] += int(value)