import requests
from dotenv import load_dotenv
import os

load_dotenv()

def weather_ville(ville):
    api_key = os.getenv("API_KEY")
    
    try:
        if not api_key:
            raise ValueError("Clé API introuvable")

        # Etape 1: Récupérer la latitude et la longitude de la ville
        geo_url = "https://api.openweathermap.org/geo/1.0/direct"

        geo_params = {
            "q": ville,
            "limit": 1,
            "appid": api_key
        }

        geo_response = requests.get(geo_url, params=geo_params, timeout=5)

        if geo_response.status_code != 200:
            raise ValueError(f"Erreur API géocodage : {geo_response.status_code}")


        geo = geo_response.json()

        # Vérifie si l'API a trouvé une ville, même si la requête fonctionne l'API peut renvoyer une liste vide
        if not geo:
            raise ValueError("Ville introuvable")


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
            raise ValueError(f"Erreur API: {weather_response.status_code} - {weather_response.text}")


        data = weather_response.json()

        if "main" not in data or "name" not in data:
            raise ValueError("Données météo manquantes")


        if "weather" not in data or not data["weather"]:
            raise ValueError("Description météo manquante")


        return data

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Erreur réseau : {e}")
