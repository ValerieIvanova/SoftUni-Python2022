string = input()
[print(f":{string[i+1]}") for i in range(len(string)) if string[i] == ':']
