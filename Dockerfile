FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

# Gebruik een statisch poortnummer voor EXPOSE
EXPOSE 10000

# Gebruik de $PORT omgevingvariabele van Render voor de CMD
CMD ["rasa", "run", "--enable-api", "-p", "$PORT", "--cors", "*", "--host", "0.0.0.0"]
