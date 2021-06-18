import redis

redis_conn = redis.Redis()


def inc_room_count(room_name):
    """Увеличивает счетчик участников в комнате чата"""


def dec_room_count(room_name):
    """Уменьшает счетчик участников в комнате чата"""


def add_message(user, room_name, message):
    """Добавляет сообщение в комнату чата"""


def get_room_list():
    """Возвращает названия всех комнат чата"""
