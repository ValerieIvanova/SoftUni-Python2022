# string = input().split(", ")
#
# for i in range(len(string)):
#     if string[i] == 'wolf' and i == len(string)-1:
#         print('Please go away and stop eating my sheep')
#         break
#     elif string[i] == 'wolf' and i < len(string):
#         print(f'Oi! Sheep number {len(string) - i-1}! You are about to be eaten by a wolf!')
#         break

string = input().split(', ')
wolf_index = string.index('wolf') + 1
sheep_index = len(string) - wolf_index
if wolf_index == len(string):
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!')