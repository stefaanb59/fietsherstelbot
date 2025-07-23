FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD ["run", "--enable-api", "--cors", "*", "-p", "5005"]
