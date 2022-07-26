countries = input().split(', ')
capitals = input().split(', ')
dictionary = dict(zip(countries, capitals))
[print(f"{country} -> {capital}") for country, capital in dictionary.items()]