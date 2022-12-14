class ValueCannotBeNegative(Exception):
    """
    negative number error
    """
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative