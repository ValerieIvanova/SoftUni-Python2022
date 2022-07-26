materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
while True:
    data = input().lower().split()
    for i in range(0, len(data), 2):
        if data[i+1] == 'shards' or data[i+1] == 'fragments' or data[i+1] == 'motes':
            materials_dict[data[i + 1]] += int(data[i])
            if data[i+1] == 'shards':
                if materials_dict['shards'] >= 250:
                    materials_dict['shards'] -= 250
                    print('Shadowmourne obtained!')
                    obtained = True
                    break
            elif data[i+1] == 'fragments':
                if materials_dict['fragments'] >= 250:
                    materials_dict['fragments'] -= 250
                    print('Valanyr obtained!')
                    obtained = True
                    break
            elif data[i+1] == 'motes':
                if materials_dict['motes'] >= 250:
                    materials_dict['motes'] -= 250
                    print('Dragonwrath obtained!')
                    obtained = True
                    break
        else:
            materials_dict[data[i+1]] = int(data[i])
    if obtained:
        break

materials_data = [f"{key}: {value}" for key, value in materials_dict.items()]
print('\n'.join(materials_data))