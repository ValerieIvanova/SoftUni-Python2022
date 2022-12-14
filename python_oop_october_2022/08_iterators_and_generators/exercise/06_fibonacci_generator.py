def fibonacci():

    prev_num = 0
    next_num = 1

    while True:
        yield prev_num
        prev_num, next_num = next_num, prev_num + next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
