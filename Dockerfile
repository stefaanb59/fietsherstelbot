FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 10000  # Gebruik een statisch poortnummer
# Gebruik de $PORT omgevingvariabele van Render voor de CMD
CMD ["rasa", "run", "--enable-api", "-p", "$PORT", "--cors", "*", "--host", "0.0.0.0"]
