capacity = int(input())
current_sum = 0
sum = 0
while True:
    number_of_people = input()
    if number_of_people == 'Movie time!':
        print(f'There are {capacity} seats left in the cinema.')
        break
    if int(number_of_people) > capacity:
        print('The cinema is full.')
        break
    capacity -= int(number_of_people)
    current_sum += int(number_of_people) * 5
    if int(number_of_people) % 3 == 0:
        current_sum -= 5
    sum += current_sum
    current_sum = 0

print(f'Cinema income - {sum} lv.')