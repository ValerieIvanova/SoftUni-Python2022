def create(n):
    if n == 1:
        return [0]
    if n == 0:
        return []
    result = [0, 1]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


def locate(target, nums):
    for i in range(len(nums)):
        current_num = nums[i]
        if current_num == target:
            return i
    return -1