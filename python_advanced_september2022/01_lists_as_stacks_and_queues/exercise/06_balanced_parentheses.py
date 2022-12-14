parentheses = input()
stack = []
balanced = False
for s in parentheses:
    if s in '({[':
        stack.append(s)
        continue
    elif s in ')}]' and stack:
        if stack[-1] + s in '(){}[]':
            stack.pop()
            balanced = True
        else:
            balanced = False
            break
    else:
        balanced = False
        break

if balanced and not stack:
    print('YES')
else:
    print('NO')