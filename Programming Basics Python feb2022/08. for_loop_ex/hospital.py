period = int(input())
treated_patients = 0
untreated_patients = 0
total_doctors = 7

for i in range(1, period + 1):
    number_of_patients_per_day = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        total_doctors += 1
    if number_of_patients_per_day <= total_doctors:
        treated_patients += number_of_patients_per_day
    else:
        treated_patients += total_doctors
        untreated_patients += number_of_patients_per_day - total_doctors


print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')