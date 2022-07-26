to_do_list = [''] * 11   # range 0 - 10 inclusive
while True:
    command = input()
    if command == 'End':
        break
    notes_info = command.split('-')
    importance = int(notes_info[0])
    note = notes_info[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, note)
final_list = [element for element in to_do_list if element != '']
print(final_list)