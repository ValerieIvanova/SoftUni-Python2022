movie_name = input()
days = int(input())
tickets = int(input())
price_of_ticket = float(input())
percent_for_the_cinema = float(input())

total_profit = (tickets * price_of_ticket) * days
profit_for_the_cinema = total_profit * (percent_for_the_cinema / 100)
movie_profit = total_profit - profit_for_the_cinema
print(f'The profit from the movie {movie_name} is {movie_profit:.2f} lv.')