def grocery_store(**kwargs):
    sorted_receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ''
    for name, quantity in sorted_receipt:
        result += f"{name}: {quantity}" + '\n'
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
