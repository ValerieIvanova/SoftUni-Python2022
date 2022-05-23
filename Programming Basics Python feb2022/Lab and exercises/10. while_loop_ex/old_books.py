book_needed = input()
counter = 0
book = input()
while book != book_needed:
    if book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {counter} books.')
        break
    counter += 1
    book = input()
if book == book_needed:
    print(f'You checked {counter} books and found it.')
