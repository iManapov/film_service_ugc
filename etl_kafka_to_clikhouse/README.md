# UGC ETL Kafka to ClikHouse

## ClikHouse setting
Before starting the process, you need to create databases and tables in them

The `db_setup.ddl` file contains an example of queries for a config with 2 nodes and 2 replicas

## Local run
Firstly create env file `core/.env` with following parameters:

```dotenv
KAFKA_HOST - Kafka host
CLICKHOUSE_HOST - ClickHouse host
```

To run ETL process execute command:
```shell
python main.py
```
