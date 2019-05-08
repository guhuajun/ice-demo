FROM goozler/zeroc_ice_python:3.7.0.1

WORKDIR /app/

COPY demo ./demo/
COPY server/app/server.py .

EXPOSE 8000

CMD [ "python", "server.py" ]
