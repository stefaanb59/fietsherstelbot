FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

# The original EXPOSE line is removed.
# This CMD line correctly uses the Render environment variable.
CMD ["rasa", "run", "--enable-api", "-p", "$PORT", "--cors", "*", "--host", "0.0.0.0"]
