rent = int(input())

statues = rent - (rent * 0.30)
catering = statues - (statues * 0.15)
sound = catering / 2

total = rent + statues + catering + sound

print(f'{total:.2f}')
