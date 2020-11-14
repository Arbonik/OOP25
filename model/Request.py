from model.Room import Room
from model.Settings import timeLife


class Request:
    # время на которое снимают номер
    time = 0
    # Какой номер необходим
    room = Room.instance()
    cost = room.cost

    @staticmethod
    def instance():
        r = Request()
        r.room = Room.instance()
        r.time = timeLife()
        return r
