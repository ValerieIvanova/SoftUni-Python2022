happiness = list(map(int, input().split()))
improvement_factor = int(input())

improved_happiness = [n * improvement_factor for n in happiness]

avr_happiness = sum(improved_happiness) / len(improved_happiness)
happiest_employees = [emp for emp in improved_happiness if emp >= avr_happiness]
# happiest_employees = list(filter(lambda emp: emp >= avr_happiness, improved_happiness))

if len(happiest_employees) >= (len(improved_happiness) / 2):
    print(f'Score: {len(happiest_employees)}/{len(improved_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happiest_employees)}/{len(improved_happiness)}. Employees are not happy!')