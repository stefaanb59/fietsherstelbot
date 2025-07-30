# Gebruik het volledige Rasa-image met SDK en spacy
FROM rasa/rasa:latest-full

# Werkdirectory in container
WORKDIR /app

# Kopieer alle bestanden naar container
COPY . /app

# Installeer extra Python-pakketten (optioneel)
USER root
RUN pip install --no-cache-dir rasa-sdk openai

# Zorg dat start.sh uitvoerbaar is
RUN chmod +x /app/start.sh

# Poorten voor Rasa server (5005) en action server (5055)
EXPOSE 5005 5055

# Voer startscript uit
ENTRYPOINT ["/app/start.sh"]
CMD ["rasa", "run", "--enable-api", "--model", "models/20250507-102541-yellow-guitar.tar.gz", "--cors", "*", "--port", "5005", "--host", "0.0.0.0"]
