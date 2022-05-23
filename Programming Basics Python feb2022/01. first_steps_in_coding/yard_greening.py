meters_that_will_be_landscaped = float(input())

the_price_for_landscaping_the_whole_yard = meters_that_will_be_landscaped * 7.61
discount = the_price_for_landscaping_the_whole_yard * 0.18

total_price = the_price_for_landscaping_the_whole_yard - discount

print(f"The final price is: {total_price} lv.")
print(f'The discount is: {discount} lv.')