#!/bin/sh

# Warnings onderdrukken (optioneel)
export SQLALCHEMY_SILENCE_UBER_WARNING=1

# Start Rasa server in achtergrond
rasa run \
  --enable-api \
  --cors "*" \
  --port 5005 \
  --debug &

# Start Rasa action server op poort 5055
rasa run actions \
  --port 5055
