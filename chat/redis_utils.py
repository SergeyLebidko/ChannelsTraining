import json
import redis
from django.conf import settings

redis_conn = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def inc_room_count(room_name):
    """Увеличивает счетчик участников в комнате чата"""

    counter_key = create_counter_key(room_name)
    counter_value = redis_conn.incr(counter_key)

    print(f'Увеличиваем счетчик: Количество участников в {room_name}', counter_value)


def dec_room_count(room_name):
    """Уменьшает счетчик участников в комнате чата"""

    counter_key = create_counter_key(room_name)
    counter_value = redis_conn.decr(counter_key)

    print(f'Уменьшаем счетчик: Количество участников в {room_name}', counter_value)

    # Если после выхода участника в чате не осталось других участников - удаляем список сообщений чата
    if counter_value == 0:
        redis_conn.delete(counter_key)

        message_list_key = create_message_list_key(room_name)
        redis_conn.delete(message_list_key)


def add_message(user, room_name, message):
    """Добавляет сообщение в комнату чата"""

    message_list_key = create_message_list_key(room_name)
    redis_conn.rpush(message_list_key, json.dumps({
        'username': user.username,
        'message': message
    }))


def get_messages(room_name):
    """Получает все сообщения для заданного чата"""

    message_list_key = create_message_list_key(room_name)

    result = []
    for index in range(redis_conn.llen(message_list_key)):
        result.append(json.loads(redis_conn.lindex(message_list_key, index)))

    return result


def get_room_list():
    """Возвращает названия всех комнат чата"""

    result = []
    message_lists = redis_conn.keys('room:counter:*')

    for message_list in message_lists:
        result.append(bytes.decode(message_list, 'utf-8').split(':')[2])

    return result


def create_counter_key(room_name):
    """Возвращает ключ для счетчика участников в переданной комнате чата"""

    return f'room:counter:{room_name}'


def create_message_list_key(room_name):
    """Возвращает ключ для списка сообщений комнаты чата"""

    return f'room:message_list:{room_name}'
