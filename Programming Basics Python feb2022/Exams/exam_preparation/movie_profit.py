movie_name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
percent_for_the_cinema = int(input())

daily_sum = ticket_price * tickets_count
profit = daily_sum * days
cinema_profit = profit * (percent_for_the_cinema / 100)
movie_profit = profit - cinema_profit
print(f"The profit from the movie {movie_name} is {movie_profit:.2f} lv.")