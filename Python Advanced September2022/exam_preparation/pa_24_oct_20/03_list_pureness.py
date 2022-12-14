from collections import deque


def best_list_pureness(numbers: list, k: int):
    numbers = deque(numbers)
    res = {
        '0': sum(numbers[i] * i for i in range(len(numbers)))
    }
    for rotation in range(1, k + 1):
        numbers.rotate(1)
        res[rotation] = sum(numbers[i] * i for i in range(len(numbers)))

    best_rotation = max(res, key=res.get)
    return f"Best pureness {res[best_rotation]} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
