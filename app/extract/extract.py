import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
ville = input("Veuillez saisir le nom de la ville: ")

try:
    if not api_key:
        print("Clé API introuvable")
        exit()

    # Etape 1: Récupérer la latitude et la longitude de la ville
    geo_url = "https://api.openweathermap.org/geo/1.0/direct"

    geo_params = {
        "q": ville,
        "limit": 1,
        "appid": api_key
    }

    geo_response = requests.get(geo_url, params=geo_params, timeout=5)

    if geo_response.status_code != 200:
        print("Erreur API géocodage :", geo_response.status_code)
        exit()

    geo = geo_response.json()

    # Vérifie si l'API a trouvé une ville, même si la requête fonctionne l'API peut renvoyer une liste vide
    if not geo:
        print("Ville introuvable")
        exit()

    lat = geo[0]["lat"]
    lon = geo[0]["lon"]

    # Etape 2: Récupérer les données météos
    weather_url = "https://api.openweathermap.org/data/2.5/weather"

    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }


    weather_response = requests.get(weather_url, params=weather_params, timeout=5)

    #Vérifie le code HTTP
    if weather_response.status_code != 200:
        print("Erreur API: ", weather_response.status_code)
        print(weather_response.text)
        exit()

    data = weather_response.json()

    if "main" not in data or "name" not in data:
        print("Données météo manquantes")
        exit()

    if "weather" not in data or not data["weather"]:
        print("Description météo manquante")
        exit()

    city = data["name"]
    # Certaines données météo peuvent ne pas être renvoyées par l'API.
    # .get() permet d'éviter une erreur si une clé est absente.
    country = data.get("sys", {}).get("country")

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


except requests.exceptions.RequestException as e:
    print("Erreur réseau :", e)


