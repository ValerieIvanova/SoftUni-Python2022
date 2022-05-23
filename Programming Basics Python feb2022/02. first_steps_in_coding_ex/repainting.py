nylon = int(input())
paint = int(input())
razr = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint * 0.1)) * 14.50
razr_price = razr * 5
materials_sum = nylon_price + paint_price + razr_price + 0.40
workers_sum = (materials_sum * 0.3) * hours
final_sum = materials_sum + workers_sum

print(final_sum)
