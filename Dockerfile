# Gebruik het volledige Rasa-image met alle dependencies
FROM rasa/rasa:latest-full

# Zet de werkmap
WORKDIR /app

# Kopieer alle bestanden uit je project naar de container
COPY . /app

# Optioneel: geef een standaardpoort aan (Render gebruikt $PORT toch dynamisch)
EXPOSE 10000

# Zorg dat shellvariabelen zoals $PORT geïnterpreteerd worden
SHELL ["/bin/sh", "-c"]

# Start Rasa met API ingeschakeld, op de Render-poort, met CORS open
CMD rasa run --enable-api --port $PORT --cors "*" --host 0.0.0.0
