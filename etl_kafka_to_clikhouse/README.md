# Код ETL процесса

## Настройка ClikHouse
Перед началом процесса необходимо создать базы данных и таблицы в них

В файле `db_setup.ddl` приведен пример запросов для конфига с 2 нодами и 2 репликами

## Локальный запуск
Предварительно необходимо создать файл `core/.env` со следующими параметрами:

```dotenv
KAFKA_HOST - сервер Kafka
CLICKHOUSE_HOST - сервер ClickHouse
```

Для запуска api необходимо выполнить команду
```shell
python main.py
```


## Запуск в Docker
Предварительно необходимо создать файл `core/docker.env` со следующими параметрами:

```dotenv
KAFKA_HOST - сервер Kafka
CLICKHOUSE_HOST - сервер ClickHouse
```