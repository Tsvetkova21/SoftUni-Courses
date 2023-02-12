def forecast(*weather):
    locations = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }
    for city, weather in sorted(weather):
        locations[weather].append(city)
    result = []
    for key in locations:
        for value in locations[key]:
            result.append(f"{value} - {key}")
    return '\n'.join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

