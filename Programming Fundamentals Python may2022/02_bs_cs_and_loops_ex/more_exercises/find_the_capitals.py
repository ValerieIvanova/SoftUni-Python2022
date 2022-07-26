string = input()
ind = []
for i in range(len(string)):
    if string[i].isupper():
        ind.append(i)
    else:
        continue
print(ind)