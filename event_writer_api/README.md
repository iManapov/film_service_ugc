# User-generated content Api

## Local run
Firstly create env file `src/core/.env` with following parameters:
```dotenv
SERVICE_SECRET_KEY - secret key from uth service
KAFKA_HOST - Kafka host
KAFKA_TOPIC - topic name in Kafka
```

To run under `uvicorn` execute following commands:
```shell
uvicorn main:app --reload --host localhost --port 8001
```
To run under `gunicorn` execute following commands:
```shell
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornH11Worker --bind 0.0.0.0:8001
```

OpenApi documentation url: http://localhost:8001/apidocs/


## Run in Docker

Create `.env` file in the root folder of project with following parameters:
```dotenv
SERVICE_SECRET_KEY - secret key from uth service
KAFKA_HOST - Kafka host
KAFKA_TOPIC - topic name in Kafka
```

To run api in `Docker` execute following command:
```shell
docker compose up --build
```

OpenApi documentation url: http://localhost/api/openapi/
