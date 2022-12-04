from src.kafka_reader import read_kafka_data


def main():
    for message in read_kafka_data():
        print(f'user={message.user_id} \tmovie_id={message.movie_id} \ttimestamp={message.timestamp}')


if __name__ == '__main__':
    main()
