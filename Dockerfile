# Image de base Python 3.12 récupérée depuis Docker Hub
FROM python:3.12

# Mon dossier de travail dans le container, différent du dossier app/ de mon code
WORKDIR /app

# Je copie requirements.txt en premier avant le reste du code
# Docker construit l'image en couches, chaque ligne est une couche mise en cache
# Si je change mon code mais pas mes dépendances, Docker réutilise le cache
# et ne réinstalle pas les dépendances — ça évite de tout reconstruire à chaque fois
COPY requirements.txt .

# J'installe mes dépendances, --no-cache-dir pour ne pas alourdir l'image
RUN pip install --no-cache-dir -r requirements.txt

# Je copie tout mon projet dans le container
COPY . .

# logs/ est dans mon .dockerignore donc il n'est pas copié
# Je le crée manuellement sinon mon FileHandler plante au démarrage
RUN mkdir -p logs

# Commande lancée au démarrage du container, même chose que : python -m app.main
CMD ["python", "-m", "app.main"]
