def first_string_longer(total, first, second):
    for i in range(len(second)):
        total += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        total += ord(first[i])
    return total


def second_string_longer(total, first, second):
    for i in range(len(first)):
        total += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        total += ord(second[i])
    return total


def even_strings(total, first, second):
    for i in range(len(first)):
        total += ord(first[i]) * ord(second[i])
    return total


first_string, second_string = input().split()
total_sum = 0
diff = abs(len(first_string) - len(second_string))

if len(first_string) > len(second_string):
    total_sum += first_string_longer(total_sum, first_string, second_string)

elif len(first_string) < len(second_string):
    total_sum += second_string_longer(total_sum, first_string, second_string)

else:
    total_sum += even_strings(total_sum, first_string, second_string)

print(total_sum)