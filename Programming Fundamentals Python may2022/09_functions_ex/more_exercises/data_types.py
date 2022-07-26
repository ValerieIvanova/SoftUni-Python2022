def data_type(type, data):
    result = None
    if type == 'int':
        result = int(data) * 2
    elif type == 'real':
        result = f'{float(data) * 1.5:.2f}'
    elif type == 'string':
        result = f'${data}$'
    return result


current_type = input()
current_data = input()
print(data_type(current_type, current_data))