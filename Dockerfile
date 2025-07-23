FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD sh -c "rasa run --enable-api -p ${PORT:-5005} --cors '*'"
