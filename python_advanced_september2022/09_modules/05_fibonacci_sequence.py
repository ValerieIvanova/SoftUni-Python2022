from fibonacci_module import locate, create


while True:
    line = input()
    if line == 'Stop':
        break
    line_args = line.split()
    if line_args[0] == 'Create':
        nums = create(int(line_args[2]))
        print(nums)
    elif line_args[0] == 'Locate':
        idx = locate(int(line_args[1]), nums)
        if idx == -1:
            print(f"The number {line_args[1]} is not in the sequence")
        else:
            print(f"The number - {line_args[1]} is at index {idx}")