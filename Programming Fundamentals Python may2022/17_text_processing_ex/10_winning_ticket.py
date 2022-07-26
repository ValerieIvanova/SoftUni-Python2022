def winning(t):
    if len(t) != 20:
        return "invalid ticket"
    left = t[:10]
    right = t[10:]
    special_symbols = ['@', '#', '$', '^']
    for s in special_symbols:
        for repeats in range(10, 5, -1):
            winning_symbol_repeats = s * repeats
            if winning_symbol_repeats in left and winning_symbol_repeats in right:
                if repeats == 10:
                    return f'ticket "{t}" - {repeats}{s} Jackpot!'
                return f'ticket "{t}" - {repeats}{s}'
    return f'ticket "{t}" - no match'


tickets = [t.strip() for t in input().split(', ')]
for ticket in tickets:
    print(winning(ticket))