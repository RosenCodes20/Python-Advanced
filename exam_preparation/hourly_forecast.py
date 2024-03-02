def forecast(*args):
    weather_forecast = {}
    sunny = ""
    cloudy = ""
    rainy = ""
    for element in args:
        town, weather = element

        if town not in weather_forecast:
            weather_forecast[town] = weather

    for town, weather in sorted(weather_forecast.items(), key=lambda x: (x[1], x[0])):
        if weather == "Sunny":
            sunny += f"{town} - {weather}\n"

        elif weather == "Cloudy":
            cloudy += f"{town} - {weather}\n"

        elif weather == "Rainy":
            rainy += f"{town} - {weather}\n"

    return sunny + cloudy + rainy


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
