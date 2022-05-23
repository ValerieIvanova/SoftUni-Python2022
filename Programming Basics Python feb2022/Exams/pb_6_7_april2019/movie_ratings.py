import sys

number_of_movies = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
total_rating = 0
max_rate_movie = ''
min_rate_movie = ''
for i in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rate_movie = movie_name
    elif movie_rating < min_rating:
        min_rating = movie_rating
        min_rate_movie = movie_name
avr_rating = total_rating / number_of_movies
print(f'{max_rate_movie} is with highest rating: {max_rating:.1f}')
print(f'{min_rate_movie} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {avr_rating:.1f}')