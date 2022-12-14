def forecast(*args):
    locations_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }
    for el in args:
        locations_dict[el[1]].append(el[0])

    result = []
    for weather, locations in locations_dict.items():
        for location in sorted(locations):
            result.append(f"{location} - {weather}")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))