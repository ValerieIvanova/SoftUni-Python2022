def shopping_cart(*args):
    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for info in args:
        if info == 'Stop':
            break
        meal = info[0]
        product = info[1]
        if meal == 'Soup' and len(cart['Soup']) == 3:
            continue
        elif meal == 'Pizza' and len(cart['Pizza']) == 4:
            continue
        elif meal == 'Dessert' and len(cart['Dessert']) == 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)

    output = ''
    empty = 0
    for m, p in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
        p = sorted(p)
        output += f"{m}:" + '\n'
        if p:
            output += ' - ' + '\n - '.join(p) + '\n'
        else:
            empty += 1
    if empty < 3:
        return output
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
