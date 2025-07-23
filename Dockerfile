<<<<<<< HEAD
FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD ["rasa", "run", "--enable-api", "-p", "5005", "--cors", "*"]
=======
FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD ["run", "--enable-api", "--cors", "*", "-p", "5005"]
>>>>>>> 6b875d3e0abd4077c9ce1f8dcffb3992fee97b6e
