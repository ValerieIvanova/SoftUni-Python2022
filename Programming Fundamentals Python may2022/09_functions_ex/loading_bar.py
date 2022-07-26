def loading(num):
    if num < 100:
        loading_bar_first_symbol = int(num / 10) * '%'
        loading_bar_second_symbol = int(10 - num / 10) * '.'
        return f"{num}% [{loading_bar_first_symbol}{loading_bar_second_symbol}]\nStill loading..."
    return '100% Complete!\n[%%%%%%%%%%]'


number = int(input())
print(loading(number))