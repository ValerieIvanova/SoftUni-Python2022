number_of_lines = int(input())
balanced = False
brackets = ''
for i in range(number_of_lines):
    string = input()
    if string == '(' or string == ')':
        brackets += string
for s in range(len(brackets)):
    if len(brackets) % 2 == 0:
        if s % 2 == 0 and brackets[s] == '(':
            balanced = True
        elif s % 2 != 0 and brackets[s] == ')':
            balanced = True
        else:
            balanced = False
            break
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')