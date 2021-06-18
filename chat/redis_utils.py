import redis
from django.conf import settings

redis_conn = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def inc_room_count(room_name):
    """Увеличивает счетчик участников в комнате чата"""


def dec_room_count(room_name):
    """Уменьшает счетчик участников в комнате чата"""


def add_message(user, room_name, message):
    """Добавляет сообщение в комнату чата"""


def get_room_list():
    """Возвращает названия всех комнат чата"""
