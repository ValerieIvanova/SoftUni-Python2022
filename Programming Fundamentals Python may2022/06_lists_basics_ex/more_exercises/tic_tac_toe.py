# first_line = input().split()
# second_line = input().split()
# third_line = input().split()
# draw = False
# empty = 0
# # Columns
# for i in range(len(first_line)):
#     if first_line[i] == second_line[i] == third_line[i]:
#         if first_line[0] == '1':
#             print('First player won')
#             break
#         elif first_line[0] == '2':
#             print('Second player won')
#             break
#         else:
#             empty += 1
#     else:
#         # Rows
#         if first_line[0] == first_line[1] == first_line[2]:
#             if first_line[0] == '1':
#                 print('First player won')
#                 break
#             elif first_line[0] == '2':
#                 print('Second player won')
#                 break
#             else:
#                 empty += 1
#         if second_line[0] == second_line[1] == second_line[2]:
#             if second_line[0] == '1':
#                 print('First player won')
#                 break
#             elif second_line[0] == '2':
#                 print('Second player won')
#                 break
#             else:
#                 empty += 1
#         # Diagonals
#         if third_line[0] == third_line[1] == third_line[2]:
#             if third_line[0] == '1':
#                 print('First player won')
#                 break
#             elif third_line[0] == '2':
#                 print('Second player won')
#                 break
#             else:
#                 empty += 1
#
#         if first_line[0] == second_line[1] == third_line[2]:
#             if first_line[0] == '1':
#                 print('First player won')
#                 break
#             elif first_line[0] == '2':
#                 print('Second player won')
#                 break
#             else:
#                 empty += 1
#         if first_line[2] == second_line[1] == third_line[0]:
#             if first_line[2] == '1':
#                 print('First player won')
#                 break
#             elif first_line[2] == '2':
#                 print('Second player won')
#                 break
#             else:
#                 empty += 1
#         else:
#             draw = True
#
# if draw:
#     print('Draw!')

field = []

first_player_win = False
second_player_win = False
draw = False
for field_row in range(3):
    current_row = input().split()
    field.append(current_row)

for row in range(3):
    if field[row][0] == field[row][1] == field[row][2] != "0":
        if field[row][0] == field[row][1] == field[row][2] == "1":
            first_player_win = True
        elif field[row][0] == field[row][1] == field[row][2] == "2":
            second_player_win = True

for col in range(3):
    if field[0][col] == field[1][col] == field[2][col] != "0":
        if field[0][col] == field[1][col] == field[2][col] == "1":
            first_player_win = True
        elif field[0][col] == field[1][col] == field[2][col] == "2":
            second_player_win = True

if field[0][0] == field[1][1] == field[2][2] != "0":
    if field[0][0] == field[1][1] == field[2][2] == "1":
        first_player_win = True
    elif field[0][0] == field[0][1] == field[2][2] == "2":
        second_player_win = True

elif field[0][2] == field[1][1] == field[2][0] != "0":
    if field[0][2] == field[1][1] == field[2][0] == "1":
        first_player_win = True
    elif field[0][2] == field[1][1] == field[2][0] == "2":
        second_player_win = True

if not first_player_win and not second_player_win:
    draw = True

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
elif draw:
    print("Draw!")