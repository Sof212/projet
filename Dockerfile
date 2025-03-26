# image python (légere) comme interpreteur
FROM python:3.10-slim

# rep de travail
WORKDIR /projet

COPY . /projet

# Installer les dépendances depuis requirements.txt
RUN pip install -r requirements.txt

# listen port de mon app
EXPOSE 5001

# Lancer l'app
CMD ["python", "app.py"]
