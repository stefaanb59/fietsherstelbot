FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 10000

# Render zet de $PORT environment variable in tijdens runtime
CMD ["sh", "-c", "rasa run --enable-api --port $PORT --cors '*' --host 0.0.0.0"]
