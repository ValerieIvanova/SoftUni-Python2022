string = input()
strength = 0
new_string = ''
for i in range(len(string)):
    if string[i] == '>':    # Getting strength, adding the ">" symbol in the new string
        strength += int(string[i+1])
        new_string += string[i]
    elif string[i] != '>' and strength > 0:  # Explosion, not adding symbols, decreasing the strength
        strength -= 1
    else:   # Adding symbols to the new string
        new_string += string[i]
print(new_string)