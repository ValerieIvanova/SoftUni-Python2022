import re
pattern = r'^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$'
furniture_list = []
total_sum = 0
while True:
    command = input()
    if command == 'Purchase':
        break
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        furniture_list.append(furniture)
        total_sum += float(price) * int(quantity)

print('Bought furniture:')
[print(item) for item in furniture_list]
print(f"Total money spend: {total_sum:.2f}")