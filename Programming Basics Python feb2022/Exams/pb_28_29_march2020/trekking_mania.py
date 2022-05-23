number_of_groups = int(input())
people = 0
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
for i in range(number_of_groups):
    number_of_people = int(input())
    people += number_of_people
    if number_of_people <= 5:
        musala += number_of_people
    elif 6 <= number_of_people <= 12:
        mont_blanc += number_of_people
    elif 13 <= number_of_people <= 25:
        kilimanjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        k2 += number_of_people
    elif number_of_people >= 41:
        everest += number_of_people

print(f'{(musala / people) * 100:.2f}%')
print(f'{(mont_blanc / people) * 100:.2f}%')
print(f'{(kilimanjaro / people) * 100:.2f}%')
print(f'{(k2 / people) * 100:.2f}%')
print(f'{(everest / people) * 100:.2f}%')