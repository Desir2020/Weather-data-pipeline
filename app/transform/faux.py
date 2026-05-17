def transform_weather_data(data):
    city = data["name"]
    # Certaines données météo peuvent ne pas être renvoyées par l'API.
    # .get() permet d'éviter une erreur si une clé est absente.
    country = data.get("sys", {}).get("country")
    print(data)

    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]

    recorded_at = data["dt"]

    weather_main = data["weather"][0]["main"]
    weather_description = data["weather"][0]["description"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data.get("wind", {}).get("speed")
