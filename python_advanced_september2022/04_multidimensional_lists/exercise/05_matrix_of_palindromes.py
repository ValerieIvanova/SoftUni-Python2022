rows, cols = [int(x) for x in input().split()]
palindrome_matrix = []
for row in range(rows):
    palindrome_matrix.append([])
    for col in range(cols):
        first_letter, last_letter = chr(97 + row) * 2  # ASCII 'a' = 97
        middle_letter = chr(97 + col + row)
        palindrome_matrix[row].append(first_letter+middle_letter+last_letter)

[print(*palindrome_matrix[row]) for row in range(rows)]