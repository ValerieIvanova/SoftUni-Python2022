box_of_clothes = input().split()
total_rack_capacity = int(input())
current_rack_capacity = total_rack_capacity
racks = 1
while box_of_clothes:
    if int(box_of_clothes[-1]) == current_rack_capacity:
        box_of_clothes.pop()
        if box_of_clothes:
            racks += 1
            current_rack_capacity = total_rack_capacity
    elif int(box_of_clothes[-1]) > current_rack_capacity:
        racks += 1
        current_rack_capacity = total_rack_capacity - int(box_of_clothes.pop())
    else:
        current_rack_capacity -= int(box_of_clothes.pop())

print(racks)
