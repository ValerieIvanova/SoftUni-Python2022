first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_sequence = []
for i in first_sequence:
    for j in second_sequence:
        if i in j and i not in new_sequence:
            new_sequence.append(i)
            break
print(new_sequence)

