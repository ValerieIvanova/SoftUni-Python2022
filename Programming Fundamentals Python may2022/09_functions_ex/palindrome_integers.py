def palindrome_numbers(n):
    for num in n:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(', ')
palindrome_numbers(numbers)