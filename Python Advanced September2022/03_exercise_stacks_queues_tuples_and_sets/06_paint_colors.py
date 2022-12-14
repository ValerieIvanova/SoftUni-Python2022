from collections import deque

substrings = deque(input().split())

COLORS = ["red", "yellow", "blue", "orange", "purple", "green"]

collected_colors = []
while substrings:
    if len(substrings) > 1:
        sub1, sub2 = substrings.popleft(), substrings.pop()
        current_color = sub1 + sub2
        current_color_var_2 = sub2 + sub1
        if current_color in COLORS:
            collected_colors.append(current_color)
        elif current_color_var_2 in COLORS:
            collected_colors.append(current_color_var_2)
        else:
            middle = len(substrings) // 2
            stripped_sub1, stripped_sub2 = sub1[:-1], sub2[:-1]
            if stripped_sub1:
                substrings.insert(middle, stripped_sub1)
            if stripped_sub2:
                substrings.insert(middle, stripped_sub2)
    else:
        current_color = substrings.popleft()
        if current_color in COLORS:
            collected_colors.append(current_color)

for color in collected_colors:
    if color == 'orange':
        if 'red' not in collected_colors or 'yellow' not in collected_colors:
            collected_colors.remove(color)
    elif color == 'purple':
        if 'red' not in collected_colors or 'blue' not in collected_colors:
            collected_colors.remove(color)
    elif color == 'green':
        if 'yellow' not in collected_colors or 'blue' not in collected_colors:
            collected_colors.remove(color)

print(collected_colors)