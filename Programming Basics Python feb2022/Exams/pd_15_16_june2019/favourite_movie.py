import sys

movies_counter = 0
max_points = -sys.maxsize
points = 0
best_movie = ''
while True:
    movies_counter += 1
    if movies_counter > 7:
        print('The limit is reached.')
        print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')
        break
    movie_name = input()
    if movie_name == 'STOP':
        print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')
        break
    for i in range(len(movie_name)):
        points += ord(movie_name[i])
        if movie_name[i].islower():
            points -= 2 * len(movie_name)
        elif movie_name[i].isupper():
            points -= len(movie_name)
    if points > max_points:
        max_points = points
        best_movie = movie_name
    points = 0

# best_movie = ""
# total_points = 0
# counter = 0
# current_points = 0
# while True:
#     movie = input()
#     if movie == "STOP":
#         break
#     counter += 1
#     if counter == 7:
#         break
#     points = 0
#     for ch in movie:
#         if ch.isupper() and ch.isalpha():
#             points = ord(ch) - len(movie)
#             current_points += points
#         elif ch.islower() and ch.isalpha():
#             points = ord(ch) - len(movie) * 2
#             current_points += points
#         else:
#             points = ord(ch)
#             current_points += points
#
#     if current_points > total_points:
#         total_points = current_points
#         best_movie = movie
#
#     current_points = 0
#
# if counter == 7:
#     print("The limit is reached.")
# print(f"The best movie for you is {best_movie} with {total_points} ASCII sum.")