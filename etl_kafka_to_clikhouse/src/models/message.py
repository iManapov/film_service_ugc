

class Message:
    """Class for keeping track of an item in inventory."""

    def __init__(self, user_movie_ids: bytes, timestamp: bytes):
        self.user_id: str = user_movie_ids.decode("utf-8").split('+')[0]
        self.movie_id: str = user_movie_ids.decode("utf-8").split('+')[1]
        self.timestamp: int = int(timestamp.decode("utf-8"))

