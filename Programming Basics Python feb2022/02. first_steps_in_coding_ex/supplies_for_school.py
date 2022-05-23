count_of_pens = int(input())
markers_count = int(input())
detergent_lt = int(input())
discount_percent = int(input())

price_of_pens = count_of_pens * 5.80
price_of_markers = markers_count * 7.20
price_detergent = detergent_lt * 1.20

total_price = price_of_pens + price_of_markers + price_detergent

final_price = total_price - (total_price * (discount_percent / 100))

print(final_price)
