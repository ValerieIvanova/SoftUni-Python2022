stack = []
lines = int(input())
for _ in range(lines):
    query = input()
    if query.startswith('1'):
        stack.append(int(query.split()[1]))
    elif stack:
        if query == '2':
            stack.pop()
        elif query == '3':
            print(max(stack))
        elif query == '4':
            print(min(stack))

result = []
while stack:
    result.append(str(stack.pop()))
print(', '.join(result))