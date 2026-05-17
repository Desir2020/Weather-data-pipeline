from datetime import datetime

def transform_weather_data(data):

    city = data["name"]

    # Certaines données météo peuvent ne pas être renvoyées par l'API.
    # .get() évite une erreur si une clé est absente.
    country = data.get("sys", {}).get("country")

    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]

    recorded_at = datetime.fromtimestamp(data["dt"])

    weather_main = data["weather"][0]["main"]
    weather_description = data["weather"][0]["description"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data.get("wind", {}).get("speed")

    weather_data = {
        "city": city,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "recorded_at": recorded_at,
        "weather_main": weather_main,
        "weather_description": weather_description,
        "temperature": temperature,
        "feels_like": feels_like,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed
    }

    return weather_data