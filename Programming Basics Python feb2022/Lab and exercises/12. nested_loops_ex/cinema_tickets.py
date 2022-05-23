total_student = 0
total_standard = 0
total_kid = 0
total_tickets = 0
while True:
    total_movie_tickets = 0
    student = 0
    standard = 0
    kid = 0
    movie_name = input()
    if movie_name == 'Finish':
        print(f'Total tickets: {total_tickets}')
        print(f'{((total_student / total_tickets) * 100):.2f}% student tickets.')
        print(f'{((total_standard / total_tickets) * 100):.2f}% standard tickets.')
        print(f'{((total_kid / total_tickets) * 100):.2f}% kids tickets.')
        break
    available_places = int(input())
    for i in range(1, available_places + 1):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kid += 1
    total_movie_tickets += student + standard + kid
    percent_full = (total_movie_tickets / available_places) * 100
    total_tickets += total_movie_tickets
    total_student += student
    total_standard += standard
    total_kid += kid
    print(f'{movie_name} - {percent_full:.2f}% full.')