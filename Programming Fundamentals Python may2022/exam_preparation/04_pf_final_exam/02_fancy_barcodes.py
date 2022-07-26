import re
lines = int(input())
valid_barcode_pattern = r'@#+[A-Z][A-Za-z\d]{4,}[A-Z]@#+'
product_group_pattern = r'\d+'
for line in range(lines):
    barcode = input()
    valid_barcode = re.search(valid_barcode_pattern, barcode)
    if valid_barcode:
        product_group = re.findall(product_group_pattern, valid_barcode.group())
        if product_group:
            group = ''.join(product_group)
            print(f'Product group: {group}')
        else:
            print("Product group: 00")
    else:
        print('Invalid barcode')