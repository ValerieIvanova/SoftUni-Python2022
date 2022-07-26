number = int(input())
plants_info = {}
plant_rating = {}
for i in range(number):
    plant, rarity = input().split('<->')
    if plant not in plants_info:
        plants_info[plant] = 0
        plant_rating[plant] = []
    plants_info[plant] += int(rarity)

while True:
    command = input().split(': ')
    command_name = command[0]
    if command_name == 'Exhibition':
        break

    elif command_name == 'Rate':
        current_plant, rating = command[1].split(' - ')
        if current_plant not in plants_info:
            print('error')
        else:
            plant_rating[current_plant].append(int(rating))

    elif command_name == 'Update':
        current_plant, new_rarity = command[1].split(' - ')
        if current_plant not in plants_info:
            print('error')
        else:
            plants_info[current_plant] = int(new_rarity)

    elif command_name == 'Reset':
        current_plant = command[1]
        if current_plant not in plants_info:
            print('error')
        else:
            plant_rating[current_plant] = []

print('Plants for the exhibition:')
for item, rarity in plants_info.items():
    if len(plant_rating[item]) > 0:
        print(f"- {item}; Rarity: {rarity}; Rating: {(sum(plant_rating[item]) / len(plant_rating[item])):.2f}")
    else:
        print(f"- {item}; Rarity: {rarity}; Rating: {sum(plant_rating[item]):.2f}")
