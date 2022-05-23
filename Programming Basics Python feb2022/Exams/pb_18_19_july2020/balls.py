from math import floor

n = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
divides = 0
for i in range(n):
    ball_color = input()
    if ball_color == 'red':
        points += 5
        red_balls += 1
    elif ball_color == 'orange':
        points += 10
        orange_balls += 1
    elif ball_color == 'yellow':
        points += 15
        yellow_balls += 1
    elif ball_color == 'white':
        points += 20
        white_balls += 1
    elif ball_color == 'black':
        divides += 1
        points = floor(points / 2)
    else:
        other_colors += 1
        continue
print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {divides}")