number_of_lines = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(number_of_lines):
    integer = int(input())
    if integer % 2 == 0:
        even.append(integer)
    else:
        odd.append(integer)
    if integer >= 0:
        positive.append(integer)
    else:
        negative.append(integer)

command = input()
print(eval(command))