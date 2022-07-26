string1 = input()
string2 = input()
for i in range(len(string1)):
    if string1[i] != string2[i]:
        print(string2[:i+1] + string1[i+1:])