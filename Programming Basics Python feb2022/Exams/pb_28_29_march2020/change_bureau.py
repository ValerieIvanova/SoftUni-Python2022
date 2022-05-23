bitcoin = int(input())
chinese_y = float(input())
commission = float(input())

bitcoin_price = bitcoin * 1168
chinese_y_price = chinese_y * 0.15
chinese_y_price_bgn = chinese_y_price * 1.76
total_bgn = bitcoin_price + chinese_y_price_bgn
total_eur = total_bgn / 1.95
commission_price = total_eur * (commission / 100)
end_price = total_eur - commission_price

print(f"{end_price:.2f}")
