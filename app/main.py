from app.extract.extract import weather_ville
from app.transform.transform import transform_weather_data


ville = input("Ville : ")

data = weather_ville(ville)

weather_data = transform_weather_data(data)

for cle,valeur in weather_data.items():
    print(f"{cle}:{valeur}")