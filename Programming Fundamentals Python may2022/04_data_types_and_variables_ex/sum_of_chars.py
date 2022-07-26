number_of_lines = int(input())
sum = 0
for i in range(1, number_of_lines + 1):
    letter = input()
    sum += ord(letter)
print(f'The sum equals: {sum}')
