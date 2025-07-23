FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD ["rasa", "run", "--enable-api", "-p", "5005", "--cors", "*"]
