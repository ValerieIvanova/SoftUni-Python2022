# string = [word for word in input().split() if len(word) % 2 == 0]
# print('\n'.join(string))

print('\n'.join(word for word in input().split() if len(word) % 2 == 0))