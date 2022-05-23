result1 = input()
result2 = input()
result3 = input()

win = 0
loses = 0
drawn = 0

if int(result1[0]) and int(result2[0]) and int(result3[0]) > int(result1[2]) and int(result2[2]) and int(result3[2]):
    win += 1
elif int(result1[0]) and int(result2[0]) and int(result3[0]) < int(result1[2]) and int(result2[2]) and int(result3[2]):
    loses += 1
else:
    drawn += 1

print(f"Team won {win} games")
print(f"Team lost {loses} games")
print(f"Drawn games: {drawn}")
