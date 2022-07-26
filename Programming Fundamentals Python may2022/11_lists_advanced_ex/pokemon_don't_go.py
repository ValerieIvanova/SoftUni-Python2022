def increase_decrease(numbers):
    numbers = [int(num) for num in numbers if num != 'none']
    for i in range(len(numbers)):
        if numbers[i] <= int(removed_element):
            numbers[i] += int(removed_element)
        elif numbers[i] > int(removed_element):
            numbers[i] -= int(removed_element)
    numbers = [str(num) for num in numbers]
    return numbers


distances = input().split()
sum_of_all_removed_indexes = 0

while distances:
    index = int(input())
    if index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])
        sum_of_all_removed_indexes += int(removed_element)
    elif index >= len(distances):
        removed_element = distances.pop(-1)
        distances.append(distances[0])
        sum_of_all_removed_indexes += int(removed_element)
    else:
        removed_element = distances.pop(index)
        distances.insert(index, 'none')
        sum_of_all_removed_indexes += int(removed_element)
    distances = increase_decrease(distances)
print(sum_of_all_removed_indexes)