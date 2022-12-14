file_path = './text.txt'

try:
    file = open(file_path, 'a+')
    print('File found')
except FileNotFoundError:
    print(f"{file_path} does not exist")