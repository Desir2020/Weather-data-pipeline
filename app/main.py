from app.extract.extract import weather_ville
from app.transform.transform import transform_weather_data
from app.load.load import load_weather

ville = input("Ville : ")

data = weather_ville(ville)

weather_data = transform_weather_data(data)


load_data = load_weather(weather_data)

for cle,valeur in weather_data.items():
    print(f"{cle}:{valeur}")
