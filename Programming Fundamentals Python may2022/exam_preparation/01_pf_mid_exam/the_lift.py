people_count = int(input())
current_state_of_the_lift = list(map(int, input().split()))
next_wagon = False
no_more_people = False
no_more_space = False
if people_count > 0:
    for wagon in range(len(current_state_of_the_lift)):
        for person in range(1, people_count+1):
            if sum(current_state_of_the_lift) == len(current_state_of_the_lift) * 4:
                no_more_space = True
                break
            if current_state_of_the_lift[wagon] < 4:
                current_state_of_the_lift[wagon] += 1
                people_count -= 1
                if people_count == 0:
                    no_more_people = True
                    if sum(current_state_of_the_lift) == len(current_state_of_the_lift) * 4:
                        no_more_space = True
                    break
            else:
                next_wagon = True
                continue
        if next_wagon:
            continue

final_state_of_the_lift = list(map(str, current_state_of_the_lift))
if no_more_people and not no_more_space:
    print('The lift has empty spots!')
    print(' '.join(final_state_of_the_lift))
elif no_more_space and not no_more_people:
    print(f"There isn't enough space! {people_count} people in a queue!")
    print(' '.join(final_state_of_the_lift))
elif no_more_space and no_more_people:
    print(' '.join(final_state_of_the_lift))