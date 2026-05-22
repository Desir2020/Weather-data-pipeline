import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

#Connexion à la base
def connect_db():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME") ,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )

    return connection

def load_weather(weather_data):
    with connect_db() as connection:
        with connection.cursor() as cursor:

            query= """
                INSERT INTO weather (
                    city,
                    country,
                    latitude,
                    longitude,
                    recorded_at,
                    weather_main,
                    weather_description,
                    temperature,
                    feels_like,
                    temp_min,
                    temp_max,
                    humidity,
                    pressure,
                    wind_speed
                )
                VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s
                )    
                
                ON CONFLICT (city,recorded_at)
                DO NOTHING
            """
            values = (
                weather_data["city"],
                weather_data["country"],
                weather_data["latitude"],
                weather_data["longitude"],
                weather_data["recorded_at"],
                weather_data["weather_main"],
                weather_data["weather_description"],
                weather_data["temperature"],
                weather_data["feels_like"],
                weather_data["temp_min"],
                weather_data["temp_max"],
                weather_data["humidity"],
                weather_data["pressure"],
                weather_data["wind_speed"]
            )

            #Prépare et execute
            cursor.execute(query, values)



