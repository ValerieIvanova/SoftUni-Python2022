def lesson_in(lesson):
    if lesson in schedule:
        return True
    else:
        return False


def add(lesson):
    if not lesson_in(lesson):
        schedule.append(lesson)
    return schedule


def insert(lesson):
    index = int(command_data[2])
    if not lesson_in(lesson):
        schedule.insert(index, lesson)
    return schedule


def remove(lesson):
    if lesson_in(lesson):
        schedule.remove(lesson)
    if lesson_in(f'{lesson}-Exercise'):
        schedule.remove(f'{lesson}-Exercise')
    return schedule


def swap(lesson, lesson2):
    if lesson_in(lesson) and lesson_in(lesson2):
        index1 = schedule.index(lesson)
        index2 = schedule.index(lesson2)
        temp = schedule[index1]
        schedule[index1] = schedule[index2]
        schedule[index2] = temp
    if lesson_in(f'{lesson}-Exercise'):
        lesson_index = schedule.index(lesson)
        exercise_index = schedule.index(f'{lesson}-Exercise')
        schedule.insert(lesson_index+1, schedule.pop(exercise_index))
    if lesson_in(f'{lesson2}-Exercise'):
        lesson_index = schedule.index(lesson2)
        exercise_index = schedule.index(f'{lesson2}-Exercise')
        schedule.insert(lesson_index+1, schedule.pop(exercise_index))
    return schedule


def exercise(lesson):
    if lesson_in(lesson) and not lesson_in(f'{lesson}-Exercise'):
        lesson_index = schedule.index(lesson)
        schedule.insert(lesson_index+1, f'{lesson}-Exercise')
    elif not lesson_in(lesson):
        schedule.append(lesson)
        schedule.append(f'{lesson}-Exercise')
    return schedule


schedule = input().split(', ')

while True:
    command_data = input().split(':')
    current_command = command_data[0]
    if current_command == 'course start':
        break
    lesson_title = command_data[1]
    if current_command == 'Add':
        add(lesson_title)
    elif current_command == 'Insert':
        insert(lesson_title)
    elif current_command == 'Remove':
        remove(lesson_title)
    elif current_command == 'Swap':
        lesson_title_2 = command_data[2]
        swap(lesson_title, lesson_title_2)
    elif current_command == 'Exercise':
        exercise(lesson_title)


for i in range(len(schedule)):
    print(f'{i+1}.{schedule[i]}')