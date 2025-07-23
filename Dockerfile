FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE $PORT # Dit is optioneel voor Render, maar goede praktijk
# Gebruik de $PORT omgevingvariabele van Render
CMD ["rasa", "run", "--enable-api", "-p", "$PORT", "--cors", "*", "--host", "0.0.0.0"]
