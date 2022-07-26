def collect(collection, current_item):
    items.append(current_item)
    return collection


def drop(collection, current_item):
    collection.remove(current_item)
    return collection


def combine_items(collection, current_item, new_item):
    index = collection.index(current_item)
    collection.insert(index + 1, new_item)
    return collection


def renew(collection, current_item):
    index = collection.index(current_item)
    collection.append(collection.pop(index))
    return collection


items = input().split(', ')

while True:
    command = input().split(' - ')
    command_name = command[0]
    if command_name == 'Craft!':
        print(*items, sep=', ')
        break
    elif command_name == 'Collect':
        item = command[1]
        if item not in items:
            items = collect(items, item)
        else:
            continue
    elif command_name == 'Drop':
        item = command[1]
        if item in items:
            items = drop(items, item)
        else:
            continue
    elif command_name == 'Combine Items':
        data = command[1].split(':')
        item1 = data[0]
        item2 = data[1]
        if item1 in items:
            items = combine_items(items, item1, item2)
        else:
            continue
    elif command_name == 'Renew':
        item = command[1]
        if item in items:
            items = renew(items, item)
        else:
            continue
