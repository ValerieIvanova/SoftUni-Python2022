number_of_1bgn = int(input())
number_of_2bgn = int(input())
number_of_5bgn = int(input())
sum = int(input())
sum2 = 0
no_match = False
for bgn1 in range(0, number_of_1bgn + 1):
    for bgn2 in range(0, number_of_2bgn + 1):
        for bgn5 in range(0, number_of_5bgn + 1):
            sum2 = (bgn1 * 1) + (bgn2 * 2) + (bgn5 * 5)
            if sum2 == sum:
                print(f"{bgn1} * 1 lv. + {bgn2} * 2 lv. + {bgn5} * 5 lv. = {sum} lv.")
            else:
                continue
        continue
    continue