import sys

number_of_movies = int((input()))
max_rated_movie = ''
min_rated_movie = ''
highest_rate = -sys.maxsize
lowest_rate = sys.maxsize
total_rating = 0
for i in range(1, number_of_movies + 1):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > highest_rate:
        highest_rate = movie_rating
        max_rated_movie = movie_name
    if movie_rating < lowest_rate:
        lowest_rate = movie_rating
        min_rated_movie = movie_name
avr_rating = total_rating / number_of_movies
print(f"{max_rated_movie} is with highest rating: {highest_rate:.1f}")
print(f"{min_rated_movie} is with lowest rating: {lowest_rate:.1f}")
print(f"Average rating: {avr_rating:.1f}")