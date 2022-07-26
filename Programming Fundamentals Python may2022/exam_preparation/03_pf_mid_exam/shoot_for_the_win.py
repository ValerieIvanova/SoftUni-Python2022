targets = list(map(int, input().split()))
count = 0

while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {count} -> {' '.join([str(e) for e in targets])}")
        break
    index = int(command)
    if 0 <= index < len(targets):
        target_value = targets[index]
        if targets[index] != -1:
            targets[index] = -1
            count += 1
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > target_value:
                    targets[i] -= target_value
                elif targets[i] <= target_value:
                    targets[i] += target_value