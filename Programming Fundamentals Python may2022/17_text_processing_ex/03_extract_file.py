path = input().split('\\')
file_name, extension = path[-1].split('.')
print(f"File name: {file_name}\n"
      f"File extension: {extension}")