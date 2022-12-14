def sum_numbers(command: str, n: list):
    reworked_list = []
    if command == 'negative':
        reworked_list = [i for i in n if i < 0]
    elif command == 'positive':
        reworked_list = [i for i in n if i >= 0]
    print(sum(reworked_list))
    return sum(reworked_list)


numbers = [int(x) for x in input().split()]
negatives = sum_numbers('negative', numbers)
positives = sum_numbers('positive', numbers)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
