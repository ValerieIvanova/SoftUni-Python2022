list_of_events = ['coding', 'dog', 'cat', 'movie']
coffees = 0
extra_sleep = False
while True:
    if coffees > 5:
        print('You need extra sleep')
        extra_sleep = True
        break
    command = input()
    if command == 'END':
        break
    if command.lower() not in list_of_events:
        continue
    else:
        if command.islower():
            coffees += 1
        else:
            coffees += 2
if not extra_sleep:
    print(coffees)