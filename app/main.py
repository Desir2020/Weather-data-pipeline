from app.extract.extract import weather_ville
from app.transform.transform import transform_weather_data
from app.load.load import load_weather
import logging
import sys

logging.basicConfig(
    # Montre les INFO les plus importants
    level=logging.INFO,
    # Veut dire: date/heure - type - message
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/pipeline.log")
    ]
)

if len(sys.argv) < 2:
    logging.error("Usage python -m app.main <ville>")
    sys.exit(1)

try:
    logging.info("Démarrage du pipeline météo")
    ville = sys.argv[1]

    logging.info("Début de la récupération météo")
    data = weather_ville(ville)

    logging.info("Transformation des données")
    weather_data = transform_weather_data(data)

    logging.info("Chargement des données dans PostgreSql")
    load_weather(weather_data)

    logging.info("Pipeline terminée")

except Exception as e:
    logging.error(f"Erreur dans le pipeline : {e}")
