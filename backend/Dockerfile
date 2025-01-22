FROM python:3.10-slim

# Installer les dépendances
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Définir la variable d'environnement FLASK_APP
ENV FLASK_APP=app.py

# Exposer le port pour Flask
EXPOSE 5000

# Lancer l'application avec flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


