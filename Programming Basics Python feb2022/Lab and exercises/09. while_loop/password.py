username = input()
password = input()

while True:
    data = input()
    if data == password:
        print(f'Welcome {username}!')
        break