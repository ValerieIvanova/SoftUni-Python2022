text = input()
[print(f"{symbol}: {text.count(symbol)} time/s") for symbol in sorted(set(text))]