# a, b, c = int(input()) , int(input()) , int(input())
# sum_current_sec = a + b + c
#
# minutes = sum_current_sec % 60
# hours = sum_current_sec // 60
#
# print(f'{hours}:{minutes:02d}')
from math import floor

a = int(input())
b = int(input())
c = int(input())

total_sec = a + b + c
minutes = total_sec // 60
seconds = total_sec % 60
total_min = (f"{minutes}:{seconds:02d}")

print(total_min)